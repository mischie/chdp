class Command:
  name = '키키'
  async def run(self, client, message, args):
    await message.channel.send('키키')
