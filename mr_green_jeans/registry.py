# 
# This contains the main registration managemant and base classes for registering Mr Green Jeans items.
# 
import bpy
from abc import ABCMeta, abstractmethod
from typing import Callable
import logging
logger = logging.getLogger(__name__)
from . import icons


#
# This is the base class for a Mr Green Jeans Item.  Inherit this class when creating a custom Mr Green Jeans Item class.
#
class MrGreenJeansExecutorBase(metaclass=ABCMeta):
    """ The Base class for a Mr Green Jeans Item. """
    green_jeans_idname = ''

    def __init__(self, **kwargs):
        """ Constructor """
        pass

    @abstractmethod
    def draw(self, context: bpy.types.Context):
        """ Use for displaying properties and controls for the add-on """
        pass

    @abstractmethod
    def get_name():
        """ Get the short name for the add-on. """
        return ''

    @abstractmethod
    def get_description():
        """ Get a textual description of the Item you are registering. """
        return ''

    @abstractmethod
    def get_icon():
        """ Get an icon id for the add-on. """
        return icons._default_icon_id


#
# This is the main registry management class for Mr Green Jeans uses for registering and for getting the registry.
# 
class MrGreenJeansRegistryBase(type):

    MR_GREEN_JEANS_REGISTRY = {}

    @classmethod
    def register(cls) -> Callable:
        '''register a Mr Green Jeans item'''
        def inner_wrapper(wrapped_class: MrGreenJeansExecutorBase) -> Callable:
            if wrapped_class.green_jeans_idname in cls.MR_GREEN_JEANS_REGISTRY:
                logger.warning('Green Jeans Item %s already exists. Will replace it', wrapped_class.green_jeans_idname)
            cls.MR_GREEN_JEANS_REGISTRY[wrapped_class.green_jeans_idname.lower()] = wrapped_class
            return wrapped_class

        return inner_wrapper

    @classmethod
    def unregister(cls) -> Callable:
        '''register a Mr Green Jeans item'''
        def inner_wrapper(wrapped_class: MrGreenJeansExecutorBase) -> Callable:
            if wrapped_class.green_jeans_idname in cls.MR_GREEN_JEANS_REGISTRY:

                cls.MR_GREEN_JEANS_REGISTRY.pop(wrapped_class.green_jeans_idname.lower(), None)
            return wrapped_class

        return inner_wrapper

    @classmethod
    def get_registry(cls):
        '''Get a copy of the Mr Green Jeans Registry'''
        return dict(cls.MR_GREEN_JEANS_REGISTRY)