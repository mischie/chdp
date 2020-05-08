import client as chdpclient

client = chdpclient.CHDPClient(prefix = '!', games = ['키키천재임', '전에메시지거짓임', '나말고 다 거짓임', '응?!'], command_dir = 'commands')

@client.event
async def on_message(message):
  await client.use_cmd(message)

client.run('키키키키키키(이거 토큰임 오해하지 마3')
