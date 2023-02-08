import discord
from commands import*
import asyncio

intents = discord.Intents.default()
intents.message_content = True


# CREATING CLIENT
class MyClient(discord.Client):
    # WHEN BOT LOGS IN
    async def on_ready(self):
        print(f'{self.user} has logged in...\n__________')
    
    # WHEN A MESSAGE IS SENT
    async def on_message(self, msg):

        # ignore bot messages
        if msg.author == self.user:
            return

        # AQUI TA FUNCIONANDO POR ENQUANTO
        if msg.content.startswith('?') or msg.content.startswith('help'):
            await help(msg)
            return

        # NÃO PODE COMEÇAR COM D
        if msg.content.startswith('d'):
            e = msg.content.replace('d', '')
            try:               
                await msg.channel.send(str((dice(e))))
            except:
                await msg.channel.send('Você fez algo de errado seu imbecil')

        

client = MyClient(intents=intents)

if __name__ == '__main__':
    client.run(open('token.txt').readline())


