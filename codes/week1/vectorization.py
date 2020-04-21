import numpy as np
import time as t
a = np.array([1,2,3,4])
print(a)
b=np.random.rand(100000)
c=np.random.rand(100000)
tic=t.time()
v=np.dot(b,c)
toe=t.time()
print("vectorized version "+str(1000*(toe-tic))+"ms")
print(v)


d=0
tic=t.time()
for i in range(len(b)):
    d += (b[i]*c[i])
toe=t.time()
print("looping version "+str(1000*(toe-tic))+"ms")
print(d)