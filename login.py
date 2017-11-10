import discord
import asyncio

client = discord.Client()

@client.event
async  def on_ready():
    print('Conectado!')
    print('Nome de usuário: ' + client.user.name)
    print('ID: ' + client.user.id)

client.run('MzA5MDA4MTExMTQ4OTkwNDY0.DOeU_g.tOCfFwBDv4s_M-VdQn61uzYZbVs')


