import discord
from commands import*
from time import sleep

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

        # HELP COMMAND
        if msg.content.startswith('?') or msg.content.startswith('help'):
            await help(msg)
            return

        # DICE ROLLING
        if msg.content.startswith('d'):
            try:
                await msg.channel.send('Rolling dice...')
                sleep(2)               
                await msg.channel.send(dice(msg.content))
            except Exception as error:
                await msg.channel.send('Você fez algo de errado seu imbecil')
                await msg.channel.send(str(error))

        

client = MyClient(intents=intents)

if __name__ == '__main__':
    client.run(open('token.txt').readline())
