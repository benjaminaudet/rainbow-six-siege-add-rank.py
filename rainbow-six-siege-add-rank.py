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
import ranks as data
import config

client = discord.Client()

server = None;

def get_rank(name):
    url = "https://api.r6stats.com/api/v1/players/%s/seasons?platform=uplay" % name
    print("getting ranks of {}".format(name))
    r = requests.get(url)
    player = json.loads(r.text)
    if 'status' in player.keys() and 'failed' in player['status']:
        return False
    elif not player['seasons']:
        return 'Bronze'
    rank = data.ranks[player['seasons'][list(player['seasons'].keys())[0]]['emea']['ranking']['rank'] - 1]['label']
    return rank

def define_role(name):
    rank = get_rank(name)
    if not rank:
        return False
    for role in server.roles:
        if rank and rank in role.name:
            return role
    return get_role_by_name('Bronze')

def print_list_roles(list):
    for l in list:
        print(l.name)

def get_role_by_name(name):
    for role in server.roles:
        if name in role.name:
            return role
    return False

def delete_others_roles(author, rank):
    roles = []
    ranks_to_remove = data.get_ranks_to_remove(rank)
    for role in author.roles:
        for rank in ranks_to_remove:
            if rank in role.name:
                roles.append(role)
    author.roles = []

def print_author_and_rank(author, rank):
    print("author: {}".format(author))
    print("role: {}".format(rank))

async def username_not_exist(message):
    await client.send_message(message.channel, "This username doesn't exist in Uplay")
    print("This username doesn't exist in Uplay")

async def rank_command(message, index):
    if index == 0:
        name = message.author.nick
    else:
        name = message.content.split()[index]
    role = define_role(name)
    if not role:
        await username_not_exist(message)
        return
    print_author_and_rank(message.author, role.name)
    delete_others_roles(message.author, role.name)
    await client.add_roles(message.author, role)

@client.event
async def on_ready():
    print("ready...")
    global server
    server = client.get_server(config.server_id)

@client.event
async def on_message(message):
    if message.content.startswith('r6s rank'):
        await rank_command(message, 2)
    elif message.content.endswith('!rank'):
        await rank_command(message, 0)
    elif message.content.startswith('!rank'):
        await rank_command(message, 1)
        
    
client.run(config.token)

