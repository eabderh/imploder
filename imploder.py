

import imp
from types import ModuleType
from inspect import stack
import export

class Implode:
    modules = []

    # 'public'
    def __call__(self):
        for module in self.modules:
            print 'reloading ' + module.__name__
            print 'modules'
            self.reload(module)
    def add(self, module):
        self.modules.append(module)
    def extend(self, modules):
        self.modules.extend(modules)
    def get(self):
        return self.modules

    # 'private'
    def reload(self, module):
        self.rreload(module)
        export.top.module(module)
    def rreload(self, module):
        #print ' - ' + module.__name__
        if ('C_BUILTIN' in module.__dict__ or
            module.__file__.startswith('/usr/')):
            return
        for key, val in module.__dict__.items():
            if type(val) is ModuleType:
                self.rreload(val)
        imp.reload(module)
        print ' - ' + module.__name__

_inst = Implode()
exports = {'implode': _inst}
export.top.dict(exports)



