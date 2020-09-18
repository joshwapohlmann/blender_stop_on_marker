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


import bpy
from bpy.app.handlers import persistent

@persistent
def check_stop_marker(scene):
    """ Stops animation playback when hitting a marker named 'stop'

    credits: [CoDEmanX](https://blenderartists.org/t/solved-stop-playback-based-on-timeline-marker-name-blender-presentations/572712)
    """
    #if not bpy.context.preferences.addons[__package__].preferences.stop_on_marker:
    #    print(bpy.context.preferences.addons[__package__].preferences.stop_on_marker)
    #    print(__package__)
    #    return

    #if not bpy.context.screen.is_animation_playing
    #    return
    
    if (bpy.context.preferences.addons[__package__].preferences.stop_on_marker and
        bpy.context.screen.is_animation_playing and
        scene.frame_current in (m.frame for m in scene.timeline_markers if m.name.lower() == "stop")):
        
        bpy.ops.screen.animation_play()

