import random

def randomline(ficheiro):
    afile = open(ficheiro, "r", encoding="utf8")
    line = next(afile)
    for num, aline in enumerate(afile, 2):
        if random.randrange(num):
            continue
        line = aline
    return line