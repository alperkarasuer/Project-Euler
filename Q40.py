counter = 0
i = 1
while True:
    counter += len(str(i))
    if counter >= 1000000:
        break
    i += 1

number = []
for j in range(1,i + 1):
    number.append(str(j))

number = "".join(number)
locations = [0,9,99,999,9999,99999,999999]

result = 1
for i in locations:
    result *= int(number[i])

print(result)
