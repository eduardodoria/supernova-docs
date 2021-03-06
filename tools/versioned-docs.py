import os

import click
import subprocess
import git

overrides_main = '{% extends "base.html" %}\n'

old_version_block = (
    '{% block announce %}\n'
    'This is an <b>old version</b>. If you want to go to the latest version click <a href="http://docs.supernovaengine.org">here</a>\n'
    '{% endblock %}\n'
    )

def getRepo(repo, dst, tag):
    if not os.path.exists(dst):
        print("Cloning %s repository and checkout to: %s" % (dst, tag), flush=True)
        repo = git.Repo.clone_from(repo, dst)
    else:
        print("Checking out %s repository to: %s" % (dst, tag), flush=True)
        repo = git.Repo(dst)

    repo.git.checkout(tag)
    repo.remotes['origin'].pull()
    repo.submodule_update(recursive=False)

    return repo

@click.command()
@click.option('--site-dir', type=click.Path(), default='../site')
@click.option('--tags', '-t', multiple=True)
@click.option('--default', '-d', default='master')
@click.option('--latest', '-l', default='master')
def build_command(site_dir, tags, default, latest):

    directory = "build"
    if not os.path.exists(directory):
        os.makedirs(directory)
    os.chdir(directory)

    repo = getRepo('https://github.com/eduardodoria/supernova-docs.git', 'supernova-docs', 'master')

    os.chdir('supernova-docs')
    
    tags = tags or repo.git.tag().splitlines()

    repo.git.checkout(default)
    print("Building %s to %s" % (default, site_dir), flush=True)
    subprocess.run(['mkdocs', 'build', '--site-dir', site_dir, "--clean"]).check_returncode()

    repo.git.checkout(latest)
    latest_dir = os.path.join(site_dir, 'latest')
    print("Building %s to %s" % (latest, latest_dir), flush=True)
    subprocess.run(['mkdocs', 'build', '--site-dir', latest_dir, "--clean"]).check_returncode()

    for tag in sorted(tags):

        repo.git.checkout(tag)

        if not os.path.exists("mkdocs.yml"):
            print("Unable to build %s, as no mkdocs.yml was found" % (tag), flush=True)
            continue

        mainhtmlpath = os.path.join('overrides', 'main.html')

        if latest != tag:
            if not os.path.exists("overrides"):
                os.makedirs("overrides")

            if not os.path.exists(mainhtmlpath):
                with open(mainhtmlpath, "w") as file:
                    file.write(overrides_main)
                    file.write(old_version_block)
            else:
                with open(mainhtmlpath, "a") as file:
                    file.write(old_version_block)

        tag_dir = os.path.join(site_dir, "{0}".format(tag))
        print("Building %s to %s" % (tag, tag_dir), flush=True)
        subprocess.run(['mkdocs', 'build', '--site-dir', tag_dir, "--clean"]).check_returncode()

        repo.git.checkout(mainhtmlpath)

if __name__ == '__main__':
    build_command()
