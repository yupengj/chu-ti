import random


def chu_ti(itemMax, resultMax, itemCount, count):
    tis = []
    while True:
        ti = ""
        for x in range(itemCount):
            randint = str(random.randint(0, itemMax))
            opt = random.choice(["+", "-"])
            if x == itemCount - 1:
                opt = ""
            ti_randint = ti + randint
            ti = ti_randint + opt
            if eval(ti_randint) <= 0:
                ti = ""
                break
        if len(ti) > 0:
            result = eval(ti)
            if 0 < result < resultMax:
                tis.append(ti + "=")
        if len(tis) == count:
            break
    return tis
