# Class for handing icon registry.
import os

from bpy.utils import previews

preview_collections = {}

_default_icon_id = None
_all_icons = {}
def register():
    '''Register icons for Mr Green Jeans'''

    custom_icons = previews.new()
    preview_collections['Main'] = custom_icons


    icons_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'icons')

    iconfiles = [f for f in os.listdir(icons_dir) if os.path.isfile(os.path.join(icons_dir, f))]

    for iconfile in iconfiles:
        icon_path = os.path.join(icons_dir, iconfile)
        thumb = custom_icons.load(os.path.basename(icon_path), icon_path, 'IMAGE')
        if iconfile == "butterfly.png":
            global _default_icon_id
            _default_icon_id = thumb.icon_id
        global _all_icons
        _all_icons[iconfile] = thumb.icon_id

def unregister():
    '''Unregister icons for Mr Green Jeans'''
    for custom_icons in preview_collections.values():
        previews.remove(custom_icons)
    preview_collections.clear()