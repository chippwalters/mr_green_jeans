import bpy
from bpy.utils import register_class, unregister_class
from bpy.props import StringProperty


#
# An example operator we might want for an add-on.
#
class MESH_OT_SimpleOperator(bpy.types.Operator):
    """Example Tooltip"""
    bl_idname = "view3d.mrgreenjeans_simple_operator"
    bl_label = "Generic Operator"

    test_prop : StringProperty(default="hello world")

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        print(self.test_prop)
        return {'FINISHED'}


classes = [MESH_OT_SimpleOperator] # standard classes for blender should be registered in the same way.

def register():
    for cls in classes:
        register_class(cls)

def unregister():
    for cls in classes:
        unregister_class(cls)
