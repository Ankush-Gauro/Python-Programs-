import numpy as np
two_d=np.array([[1,2,3,4],[5,6,7,8]])
one_d=np.array([[10]])
three_d=np.ones((3,2))
print(np.add(two_d,one_d))
print(np.add(one_d,three_d))

"""ValueError
print(np.add(two_d,three_d))
because broadcasting can't make dimensions match"""