import discord
import os
import importlib
import asyncio
import inspect
import time

def get_varnames(func):
    return list(func.__code__.co_varnames)

async def use_func(func, *args):
    if check_async(func):
        await func(*args)
    else:
        func(*args)

def check_async(o):
    return inspect.iscoroutinefunction(o)

class CHDPClient(discord.AutoShardedClient):
    def __init__(self, prefix = None, spaceinprefix = False, command_dir = 'commands', sub_dir = True, ignore_folder = ['__pycache__', 'ignore'], logging = False):
        super().__init__()
        
        if prefix:
            self.prefix = prefix
        else: 
            self.prefix = ''
        
        self.spaceinprefix = spaceinprefix
        self.command_dir = command_dir
        self.sub_dir = sub_dir
        self.ignore_folder = ignore_folder
        self.logging = logging
        
        self.blacklist = []
        self.cmds = []
        self.cooltimelst = {}

        for f in os.listdir(command_dir):
            if not '.' in f and sub_dir:
                for f2 in os.listdir(command_dir + '/' + f):
                    if f2.endswith('.py'):
                        self.cmds.append(importlib.import_module(command_dir + '.' + f + '.' + f2.split('.')[0]))
                        self.log(f"Extension {command_dir + '.' + f + '.' + f2.split('.')[0]} Loaded")
            if f.endswith('.py'):
                self.cmds.append(importlib.import_module(command_dir + '.' + f.split('.')[0]))
                self.log(f"Extension {command_dir + '.' + f.split('.')[0]} Loaded")
    
    def run_server(self, token = None, bot = True):
        self.starttime = self.time()
        return self.run(token = token, bot = bot)

    def remove_cmd(self, cmdname):
        self.cmds.remove(importlib.import_module(str(cmdname)))
    
    def append_cmd(self, cmdname):
        self.cmds.append(importlib.import_module(self.command_dir + '.' + str(cmdname)))
    
    def reload_cmd(self, cmdname):
        self.remove_cmd(cmdname)
        self.cmds.append(importlib.reload(importlib.import_module(self.command_dir + '.' + str(cmdname))))
    
    @property
    def uptime(self):
        return self.time() - self.starttime

    async def change_presence_loop(self, games, wait = 5):
        await self.wait_until_ready()

        while not self.is_closed():
            for game in games:
                await self.change_presence(status = discord.Status.online, activity = discord.Game(str(game).replace('[u]', str(len(super().users))).replace('[g]', str(len(super().guilds))).replace('[p]', self.prefix)))
                await asyncio.sleep(wait)
    
    async def use_cmd(self, message):
        if not message.content.startswith(self.prefix): return
        if message.author.bot: return
        if message.author in self.blacklist: return
        
        ix = 0
        if self.spaceinprefix:
            ix = 1
        index = message.content.split(self.prefix)[1].split(' ')[ix]
        args = message.content.split(index)[1][1:].split(' ')

        self.log(f'{message.author.name}: Index - {index}\tArgs - {args}')

        async def error(c, code, msg):
            if 'error' in dir(c):
                await use_func(c.error, self, message, code, msg)

        async def run(c):
            dirs = dir(c)
            if 'before_run' in dirs:
                await use_func(c.beforerun)
            if 'use_per' in dirs:
                r = self.check_permissions(message.author, c.user_per)
                if not r: 
                    await error(c, code = 1, msg = 'Permission Required')
                    return
            if 'bot_per' in dirs:
                r = self.check_permissions(message.guild.me, c.user_per)
                if not r: 
                    await error(c, code = 2, msg = 'User Permission Required')
                    return 
            if 'cooltime' in dirs:
                tm = self.time()
                tmlst = self.get_item_lst(self.cooltimelst, 'name')
                v = self.get_item_lst(tmlst, str(message.author.id))
                if not (tm - v > int(c.cooltime)):
                    await error(c, code = 3, msg = 'Cooltime Not Passed')
                    return
            await use_func(c.run, self, message, args)
            if 'after_run' in dirs:
                await use_func(c.afterrun)

        for m in self.cmds:
            c = m
            if 'Command' in dir(c):
                c = c.Command()
                dirs = dir(c)
            if not 'name' in dirs and not index:
                await run(c)
                return
            if not 'aliases' in dirs and index == c.name: 
                await run(c)
                return
            if index in c.aliases or index == c.name:
                await run(c)
                return
    
    def log(self, msg):
        if self.logging:
            print(msg)
    
    def check_permissions(self, author, ps):
        c = []
        for p in ps:
            if not self.check_permission(author, p): return False
        return True

    def check_permission(self, author, p):
        memper = author.guild_permissions
        p = p.replace(' ', '_').lower()

        if memper.administrator:
            return True

        if p == '':
            return True

        elif p == 'guildowner':
            if author.guild.owner == author:
                return True
            else:
                return False
        
        elif p == 'create_instance_invite' and memper.create_instance_invite:
            return True

        elif p == 'kick_members' and memper.kick_members:
            return True
        
        elif p == 'ban_members' and memper.ban_members:
            return True
        
        elif p == 'manage_channels' and memper.manage_channels:
            return True
        
        elif p == 'manage_guild' and memper.manage_guild:
            return True
        
        elif p == 'add_reactions' and memper.add_reactions:
            return True
        
        elif p == 'view_audit_log' and memper.view_audit_log:
            return True
        
        elif p == 'priority_speaker' and memper.priority_speaker:
            return True
        
        elif p == 'stream' and memper.stream:
            return True
        
        elif p == 'send_ttx' and memper.send_tts:
            return True
        
        elif p == 'mention_everyone' and memper.mention_everyone:
            return True
        
        elif p == 'external_emojis' and memper.external_emojis:
            return True
        
        elif p == 'view_guild_insights' and memper.view_guild_insights:
            return True
        
        elif p == 'connect' and memper.connect:
            return True
        
        elif p == 'speak' and memper.speak:
            return True
        
        elif p == 'mute_members' and memper.mute_members:
            return True
        
        elif p == 'deafen_members' and memper.deafen_members:
            return True
        
        elif p == 'move_members' and memper.move_members:
            return True
        
        elif p == 'manage_emojis' and memper.manage_emojis:
            return True
        
        elif p == 'manage_webhooks' and memper.manage_webhooks:
            return True
        
        elif p == 'manage_roles' and memper.manage_roles:
            return True
        
        elif p == 'manage_nicknames' and memper.manage_nicknames and memper.change_nickname:
            return True
        
        elif p == 'use_voice_activation' and memper.use_voice_activation:
            return True
        
        else: return False
    
    async def get_reaction(self, msg, message, emojilist = ['⭕', '❌'], timeout = 60, cls_reaction = False):
        def check(reaction, user):
            return user == msg.author and str(reaction) in emojilist

        for e in emojilist:
            await message.add_reaction(str(e))

        try:
            reaction = await self.wait_for('reaction_add', timeout = timeout, check = check)
        except asyncio.TimeoutError:
            await asyncio.gather(message.delete(), message.channel.send(embed = discord.Embed(title = '시간이 종료되었습니다', description = f'{timeout}초가 지나서 자동으로 반응 콜랙터가 종료되었습니다', color = self.color.red)))
            return None
        else:
            if cls_reaction and message.guild.me.guild_permissions.manage_messages:
                await message.clear_reactions()
            return str(reaction[0].emoji)
    
    async def get_message(self, message, timeout = 60):
        def check(msg):
            return msg.channel == message.channel and msg.author == message.author
        
        try:
            m = await self.wait_for('message', timeout = timeout, check = check)
        except asyncio.TimeoutError:
            await message.channel.send(embed = discord.Embed(title = '시간이 종료되었습니다', description = f'{timeout}초가 지나서 자동으로 메시지 콜랙터가 종료되었습니다', color = self.color.red))
            return None
        else:
            return m
    
    def get_user_msg(self, message, index = 0):
        member = message.mentions
        try:
            if member[0]:
                return member[0]
        except Exception:
            pass
        try:
            userid = str(message.content).split(' ')[1 + index]
        except Exception:
            return message.author
        if userid == '봇':
            return message.guild.me
        try:
            user = message.guild.get_member(int(userid))
        except ValueError:
            return message.author
        if user:
            return user
        return message.author
    
    def get_item_lst(self, lst, k):
        try:
            return lst[str(k)]
        except KeyError:
            return 0
    def set_item_lst(self, lst, k, v):
        lst[str(k)] = v
        return lst
    
    def time(self):
        return round(time.time())
