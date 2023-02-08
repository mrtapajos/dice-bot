import discord
from random import randint

def dice(cmd):
    num = int(cmd.replace('d', ''))
    random_number = randint(1, num)
    return random_number
   


async def help(cmd):
    if cmd.content.startswith('?'):
       await cmd.author.send('''
---------- x DICES x -----------

d2 --> TWO SIDES
d4 --> FOUR SIDES
d6 --> SIX SIDES
d10 --> TEN SIDES
d12 --> TWELVE SIDES
d20 --> TWENTY SIDES
d100 --> ONE HUNDRED SIDES''')

    elif cmd.content.startswith('help'):
      await cmd.channel.send('Send anything with an "?" at the start for help!')

