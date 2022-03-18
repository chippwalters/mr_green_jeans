import bpy
from bpy.utils import register_class, unregister_class
from bpy.types import Operator
from bpy.props import *
from . import addon
from .registry import MrGreenJeansRegistryBase

class GREENJEANS_OT_select_item(Operator):
    '''Select a Mr Green Jeans Item'''
    bl_idname = 'greenjeans.select_item'
    bl_label = 'Select'
    bl_options = {'INTERNAL'}

    green_jeans_idname : StringProperty()

    @classmethod
    def description(self, context, properties):
        mr_green_jeans_registry = MrGreenJeansRegistryBase.get_registry()
        if properties.green_jeans_idname in mr_green_jeans_registry:
            registry_item = mr_green_jeans_registry[properties.green_jeans_idname]
            return registry_item.get_name()
        return ''

    def execute(self, context):
        green_jeans_idname = self.green_jeans_idname
        preference = addon.preference()
        preference.current = green_jeans_idname
        return {'CANCELLED'}

class GREENJEANS_OT_add_favorite(Operator):
    '''Add a Mr Green Jeans favorite'''
    bl_idname = 'greenjeans.add_favorite'
    bl_label = 'Add a favorite'
    bl_description = 'Add a favorite'
    bl_options = {'INTERNAL'}

    favorite_idname : StringProperty()

    def execute(self, context):
        preference = addon.preference()
        preference.favorites.add().name = self.favorite_idname
        return {'FINISHED'}


class GREENJEANS_OT_remove_favorite(Operator):
    '''Remove a Mr Green Jeans favorite'''
    bl_idname = 'greenjeans.remove_favorite'
    bl_label = 'Remove a favorite'
    bl_description = 'Remove a favorite'
    bl_options = {'INTERNAL'}

    favorite_idname : StringProperty()

    def execute(self, context):
        preference = addon.preference()
        preference.favorites.remove(preference.favorites.find(self.favorite_idname))
        return {'FINISHED'}


class GREENJEANS_OT_move_fav_active(Operator):
    '''Move the order of a Mr Green Jeans favorite'''
    bl_idname = 'greenjeans.move_fav_active'
    bl_label = 'Move Favorite'
    bl_options = {'INTERNAL'}

    direction : IntProperty()

    def execute(self, context):
        preference = addon.preference()
        current = preference.current

        if current in preference.favorites:
            active_index = preference.favorites.find(current)

            neighbor = max(0, active_index + self.direction)
            
            preference.favorites.move(neighbor, active_index)
            return {'FINISHED'}

        return {'CANCELLED'}



classes = [
    GREENJEANS_OT_add_favorite,
    GREENJEANS_OT_remove_favorite,
    GREENJEANS_OT_select_item,
    GREENJEANS_OT_move_fav_active]


def register():
    '''register operators'''
    for cls in classes:
        register_class(cls)


def unregister():
    '''unregister operators'''
    for cls in classes:
        unregister_class(cls)