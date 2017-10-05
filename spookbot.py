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

@client.event
async def on_message(message):
    if message.content[0:5] == '.doot':
        await client.send_message(message.channel, message.author.mention + ' doot doot')


print("https://discordapp.com/oauth2/authorize?&client_id=365601279713476608&scope=bot&permissions=0")
client.run(auth['token'])
