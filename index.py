import discord
import funcs

cmds = funcs.get_cmds()

client = discord.Client()
token = 'Your Bot\'s Token'
prefix = 'Your Bot\'s Prefix'
game = 'Your Bot\'s Game'

@client.event
async def on_ready():
    print('The Bot is ready!')
    await client.change_presence(status = discord.Status.online  , activity = discord.Game(game))

@client.event
async def on_message(message):
    if message.channel.type == 'private': return
    if message.author.bot: return
    if not message.content.startswith(prefix): return
    
    cmd = message.content.split(prefix)[1].split(' ')[0]
    args = message.content.split(cmd)[1][1:].split(' ')
    
    for c in cmds:
        if cmd in c[0]:
            await c[1].run(client, message, args)
            
            break

client.run(token)   
