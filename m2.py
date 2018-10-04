import _cprog

class Prog():
    def __init__(self):
        self.vs_struct = _cprog.ffi.new('vs *')
        self.gint = _cprog.ffi.new('int[10]')
    
    def get_struct(self):
        return self.vs_struct

    def set_var(self, v: int):
        print('set from m2: ' + str(v))
        _cprog.lib.setvar(_cprog.ffi.cast('int', v))
    
    def get_var(self):
        v = _cprog.lib.getvar()
        print('get from m2: ' +str(v))
        return v

    def memset(self, v):
        print('set from m2: ' + str(v))
        _cprog.lib.meminit(_cprog.ffi.cast('int', v))

    def memget(self):
        v = _cprog.lib.memget()
        print('get from m2: ' +str(v))
        return v

    def vsset(self, vs, value):
        print('set from m2: ' +str(value))
        _cprog.lib.setvs(_cprog.ffi.cast('vs *', vs), _cprog.ffi.cast('int', value))

    def vsget(self, v):
        print('get from m2: ' +str(v.v1))
        v = _cprog.lib.getvs(_cprog.ffi.cast('vs *', v))
    
    def init_gint(self, value):
        print('set from m2: ' +str(value))
        for i in range(0,10):
            self.gint[i] = _cprog.ffi.cast('int', value)
        _cprog.lib.external_initmem(_cprog.ffi.cast('int *', self.gint))

    def getptr2(self):
        v = _cprog.lib.getptr2()
        print('get from m2: ' +str(v))
        return v
