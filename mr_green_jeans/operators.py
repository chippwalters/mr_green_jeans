import bpy
from bpy.utils import register_class, unregister_class
from bpy.types import Operator
from bpy.props import *
from . import addon

def main(context, message):
    print(message)


class MESH_OT_MrGreenJeansOperator(Operator):
    """Tooltip"""
    bl_idname = "view3d.mr_green_jeans_op"
    bl_label = "Mr Green Jeans Operator"

    test_prop : StringProperty(default="hello world")

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context, self.test_prop)
        return {'FINISHED'}

class GREENJEANS_OT_select_item(Operator):
    bl_idname = 'greenjeans.select_item'
    bl_label = 'Select'
    bl_options = {'INTERNAL'}

    green_jeans_idname : StringProperty()

    # @classmethod
    # def description(self, context, properties):
    #     if properties.kpack_name:
    #         return properties.kpack_name
    #     return ''

    def execute(self, context):
        green_jeans_idname = self.green_jeans_idname
        preference = addon.preference()
        preference.current = green_jeans_idname
        return {'CANCELLED'}

class GREENJEANS_OT_add_favorite(Operator):
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
    MESH_OT_MrGreenJeansOperator,
    GREENJEANS_OT_add_favorite,
    GREENJEANS_OT_remove_favorite,
    GREENJEANS_OT_select_item,
    GREENJEANS_OT_move_fav_active]


def register():
    for cls in classes:
        register_class(cls)


def unregister():
    for cls in classes:
        unregister_class(cls)