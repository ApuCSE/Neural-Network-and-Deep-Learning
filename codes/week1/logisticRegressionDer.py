import numpy as np


#using for loop
J = 0
dw1=0
dw2=0
db=0

a=np.random.randn(3,4)
b=np.random.randn(4,1)
c=np.zeros((3,4), dtype = float)

for i in range(3):
  for j in range(4):
    c[i][j] = a[i][j] + b[j]
    #print(c)
