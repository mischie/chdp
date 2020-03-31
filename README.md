# CHDP
![Made by kiki](https://img.shields.io/badge/Made%20By%20KIKI-Good%20Job-brightgreen)
CHDP-Commands Handler for Discord.Py

[Server1](https://discord.gg/8AhTEAt)

[Server2](https://discord.gg/XSSbcvm)

[Invite Bot made with this](https://discordapp.com/api/oauth2/authorize?client_id=676003241129017354&permissions=8&scope=bot)

## Download It

git clone https://github.com/kiki7000/chdp.git

## How to use it

Don't touch the `command.py`

Open the `index.py`

Change variable prefix to your bot's prefix

Change variable token to your bot's token

Change variable game to your bot's Game

Then close index.py

Make a new python file on the folder `commands` 

Make a array `aliases` on that file

Make that array `aliases` would have an list of command's aliases

Make a async function `run(client, message, args)` 

Make that function`run(client, message, args)` would do what the command must do

client is the client

message is the message 

args is the message.content splited with spaces

There is an example file on the commands folder

```python
aliases = ['example', 'example1']

async def run(client, message, args):
    await message.channel.send('CHDP is Great')
```

Thanks for using it^^

