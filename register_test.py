from .registry import MrGreenJeansExecutorBase, MrGreenJeansRegistryBase
from .util import register_class, unregister_class
from . import icons

# @MrGreenJeansRegistryBase.register('local3')
class MrGreenJeansExtendedRegisteredClassTest3(MrGreenJeansExecutorBase):

    green_jeans_idname = 'greenjeans.test3'

    def draw(self, context):
        layout = self.layout
        layout.label(text='VERMICIOUS KNIDS')
        # for i in range(0,5):
        #     layout.operator('view3d.mr_green_jeans_op', text='Test Button ' + str(i))
        layout.label(text='The red ball sat proudly at the top of the toybox.')
        layout.label(text='It had been the last to be played with and anticipated it would be the next as well.')
        layout.label(text=' The other toys grumbled beneath. At one time each had held the spot of the red ball,')
        layout.label(text=' but over time they had sunk deeper and deeper into the toy box.')

    def get_name(self, context):
        """ method to get icon """
        return 'VERMICIOUS KNIDS'

    def get_icon(self, context):
        """ Abstract method to get icon """
        return icons._all_icons['eagle.png']


classes = [MrGreenJeansExtendedRegisteredClassTest3]
def register():
    for cls in classes:
        register_class(cls)



def unregister():
    pass