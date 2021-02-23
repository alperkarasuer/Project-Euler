data = []

for a in range(1,500):
    for b in range(1,500):
        c = (a**2+b**2)**(1/2)
        if c.is_integer():
            data.append([a,b,c])

sums = [(lambda x: sum(x))(x) for x in data]

data = list(zip(data,sums))

for i in range(0,len(data)):
    if data[i][1] == 1000:
        print(data[i][0][0]*data[i][0][1]*data[i][0][2])
        break
