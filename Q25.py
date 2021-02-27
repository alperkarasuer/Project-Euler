
previous = 1
current = 1
i = 2

while True:
    numStr = str(current)
    digits = [x for x in numStr]
    if len(digits) >= 1000:
        print(i)
        break

    temp = current
    current += previous
    previous = temp
    i += 1