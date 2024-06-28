import discord
import random
import os
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command(name='isbotcool')
async def _bot(ctx):
    await ctx.send('Да, я, FuelTankLover великолепен.')

@bot.command(name='8!')
async def _bot(ctx):
    await ctx.send('40320')

@bot.command(name='!8!')
async def _bot(ctx):
    await ctx.send('-40320')

#@bot.command(name='smile')
#async def _bot(ctx):
 #   await ctx.send(gen_emodji)

@bot.command(name='mem')
async def mem(ctx):
    img_name = random.choice(os.listdir('memes'))
    with open(f'memes/{img_name}', 'rb') as f:
            picture = discord.File(f)

@bot.command(name='rare_mem')
async def mem(ctx):
    raremem = random.randint(0, 10)
    if raremem <= 5:
        img_name = random.choice(os.listdir('meme_rare1'))
        with open(f'meme_rare1/{img_name}', 'rb') as f:
                picture = discord.File(f)
        await ctx.send(file=picture)
    elif raremem <= 6:
        img_name = random.choice(os.listdir('meme_rare2'))
        with open(f'meme_rare2/{img_name}', 'rb') as f:
                picture = discord.File(f)
        await ctx.send(file=picture)
    elif raremem == 10:
        img_name = random.choice(os.listdir('meme_rare3'))
        with open(f'meme_rare3/{img_name}', 'rb') as f:
                picture = discord.File(f)
        await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)




bot.run("")
