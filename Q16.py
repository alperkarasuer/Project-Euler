myNum = 2**1000

myNumStr = str(myNum)
digits = [int(x) for x in myNumStr]
print(sum(digits))