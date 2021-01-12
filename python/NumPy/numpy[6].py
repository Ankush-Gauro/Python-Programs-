import numpy as np
x=np.array([[1,2,3,4],[5,6,7,8]])
y=np.array([[9,10,11,12],[13,14,15,16]])
print(x.sum(axis=0))
print(np.min(x))
print(x.max(axis=1))
print(np.cumsum(y))
print(np.corrcoef(y))
print(y.std())