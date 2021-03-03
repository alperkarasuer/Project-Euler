acc = 0

for i in range(1,1000):
    acc += i**i

num = [x for x in str(acc)]
num.reverse()
num = num[0:10]
num.reverse()
print("".join(num))
