#!/usr/bin/env python3

import discord
import json
import random

with open('config.json') as config:
    config = json.load(config)

bot = discord.Bot()


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}#{bot.user.discriminator} ({bot.user.id})')
    print(f'https://discordapp.com/oauth2/authorize?&client_id={bot.user.id}&scope=scope=bot%20applications.commands&permissions=0')


@bot.slash_command(name='doot')
async def doot(ctx: discord.ApplicationContext):
    await ctx.respond(ctx.interaction.user.mention + ' doot doot')


@bot.slash_command(name='funnycatchphrase')
async def funnycatchphrase(ctx: discord.ApplicationContext):
    messages = ['Doot', 'AssFuck', 'Shit Bruh', 'Thank you very mulch']
    await ctx.respond(random.choice(messages))


@bot.slash_command(name='calciumfix')
async def calciumfix(ctx: discord.ApplicationContext):
    with open('gifs.txt') as file:
        gifs = file.readlines()
    await ctx.respond(random.choice(gifs).rstrip('\n'))


@bot.slash_command(name='spookmeter')
async def spookmeter(
                     ctx: discord.ApplicationContext,
                     level: discord.Option(str, 'Spookmeter Level', choices=['not spooky', 'spoopy', 'p spoopy', 'spooky', '2spooky'])
                     ):
    match level:
        case 'not spooky':
            await ctx.respond('https://i.imgur.com/OtHOWy4.gif')
        case 'spoopy':
            await ctx.respond('https://i.imgur.com/UvoCUa0.gif')
        case 'p spoopy':
            await ctx.respond('https://i.imgur.com/HmJXXfh.gif')
        case 'spooky':
            await ctx.respond('https://i.imgur.com/o1aLBqG.gif')
        case '2spooky':
            await ctx.respond('https://i.imgur.com/FToVdJR.gif')


bot.run(config['token'])
