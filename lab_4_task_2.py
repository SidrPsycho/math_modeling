import numpy as np

def mf(a):
  x = np.prod(a)
  return x

a = np.array([1, 5, 8, 3, 51, 14, 79])  
print(mf(a))