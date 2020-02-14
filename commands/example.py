def name():
    return 'example'

def aliases():
    return ['example1', 'example2']

async def run(client, message, args):
    await message.channel.send('CHDP is Great')