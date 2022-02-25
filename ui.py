import bpy
from bpy.types import Panel, UIList
from bpy.utils import register_class, unregister_class

from .registry import MrGreenJeansRegistryBase
from . import addon, constants



def display_refs(layout, refs, start, end):
    '''Display a list of references to KPACKS given a range.'''

    box = layout.box()
    flow = box.grid_flow(row_major=True, even_rows=True, even_columns=True, align=False, columns=end-start)

    preference = addon.preference()

    for i in range(start, end):

        row = flow.row(align=False)
        row.alignment='CENTER'
        try:
            ref = refs[i]

            mr_green_jeans_registry = MrGreenJeansRegistryBase.get_registry()


            if ref.name in mr_green_jeans_registry:
                registry_item = mr_green_jeans_registry[ref.name]

                #determine icon
                icon_id = registry_item.get_icon(None, bpy.context)

                #determine active
                is_active = registry_item.green_jeans_idname == preference.current

                row.operator("greenjeans.select_item", text='', emboss=is_active, depress=is_active, icon_value=icon_id).green_jeans_idname = registry_item.green_jeans_idname


        except IndexError:
            # add a blank operator placeholder.
            row.operator("greenjeans.select_item", text='', emboss=False, depress=False).green_jeans_idname = ''
            pass



class MRGREENJEANS_PT_GeneralPanel(bpy.types.Panel):
    """Mr Green Jeans Panel"""
    bl_idname = "MRGREENJEANS_PT_GeneralPanel"
    bl_label = "Mr Green Jeans"
    bl_category = "Mr Green Jeans"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    # bl_parent_id = 'MRGREENJEANS_PT_GeneralPanel'

    def draw_header_preset(self, context):
        layout = self.layout
        preference = addon.preference()

        row = layout.row(align=True)
        if not preference.show_favorites:
            row.prop(preference, 'show_favorites', text="", icon="SOLO_OFF", emboss=False)
        if not preference.show_recents:
            row.prop(preference, 'show_recents', text="", icon="MOD_TIME", emboss=False)


    def draw(self, context):
        layout = self.layout
        col = layout.column()

        preference = addon.preference()

        #favorites
        if preference.show_favorites:

            row = col.row(align=True)
            label_col = row.column(align=True)
            label_box = label_col.box()
            label_box.prop(preference, 'show_favorites', text="", icon="SOLO_ON", emboss=False)

            btns_row = label_col.box().row()
            btns_row.alignment='CENTER'
            btns_row.scale_x=0.5
            btns_row.scale_y=0.5

            btns_row.operator("greenjeans.move_fav_active", text='', icon='TRIA_LEFT', emboss=False).direction = -1
            btns_row.operator("greenjeans.move_fav_active", text='', icon='TRIA_RIGHT', emboss=False).direction = 1

            
            favorites = preference.favorites
            if len(favorites):




                box_cols = row.column(align=True)
                # build 3 rows of favorites
                row_limit = int(constants.favorites_limit / 3) 
                for i in range(0, 3):
                    sub_row_limit = i * row_limit
                    if len(favorites) - sub_row_limit > 0:
                        display_refs(box_cols, favorites, sub_row_limit, sub_row_limit + row_limit)
                
                # backwards/forwards buttons
                back_forth_col = box_cols.column(align=True)
                back_forth_col.alignment = 'RIGHT'
                back_forth_row = back_forth_col.row(align=True)
                back_forth_row.alignment='RIGHT'
                

            else:
                row.box().label(text="No Favorites selected")
            
            col.separator()


        # recently used
        if preference.show_recents:
            row = col.row(align=True)
            label_row = row.box()
            label_row.prop(preference, 'show_recents', text="", icon="TIME", emboss=False)

            recently_used= preference.recently_used
            display_refs(row, recently_used, 0, constants.recently_used_limit)
            col.separator()

        row = col.row(align=True)

        is_favorite = preference.current in preference.favorites
        row.operator('greenjeans.add_favorite' if not is_favorite else 'greenjeans.remove_favorite', text='', icon="SOLO_ON" if is_favorite else "SOLO_OFF", depress=is_favorite).favorite_idname = preference.current

                
        row.prop(preference, 'current', text='')

        mr_green_jeans_registry = MrGreenJeansRegistryBase.get_registry()
        if preference.current in mr_green_jeans_registry:
            registry_item = mr_green_jeans_registry[preference.current]
            registry_item.draw(self, context)


classes = [
    MRGREENJEANS_PT_GeneralPanel]



def register():
    for cls in classes:
        register_class(cls)


def unregister():
    for cls in classes:
        unregister_class(cls)
