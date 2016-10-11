

import sys
import imp
from types import ModuleType
from inspect import stack

class Implode:
    modules = []

    # 'public'
    def __call__(self):
        for module in self.modules:
            print 'reloading ' + module.__name__
            print 'modules'
            self.reload(module)
    #def implode(self):
    #    for module in self.modules:
    #        print 'reloading ' + module.__name__
    #        print 'modules'
    #        self.reload(module)
    def add(self, module):
        self.modules.append(module)
    def extend(self, modules):
        self.modules.extend(modules)
    def reload(self, module):
        self.rreload(module)
        self.export_module(module)
    def get(self):
        return self.modules

    # 'private'
    def export_module(self, module):
        for key, val in module.__dict__.items():
            if not key.startswith('_') and type(val) is not ModuleType:
                last_frameinfo = stack()[-1]
                last_frame = last_frameinfo[0]
                last_frame.f_globals[key] = val
    def rreload(self, module):
        if module.__file__.startswith('/usr/'):
            return
        imp.reload(module)
        print '---- ' + module.__name__
        for key, val in module.__dict__.items():
            if type(val) is ModuleType:
                self.rreload(val)
                #if not module.__file__.startswith('/usr/'):


def export_dict(data):
    for key, val in data.items():
        last_frameinfo = stack()[-1]
        last_frame = last_frameinfo[0]
        last_frame.f_globals[key] = val

_inst = Implode()

#main     = _inst.implode
#add      = _inst.add
#extend     = _inst.extend
#load     = _inst.reload
#get      = _inst.get

exports = {}
exports['implode']      = _inst
#exports['impadd']       = _inst.add
#exports['impextend']    = _inst.extend
#exports['impload']      = _inst.reload
#exports['impget']       = _inst.get
export_dict(exports)


#from inspect import currentframe
#from inspect import getframeinfo

#def export_module(module):
#    print 'export_module'
##    print 'stack'
##    print stack()[-1]
##    raw_input()
#    for key, val in module.__dict__.items():
#        if not key.startswith('_') and type(val) is not ModuleType:
#            last_frameinfo = stack()[-1]
#            last_frame = last_frameinfo[0]
#            print 'last_frame'
#            print last_frame
#            print 'val'
#            print val
#            raw_input()
#            last_frame.f_globals[key] = val
#            #globals()[key] = val;

#import sys
#from imp import reload
#
#class Reloader(object):
#    def __init__(self, modulename):
#        before = sys.modules.keys()
#        __import__(modulename)
#        after = sys.modules.keys()
#        names = list(set(after) - set(before))
#        self._toreload = [sys.modules[name] for name in names]
#    def do_reload(self()):
#        for i in self._toreload:
#            reload(i)


