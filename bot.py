import discord
from bot_logic import gen_pass
from bot_logic_2 import flip_coin
from discord.ext import commands
from bot_logic import get_duck_image_url
import os
import random

    # La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
    # Activar el privilegio de lectura de mensajes
intents.message_content = True
    # Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix="$", intents=intents)
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("hi!")

@bot.command()
async def bye(ctx):
    await ctx.send("😢👋")

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def coin(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def mem(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)


@bot.command()
async def mem_r(ctx):
    meme_r= random.choice(os.listdir("images"))
    with open(f'images/{meme_r}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
bot.run("")

