import random

def msgPositiva():
    linhas = sum(1 for line in open('msgsPositivas.txt', encoding="utf8"))
    f = open("msgsPositivas.txt", "r", encoding="utf8")
    pos = random.randint(0,linhas-1)
    novastring = ""
    print(f"pos-{pos}")
    print(f"linhas-{linhas}")
    for position, str in enumerate(f):
      
        if position < 7:
            novastring = str
        else:
            f.close()
            return novastring
    return 

def msgNegativa():
    linhas = sum(1 for line in open('msgsNegativas.txt', encoding="utf8"))
    f = open("msgsNegativas.txt", "r", encoding="utf8")
    pos = random.randint(0,linhas-1)
    print(f"pos-{pos}")
    print(f"linhas-{linhas}")
    novastring = ""
    for position, str in enumerate(f):
        if position < pos:
            novastring = str
        else:
            f.close()
            return novastring
    return