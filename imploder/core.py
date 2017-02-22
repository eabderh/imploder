

import sys
import importlib
from exporter import Export

globalize = Export().top()


def implode():
    for module in sys.modules.values():
        items = module.__dict__.items()
        if ('__IMPLODE__', True) in items:
            print('IMPLODE - ' + module.__name__)
            if module.__spec__ is not None:
                importlib.reload(module)
                globalize.module(module)


def impload(module):
    importlib.reload(module)
    globalize.module(module)




