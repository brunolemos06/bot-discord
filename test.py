from dotenv import load_dotenv
import os
from os.path import join,dirname
import discord
import random
from discord.ext import commands

dotenv_path = join(dirname(__file__),'.env')
load_dotenv(dotenv_path)
TOKEN_KEY = os.environ.get("TOKEN")

client = commands.Bot(command_prefix = "#", case_insensitive = True)
linhas = sum(1 for line in open('messages.txt', encoding="utf8"))

#EVENTOS
@client.event    #IM IN SON
async def on_ready():
  print('Entramos como {0.user}' .format(client))
  channel = client.get_channel(816788040215298065)
  await channel.send("AYE IM IN SON")
  

  

@client.event    #ayy LMAO
async def on_message(msg):
  
    if "ayy" in msg.content:
        await msg.channel.send("LMAOOOO :smile:")
    await  client.process_commands(msg)

@client.listen() #love is gay
async def on_message(msg):
    if "love" in msg.content:
        await msg.channel.send("damn son thats kinda gay ngl")
    await client.process_commands(msg)

#COMANDOS
# @client.command(brief='cara ou coroa')
# async def moeda(ctx):
#     if(random.randint(1,2)==1):
#         print("cara")
#     else:
#         print("coroa")

    
@client.command(brief='End me')
async def dc(ctx):
    await client.logout()


@client.command(brief='Saudações amigão')
async def ola (ctx):
    await ctx.send(f'Olá, {ctx.author}  :nerd:')

@client.command(brief='Recebe ganda conselho')
async def conselho(ctx):
    await ctx.send(randIspira())


@client.command(brief="Cota Milindro vai te subiR")
async def che(ctx):
    await ctx.send("CHE MADJÉ COTA MLINDRO TÁ ONLINE :green_circle:")


def randIspira():
    pos = random.randint(0,linhas-1)    # inteiro
    f = open("messages.txt", "r", encoding="utf8")
    
    for position, str in enumerate(f):
      
        if position < pos:
            novastring = str
        else:
            print(position)
            f.close()
            return novastring
    return "Não há mais inspiração para ti"
   
    
client.run(TOKEN_KEY) 
