@bot.command()
async def mem(ctx):
    res=os.listdir('images')
    UwU = random.choices([1,2,3], weights=[.6, .3, .1])
    img_name = res[int(''.join(map(str, UwU)))-1]
    with open(f'images/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)