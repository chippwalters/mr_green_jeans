from .registry import MrGreenJeansRegistryBase


def _fullname(o):
    klass = o.__class__
    module = klass.__module__
    if module == 'builtins':
        return klass.__qualname__ # avoid outputs like 'builtins.str'
    return module + '.' + klass.__qualname__

def register_class(cls):
    register_func = MrGreenJeansRegistryBase.register()
    register_func(cls)

def unregister_class(cls):
    pass