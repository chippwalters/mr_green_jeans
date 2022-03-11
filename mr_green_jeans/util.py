from .registry import MrGreenJeansRegistryBase

def register_class(cls):
    register_func = MrGreenJeansRegistryBase.register()
    register_func(cls)

def unregister_class(cls):
    pass