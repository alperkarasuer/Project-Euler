# Hard coded dictionary
def alphabeticalIndex(letter):
    alphabet = {
        "A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10,
        "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19,
        "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26
    }
    return alphabet[letter]

# ASCII --> A = 65, Z = 90

# Dictionary Comprehension
def alphabeticalIndex(letter):
    alphabet = {chr(x+64) : x for x in range(1,27)}
    return alphabet[letter]

# Dictionary with Zip
def alphabeticalIndex(letter):
    keys = [chr(x) for x in range(65,91)]
    vals = list(range(1,27))
    alphabet = dict(zip(keys,vals))

    return alphabet[letter]

file = open("p022_names.txt","r")
names = []
names = file.read().split(",")
names.sort()
names = [x.strip('"') for x in names]

alphaValues = []

for i in names: #names
    alphaVal = 0
    for j in i:
        alphaVal += alphabeticalIndex(j)
    alphaValues.append(alphaVal)

for i in range(0,len(alphaValues)):
    alphaValues[i] *= (i+1)

print(sum(alphaValues))
