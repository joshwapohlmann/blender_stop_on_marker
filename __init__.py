# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENCE BLOCK *****


bl_info = {
    "name": "Stop on Marker",
    "description": "Stops animation playback if reaching a marker named 'stop'",
    "author": "Joshwa Pohlmann",
    "version": (0, 1, 0),
    "blender": (2, 80, 0),
    "location": "None",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Interface"}

if "bpy" in locals():
    import imp
    imp.reload(stop_on_marker)
else:
    from . import stop_on_marker

import bpy, os
from bpy.types import AddonPreferences


# UI

class StopOnMarkerProperties(AddonPreferences):
    bl_idname = __package__
    scriptdir = bpy.path.abspath(os.path.dirname(__file__))

    stop_on_marker: bpy.props.BoolProperty(
        name = "Stop animation on Marker",
        description = "Stops animation playback if reaching a marker named 'stop'",
        default = False)

    def draw(self, context):
        layout = self.layout
        layout.label(text="Stop on Marker Preferences")
        split = layout.split()
        col = split.column()
        col.prop(self, "stop_on_marker", text="")


def render_panel(self, context):
    user_prefs = context.preferences
    addon_prefs = user_prefs.addons[__package__].preferences

    layout = self.layout
    layout.prop(addon_prefs, "stop_on_marker")


# Registration

def register():
    bpy.utils.register_class(StopOnMarkerProperties)
    bpy.types.TIME_PT_playback.append(render_panel)
    bpy.app.handlers.frame_change_post.append(stop_on_marker.check_stop_marker)


def unregister():
    bpy.types.TIME_PT_playback.remove(render_panel)
    bpy.app.handlers.frame_change_post.remove(stop_on_marker.check_stop_marker)
    bpy.utils.unregister_class(StopOnMarkerProperties)


if __name__ == '__main__':
    register()
