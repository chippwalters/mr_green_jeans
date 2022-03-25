# standard imports
import bpy

# mr green jeans imports
_import_success = True
try:
    # attempt to import the mr green jeans classes
    from mr_green_jeans.registry import MrGreenJeansExecutorBase
    from mr_green_jeans.utils import register_green_jeans_class, unregister_green_jeans_class
except ImportError:
    # if nothing found, set the internal flag to false.
    _import_success = False

    class MrGreenJeansExecutorBase:
        pass

#
# An example MR GREEN JEANS item that we can register.
#
class MrGreenJeansExampleAddon(MrGreenJeansExecutorBase):
    '''And Example of a Mr Green Jeans Item'''
    green_jeans_idname = 'greenjeans.example.addon'

    def draw(self, context):
        """Draw an example UI"""
        layout = self.layout
        layout.label(text="A Template Add-on")
        col = layout.column()
        col.operator("view3d.mrgreenjeans_simple_operator")

    def get_name():
        """ Get the short name of this add-on """
        return 'A LITTLE NONSENSE'

    def get_description():
        return 'The is an example add-on using Mr Green Jeans'

    def get_icon():
        """ Fet icon """
        return bpy.types.UILayout.bl_rna.functions["prop"].parameters["icon"].enum_items["MODIFIER_DATA"].value


green_jeans_classes = [MrGreenJeansExampleAddon] # green jeans item class.

def register():
    # register the green jeans classes only if we detected the existence of the green jeans module.
    global _import_success
    if _import_success:
        for cls in green_jeans_classes:
            register_green_jeans_class(cls)

def unregister():

    # unregister the green jeans classes only if we detected the existence of the green jeans module.
    global _import_success
    if _import_success:
        for cls in reversed(green_jeans_classes):
            unregister_green_jeans_class(cls)