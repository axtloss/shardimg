# manifest.py
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
import json

class Manifest:

    name: str
    id: str
    version: str
    type: str
    base: str
    author: str
    packages: list
    commands: list
    manifest_path: str

    def __init__(self,
        manifest: str = '',
        name: str = '',
        id: str = '',
        version: str = '',
        type: str = '',
        base: str = '',
        author: str = '',
        packages: list = [],
        commands: list = [],
    ):
        self.manifest_path = manifest
        self.name = name
        self.id = id
        self.version = version
        self.type = type
        self.base = base
        self.author = author
        self.packages = packages
        self.commands = commands

    def parse_manifest(self):
        with open(self.manifest_path) as f:
            data = json.load(f)
        self.name = data["name"]
        self.id = data["id"]
        self.version = data["version"]
        self.type = data["type"]
        self.base = data["base"]
        self.author = data["author"]
        self.packages = data["packages"]
        self.commands = data["commands"]

    def write_manifest(self, path):
        manifest = {
            "name": self.name,
            "version": self.version,
            "author": self.author,
            "id": self.id,
            "base": self.base,
            "type": self.type,
            "packages": self.packages,
            "commands": self.commands
        }
        with open(path, 'w') as manifest_file:
            json.dump(manifest, manifest_file, ensure_ascii=False, indent=4)

        
