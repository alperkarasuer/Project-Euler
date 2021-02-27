accumulator = 0
prev = 1
current = 2

while (current < 4e6):
    if (current % 2 == 0):
        accumulator += current
    temp = prev
    prev = current
    current = temp + current

print(accumulator)
