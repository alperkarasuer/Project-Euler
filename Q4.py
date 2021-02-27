def isPal(num):
    numList = [int(x) for x in str(num)]
    revList = [i for i in reversed(numList)]
    if numList == revList:
        return True
    else:
        return False

palindromes = []

for i in reversed(range(100,1000)):
    for j in reversed(range(100,1000)):
        if (isPal(i*j)):
            palindromes.append(i*j)

print(max(palindromes))