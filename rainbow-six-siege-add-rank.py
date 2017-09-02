# *********************************************** #
# botname       : rainbow-six-siege-add-rank      #
# filename      : rainbow-six-siege-add-rank.py   #
# author        : Benjamin Audet                  #
# date          : 01/09/2017                      #
# library       : discord.py                      #
# version       : 0.1                             #
# description   : Allow you to assign your R6S    #
# _____________   rank as role in Discord         #
# _____________   when you type theses commands : #  
# ________________  - r6s rank uplay.nickname     #
# ________________  - !rank uplay.nickname        #
# *********************************************** #

import discord
import asyncio
import requests
import json

client = discord.Client()

server = None;

def get_rank(name):
    url = "https://api.r6stats.com/api/v1/players/%s/seasons?platform=uplay" % name
    print("getting ranks...")
    r = requests.get(url)
    
    player = json.loads(r.text)
    if not player['seasons']:
        rank = None
    # elif player['seasons'][list(player['seasons'].keys())[0]]['emea']['ranking']['rank'] <= 4:
    #     rank = 'Cuivre'
    elif player['seasons'][list(player['seasons'].keys())[0]]['emea']['ranking']['rank'] <= 8:
        rank = 'Bronze'
    elif player['seasons'][list(player['seasons'].keys())[0]]['emea']['ranking']['rank'] <= 12:
        rank = 'Argent'
    elif player['seasons'][list(player['seasons'].keys())[0]]['emea']['ranking']['rank'] <= 16:
        rank = 'Or'
    elif player['seasons'][list(player['seasons'].keys())[0]]['emea']['ranking']['rank'] <= 20:
        rank = 'Platine'
    else:
        rank = 'Diamant'

    print("rank acquired")
    return rank

def define_role(name):
    rank = get_rank(name)
    for role in server.roles:
        if 'Bronze' in role.name:
            no_rank = role
        if rank and rank in role.name:
            print("role finded")
            return role
    return no_rank

@client.event
async def on_ready():
    global server
    server = client.get_server('server_id')

@client.event
async def on_message(message):
    if message.content.startswith('r6s rank'):
        name = message.content.split()[2]
        role = define_role(name)
        print("author: {}".format(message.author))
        print("role: {}".format(role.name))
        await client.add_roles(message.author, role)

client.run('token')

