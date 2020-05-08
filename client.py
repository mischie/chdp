import discord
import os
import importlib
import asyncio

class CHDPClient(discord.AutoShardedClient):
    def __init__(self, prefix = None, games = ['CHDP 사용중', '키키는 천재임 ㅎㅎ'], wait = 5, command_dir = 'commands', sub_dir = True, ignore_folder = ['__pycache__', 'ignore']):
        super().__init__()
        
        if prefix:
            self.prefix = prefix

        self.command_dir = command_dir
        self.sub_dir = sub_dir
        self.ignore_folder = ignore_folder
        self.games = games
        self.wait = wait 

        self.cmds = []

        for f in os.listdir(command_dir):
            if not '.' in f and sub_dir:
                for f2 in os.listdir(command_dir + '/' + f):
                    if f2.endswith('.py'):
                        self.cmds.append(importlib.import_module(command_dir + '.' + f + '.' + f2.split('.')[0]))
            if f.endswith('.py'):
                self.cmds.append(importlib.import_module(command_dir + '.' + f.split('.')[0]))
    
    def remove_cmd(self, cmdname):
        self.cmds.remove(str(cmdname))
    
    def append_cmd(self, cmdname):
        self.cmds.append(importlib.import_module(self.command_dir + '.' + str(cmdname)))
    
    def reload_cmd(self, cmdname):
        self.remove_cmd(cmdname)
        self.append_cmd(cmdname)

    async def change_presence_loop(self):
        await super().wait_until_ready()

        while not super().is_closed():
            for game in self.games:
                await super().change_presence(status = discord.Status.online, activity = discord.Game(str(game).replace('[u]', str(len(super().users))).replace('[g]', str(len(super().guilds))).replace('[p]', self.prefix)))
                await asyncio.sleep(self.wait)
    
    async def use_cmd(self, message):
        if not message.content.startswith(self.prefix): return
        
        index = message.content.split(self.prefix)[1].split(' ')[0]
        args = message.content.split(index)[1][1:].split(' ')

        print(f'{message.author.name}: Index - {index}\tArgs - {args}')

        for c in self.cmds:
                continue
            if index in c.aliases or index == c.name:
                await c.run(self, message, args)
                return
