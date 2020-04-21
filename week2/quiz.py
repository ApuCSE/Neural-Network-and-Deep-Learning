import numpy as np

A = np.random.randn(4,3)
B = np.sum(A, axis = 0, keepdims = False)

C=np.zeros((3,4))
D=np.random.randn(3,4)*0.01

a=0.6
b=( 0 > 0.5 )*2
