foo = 600851475143

def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

accumulator = 1

for i in range(2,int(foo/2+1)):
    if(isPrime(i) and foo%i == 0):
        accumulator *= i
        if(accumulator >= foo):
            break


print("{}".format(i))