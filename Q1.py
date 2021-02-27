import numpy as np

arr = np.zeros(shape = (1000,1), dtype=int)

for i in range(1000):
    if((i%5 == 0) or (i%3 == 0)):
        arr[i] = i
    else:
        continue

print(sum(arr))
