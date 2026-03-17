import os
import random
import discord
from discord.ext import commands
from bot_token import TOKEN
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


@bot.command()
async def rastgele_emoji(ctx):
    emojiler=["😀", "😃", "😁", "🤬", "🥳", "👾", "🎃", "🤑", "🤔"]
    emoji=random.choice(emojiler)
    await ctx.send(emoji)

@bot.command()
async def rastgele_cızgıemoji(ctx):
    cızgı_emojiler=["(─ ‿ ─)", "(づ๑•ᴗ•๑)づ♡", "⇄ ◀ 𓊕 ▶ ↻", "︶ ⏝ ︶ ୨୧ ︶ ⏝ ︶", "࿔‧ ֶָ֢˚˖𐦍˖˚ֶָ֢ ‧࿔", "ᓚ₍⑅^..^₎", "/ᐠ˵- ⩊ -˵マ", "(๑>؂•̀๑)", "/ᐠ˵- ⩊ -˵マ"]
    cızgı_emoji=random.choice(cızgı_emojiler)
    await ctx.send(cızgı_emoji)


@bot.command()
async def sifre_uret(ctx, uzunluk: int):
    if 1 <= uzunluk <= 10:
        karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        sifre = ''.join(random.choice(karakterler) for _ in range(uzunluk))
        await ctx.send(f" Rastgele şifren: `{sifre}`")
    else:
        await ctx.send("Lütfen 1 ile 10 arasında bir sayı gir.")

@bot.command()
async def detect(ctx):
    
    if ctx.message.attachments:
        await ctx.send("Algılama başladı...")
        for attachment in ctx.message.attachments:
            filename = attachment.filename
            await attachment.save(f"images/{filename}")
    else:
       await ctx.send("Lütfen bir fotoğraf yükleyin.")
    


bot.run(TOKEN)

