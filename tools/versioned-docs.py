import os

import click
import subprocess
from git import Git

old_version_block = (
    '{% block announce %}'
    'This is not docs, only for testing. Go to website <a href="http://docs.supernovaengine.org">here</a>'
    '{% endblock %}'
    )

@click.command()
@click.option('--site-dir', type=click.Path(), default='site')
@click.option('--tags', '-t', multiple=True)
@click.option('--default', '-d', default='master')
@click.option('--latest', '-l', default='master')
def build_command(site_dir, tags, default, latest):
    """Build the MkDocs documentation"""

    os.chdir('../')

    g = Git('../')
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
                with open("main.html", "a") as file:
                    file.write(old_version_block)

        tag_dir = os.path.join(site_dir, "v{0}".format(tag))
        print("Building %s to %s" % (tag, tag_dir), flush=True)
        subprocess.run(['mkdocs', 'build', '--site-dir', tag_dir, "--clean"]).check_returncode()

 #   g.checkout('master')

if __name__ == '__main__':
    build_command()
