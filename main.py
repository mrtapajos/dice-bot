import discord 
from discord.ext import commands 
from random import randint, choice
import logging


# LOGGER
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# INTENTS 
intents = discord.Intents.default()
intents.members = True
intents.message_content = True


# BOT
bot = commands.Bot(command_prefix='!', intents=intents)


# EVENTOS

@bot.event
async def on_ready():
    print(f'''
    Loggin in the Tapajos' robot: {bot.user}...
    ID: {bot.user.id}''')

@bot.event
async def on_message(ctx):
    if bot.user.mentioned_in(ctx) and ctx.mention_everyone is False:
        await ctx.author.send("""
LISTA DE COMANDOS:

ROLAR DADO  ---> !roll `NdN` (número de dados(N) e número de lados(N))
ESCOLHER MEMBRO ALEATÓRIO DADO O CARGO  ---> !pick `nome do cargo`
REPETIR ALGO  ---> !repeat  `numero de vezes` `algo` """)
        
    await bot.process_commands(ctx)


# COMANDOS

@bot.command()
async def roll(ctx, dice: str):   
    try:
        rolls, limit = map(int, dice.split('d'))   
        print(rolls, limit, sep=' // ')    
    except Exception:
        await ctx.send('Format: NdN')
        return

    result = ', '.join(str(randint(1, limit)) for _ in range(rolls))
    await ctx.send(result)

@bot.command()
async def repeat(ctx, times: int, content='repetindo...'):
    for _ in range(times):
        await ctx.send(content)


# RANDOM MEMBER
@bot.command()
async def pick(ctx, role_name):
    role = discord.utils.get(ctx.guild.roles, name=role_name)
    if not role:
        await ctx.send(f'Cargo {role_name} não foi encontrado!')
        return
    
    members = [m for m in ctx.guild.members if role in m.roles]
    if not members:
        await ctx.send('Nenhum membro achado com esse cargo')
        return

    member = choice(members)
    await ctx.send(f'Escolhido: {member.mention}')

if __name__ == '__main__':
    bot.run(open('token.txt').readline())
