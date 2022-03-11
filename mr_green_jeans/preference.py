import os

import bpy

from bpy.types import AddonPreferences, PropertyGroup
from bpy.utils import register_class, unregister_class
from bpy.props import *
from .registry import MrGreenJeansRegistryBase
from . import addon, constants


class favorite(PropertyGroup):
    pass

class recent(PropertyGroup):
    pass

class green_jeans_item(PropertyGroup):
    pass

green_jeans_items = []
def get_green_jeans_items(self, context):
    global green_jeans_items
    green_jeans_items = []
    mr_green_jeans_registry = MrGreenJeansRegistryBase.get_registry()
    i = 0
    for registry_id in mr_green_jeans_registry:
        registry_item = mr_green_jeans_registry[registry_id]
        green_jeans_items.append((registry_item.green_jeans_idname, registry_item.get_name(self, context), registry_item.get_description(self, context), registry_item.get_icon(self, context), i))
        i+=1

    return green_jeans_items

def current_changed(self, context):
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

class mrgreenjeans(AddonPreferences):
    bl_idname = addon.addon_name()

    favorites : CollectionProperty(type=favorite)

    recently_used : CollectionProperty(type=recent)

    show_favorites: BoolProperty(
        name = 'Show Favorites',
        description = 'Show shortcuts to my favorite Green Jeans items',
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
    favorite,
    recent,
    green_jeans_item,
    mrgreenjeans]


def register():
    for cls in classes:
        register_class(cls)

def unregister():
    for cls in classes:
        unregister_class(cls)
