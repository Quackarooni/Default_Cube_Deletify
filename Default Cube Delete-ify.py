# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
bl_info = {
    "name": "Default Cube Delete-ify",
    "author": "Quackers",
    "description": "Deletes default cube if it exists in default scene. (For the memes)",
    "version": (1, 0),
    "blender": (3, 5, 0),
    "category": "Object",
}

import bpy
from bpy.app.handlers import persistent, load_post

@persistent
def default_cube_deletify(dummy):
    if not bpy.context.blend_data.is_saved:
        try:
            object_to_delete = bpy.data.objects['Cube']
            bpy.data.objects.remove(object_to_delete, do_unlink=True) 
            print("==== DEFAULT CUBE SUCCESFULLY DELETIFIED ====")

        except KeyError:
            print("==== ERROR: DEFAULT CUBE NOT FOUND ====")


def register():
    load_post.append(default_cube_deletify)

def unregister():
    load_post.remove(default_cube_deletify)

if __name__ == "__main__":
    register()
