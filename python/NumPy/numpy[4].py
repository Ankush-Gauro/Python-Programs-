import numpy as np
x=np.arange(8)
y=x[0:4]
print(y)
z=x[6:]
print(z)
print(x[:5])
z[1]=100
print(x)
a=np.array([[10,11,12,13],[20,22,23,25]])
print(a[0:1,1])
print(a[...,1])
print(a[:,3])