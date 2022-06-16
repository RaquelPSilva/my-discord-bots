import os
import discord
from datetime import datetime
from pytz import timezone
from util import proxima_data

my_secret = os.environ['TOKEN']
client = discord.Client()

@client.event

# Evento: mensagem recebida
async def on_message(message):
  # Identificando o autor da mensagem
  if message.author == client.user:
    return
  if message.content == "$How long until the game starts?":
    autor = message.author
    nome = str(autor.display_name)
    papeis = autor.roles

    # Identificando o jogo do qual o autor participa
    jogo_ativo = ""
    for papel in (papeis):
      if papel.name == "Active1":
        jogo_ativo = "DotMM1"
        break
      elif papel.name == "Active2":
        jogo_ativo = "DotMM2"
        break

      # Preparando a resposta
    if jogo_ativo == "":
      mensagem = "I'm sorry, " + nome + ". I don't see your name in any active games. You'd better ask the DM."
    else:    
      fuso_dm = timezone("America/Sao_Paulo")
      agora = datetime.now(fuso_dm)
      if jogo_ativo == "DotMM1":
        dia_semana_jogo = 1
        hora_jogo = 21
        minuto_jogo = 30
      elif jogo_ativo == "DotMM2":
        dia_semana_jogo = 0
        hora_jogo = 19
        minuto_jogo = 30
      # Encontrando a data do próximo jogo
      proximo_jogo = proxima_data(dia_semana_jogo, fuso_dm)
      # Inserindo a informação de horário do jogo
      proximo_jogo = proximo_jogo.replace(hour = hora_jogo, minute = minuto_jogo, second = 0, microsecond = 0)
      delta = (proximo_jogo - agora).total_seconds()
      horas = delta // 3600
      minutos = (delta - horas * 3600) // 60
      if horas == 0:
        how_long = f"{minutos:.0f} minutes"
      else:
        how_long = f"{horas:.0f} hours and {minutos:.0f} minutes"
      mensagem = how_long + ", " + nome + "."
  elif message.content == "$Help":
    mensagem = "Type '$How long until the game starts?'"
  #Respondendo a pergunta
  await message.channel.send(mensagem)

client.run(os.getenv('TOKEN'))