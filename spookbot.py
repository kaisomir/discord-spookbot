#!/usr/bin/env python3

import asyncio
import discord
import logging
import json

logger = logging.getLogger('spookbot')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='spookbot.log', mode='w', encoding='utf-8')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

with open("auth.json") as auth:
    auth = json.load(auth)

client = discord.Client()

commands = {}

def command(func):
    commands[func.__name__] = func
    return func

@client.event
async def on_message(message):
    for command in commands.keys():
        if message.content.startswith('.' + command):
            logger.info('Command `%s` called from message: %s', command, message.content)
            await commands[command](message)

# {{{ Commands

@command
async def doot(message):
    await client.send_message(message.channel, message.author.mention + ' doot doot')

@command
async def spookmeter(message):
    endswith = message.content.lower().endswith
    async def send(url):
        await client.send_message(message.channel, url)
        
    if endswith('not spooky') or endswith('1'):
        await send('https://i.imgur.com/OtHOWy4.gif')
    elif endswith('spoopy') or endswith('2'):
        await send('https://i.imgur.com/UvoCUa0.gif')
    elif endswith('p spoopy') or endswith('3'):
        await send('https://i.imgur.com/HmJXXfh.gif')
    elif endswith('spooky') or endswith('4'):
        await send('https://i.imgur.com/o1aLBqG.gif')
    elif endswith('2spooky') or endswith ('5'):
        await send('https://i.imgur.com/FToVdJR.gif')


# }}}

print("https://discordapp.com/oauth2/authorize?&client_id=365601279713476608&scope=bot&permissions=0")
client.run(auth['token'])
