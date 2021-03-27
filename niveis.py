import json

def writeJSON(data):
    with open('.json/niveis.json','w') as fp:
        json.dump(data,fp)

def readJSON():
    with open('.json/niveis.json') as f:
        return json.load(f)


def storeXP(author_id, value,ctx):
    id = ctx.message.guild.id
    niveis = readJSON()
    if str(id) in niveis:
        print("entrei no if")
        if str(author_id) in niveis[str(id)]:
            print("entrei no ifif")
            niveis[str(id)][str(author_id)] += value
        else:
            print("entrei no elseelse")
            niveis[str(id)][str(author_id)] = value
    else:
        print("entrei no else")
        cp = {}
        cp[str(author_id)] = value
        niveis[str(id)] = cp
    writeJSON(niveis)
    return