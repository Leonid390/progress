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
    await ctx.send(f'Привет! Я бот {bot.user}, я буду ведать об экологии!')

@bot.command(name='isbotcool')
async def _bot(ctx):
    await ctx.send('Да, я, FuelTankLover великолепен.')

@bot.command(name='eco_mem')
async def eco_mem(ctx):
    raremem = random.randint(1, 99)
    if raremem <= 39:
        img_name = random.choice(os.listdir('meme_rare1'))
        with open(f'meme_rare1/{img_name}', 'rb') as f:
                picture = discord.File(f)
        await ctx.send(file=picture)
        await ctx.send('выращивание и сбор растений, содержание животных, производство продуктов животного происхождения, переработка, упаковка и логистика - всё это часть экологии')
    elif raremem <= 40:
        img_name = random.choice(os.listdir('meme_rare2'))
        with open(f'meme_rare2/{img_name}', 'rb') as f:
                picture = discord.File(f)
        await ctx.send(file=picture)
        await ctx.send('Браконьерство это очень важная проблема общества и государства. Из-за браконьерства, страдает экологическая система, лесов, рек, парков, озер, лугов, полей. Неумеренная охота и браконьерство приводит к истреблению некоторых видов животных, населяющих лес.')
    #elif raremem == 100:
     #   await ctx.send('когда Ктулху проснётся, то небеса заплачут кровавыми слёзами, реки будут кипеть и выходить из берегов, а морские животные будут источать яд мёртвими телами...')


@bot.command(name='recycle_plastic')
async def recycle_plastic(ctx):
    await ctx.send('Пластиковые предметы перерабатываются следующим образом: сначала они тщательно очищаются, промываются и сушатся на специальном оборудовании. Высушенные предметы измельчаются, плавятся и преобразуются в нити для трёхмерной печати. Полученные нити заправляются в 3D-принтер. Если нет желания этим заниматься, то можно сдавать в оранжевый ящик')

@bot.command(name='recycle_glass')
async def recycle_glass(ctx):
    await ctx.send('Прежде чем сдать стекло, его надо ополоснуть от остатков содержимого и снять с тары крышку. Этикетку отрывать не нужно. При этом вместе со стеклом нельзя сдавать на переработку: керамическую и стеклянную посуду (бокалы, стаканы, кружки, тарелки). Переработка в домашних условиях невозможна, следует сдавать в зеленый ящик')

@bot.command(name='recycle_organic')
async def recycle_organic(ctx):
    await ctx.send('При переработки органики можно получить очень полезное удобрение для сада — компост, который в садовых центрах стоит от 80 до 120 рублей за литр. Органику сдавать в чёрный ящик')

@bot.command(name='recycle_paper')
async def recycle_paper(ctx):
    await ctx.send('Переработка бумаги выглядит следующим образом: Бумага нарезается на мелкие кусочки и нагревается, чтобы запустить процесс рециркуляции целлюлозы. После этого бумагу готовят к переработке, смешивая с водой в специальной машине, похожей на гигантский миксер.')

bot.run("")