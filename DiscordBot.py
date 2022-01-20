import sys
import discord
import random

TOKEN = ''
f = open("TOKEN", "r")
TOKEN = f.read()

if TOKEN == '' :
    sys.exit("Token non défini")

client = discord.Client()

@client.event
async def on_ready():
    print('We have successfully loggged in as {0.user}'.format(client))
    sys.stdout.flush()

random_answers =  [
    "Très clairement !",
    "C'est évident.",
    "Beurk... Non !",
    "Peut-être...",
    "Je ne pense pas.",
]



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == 'salut':
        await message.channel.send(f'Coucouu {message.author.display_name} !')
        return

    if client.user in message.mentions:
        await message.channel.send("Qui me ping ?!")
        return

    if "?" in message.content:
        answer = random.choice(random_answers)
        await message.channel.send(answer)
        return


client.run(TOKEN)