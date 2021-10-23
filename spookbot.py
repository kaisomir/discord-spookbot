#!/usr/bin/env python3

import asyncio
import discord
import json
import logging
import random
import re

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
# mee6 level up preventative measures
    if message.author.id == 159985870458322944 and re.search(r"deceived \d{1,2} times", message.content):
        channel = message.channel
        x = ''.join(str(e) for e in re.findall(r"deceived \d{1,2} times", message.content))
        x = ''.join(str(e) for e in re.findall(r"\d{1,2}", x))

        def check(message1):
            return x in message1.content and message1.channel == channel and message1.author.id != 757703113800024136
        msg = await client.wait_for('message', check=check, timeout=600.0)
        await channel.send(msg.author.mention + f", IT IS I THE GHOST OF HALLOWEEN!!!!!!! MUTHAFUCKA!!!!!!!!!!!!! \nYOU BITCH ASS JUST FUCKED UP!!!! U THINK U CAN SAY A NUMBER AFTER A LEVEL UP MESSAFGE SO EASILY>???? NOT ANYMORE BITXH!!!!! IM DRAGGING YOU DOWN TO HELL WHERE I WILL BE DRAGGING MY BALLS ALL OVER YOUR FACE!!! DUMBASS!!!!! REPENT FOR YOUR SINS!!!!!! YOUR LEVEL UP NUMBER POSTING IS NOT ADDING TO THE CONVERSATUON!!!!!! NOW DIE AND BURN IN HEELLLLL FOR ETERNIFY!!!!! \nhttps://cdn.discordapp.com/attachments/345239684009426955/893556706771087390/cool_ass_skeleton.gif".format(msg))
    for command in commands.keys():
        if message.content.startswith('.' + command):
            logger.info('Command `%s` called from message: %s', command, message.content)
            await commands[command](message)

# {{{ Commands

@command
async def doot(message):
    await message.channel.send(message.author.mention + ' doot doot')

@command
async def funnycatchphrase(message):
    messages = ["Doot", "AssFuck", "Shit Bruh"]
    await message.channel.send(random.choice(messages))

@command
async def calciumfix(message):
    messages = ["https://mbtskoudsalg.com/images/transparent-stuff-vaporwave-3.gif", "https://media.giphy.com/media/3ohhwqrNt7rd9yuj7O/source.gif", "https://tenor.com/view/waiting-skeleton-gif-6159814", "https://tenor.com/view/waiting-gif-9030040", "https://tenor.com/view/iphone-skeleton-gif-5452826", "https://tenor.com/view/skeleton-waiting-eating-bored-playing-around-gif-14558363", "https://tenor.com/view/shaking-skeleton-skeletons-gif-4757109", "https://tenor.com/view/skeleton-waiting-keyboard-bored-life-gif-14558359", "https://tenor.com/view/skeleton-tea-gif-10625213", "https://tenor.com/view/skeleton-ruby-swipe-hearts-gif-10625183", "https://media3.giphy.com/media/26BRDDhIt8oiyEjS0/source.gif", "https://media3.giphy.com/media/3o7TKpmHsAZiTTekve/source.gif", "https://media0.giphy.com/media/3o7TKqNtiUdqSfB6EM/source.gif", "https://media0.giphy.com/media/l3fQ6Fh6Ze3rMXn4A/source.gif", "https://media2.giphy.com/media/3o7TKJNbIxU09eccuI/source.gif", "https://media0.giphy.com/media/26BRxmqeqsRPBBOpy/source.gif", "https://media1.giphy.com/media/l46CpUQRyLgvVhvfW/source.gif", "https://media3.giphy.com/media/26BRCc2VNkdZ5tjvG/source.gif", "https://media2.giphy.com/media/l0MYzSbsaFfUZ1DTa/source.gif", "https://format-magazine-production-res.cloudinary.com/image/upload/c_limit,w_540,h_540,f_gif,f_auto/jjjjjohn-skeleton-4", "https://i.gifer.com/WYLS.gif", "https://media0.giphy.com/media/3owyp71e0oJZg3RQsw/source.gif", "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwi3o7_j3vvkAhXYGrkGHSQ1AKwQjRx6BAgBEAQ&url=%2Furl%3Fsa%3Di%26rct%3Dj%26q%3D%26esrc%3Ds%26source%3Dimages%26cd%3D%26ved%3D%26url%3Dhttps%253A%252F%252Fgiphy.com%252Fstickers%252Fskeleton-cds-making-it-rain-l0MYPqg7VQWLK9yWQ%26psig%3DAOvVaw2xm1MH0j04_SUAtE8P-Zw6%26ust%3D1570042508187445&psig=AOvVaw2xm1MH0j04_SUAtE8P-Zw6&ust=1570042508187445", "https://upload-assets.vice.com/files/2016/08/02/1470174545JohnKarel7.gif", "https://i.pinimg.com/originals/09/3e/4b/093e4b66b0a3d888db0184f4dc119204.gif", "https://media2.giphy.com/media/xTiTnpT1zjQ8msSQbS/source.gif", "https://i.pinimg.com/originals/c6/db/a2/c6dba2e9a5b48db157c6a2fea4a8b692.gif", "https://media3.giphy.com/media/26gJAECj4uH3zpjAQ/200w.gif", "https://pa1.narvii.com/6991/847644c6226d4e577370be3d4ac6c09b7159ac53r1-540-540_hq.gif", "http://artfcity.com/wp-content/uploads/2016/09/tumblr_o3lj2ehrmY1qza1qzo1_500.gif", "https://i.gifer.com/PaE.gif", "https://media2.giphy.com/media/l0MYR7ATNClP1GjcI/source.gif", "https://i.pinimg.com/originals/cd/e4/e2/cde4e242d5c3ace213a72d33cea9b16e.gif", "https://media1.giphy.com/media/3o6ZtaV6slZPhE0ftu/source.gif", "https://format-magazine-production-res.cloudinary.com/image/upload/c_limit,w_540,h_540,f_gif,f_auto/jjjjjohn-skeleton-9", "https://66.media.tumblr.com/d30560fbc829bcb17b9fd92844088487/tumblr_naes2zz8im1qza1qzo1_500.gif", "https://pa1.narvii.com/6991/533e5f5d561d5c58aff06092fbf12e6fdfb52ecar1-540-540_hq.gif", "https://upload-assets.vice.com/files/2016/08/02/1470174546JohnKarel10.gif", "https://i.kym-cdn.com/photos/images/original/001/186/745/526.gif", "https://media3.giphy.com/media/3o6ZtmOg5coyOIc3OU/source.gif", "https://upload-assets.vice.com/files/2016/08/02/1470174545JohnKarel6.gif", "https://i.pinimg.com/originals/b6/85/99/b6859978fb0af8249b58a52f4755647b.gif", "https://i.kym-cdn.com/photos/images/original/001/178/761/062.gif", "https://format-magazine-production-res.cloudinary.com/image/upload/c_limit,w_540,h_540,f_gif,f_auto/jjjjjohn-skeleton-6", "https://upload-assets.vice.com/files/2016/08/02/1470174545JohnKarel4.gif", "https://78.media.tumblr.com/a7411f14760a4d7978e735d55ed438a6/tumblr_nvdixx3Jxs1qac28vo1_r2_500.gif", "https://cdn.shopify.com/s/files/1/2128/8929/files/skeleton_pizzabites.gif?v=1559674098", "https://upload-assets.vice.com/files/2016/08/02/1470174546JohnKarel8.gif", "https://pa1.narvii.com/6991/1a26e49708a6234f5e34b495b0744ea2564a0623r1-540-540_hq.gif", "https://szx3iab.files.wordpress.com/2016/11/tumblr_n995vvy5dv1qza1qzo1_500.gif?w=352", "https://upload-assets.vice.com/files/2016/08/02/1470174544JohnKarel5.gif", "https://i.pinimg.com/originals/e7/1a/fb/e71afbdcda22ae75f71ddd438074504e.gif", "https://i.pinimg.com/originals/32/80/6f/32806fc20098726a64c8ff3021f80845.gif", "https://66.media.tumblr.com/e1dc70d9af348d26a9e9bae24fea7def/tumblr_p62tyfOY9a1qza1qzo1_540.gifv", "https://szx3iab.files.wordpress.com/2016/11/tumblr_nbvddjrphx1qza1qzo1_r1_500.gif?w=352", "https://i.kym-cdn.com/photos/images/original/001/181/074/55e.gif", "https://i.pinimg.com/originals/ea/28/e5/ea28e5e9c44c07fa5cee1011a80162cd.gif", "https://66.media.tumblr.com/6a49a3078ea1b35fc676812bd59c7bf8/tumblr_pfov6xxunm1qza1qzo1_540.gif", "https://pa1.narvii.com/6992/c80cbaad5797bcbbeb497db6f97317614959575br1-500-500_hq.gif", "https://66.media.tumblr.com/6fcc55ccbccd8cdad80a4c80eca8298a/tumblr_p9ihvfJ6Bg1qza1qzo1_540.gif", "https://414foto.com/image/289002-full_halloween-magic-gif-by-jjjjjohn-find-share-on-giphy.gif", "https://pa1.narvii.com/6991/145a1099ffab05aeefc24b787f3eaa91d5c245c5r1-540-540_hq.gif", "https://aws1.discourse-cdn.com/woot/original/3X/b/c/bcc6725e388cb4f1ddf0c242ca1f4b50169b912c.gif", "https://img.buzzfeed.com/buzzfeed-static/static/2015-11/18/21/enhanced/webdr03/anigif_original-921-1447900549-1.gif", "https://66.media.tumblr.com/f034b9b7e673fc704a946f845c4775d4/tumblr_nvzf29ynN71qza1qzo1_500.gif", "https://i2.wp.com/www.doperadcool.com/wp-content/uploads/2019/08/jjjjjohn-skeleton-plants-perfect-score.gif?fit=500%2C500&ssl=1", "https://i.pinimg.com/originals/a9/86/cc/a986cc2005b7be0f650f2b92a12a787e.gif", "https://pa1.narvii.com/6991/720fe80da48d6e095924cead73f1ba4da2218789r1-540-540_hq.gif", "https://media0.giphy.com/media/3o7TKWGiPEqIhF0Yrm/source.gif", "https://media.giphy.com/media/y6Xvxvx5Q37LW/giphy.gif", "https://media1.giphy.com/media/3oriNWxJAEYUt59Ego/source.gif", "https://aws1.discourse-cdn.com/woot/original/3X/7/1/71e6d474061c0a43bb671c0e2289fddfb6f81c97.gif", "https://66.media.tumblr.com/62ab226c367aa62d7f13d042486ff083/tumblr_pk23ycWYPE1qza1qzo1_r1_540.gif", "https://media2.giphy.com/media/5t4gL5cVbiN0nSyKkd/source.gif", "https://szx3iab.files.wordpress.com/2016/11/tumblr_nljo30cjit1qza1qzo1_500.gif?w=352", "https://pa1.narvii.com/6991/1823151f01188539eee8c67dfb806241abea6532r1-540-540_hq.gif", "https://media2.giphy.com/media/lJMgI0zIW8Wz49Qc13/source.gif", "https://aws1.discourse-cdn.com/woot/original/3X/b/7/b7c97a5d9f42ddfc429220fcc63a478010bec6d2.gif", "https://img.buzzfeed.com/buzzfeed-static/static/2019-09/23/3/asset/4d8c340c3380/anigif_sub-buzz-6141-1569209960-1.gif?output-quality=auto&output-format=auto&downsize=360:*", "https://aws1.discourse-cdn.com/woot/original/3X/d/b/dbbc1a1f1cbe907160e603da114603116b315252.gif", "https://media3.giphy.com/media/l46CxfeUUs4NV2KJ2/source.gif", "https://i.pinimg.com/originals/e8/e6/c6/e8e6c608e0346ffdcbc20a2344be62bd.gif", "https://i.pinimg.com/originals/ec/ca/89/ecca896e384db32a5b975a7c79741fa3.gif"]
    await message.channel.send(random.choice(messages))

@command
async def spookmeter(message):
    endswith = message.content.lower().endswith
    async def send(url):
        await message.channel.send(url)
        
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

print("https://discordapp.com/oauth2/authorize?&client_id=" + auth['clientId'] + "&scope=bot&permissions=0")
client.run(auth['token'])

