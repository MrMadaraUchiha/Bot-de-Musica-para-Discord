import os
import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('GUILD')

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!levelup'):
        with open('levels.txt', 'r') as f:
            levels = f.read().splitlines()
        user_id = str(message.author.id)
        if user_id in levels:
            current_level = int(levels[user_id])
            current_level += 1
            levels[user_id] = str(current_level)
        else:
            levels[user_id] = '1'
        with open('levels.txt', 'w') as f:
            f.write('\n'.join(levels))

client.run(TOKEN)
