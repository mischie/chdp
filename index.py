import discord
import os
import command

client = discord.Client()
token = 'Your Bot\'s Token'
prefix = 'Your Bot\'s Prefix'
game = 'Your Bot\'s Game'

@client.event
async def on_ready():
    print('The Bot is ready!')
    await client.change_presence(status=discord.Status.online  , activity=discord.Game(game))

@client.event
async def on_message(message):
    if message.channel.type == 'private': return
    if message.author.bot: return
    if message.content.startswith(prefix) == False: return

    await command.cmdrun(client, message, prefix)


client.run(token)   