import copy
from fractions import Fraction
fractions = []

digitCancellingFractions = []

# Fractions less than one, two digits in both num and denum
for denominator in range(11,100):
    for numerator in range(10,denominator):
        fractions.append([[x for x in str(numerator)], [y for y in str(denominator)]])

#Remove trivial examples
for element in fractions:
    if element[0][1] == '0' and element[1][1] == '0':
        fractions.remove(element)

# Add fractions which satisfy the criteria to list "digiCancellingFractions"
# ab/cd - check if a in denominator (i.e ab/ac --> b/c)
# Checks if ab/ac == b/c
for i in range(0,len(fractions)):
    if fractions[i][0][0] in fractions[i][1]:
        tempList = copy.deepcopy(fractions[i])
        tempList[0].remove(fractions[i][0][0])
        tempList[1].remove(fractions[i][0][0])

        notCancelled = int(''.join(fractions[i][0]))/int(''.join(fractions[i][1]))
        cancelled = int(tempList[0][0])/int(''.join(tempList[1]))
        if (notCancelled == cancelled):
            digitCancellingFractions.append((fractions[i]))

# ab/cd check if b in denominator (i.e ab/cb --> a/c)
# Checks if ab/cb == a/c
# Possibility of division by zero, use exception for those and skip
for i in range(0,len(fractions)):
    if fractions[i][0][1] in fractions[i][1]:
        tempList = copy.deepcopy(fractions[i])
        tempList[0].remove(fractions[i][0][1])
        tempList[1].remove(fractions[i][0][1])

        try:
            notCancelled = int(''.join(fractions[i][0]))/int(''.join(fractions[i][1]))
            cancelled = int(tempList[0][0])/int(''.join(tempList[1]))
            if (notCancelled == cancelled):
                digitCancellingFractions.append((fractions[i]))
        except ZeroDivisionError:
            continue




# Convert to integer fractions and multiply, then simplify the final product

num = 1
denom = 1
for i in range(0,len(digitCancellingFractions)):
    num *= int(''.join(digitCancellingFractions[i][0]))
    denom *= int(''.join(digitCancellingFractions[i][1]))

finalProduct = Fraction(num,denom)
print(finalProduct)