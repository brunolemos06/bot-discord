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
channel = client.get_channel(816788040215298065)

#EVENTOS
@client.event    #IM IN SON
async def on_ready():
  print('Entramos como {0.user}' .format(client))
  channel = client.get_channel(816788040215298065)
  await channel.send("BOT ESTÁ ONLINE :green_circle:")
  

@client.event    #Message handler
async def on_message(msg):
    if(msg.author.id != 816787135825838090):
        if "ayy" in msg.content.lower():
            await msg.channel.send("LMAOOOO :smile:")
        if "love" in msg.content.lower():
            await msg.channel.send("Thats kinda gay ngl")
        if ('caralho' in msg.content.lower() or 'merda' in msg.content.lower()):
            await msg.channel.send("NAO DIGAS ASNEIRAS NESTE DISCORD CARALHO, ESTAS TODO TURBINADO")
        await  client.process_commands(msg)


############################----GALO----#########################
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
            #print("Siga nessa vanessa 1") 


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
    else:                                          # errado
        await ctx.send("usar: #galo @mention  ou apenas #galo")
        return
    

    #começa o jogo entre player1 e player2
    await ctx.send(f"JOGO DO GALO : {player1.mention} vs {player2.mention}")
    # await ctx.send("Utilizar numeros de 1 a 9 para jogar")
    simbplayer1 = '🟢'
    simbplayer2 = '❌'
    array = init_galo()
    
    await print_galo(array,player1.mention, ctx)
    current_player=player1
    numjogadas = 0

    def jogadorCerto(m):
        return m.author == current_player

    while not check_end_galo(array,numjogadas):
        play = await client.wait_for('message', check=jogadorCerto)
        print(play.content)
        if not play:
            await ctx.send("Jogador errado ó nabo!")        
        if not check_empty_pos_galo(array, (int)play.content-1):
            await ctx.send("Jogada inválida!")
        
        jogada = play.content
        x = jogada/3
        y = jogada%3
        if current_player == jogador1:
            array[x][y] = simbplayer1
            current_player = jogador2
        elif current_player == jogador2:
            array[x][y] = simbplayer2
            current_player = jogador1
        else:
            print("Jogador Inválido")
        numjogadas = numjogadas + 1
        await print_galo(array,current_player.mention, ctx)
        

        

def check_end_galo(array,numjogadas):
    
    end = False
    if numjogadas == 9:
        return True
    if(array[0][0] == array[0][1] == array[0][2]) and array[0][0]!="⬛":
        end = True
    elif(array[1][0] == array[2][1] == array[1][2]and array[1][0]!="⬛"):
        end = True
    elif(array[2][0] == array[2][1] == array[2][2]and array[2][0]!="⬛"):
        end = True
    elif(array[0][0] == array[1][0] == array[2][0]and array[0][0]!="⬛"):
        end = True
    elif(array[0][1] == array[1][1] == array[2][1]and array[0][1]!="⬛"):
        end = True
    elif(array[0][2] == array[1][2] == array[2][2]and array[0][2]!="⬛"):
        end = True
    elif(array[0][0] == array[1][1] == array[2][2]and array[0][0]!="⬛"):
        end = True
    elif(array[0][2] == array[1][1] == array[2][0]and array[0][2]!="⬛"):
        end = True
    return end

def check_empty_pos_galo(array, pos):
    # x = pos/3;
    # y = pos%3;
    if(array[pos/3,pos%3] == "⬛"):
        return True
    return false

def init_galo():
    n = 3
    array = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            array[i][j] = "⬛"
    return array

async def print_galo(array, jogador, ctx):
    embed = discord.Embed(title="Jogo Do Galo",description = "jogador->"+jogador,color = discord.Colour.red())
    embed.set_thumbnail(url = "https://i.pinimg.com/originals/94/ac/6c/94ac6c4d019bea87e1a7e6fb2ce26b23.jpg")
    embed.set_footer(text="Utilizar numeros de 1 a 9 para jogar")
    embed.add_field(name = f"{array[0][0]}   |", value = '----', inline=True)
    embed.add_field(name = f"{array[0][1]}   |", value = '----', inline=True)
    embed.add_field(name = f"{array[0][2]}", value = '----', inline=True)
    embed.add_field(name = f"{array[1][0]}   |", value = '----', inline=True)
    embed.add_field(name = f"{array[1][1]}   |", value = '----', inline=True)
    embed.add_field(name = f"{array[1][2]}", value = '----', inline=True)
    embed.add_field(name = f"{array[2][0]}   |", value = '----', inline=True)
    embed.add_field(name = f"{array[2][1]}   |", value = '----', inline=True)
    embed.add_field(name = f"{array[2][2]}", value = '----', inline=True)
    await ctx.send(embed=embed)
    

############----COIN----############
@client.command(brief='cara ou coroa') #Flip that coin sis
async def coin(ctx):
    smile = '\N{SLIGHTLY SMILING FACE}'
    coroa = '\N{CROWN}'
    choice = random.randint(1,2)
    if(choice == 1):
        return await ctx.message.add_reaction(smile)
    else:
        return await ctx.message.add_reaction(coroa)

###########----DISCONNECT----#############  
@client.command(brief='shut down BOT MOCS') #Disconnect
async def dc(ctx):
    # amaral e bruno autorizados
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
    linhas = sum(1 for line in open('messages.txt', encoding="utf8"))
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
    linhas = sum(1 for line in open('guitz.txt', encoding="utf8"))
    pos = random.randint(0,linhas-1)    # inteiro
    f = open("guitz.txt", "r", encoding="utf8")
    
    for position, str in enumerate(f):
      
        if position < pos:
            novastring = str
        else:
            f.close()
            return await ctx.send(novastring)       
    return "Não há mais inspiração para ti"

client.run(TOKEN_KEY) 
