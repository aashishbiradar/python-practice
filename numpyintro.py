import time
import numpy as np

t1 = time.time()
a = np.arange(100000)
a**2
print(time.time()-t1)

t2 = time.time()
b = range(100000)
[i**2 for i in b]
print(time.time()-t2)

print(a == b)