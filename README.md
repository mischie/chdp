# CHDP
CHDP-Commands Handler for Discord.Py

[Server1](https://discord.gg/8AhTEAt)

[Server2](https://discord.gg/XSSbcvm)

[Invite Bot made with this](https://discordapp.com/api/oauth2/authorize?client_id=676003241129017354&permissions=8&scope=bot)

## Download It

[Google Drive](https://drive.google.com/file/d/19yZBTg2AwRIz27AhlqrKcP4qqNdexJ-_/view?usp=sharing)

## How to use it

Don't touch the `command.py`

Open the `index.py`

Change variable prefix to your bot's prefix

Change variable token to your bot's token

Change variable game to your bot's Game

Then close index.py

Make a new python file on the folder `commands` 

Make a function `name()` on that file

Make that function `name()` would return the command's name

Make a function `aliases()` on that file

Make that function `aliases()` would return an list of command's aliases

Make a async function `run(client, message, args)` 

Make that function`run(client, message, args)` would do what the command must do

client is the client

message is the message 

args is the message.content splited with spaces

There is an example file on the commands folder

```python
def name():
    return 'example'

def aliases():
    return ['example1', 'example2']

async def run(client, message, args):
    await message.channel.send('CHDP is Great')
```

Thanks for using it^^

