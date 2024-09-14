import discord
from bot_logic import gen_pass
from bot_logic_2 import flip_coin
from discord.ext import commands
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

bot.run("")

