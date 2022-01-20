import sys
import discord


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

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == 'salut':
        await message.channel.send(f'Coucouu {message.author.display_name}!')
        return

    if client.user in message.mentions:
        await message.channel.send("Qui me ping ?!")
        return



client.run(TOKEN)