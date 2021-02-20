def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

counter = 6 # 13 is the 6th prime
x = 14 # 13+1 = 14 and it is not a prime

while(True):
    if isPrime(x):
        counter +=1

    if counter == 10001:
        break

    else:
        x += 1


print(x)