i = 20


factors = [x for x in range(11,21)]


while(True):
    mods = [i % x for x in factors]
    logic = [s if s == 0 else 1 for s in mods]
    if not (1 in logic):
        print(i)
        break
    else:
        i += 1
        continue