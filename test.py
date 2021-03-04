from dotenv import load_dotenv
import os
from os.path import join,dirname
import discord
import random
from discord.ext import commands
import emoji
import asyncio

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
  await channel.send("BOT ESTÁ ONLINE :green_circle:")
  

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

@client.command(brief = 'Jogo do galo')
async def galo(ctx):                                             #GANDA JOGO DO GALO MALUCO
    player1 = ctx.author
    if(ctx.message.content.lower() == "#galo"): #sem tagar ninguem
        msg = await ctx.send("O jogador que quiser enfrentar tem que reagir aqui no certo YA")
        
        def checkReaction(reaction, player2):
            if(player2 == msg.author):
                return False
            return str(reaction.emoji) == '\N{white heavy check mark}'

        try:
            certo = '\N{white heavy check mark}'
            await msg.add_reaction(certo)
            reaction, player2 = await client.wait_for('reaction_add', check = checkReaction, timeout=10.0)
        except asyncio.TimeoutError:
            return await ctx.send("Too long fool")
        else: #funcionou
            if(player1 == player2):
                await ctx.send("Burralho de treta nao te deixo jogar contigo proprio")
                return
            print("Siga nessa vanessa 1") 


    elif ctx.message.mentions: # com tag
        
        player2 = ctx.message.mentions[0]
        if player1 == player2:
            await ctx.send("Burralho de treta nao te deixo jogar contigo proprio")
            return
        msg = await ctx.send(f'Aceitar jogo do galo entre o grande {player1.mention} e grande noob {player2.mention}')

        def checkReaction(reaction, reactor):
            if(player2 == msg.author):
                return False
            return str(reaction.emoji) == '\N{white heavy check mark}' and reactor == player2 and player1 != reactor

        try:
            certo = '\N{white heavy check mark}'
            await msg.add_reaction(certo)
            reaction, player2 = await client.wait_for('reaction_add', check = checkReaction, timeout=10.0)
        except asyncio.TimeoutError:
            return await ctx.send("Too long fool")
        else:
            print("Siga boi")
    else:                                          # errado
        await ctx.send("usar: #galo @mention  ou apenas #galo")
        return
    

    #começa o jogo entre player1 e player2
    await ctx.send(f"JOGO DO GALO : {player1.mention} vs {player2.mention}")  
    
@client.command(brief='cara ou coroa') #Flip that coin sis
async def coin(ctx):
    a = 0
    
    
@client.command(brief='shut down BOT MOCS') #Disconnect
async def dc(ctx):
    if(ctx.author.id == 431857111018897409 or ctx.author.id == 366292034669248514):
        await ctx.send("BOT MOCS OFFLINE 🔴")
        await client.logout()
    else:
        await ctx.send("Não tens acesso a este codigo bem potente")

@client.command(brief ='Guess the dice :p') #JOGA ESSE DADO
@commands.cooldown(1, 5, commands.BucketType.user)
async def dice(ctx):

        def is_correct(m):
            return m.author == ctx.author

        answer = random.randint(1,6)
        try:
            await ctx.send(f"{ctx.author.mention} chuta um numero de 1 a 6 e vê se adivinhas")
            guess = await client.wait_for('message', check = is_correct, timeout=10.0)
        except asyncio.TimeoutError:
            return await ctx.send("Ès buèDA LENto ya")
        
        if (guess.content.isdigit()):
            if(int(guess.content) == answer):
                return await ctx.send(f"Siga {ctx.author.mention}, acertaste em cheio\n") 
            else:
                return await ctx.send(f"Burro do caralho {ctx.author.mention} , não sabes jogar isto\n")
        else:
            return await ctx.send(f"{ctx.author.mention} isso não é um numero nabo")


@client.command(brief='Saudações amigão') #Boas jovem
async def ola (ctx):
    await ctx.send(f'Olá, {ctx.author.mention}  :nerd:')

@client.command(brief='Recebe ganda conselho') #Concelho master
async def conselho(ctx):
    await ctx.send(randIspira())


@client.command(brief="Cota Milindro vai te subiR") #COTA MILINDRE
async def che(ctx):
    await ctx.send("CHE MADJÉ COTA MLINDRO TÁ ONLINE :green_circle:")
    message = await ctx.send(file=discord.File('milindro.PNG'))
    emoji = '\N{Heavy Black Heart}'
    await message.add_reaction(emoji)
    emoji = '\N{Smiling Face with Heart-Shaped Eyes}'
    await message.add_reaction(emoji)
    emoji = '\N{DOUGHNUT}'
    await message.add_reaction(emoji)

@client.command(brief="Guitapimpolho playlist") # guitapimpolho
async def guita(ctx):
    await ctx.send("https://www.youtube.com/watch?v=XsJo97effsk")
    return


def randIspira():
    pos = random.randint(0,linhas-1)    # inteiro
    f = open("messages.txt", "r", encoding="utf8")
    
    for position, str in enumerate(f):
      
        if position < pos:
            novastring = str
        else:
            #print(position)
            f.close()
            return novastring
    return "Não há mais inspiração para ti"
   
    
client.run(TOKEN_KEY) 
