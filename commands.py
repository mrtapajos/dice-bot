import discord
from random import randint

def dice(cmd):
    num = int(cmd.replace('d', ''))
    random_number = randint(1, num+1)
    return f'Number: {random_number}'
   

    """ if msg == 'd2':
        msg.channel.send(randint(1,2))
    elif msg == 'd4':
        msg.channel.send(randint(1,4))
    elif msg == 'd6':
        msg.channel.send(randint(1,6))
    elif msg == 'd10':
        msg.channel.send(randint(1,10))
    elif msg == 'd12':
        msg.channel.send(randint(1,12))
    elif msg == 'd20':
        msg.channel.send(rand) """

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

