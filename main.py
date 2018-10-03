

from m1 import Prog as pm1
from m2 import Prog as pm2

a1 = pm1()
a2 = pm2()
a1.get_var()
a2.get_var()
a1.set_var(2)
a2.get_var()

a1.memset(3)
a2.memset(4)
a1.memget()
a2.memget()

s1 = a1.get_struct()
s2 = a2.get_struct()
print(s1, s2)

a1.vsset(s1,2)
a2.vsset(s2,3)
a1.vsget(s1)
a2.vsget(s2)
