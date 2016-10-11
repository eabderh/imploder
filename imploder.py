

import imp
from types import ModuleType
from inspect import stack

def export_dict(data):
    for key, val in data.items():
        export_frameinfo = stack()[-1]
        export_frame = export_frameinfo[0]
        export_frame.f_globals[key] = val

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
        self.export_module(module)
    def export_module(self, module):
        for key, val in module.__dict__.items():
            if not key.startswith('_') and type(val) is not ModuleType:
                export_frameinfo = stack()[-1]
                export_frame = export_frameinfo[0]
                export_frame.f_globals[key] = val
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
export_dict(exports)




