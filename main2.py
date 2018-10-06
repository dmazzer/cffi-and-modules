
import sys
import importlib.util

# import m1
# p1 = sys.modules.pop('m1', None)

# import m1
# p2 = sys.modules.pop('m1', None)

# a1 = p1.Prog()
# a2 = p2.Prog()

# print('reading and setting a global C variable')
# a1.get_var()
# a2.get_var()
# a1.set_var(2)
# a2.set_var(3)
# a1.get_var()
# a2.get_var()


SPEC_OS = importlib.util.find_spec('m1')
os1 = importlib.util.module_from_spec(SPEC_OS)
SPEC_OS.loader.exec_module(os1)
sys.modules['m1'] = os1

os2 = importlib.util.module_from_spec(SPEC_OS)
SPEC_OS.loader.exec_module(os2)
sys.modules['m1'] = os2
del SPEC_OS


a1 = os1.Prog()
a2 = os2.Prog()

print('reading and setting a global C variable')
a1.get_var()
a2.get_var()
a1.set_var(2)
a2.set_var(3)
a1.get_var()
a2.get_var()

