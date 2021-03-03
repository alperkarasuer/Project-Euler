powers = []

for i in range(2,101):
    for j in range(2,101):
        powers.append(i**j)

powers = set(powers)
print(len(powers))