from dotenv import load_dotenv
import os
from os.path import join,dirname
import discord
import random
from discord.ext import commands
import emoji

dotenv_path = join(dirname(__file__),'.env')
load_dotenv(dotenv_path)
TOKEN_KEY = os.environ.get("TOKEN")

client = commands.Bot(command_prefix = "#", case_insensitive = True)
linhas = sum(1 for line in open('messages.txt', encoding="utf8"))
channel = client.get_channel(816788040215298065)

#EVENTOS
@client.event    #IM IN SON
async def on_ready():
  print('Entramos como {0.user}' .format(client))
  channel = client.get_channel(816788040215298065)
  await channel.send("AYE IM IN THE MAINFRAME SON LEZ GE'IT")
  

@client.event    #Message handler
async def on_message(msg):
  
    if "ayy" in msg.content.lower():
        await msg.channel.send("LMAOOOO :smile:")
    if "love" in msg.content.lower():
        await msg.channel.send("Thats kinda gay ngl")
    if "#coin" == msg.content.lower():
        smile = '\N{SLIGHTLY SMILING FACE}'
        coroa = '\N{CROWN}'
        choice = random.randint(1,2)
        if(choice == 1):
            await msg.add_reaction(smile)
        else:
            await msg.add_reaction(coroa)
    await  client.process_commands(msg)


            
# COMANDOS
@client.command(brief='cara ou coroa') #Flip that coin sis
async def coin(ctx):
    a = 0
    
    
@client.command(brief='shut down BOT MOCS') #Disconnect
async def dc(ctx):
    await client.logout()

@client.command(brief ='Guess the dice :p')
async def dice(ctx):
    await ctx.send("Chuta um numero de 1 a 6 e vê se adivinhas")
    
    def is_correct(m):
        return m.author == ctx.author and m.content.isdigit()

    answer = random.randint(1,6)

    guess = await client.wait_for('message', check = is_correct, timeout = 5.0)

    if(int(guess.content) == answer):
        await ctx.send("Siga zeca, acertaste em cheio\n") 
    else:
        await ctx.send("Burro do caralho, foi ao lado\n")


@client.command(brief='Saudações amigão') #Boas jovem
async def ola (ctx):
    await ctx.send(f'Olá, {ctx.author.mention}  :nerd:')

@client.command(brief='Recebe ganda conselho') #Concelho master
async def conselho(ctx):
    await ctx.send(randIspira())


@client.command(brief="Cota Milindro vai te subiR") #COTA
async def che(ctx):
    await ctx.send("CHE MADJÉ COTA MLINDRO TÁ ONLINE :green_circle:")
    message = await ctx.send(file=discord.File('milindro.PNG'))
    emoji = '\N{Heavy Black Heart}'
    await message.add_reaction(emoji)
    emoji = '\N{Smiling Face with Heart-Shaped Eyes}'
    await message.add_reaction(emoji)
    emoji = '\N{DOUGHNUT}'
    await message.add_reaction(emoji)


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
