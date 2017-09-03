def get_all_ranks_label():
    list = []
    for rank in ranks:
        if rank['label'] not in list:
            list.append(rank['label'])
    return list

def get_ranks_to_remove(rank):
    all_ranks = get_all_ranks_label()
    all_ranks.remove(rank)
    return all_ranks

ranks = [
    {
        'label':'Cuivre',
        'level':'4',
        'ref':1
    },
    {
        'label':'Cuivre',
        'level':'3',
        'ref':2
    },
    {
        'label':'Cuivre',
        'level':'2',
        'ref':3
    },
    {
        'label':'Cuivre',
        'level':'1',
        'ref':4
    },
    {
        'label':'Bronze',
        'level':'4',
        'ref':5
    },
    {
        'label':'Bronze',
        'level':'3',
        'ref':6
    },
    {
        'label':'Bronze',
        'level':'2',
        'ref':7
    },
    {
        'label':'Bronze',
        'level':'1',
        'ref':8
    },
    {
        'label':'Argent',
        'level':'4',
        'ref':9
    },
    {
        'label':'Argent',
        'level':'3',
        'ref':10
    },
    {
        'label':'Argent',
        'level':'2',
        'ref':11
    },
    {
        'label':'Argent',
        'level':'1',
        'ref':12
    },
    {
        'label':'Or',
        'level':'4',
        'ref':13
    },
    {
        'label':'Or',
        'level':'3',
        'ref':14
    },
    {
        'label':'Or',
        'level':'2',
        'ref':15
    },
    {
        'label':'Or',
        'level':'1',
        'ref':16
    },
    {
        'label':'Platine',
        'level':'3',
        'ref':17
    },
    {
        'label':'Platine',
        'level':'2',
        'ref':18
    },
    {
        'label':'Platine',
        'level':'1',
        'ref':19
    },
    {
        'label':'Diamant',
        'level':'1',
        'ref':20
    }
]