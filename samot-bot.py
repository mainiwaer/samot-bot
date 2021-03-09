import discord
import os 
import sys

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.find('time') != -1:

        await message.channel.send('Is it time already...')

    if message.content.find('want') != -1:

        await message.channel.send("I can't have what I want :(")

client.run(os.environ['DISCORD_TOKEN'])