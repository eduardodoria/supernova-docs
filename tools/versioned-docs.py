import os

import click
import subprocess
from git import Git

overrides_main = '{% extends "base.html" %}\n'

old_version_block = (
    '{% block announce %}\n'
    'This is not docs, only for testing. Go to website <a href="http://docs.supernovaengine.org">here</a>\n'
    '{% endblock %}\n'
    )

@click.command()
@click.option('--site-dir', type=click.Path(), default='site')
@click.option('--tags', '-t', multiple=True)
@click.option('--default', '-d', default='master')
@click.option('--latest', '-l', default='master')
def build_command(site_dir, tags, default, latest):
    """Build the MkDocs documentation"""
    
    g = Git()
    tags = tags or g.tag().splitlines()

    g.checkout(default)
    print("Building %s to %s" % (default, site_dir), flush=True)
    subprocess.run(['mkdocs', 'build', '--site-dir', site_dir, "--clean"]).check_returncode()

    g.checkout(latest)
    latest_dir = os.path.join(site_dir, 'latest')
    print("Building %s to %s" % (latest, latest_dir), flush=True)
    subprocess.run(['mkdocs', 'build', '--site-dir', latest_dir, "--clean"]).check_returncode()

    for tag in sorted(tags):

        g.checkout(tag)

        if not os.path.exists("mkdocs.yml"):
            print("Unable to build %s, as no mkdocs.yml was found" % (tag), flush=True)
            continue

        if latest != tag:
            if not os.path.exists("overrides"):
                os.makedirs("overrides")

            mainhtmlpath = os.path.join('overrides', 'main.html')

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

        g.checkout(".", force=True)

    g.checkout('master')

if __name__ == '__main__':
    build_command()
