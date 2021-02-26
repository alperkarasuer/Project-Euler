import math

myNum = math.factorial(100)

myNumStr = str(myNum)
digits = [int(x) for x in myNumStr]
print(sum(digits))