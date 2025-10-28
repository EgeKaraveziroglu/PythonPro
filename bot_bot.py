import os
import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!') 

@bot.command()
async def yardım(ctx):
    await ctx.send(f"merhaba demek için $help hehehhehhe yazdırmak için $heh")

@bot.command()
async def bye(ctx):
    await ctx.send(f":D görüşürüz")


@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def ha(ctx, count_ha = 5):
    await ctx.send("ha" * count_ha)



@bot.command()
async def mem(ctx):
    images= os.listdir("mem")
    img_name = random.choice(images)
    with open(f'mem/{img_name}', 'rb') as f:
            picture = discord.File(f) 
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

bot.run("")
