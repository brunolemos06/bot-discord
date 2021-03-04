from dotenv import load_dotenv
import os
from os.path import join,dirname
import discord
import random
from discord.ext import commands
import emoji
import asyncio
#from disco.types.message import MessageEmbed

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
############----GALO----##############
@client.command(brief = 'Jogo do galo')
@commands.cooldown(1, 10, commands.BucketType.user)
async def galo(ctx):                                                #GANDA JOGO DO GALO MALUCO
    player1 = ctx.author
    if(ctx.message.content.lower() == "#galo"): #sem tagar ninguem
        msg = await ctx.send(f"Quem quer jogar ao galo com {player1.mention}")
        
        def checkReaction(reaction, player2):
            if(player2 == msg.author):
                return False
            return str(reaction.emoji) == '\N{white heavy check mark}'

        try:
            certo = '\N{white heavy check mark}'
            await msg.add_reaction(certo)
            reaction, player2 = await client.wait_for('reaction_add', check = checkReaction, timeout=10.0)
        except asyncio.TimeoutError:
            return await ctx.send("Jogo do Galo: Demorou muito tempo a aceitar o pedido de jogo")
        else: #funcionou
            if(player1 == player2):
                await ctx.send("Jogo do Galo : não podes jogar contigo mesmo lul")
                return
            print("Siga nessa vanessa 1") 


    elif ctx.message.mentions: # com tag
        
        player2 = ctx.message.mentions[0]
        if player1 == player2:
            await ctx.send("BARRAQUEIRO da treta nao te deixo jogar contigo proprio")
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
    await ctx.send("Utilizar numeros de 1 a 9 para jogar")
    simbplayer1 = '🟢�'
    simbplayer2 = '❌'
    array = init_galo()
    
    await print_galo(ctx,player1.mention)
    current_player=player1
        
        


def check_end_galo(array):
    end = False
    if(array[0][0] == array[0][1] == array[0][2]):
        end = True
    elif(array[1][0] == array[2][1] == array[1][2]):
        end = True
    elif(array[2][0] == array[2][1] == array[2][2]):
        end = True
    elif(array[0][0] == array[1][0] == array[2][0]):
        end = True
    elif(array[0][1] == array[1][1] == array[2][1]):
        end = True
    elif(array[0][2] == array[1][2] == array[2][2]):
        end = True
    elif(array[0][0] == array[1][1] == array[2][2]):
        end = True
    elif(array[0][2] == array[1][1] == array[2][0]):
        end = True
    return end

def check_empty_pos_galo(array,pos):
    # x = pos/3;
	# y = pos%3;
    if(array[pos/3,pos%3] == "⬜"):
        return True
    return false

def init_galo():
    n = 3
    array = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            array[i][j] = "⬜"
    return array

async def print_galo(ctx,name):
    embed = discord.Embed(title="Jogo Do Galo",description = name,color = discord.Colour.red())
    embed.add_field(name = "⬜   |", value = '----', inline=True)
    embed.add_field(name = "⬜   |", value = '----', inline=True)
    embed.add_field(name = "🟢", value = '----', inline=True)
    embed.add_field(name = "❌   |", value = '----', inline=True)
    embed.add_field(name = "❌   |", value = '----', inline=True)
    embed.add_field(name = "⬜", value = '----', inline=True)
    embed.add_field(name = "⬜   |", value = '----', inline=True)
    embed.add_field(name = "🟢   |", value = '----', inline=True)
    embed.add_field(name = "⬜", value = '----', inline=True)
    await ctx.send(embed=embed)
    

############----COIN----############
@client.command(brief='cara ou coroa') #Flip that coin sis
async def coin(ctx):
    a = 0

    
###########----DISCONNECT----#############  
@client.command(brief='shut down BOT MOCS') #Disconnect
async def dc(ctx):
    if(ctx.author.id == 431857111018897409 or ctx.author.id == 366292034669248514):
        await ctx.send("BOT MOCS OFFLINE 🔴")
        await client.logout()
    else:
        await ctx.send("Não tens acesso a este codigo bem potente")


##############----DICE----#################
@client.command(brief ='Guess the dice :p') #JOGA ESSE DADO
@commands.cooldown(1, 7, commands.BucketType.user)
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


#############----OLA----################
@client.command(brief='Saudações amigão') #Boas jovem
async def ola (ctx):
    await ctx.send(f'Olá, {ctx.author.mention}  :nerd:')


############----CONCELHO----#################
@client.command(brief='Recebe ganda conselho') #Concelho master
async def conselho(ctx):
    await ctx.send(randIspira())


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


############----COTA-MILINDRO----#################
@client.command(brief="Cota Milindro vai te subiR") #COTA MILINDRE
async def che(ctx):
    await ctx.send("CHE MADJÉ COTA MLINDRO VAI TE SUBIR LÁ HM")
    message = await ctx.send(file=discord.File('milindro.PNG'))
    emoji = '\N{Heavy Black Heart}'
    await message.add_reaction(emoji)
    emoji = '\N{Smiling Face with Heart-Shaped Eyes}'
    await message.add_reaction(emoji)
    emoji = '\N{DOUGHNUT}'
    await message.add_reaction(emoji)

#############----GUITA----####################
@client.command(brief="Guitapimpolho playlist") # guitapimpolho
async def guita(ctx):
    x = sum(1 for line in open('guitz.txt', encoding="utf8"))
    pos = random.randint(0, x-1)
    f = open("guitz.txt", "r", encoding="utf8")
    for position, str in enumerate(f):
      
        if position < pos:
            novastring = str
        else:
            f.close()
            await ctx.send(novastring)
    return "Não há mais guitz pimpoilz para ti"
   
    
client.run(TOKEN_KEY) 
