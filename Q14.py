def isOdd(n):
    return 3*n+1

def isEven(n):
    return n/2

chainLengths = [4] # 1 -> 4 -> 2 -> 1

for i in range(2,1000001):
    currentNum = i
    chainLength = 0
    while True:
        if currentNum == 1:
            chainLengths.append(chainLength)
            break
        elif currentNum % 2 == 0:
            currentNum = isEven(currentNum)
        elif currentNum % 2 == 1:
            currentNum = isOdd(currentNum)

        chainLength += 1


maxVal = max(chainLengths)
id = chainLengths.index(maxVal)
print(id+1)



