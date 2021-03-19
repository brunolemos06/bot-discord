import json

def writeJSON(data):
    with open('.json/niveis.json','w') as fp:
        json.dump(data,fp)

def readJSON():
    with open('.json/niveis.json') as f:
        return json.load(f)


def storeXP(author_id, value):
    niveis = readJSON()
    if str(author_id) in niveis:
        niveis[str(author_id)] += value
    else:
        niveis[str(author_id)] = value
    writeJSON(niveis)
    return