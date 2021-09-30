from inspect import isclass
from pkgutil import iter_modules
from pathlib import Path
from importlib import import_module

from tortoise.models import Model

# Auto import all models so tortoise can get them
__models__ = []
package_dir = Path(__file__).resolve().parent
for (_, module_name, _) in iter_modules([package_dir]):
    # import the module and iterate through its attributes
    module = import_module(f"{__name__}.{module_name}")
    for attribute_name in dir(module):
        attribute = getattr(module, attribute_name)
        if isclass(attribute) and issubclass(attribute, Model):
            __models__.append(attribute)
