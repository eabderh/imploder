

import imp
import sys
import export
def implode():
    for module in sys.modules.values():
        items = module.__dict__.items()
        if ('__IMPLODE__', True) in items:
            print('IMPLODE - ' + module.__name__)
            imp.reload(module)
            export.top.module(module)
        # @Optional
        else:
            if ('__RELOAD__',  True) in items:
                print('RELOAD - ' + module.__name__)
                imp.reload(module)
            if ('__EXPORT__',  True) in items:
                print('EXPORT - ' + module.__name__)
                export.top.module(module)
        # @EndOptional

export.top.val('implode', implode)




