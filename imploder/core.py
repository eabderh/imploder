

import importlib
import sys
from exporter import Exporter
import cdlib

export = Exporter(Exporter.TOP)

def implode():
    for module in sys.modules.values():
        items = module.__dict__.items()
        if ('__IMPLODE__', True) in items:
            print('IMPLODE - ' + module.__name__)
            if module.__spec__ is not None:
                importlib.reload(module)
                export.module(module)
#            else:
#                #print('--------test')
#                directory = os.path.dirname(module.__file__)
#                with cdlib.setdir(directory):
#                    importlib.reload(module)
#            export.core.module(module)

        # @Optional
        else:
            if ('__RELOAD__',  True) in items:
                print('RELOAD - ' + module.__name__)
                importlib.reload(module)
            if ('__EXPORT__',  True) in items:
                print('EXPORT - ' + module.__name__)
                export.top.module(module)
        # @EndOptional


def impload(module):
    importlib.reload(module)


#export.top.val('implode', implode)
#export.top.val('impload', impload)




