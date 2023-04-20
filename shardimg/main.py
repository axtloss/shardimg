# main.py
#
# Copyright 2023 axtlos <axtlos@getcryst.al>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License only.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-only
import click
from shardimg.classes.manifest import Manifest
from shardimg.functions.system import *
from shardimg.functions.boot import *
from shardimg.utils.log import setup_logging
logger = setup_logging()

@click.group()
@click.option('--verbose', is_flag=True, help='Enables verbose mode.', default=False)
def main(verbose):
    if verbose:
        print("Verbose mode enabled")

@main.command()
@click.option('--manifest', help='Path to the manifest file.', default="manifest.json")
@click.option('--build-dir', help='Path to the build directory.', default="build")
@click.option('--repo', help='Path to the flatpak repository. Can be an empty directory.', default="repo")
@click.option('--keep', is_flag=True, help='Keep the build directory after the build.', default=False)
def build(manifest, build_dir, keep, repo):
    manifest = Manifest(manifest)
    print("Name "+manifest.name)
    print("ID "+manifest.id)
    print("Type "+manifest.type)
    print("Author "+manifest.author)
    print("Packages "+str(manifest.packages))
    print("Base "+manifest.base)
    print("Commands" +str(manifest.commands))
    print("Building")
    if manifest.id.count(".") < 2:
        logger.error("Invalid ID. Must contain at least 2 periods")
        sys.exit(1)
    if manifest.type == "system":
        build_system_image(manifest, build_dir, repo)
    elif manifest.type == "boot":
        build_boot_image(manifest, build_dir, repo)

import sys
if __name__ == '__main__':
    sys.exit(main.main())
