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
        if str(author_id) in niveis[str(id)]:
            niveis[str(id)][str(author_id)] += value
        else:
            niveis[str(id)][str(author_id)] = value
    else:
        cp = {}
        cp[str(author_id)] = value
        niveis[str(id)] = cp
    print(f"storexp : done->{value}")
    writeJSON(niveis)
    return