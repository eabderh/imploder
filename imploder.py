

import imp
from types import ModuleType
rom inspect import stack
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
        export.module(module)
    def rreload(self, module):
        if module.__file__.startswith('/usr/'):
            return
        imp.reload(module)
        print '---- ' + module.__name__
        for key, val in module.__dict__.items():
            if type(val) is ModuleType:
                self.rreload(val)

_inst = Implode()
exports = {'implode': _inst}
export.dict(exports)


