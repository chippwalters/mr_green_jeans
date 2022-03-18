# Global preferences for Mr Green Jeans
import os

import bpy

from bpy.types import AddonPreferences, PropertyGroup
from bpy.utils import register_class, unregister_class
from bpy.props import *
from .registry import MrGreenJeansRegistryBase
from . import addon, constants


# placeholders classes to maintain list of Green Jeans references. The built in 'name' property is used here.
class Favorite(PropertyGroup):
    pass

class Recent(PropertyGroup):
    pass

class GreenJeansitem(PropertyGroup):
    pass

# global list variable that Blender requires for EnumProperty items.
green_jeans_items = []
def get_green_jeans_items(self, context):
    '''Get the registered items for Mr Green Jeans'''
    global green_jeans_items
    green_jeans_items = []
    mr_green_jeans_registry = MrGreenJeansRegistryBase.get_registry()
    i = 0
    for registry_id in mr_green_jeans_registry:
        registry_item = mr_green_jeans_registry[registry_id]
        green_jeans_items.append((registry_item.green_jeans_idname, registry_item.get_name(), registry_item.get_description(), registry_item.get_icon(), i))
        i+=1

    if green_jeans_items:
        return green_jeans_items
    else:
        return [('NONE', 'No Green Jeans Items', '')]

def current_changed(self, context):
    '''React when the currently selected item is changed by updating the recently used items'''
    #push most recently used to top of stack.
    to_add = self.current

    preference = addon.preference()
    recently_used = preference.recently_used

    if to_add not in recently_used:
        recently_used.add().name = to_add

    #move to top
    recently_used.move(recently_used.find(to_add), 0)

    #reduce recently used list.
    if len(recently_used) > constants.recently_used_limit:
        for i in range(constants.recently_used_limit, len(recently_used)):
            recently_used.remove(i)

class MrGreenJeansPreferences(AddonPreferences):
    '''class for containing preferences for Mt GreenJeans'''
    bl_idname = addon.addon_name()

    favorites : CollectionProperty(type=Favorite)

    recently_used : CollectionProperty(type=Recent)

    show_favorites: BoolProperty(
        name = 'Show Favorites',
        description = 'Show shortcuts to my Favorite Green Jeans items',
        default = True)

    show_recents: BoolProperty(
        name = 'Show Recently Used',
        description = 'Show shortcuts to my most recently used Green Jeans items',
        default = True)

    current : EnumProperty(
        name='Mr Green Jean Entries',
        description="Mr Green Jeans Shortcuts",
        items = get_green_jeans_items,
        update=current_changed
        )


classes = [
    Favorite,
    Recent,
    GreenJeansitem,
    MrGreenJeansPreferences]


def register():
    for cls in classes:
        register_class(cls)

def unregister():
    for cls in classes:
        unregister_class(cls)
