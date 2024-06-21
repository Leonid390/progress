import discord
import random
import os
from bot_logic import gen_pass
from bot_logic import flip_coin
from bot_logic import gen_emodji
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

@bot.command(name='smile')
async def _bot(ctx):
    await ctx.send(gen_emodji)

bot.run("")