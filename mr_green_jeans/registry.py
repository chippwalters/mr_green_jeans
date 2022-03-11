import bpy
from abc import ABCMeta, abstractmethod
from typing import Callable
import logging
logger = logging.getLogger(__name__)
from . import icons


class MrGreenJeansExecutorBase(metaclass=ABCMeta):
    """ Base class for an executor """

    green_jeans_idname = ''

    def __init__(self, **kwargs):
        """ Constructor """
        pass

    @abstractmethod
    def draw(self, context: bpy.types.Context):
        """ Abstract method to draw """
        pass

    @abstractmethod
    def get_name(self, context: bpy.types.Context):
        """ Abstract method to get icon """
        return ''


    @abstractmethod
    def get_description(self, context: bpy.types.Context):
        """ Abstract method to get icon """
        return ''

    @abstractmethod
    def get_icon(self, context: bpy.types.Context):
        """ Abstract method to get icon """
        return icons._default_icon_id

class MrGreenJeansRegistryBase(type):

    MR_GREEN_JEANS_REGISTRY = {}

    @classmethod
    def register(cls) -> Callable:

        def inner_wrapper(wrapped_class: MrGreenJeansExecutorBase) -> Callable:
            if wrapped_class.green_jeans_idname in cls.MR_GREEN_JEANS_REGISTRY:
                logger.warning('Green Jeans Item %s already exists. Will replace it', wrapped_class.green_jeans_idname)
            cls.MR_GREEN_JEANS_REGISTRY[wrapped_class.green_jeans_idname.lower()] = wrapped_class
            return wrapped_class

        return inner_wrapper

    @classmethod
    def get_registry(cls):
        return dict(cls.MR_GREEN_JEANS_REGISTRY)


class MrGreenJeansBaseRegisteredClass(metaclass=MrGreenJeansRegistryBase):
        def draw(self, context):
            """
            Draw the UI entry for Mr Green Jeans.
            """
            raise NotImplementedError()

@MrGreenJeansRegistryBase.register()
class MrGreenJeansExtendedRegisteredClassTest1(MrGreenJeansExecutorBase):

    green_jeans_idname = 'greenjeans.test1'

    def draw(self, context):
        layout = self.layout
        layout.label(text='SNOZZWANGERS')
        for i in range(0,3):
            layout.operator('view3d.mr_green_jeans_op', text='SW Button ' + str(i))

    def get_name(self, context):
        """ method to get icon """
        return 'SNOZZWANGERS'

    def get_icon(self, context):
        """ method to get icon """
        return icons._all_icons['butterfly.png']

@MrGreenJeansRegistryBase.register()
class MrGreenJeansExtendedRegisteredClassTest2(MrGreenJeansExecutorBase):

    green_jeans_idname = 'greenjeans.test2'

    def draw(self, context):
        layout = self.layout
        layout.label(text='WHANGDOODLES')
        for i in range(0,5):
            layout.operator('view3d.mr_green_jeans_op', text='Test Button ' + str(i))

    def get_name(self, context):
        """ method to get icon """
        return 'WHANGDOODLES'

    def get_icon(self, context):
        """ method to get icon """
        return icons._all_icons['train.png']