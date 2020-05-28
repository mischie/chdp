import client as chdpclient

client = chdpclient.CHDPClient(prefix = '!')

@client.event
async def on_message(message):
  await client.use_cmd(message)

client.run('키키키키키키(이거 토큰임 오해하지 마3')
