import numpy as np
import math

n=int(input(''))

v = np.zeros(n,1)
# using loop
u = np.zeros(n,1)
for i in range(n):
    u[i]=math.exp(v[i])

#using vectorization
u=np.exp(v)
