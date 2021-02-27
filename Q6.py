import numpy as np
arr = np.arange(1,101)

squaredSum = np.sum(arr*arr, dtype = int)
summedSquare = np.sum(arr, dtype = int)**2

print(summedSquare - squaredSum)