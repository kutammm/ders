import discord
import requests
import os
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def mem(ctx):
    with open('images/mem2.png', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)


@bot.command()
async def rastgele(ctx):
    files= os.listdir('images')
    img_name=random.choice(files)
    with open(f"images/{img_name}", "rb") as f:
        picture = discord.File(f)
        await ctx.send(file=picture)


@bot.command()
async def geri_donusum(ctx, materyal: str):
    materyal = materyal.lower()
    if materyal in geri_donusum_rehberi:
        await ctx.send(geri_donusum_rehberi[materyal])
    else:
        await ctx.send(f"Üzgünüm, '{materyal}' için bir geri dönüşüm rehberi bulunamadı. Lütfen doğru bir materyal girin (plastik, kağıt, cam, metal, organik).")

geri_donusum_rehberi = {
    "plastik": "Plastik atıkları yıkayıp kuruttuktan sonra geri dönüşüm kutusuna atabilirsiniz.",
    "kağıt": "Kağıt ve karton atıkları temiz ve kuru bir şekilde geri dönüşüm kutusuna atabilirsiniz.",
    "cam": "Cam şişe ve kavanozları yıkayıp geri dönüşüm kutusuna atabilirsiniz.",
    "metal": "Metal kutuları ezip geri dönüşüm kutusuna atabilirsiniz.",
    "organik": "Organik atıkları kompost yapmak için kullanabilirsiniz."
}

@bot.command()
async def yardim(ctx):
    yardim_mesaji = (
        "Bu bot geri dönüşüm konusunda size yardımcı olabilir!\n"
        "Komutlar:\n"
        "- `.geri_donusum [materyal]`: Belirtilen materyalin nasıl geri dönüştürüleceğini öğrenin.\n"
        "- `.yardim`: Bu yardım mesajını gösterir."
    )
    await ctx.send(yardim_mesaji)



def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("token")
