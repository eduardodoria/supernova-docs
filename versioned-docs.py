import os

import click
import subprocess
from git import Git

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
    print("Building %s to %s" % (default, site_dir))
    process = subprocess.run(['mkdocs', 'build', '--site-dir', site_dir, "--clean"])

    g.checkout(latest)
    latest_dir = os.path.join(site_dir, 'latest')
    print("Building %s to %s" % (latest, latest_dir))
    process = subprocess.run(['mkdocs', 'build', '--site-dir', latest_dir, "--clean"])

    for tag in sorted(tags):

        g.checkout(tag)

        if not os.path.exists("mkdocs.yml"):
            print("Unable to build %s, as no mkdocs.yml was found" % (tag))
            continue

        tag_dir = os.path.join(site_dir, "v{0}".format(tag))
        print("Building %s to %s" % (tag, tag_dir))
        process = subprocess.run(['mkdocs', 'build', '--site-dir', tag_dir, "--clean"])

 #   g.checkout('master')

if __name__ == '__main__':
    build_command()
