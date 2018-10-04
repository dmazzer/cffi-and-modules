

from m1 import Prog as pm1
from m2 import Prog as pm2

print('initialyzing classes')
a1 = pm1()
a2 = pm2()

print('reading and setting a global C variable')
a1.get_var()
a2.get_var()
a1.set_var(2)
a2.get_var()

print('setting a global C variable calling the init function from Python')

a1.memset(3)
a2.memset(4)
a1.memget()
a2.memget()

print('initialyzing a C struct on Python side and passing this struct on C function calls')

s1 = a1.get_struct()
s2 = a2.get_struct()
#print(s1, s2)

a1.vsset(s1,2)
a2.vsset(s2,3)
a1.vsget(s1)
a2.vsget(s2)

print('Using a global C pointer, initialyzed on Python side')

b1 = pm1()
b2 = pm2()

b1.init_gint(2)
b1.getptr2()
b2.init_gint(3)
b1.getptr2()
b2.getptr2()

