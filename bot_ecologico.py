import discord
from discord.ext import commands
import random, os

    # La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
    # Activar el privilegio de lectura de mensajes
intents.message_content = True
    # Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix="_", intents=intents)
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("hola ecologista")
@bot.command()
async def ayuda(ctx):
    await ctx.send("comandos: maceta: muestra una imagen de macetas. maceta2: muestra una imagen de macetas. maceta3: muestra una imagen de macetas. maceta_r: muestra una imagen de macetas aleatorias entre las tres imagenes integrades del bot")

@bot.command()
async def instructivo(ctx):
    await ctx.send("paso 1: recorta una botella de plastico. paso 2: añade agujeros para filtrar el agua. paso 3: añade tierra y semillas paraplantar la planta. paso 4: espera hasta que la semilla germine y añade agua constantemente para que no se muera por deshidratación. paso 5: disfruta de la planta")



@bot.command()
async def maceta(ctx):
    with open('macetas/maceta1.png', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture )
    await ctx.send("paso 1: recorta una botella de plastico. paso 2: añade agujeros para filtrar el agua. paso 3: añade tierra y semillas paraplantar la planta. paso 4: espera hasta que la semilla germine y añade agua constantemente para que no se muera por deshidratación. paso 5: disfruta de la planta")

@bot.command()
async def maceta2(ctx):
    with open('macetas/maceta2.png', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def maceta3(ctx):
    with open('macetas/maceta3.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
@bot.command()
async def maceta_r(ctx):
    maceta_r= random.choice(os.listdir("macetas"))
    with open(f'macetas/{maceta_r}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

bot.run("")
