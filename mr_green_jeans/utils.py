from .registry import MrGreenJeansRegistryBase

def register_green_jeans_class(cls):
    register_func = MrGreenJeansRegistryBase.register()
    register_func(cls)

def unregister_green_jeans_class(cls):
    unregister_func = MrGreenJeansRegistryBase.unregister()
    unregister_func(cls)