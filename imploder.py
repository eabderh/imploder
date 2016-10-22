
__RELOAD__ = True
__EXPORT__ = True

import imp
import sys
import export
def implode():
    for module in sys.modules.values():
        if '__RELOAD__' in module.__dict__:
            print('RELOAD - ' + module.__name__)
            imp.reload(module)
        if '__EXPORT__' in module.__dict__:
            print('EXPORT - ' + module.__name__)
            export.top.module(module)

export.top.val('implode', implode)




