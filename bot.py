from dotenv import load_dotenv
import os
from os.path import join,dirname
import discord
import random as ran
from discord.ext import tasks,commands
import emoji
import asyncio
from randomMessages import randomline
import time
import youtube_dl
from discord.voice_client import VoiceClient
from requests import get
from youtube_dl import YoutubeDL
from discord import FFmpegPCMAudio
from discord.utils import get
from asyncio import sleep
from niveis import readJSON,writeJSON,storeXP
from weather import InfoByCity


dotenv_path = join(dirname(__file__),'.env')
load_dotenv(dotenv_path)
TOKEN_KEY = os.environ.get("TOKEN")
APIKEY = os.environ.get("APIKEY")
listgalo = []
listmusics ={}
listtitles ={}
listemojiAJ=["🇦","🇧","🇨","🇩","🇪","🇫","🇬","🇭","🇮","🇯"]
prefix = "$"
client = commands.Bot(command_prefix = prefix, case_insensitive = True)
channel = client.get_channel(817878165325611069)

#EVENTOS
@client.event    #IM IN SON
async def on_ready():
 print('BotMOCS está online: {0.user}' .format(client))
    #channel = client.get_channel(817878165325611069)
    #await channel.send("BOT ESTÁ ONLINE :green_circle:")

@client.event    #Message handler
async def on_message(msg):
    if(msg.author.id != 816787135825838090):
        if "ayy" in msg.content.lower():
            await msg.channel.send("LMAOOOO :smile:")
        if "love" in msg.content.lower():
            await msg.channel.send("Thats kinda gay ngl")
        if ('caralho' in msg.content.lower() or 'merda' in msg.content.lower() or 'foda-se' in msg.content.lower() or 'puta' in msg.content.lower()):
            await msg.channel.send("NAO DIGAS ASNEIRAS NESTE DISCORD CARALHO, ESTAS TODO TURBINADO")
        if "che" in msg.content.lower():
            await msg.channel.send("CHE MADJÉ COTA MLINDRO VAI TE SUBIR LÁ HM")
            message = await msg.channel.send(file=discord.File('.png/milindro.png'))
            emoji = '\N{Heavy Black Heart}'
            await message.add_reaction(emoji)
            emoji = '\N{Smiling Face with Heart-Shaped Eyes}'
            await message.add_reaction(emoji)
            emoji = '\N{DOUGHNUT}'
            await message.add_reaction(emoji)
        if "turbina" in msg.content.lower():
            await msg.channel.send(file=discord.File('.png/turbina.png'))
        if "satelite" in msg.content.lower():
            await msg.channel.send(file=discord.File('.png/satelite.png'))
        if ('cona' in msg.content.lower() or 'penis' in msg.content.lower() or 'pila' in msg.content.lower() or 'vagina' in msg.content.lower() or 'pipi' in msg.content.lower() or 'dick' in msg.content.lower() or 'pussy' in msg.content.lower() or 'piça' in msg.content.lower()) :
            await msg.channel.send("ESTÁS COM FALTA DE PENIS OU DE CONA HMMMM ?")
        if  '<@!816787135825838090>' == msg.content :
            embed = discord.Embed(title="Settings for this server",description = f" -> The prefix is **{prefix}**",color = discord.Colour.green())
            embed.set_thumbnail(url = client.user.avatar_url)
            embed.set_footer(text="Enjoy our amazing BOTMOCS e fica com a maior moca de todos os tempos !!!")
            await msg.channel.send(embed=embed)
        if (prefix+"concelho") == msg.content:
            await msg.channel.send("CHE GANDA BURRO NAO É assim que se pede um conselho YA")
        if (prefix+"credits") == msg.content.lower():
            await  creditos(msg.channel)
        await  client.process_commands(msg)

#COMANDOS
##########----temp----##############
@client.command(brief="Mostra a temperatura para hoje numa cidade", help=f"Uso : {prefix}temp cidade")
@commands.cooldown(1,5,commands.BucketType.user)
async def temp(ctx,city):
    #try:
    temp,iconurl = InfoByCity(city,APIKEY)
    embed = discord.Embed(title="Informação do tempo",description = f"Em {city}:", color = discord.Colour.blue())
    embed.set_thumbnail(url=iconurl)
    embed.add_field(name=f"Temperatura", value=f"{temp}", inline=False)
    return await ctx.send(embed=embed)
   # except:
        #return await ctx.send("`Cidade inválida`")
##########----XP----##############
@client.command(brief="Mostra os niveis das pessoas jogaDORAS", help=f"Uso : {prefix}xp ou {prefix}xp @user")
@commands.cooldown(1,2,commands.BucketType.user)
async def xp(ctx, mention:str=None):
    niveis = readJSON()     
    if mention == None:
        cont = 0
        embed = discord.Embed(title="MALTA PRO NO JOGO",description = "Níveis dos 7 melhores jogadores", color = discord.Colour.red())
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Video_game_controller_icon_designed_by_Maico_Amorim.svg/1200px-Video_game_controller_icon_designed_by_Maico_Amorim.svg.png")
        ordenado = sorted(niveis, key=niveis.get, reverse=True)
        for user in ordenado:
            cont+=1
            embed.add_field(name=f"Top {cont} - {niveis[user]} XP", value="<@"+user+">", inline=False)
            if(cont==7): break
    else:
        
        nome = mention.replace("<","").replace(">","").replace("@","").replace("!","")
        if len(str(nome)) != 18 or nome == "816787135825838090":
            return await ctx.send("@ invalido ! Uso: $xp ou $xp @user")
        try:
            xp = niveis[nome]
            embed = discord.Embed(title="GRANDE JOGADOR",description = "O Seu nivel de xp", color = discord.Colour.red())
            embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Video_game_controller_icon_designed_by_Maico_Amorim.svg/1200px-Video_game_controller_icon_designed_by_Maico_Amorim.svg.png")
            embed.add_field(name=f"{xp}XP", value="<@"+nome+">", inline=False)
        except:
            embed = discord.Embed(title="jogador PODRE",description = "não joga nada YA", color = discord.Colour.purple())
            embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Video_game_controller_icon_designed_by_Maico_Amorim.svg/1200px-Video_game_controller_icon_designed_by_Maico_Amorim.svg.png")
            embed.add_field(name="0XP", value="<@"+nome+">", inline=False)
    return await ctx.send(embed=embed)
                

###########----FORCA----##############
@client.command(brief="Joga uma forca com essa malta fixe YA", help=f"Uso : {prefix}forca e tenta descobrir a palavra")
@commands.cooldown(1,15,commands.BucketType.user)
async def forca(ctx):
    msg = await ctx.send("Quem quiser jogar a forca MOCADA reaja aí CHÉ yA em 7 segundos")
    await msg.add_reaction('✔️')
    channel = client.get_channel(715512000720928779)
    await sleep(7.0)
    message = await channel.fetch_message(msg.id)
    users = []
    users.append(ctx.author)
    for reaction in message.reactions:
        async for user in reaction.users():
            users.append(user)
    palavra, msg = await init_forca(ctx)
    if(not palavra):
        palavra = "prancha"
    #print(palavra)
    def checkJogador(m):
        return m.author in users
    await ctx.send("CHE MALTA Voces tem 10 tentativas, gud luck :P")
    tentativas = 10
    usadas = []
    while True:
        if(not "❓" in msg):
            for user in users:
                if(user.id != 816787135825838090):
                    xp = 10*int(tentativas/2)
                    storeXP(str(user.id),xp)
            return await ctx.send("`WINNER DINNER DA CHICKEN: "+ randomline(".txt/msgsPositivas.txt")+"`")
        elif(tentativas==0):
            return await ctx.send(f"NABOS. ja não há mais tentativas! A palavra era `{palavra}`")
        else:
            play = await client.wait_for('message', check=checkJogador)
            if(play.content == prefix+"desisto"):
                return await ctx.send("`Desistiram do jogo a palavra era -> "+palavra+"`")
            if (play.content.lower().strip() == palavra.lower().rstrip()):
                xp = 12*tentativas-5
                storeXP(str(play.author.id),xp)
                for user in users:
                    if(user.id != 816787135825838090):
                        storeXP(str(user.id),8)
                await ctx.send("```" + palavra + "```")
                await ctx.send(f"FOda-sE este gajo é um MESTRE CONGRATS")
                return await ctx.send(f"`Ganhaste{xp}XP !!`")
            if(len(play.content) != 1):
                tentativas-=1
                await ctx.send(f"`Utiliza apenas uma letra BARRAQUERo, já so tens mais {tentativas} disponíveis`")
            else:
                pos = [idx for idx, item in enumerate(palavra.lower()) if play.content.lower() in item]
                msgList = list(msg)
                if pos:
                    if(play.content in usadas):
                        await ctx.send(f"`Letra já usada: Tens {tentativas} tentativas disponiveis`")
                    else:
                        usadas.append(play.content)
                    for p in pos:
                        msgList[p] = play.content
                    msg = "".join(msgList)
                    await ctx.send(msg)  
                    text=""
                    k=0
                    for letra in usadas:
                        if(k==0):
                            text+=letra
                            k+=1
                        else:
                            text+=", "+letra
                    await ctx.send(f"Letras usadas: {text}") 
                else:
                    if(play.content in usadas ):
                        await ctx.send(f"`Letra já usada: Tens {tentativas} tentativas disponiveis`") 
                    else:
                        usadas.append(play.content)
                        tentativas-=1
                        await ctx.send(f"`Errado nabo, so há mais {tentativas} tentativas disponiveis`")
                    pos = [idx for idx, item in enumerate(palavra.lower()) if play.content.lower() in item]
                    msgList = list(msg)
                    if pos:
                        for p in pos:
                            msgList[p] = play.content
                    msg = "".join(msgList)
                    await ctx.send(msg)
                    text=""
                    k=0
                    for letra in usadas:
                        if(k==0):
                            text+=letra
                            k=1
                        else:
                            text+=", "+letra
                    await ctx.send(f"Letras usadas: {text}")

async def init_forca(ctx):
    palavra = randomline(".txt/words.txt")
    msg = ""
    for x in range(len(palavra)):
        if(x==len(palavra)-1 and not "-" in palavra):
            break
        if(not palavra[x]=="-"):
            msg = msg + "❓"
        else:
            msg = msg + '-'
    await ctx.send("```" + msg + "```")
    return [palavra,msg]

###########----RANDOM----###########
@client.command(brief="Experimenta bro", help=f"Usar: {prefix}random, Faz o que ? Mistery")
@commands.cooldown(1,5,commands.BucketType.user)
async def random(ctx):
    url = randomline(".txt/noises.txt")
    return await p(ctx=ctx, query=url)

############----CLEAR----############
@client.command(brief="Limpa a queue", help=f"Usar: {prefix}clear para limpar a lista de musicas")
@commands.cooldown(1,5, commands.BucketType.user)
async def clear(ctx):
    id = ctx.message.guild.id
    try:
        del(listmusics[id])
        del(listtitles[id])
    except:
        return await ctx.send("`A queue já estava limpa`")
    return await ctx.send("```As músicas foram limpas BRO ao contrário do teu cu YA```")

###########----POLLS----############
@client.command(brief="Poll todo maluco", help=f"Usar: {prefix}poll pergunta, opção1, opção2, (...), opção10")
@commands.cooldown(1,5, commands.BucketType.user)
async def poll(ctx, *, params=None):
    # array de 10 opções -> listemojiAJ
    if(params==None):
        return await ctx.send("```Usar $poll pergunta, opção1, opção2, (...), opção10```")
    else:
        opts = params.split(',')
        if(len(opts) < 3 or len(opts)>10):
            return await ctx.send("```Introduz a pergunta e 2 a 10 opções separados por virgulas```")
        embed = discord.Embed(title = f"{opts[0]}", color = discord.Colour.teal())
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Request by {ctx.author.name}")
        for val in range(len(opts)):
            if(val==len(opts)-1):
                break
            embed.add_field(name = '\u200b', value=listemojiAJ[val] + " : " + f"{opts[val+1]}", inline=False)
        embed.add_field(name = '\u200b', value='\u200b', inline=False)
        msg = await ctx.send(embed=embed)
        storeXP(ctx.author.id,5)
        for i in range(len(opts)-1):
            await msg.add_reaction(listemojiAJ[i])
        return
    
###########----SKIP_SONG----##########
@client.command(brief="Passa essa musica horrivel à frente", help=f"Usar: {prefix}skip, dá skip a musica")
@commands.cooldown(1,3,commands.BucketType.user)
async def skip(ctx):
    return await p(ctx=ctx, query="skip")

###########----REMOVE_SONG----##########
@client.command(brief="Limpa a musica que nao gostas da lista", help=f"Usar: {prefix}remove num, XAU MUSICA")
@commands.cooldown(1,3,commands.BucketType.user)
async def remove(ctx, num):
    val = "remove " + num
    return await p(ctx=ctx, query=val)


##############----QUEUE----################
@client.command(brief="Mosta a queue de musicas a bombar", help=f"Usar: {prefix}queue, Lista de musicas prontas para bombar")
@commands.cooldown(1,3,commands.BucketType.user)
async def queue(ctx):
    id = ctx.message.guild.id
    if(id in listtitles and len(listtitles[id])!=0):
        embed = discord.Embed(title="Queue de músicas",description = "Lista de músicas na fila", color = discord.Colour.purple())
        embed.set_thumbnail(url="https://www.creativefabrica.com/wp-content/uploads/2019/02/Music-Icon-by-Kanggraphic-1-580x386.jpg")
        counter = 0
        for x in listtitles[id]:
            counter = counter + 1
            embed.add_field(name=str(counter), value=str(x), inline=False)
        return await ctx.send(embed=embed)
    else:  
        return await ctx.send("``Não há musicas na queue bro``")

###############----PLAY ANYTHING----################
@client.command(brief="TOCA O QUE quiseres bro", help=f"Usar: {prefix}play, Eu toco para ti o que tu quiseres lido")
@commands.cooldown(1,2,commands.BucketType.user)
async def p(ctx, *, query):
    #id no server
    #skip sem nada na list
    id = ctx.message.guild.id
    if(query == "skip" and id in listmusics and len(listmusics[id]) == 0):
        return await ctx.send("```CHE TAS TODO TURBINADO, não há nada para dar skip FOOL```")
    #remove sem nada na lista
    if("remove" in query and  id in listmusics and len(listmusics[id]) ==0):
        return await ctx.send("```CHE GANDA NABO, não há nada para remover TONE```")
    #spotify playlist
    if("open.spotify.com" in query):
        return await ctx.send("```POr enqunato o spotify não funciona, está todo TURBINADO```")
    #youtube music playlist
    
    FFMPEG_OPTS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    if not ctx.message.author.voice:
        await ctx.send("Tens que tar conectado a um VoiceChannel BARRAQUEIRO YA")
        return
    
    else:
        channel = ctx.message.author.voice.channel
    try:
        await channel.connect()
    except:
        print("ja ca estava dentro mas vou por a tocar")

    voice = get(client.voice_clients, guild=ctx.guild)
    #skip(com musicas)
    if(query == "skip" and  id in listmusics and  id in listtitles and len(listmusics[id])!=0 and len(listtitles[id])!= 0):
        voice.stop()
        del(listmusics[id][0])
        del(listtitles[id][0])
        return await play_next(voice, ctx)
    #remove
    if("remove" in query and id in listmusics and len(listmusics[id])!=0):
        num = int(query.split(' ')[1])
        print(num)
        if(num-1 == 0):
            return await ctx.send("```BRO para remover a primeira musica faz $skip duh```")
        try:
            titulo = listtitles[id][num-1]
        except IndexError:
            return await ctx.send("```MAS ESSA musica não existe YA```")
        del(listtitles[id][num-1])
        del(listmusics[id][num-1])
        msg = "```Música removida: " + titulo  + "```"
        return await ctx.send(msg)
    
    async with ctx.typing():
        video, source = search(query)

    msg = "Adicionada à queue: " + str(video['title'])
    url = FFmpegPCMAudio(source, **FFMPEG_OPTS)
    
    await ctx.send("```" + msg + "```")

    #verifica se ja tem musicas na queue, adicionando se ja tiver
    if(id in listmusics and len(listmusics[id])!=0):
        listmusics[id].append(url)
        listtitles[id].append(str(video['title']))
    #se nao tiver, cria uma queue e põe a bombar
    else:
        cp = [url]
        mp = [str(video['title'])]
        listmusics[id] = cp
        listtitles[id] = mp
        await play_next(voice, ctx)

    timer = 0
    
    while(not voice.is_playing()):
        await sleep(1)
        timer = timer + 1
        if(timer == 480 and voice and voice.is_connected()):
            await ctx.send("Musica : Não tava a tocar nada por isso bazei")
            await voice.disconnect()
            break

async def play_next(voice, ctx):
    id = ctx.message.guild.id
    print(len(listmusics[id]))
    while len(listmusics[id]) != 0:
        print("vou tocar")
        voice.play(listmusics[id][0], after=lambda e:print('done', e))
        atual = "Now playing: " + listtitles[id][0]
        await ctx.send("```" + atual + "```")
        while(voice.is_playing()):
            await sleep(1)
        try:
            del(listmusics[id][0])
            del(listtitles[id][0])
        except:
            pass

def search(arg):
    with YoutubeDL({'format': 'bestaudio', 'noplaylist':'True'}) as ydl:
        try: requests.get(arg)
        except: info = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
        else: info = ydl.extract_info(arg, download=False)
    return (info, info['formats'][0]['url'])

###############----PROFILE-----#####################
@client.command(brief='Procurar perfil',help=f'Usar: {prefix}profile @user')
@commands.cooldown(1,2, commands.BucketType.user)
async def profile(ctx):
    try:
        member = ctx.message.mentions[0]
        embed = discord.Embed(title = member.name,description = member.mention, color = discord.Colour.red())
        embed.add_field(name = "Name", value = member.name, inline = True)
        embed.add_field(name = "TopRole", value = member.top_role, inline = True)
        embed.set_thumbnail(url = member.avatar_url)
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Request by {ctx.author.name}")
        await ctx.send(embed = embed)
    except:
        msg = "Introduz um mention valido | usar : "+prefix+"profile @user"
        return await ctx.send(msg)

###############----CREDITOS----#####################
@client.command(brief='Creditos da malta por trás do MOCS YA', help=f'Usar: {prefix}creditos | {prefix}credits para ver os creditos')
@commands.cooldown(1,2, commands.BucketType.user)
async def creditos(ctx):
     embed = discord.Embed(title="Créditos",description = "Cérebros por trás do BOTMOCS", color = discord.Colour.red())
     embed.set_thumbnail(url="https://cdn.jornaldebrasilia.com.br/wp-content/uploads/2019/07/cerebro-1000x600.jpg")
     embed.add_field(name="Programadores: ", value='\u200b', inline=True)
     embed.add_field(name="João Amaral", value ='<@366292034669248514>', inline=True)
     embed.add_field(name="Bruno Lemos", value ='<@431857111018897409>', inline=True)
     embed.add_field(name="Agradecimentos: ", value='\u200b', inline=True)
     embed.add_field(name="Pedro Rocha", value ='<@539520976577363981>', inline=True)
     embed.add_field(name="André Clérigo", value ='<@239323719300939776>', inline=True)
     await ctx.send(embed=embed)
    
###############----GUITA----####################
@client.command(brief='Connect BOTMOCS para bombar GUITZ', help=f'Usar: {prefix}guita para conectar BOTMOCS para bonmbar GUITZPIMS')
@commands.cooldown(1, 2, commands.BucketType.user)
async def guita(ctx):
    url = randomline(".txt/guitz.txt")
    return await p(ctx=ctx, query=url)
  
####################----DC channel voice--------#############
@client.command(brief='Disconnect BOTMOCS from channel',help=f'Usar: {prefix}dc para desconectar de um voice channel [necessário estar no vc]')
@commands.cooldown(1, 2, commands.BucketType.user)
async def dc(ctx):
    try:
        if ctx.author.voice.channel and ctx.author.voice.channel == ctx.voice_client.channel:
            server = ctx.message.guild.voice_client
            await server.disconnect()
            listmusics = []
        else:
            await ctx.send("Tens que estar no mesmo canal que o BOT MOCS YA")
    except AttributeError:
        await ctx.send("O BOT MOCS NÃO ESTÁ EM NENHUM CHANNEL")

############################----GALO----#########################
@client.command(brief = 'Jogo do galo',help =f'Usar: {prefix}galo @user | {prefix}galo para começar um jogo do galo')
@commands.cooldown(1, 10, commands.BucketType.user)
async def galo(ctx):
    if(listgalo.count(ctx.author) > 0):
        return await ctx.send("Já estás no meio de um jogo, acaba o jogo ou desiste")
    player1 = ctx.author
    if(ctx.message.content.lower() == (prefix+"galo")): #sem tagar ninguem
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
            return await ctx.send("Ninguém quer jogar contigo zeca :(")
    else:
        msg = "usar: "+prefix+"galo @mention  ou apenas "+prefix+"galo"                         # errado
        return await ctx.send("usar: $galo @mention  ou apenas $galo")
    
    
    ############----COMEÇA A JOGAR O JOGO DO GALO ----############
    if(listgalo.count(player2) >0):
        return await ctx.send(f"{player2.mention} já estás no meio de um jogo, acaba o jogo ou desiste [{prefix}desisto]")
    listgalo.append(player1)
    listgalo.append(player2)
    await ctx.send(f"JOGO DO GALO : {player1.mention} vs {player2.mention}")
    await ctx.send(f"```Para desistir usar o comando {prefix}desisto```")
    simbplayer1 = "🟢"
    simbplayer2 = "❌"
    array = init_galo()
    
    await print_galo(array,player1.mention, ctx)
    current_player=player1
    numjogadas = 0

    def jogadorCerto(m):
        return m.author == current_player

    while True :
        if(check_end_galo(array,numjogadas)== -1 and ctx.author.id != 816787135825838090): # continue
            play = await client.wait_for('message', check=jogadorCerto)
            if(play.content != (prefix+"desisto")):
                try:
                    jogada = int(play.content)-1        
                    if jogada>8 or jogada<0 or (not check_empty_pos_galo(array,jogada)):
                        await ctx.send("Jogada inválida!")
                        await print_galo(array,current_player.mention, ctx)
                    else:
                        x = int(jogada/3)
                        y = int(jogada%3)
                        if current_player == player1:
                            array[x][y] = simbplayer1
                            current_player = player2
                        elif current_player == player2:
                            array[x][y] = simbplayer2
                            current_player = player1
                        else:
                            print("Jogador Inválido")
                        numjogadas = numjogadas + 1
                        await print_galo(array,current_player.mention, ctx)
                except ValueError:
                    if(play.content != (prefix+"galo")):
                        await ctx.send("Jogada inválida, introduzir numeros de 1 a 9")
                    await print_galo(array,current_player.mention, ctx)
            else:
                listgalo.remove(player1)
                listgalo.remove(player2) 
                if(current_player == player1):
                    storeXP(str(player2.id),50)
                    return await ctx.send(f"Vencedor {player2.mention}, " + randomline(".txt/msgsPositivas.txt").lower())
                elif(current_player == player2):
                    storeXP(str(player1.id),50)
                    return await ctx.send(f"Vencedor {player1.mention}, " + randomline(".txt/msgsPositivas.txt").lower())
        elif(check_end_galo(array,numjogadas)==1):
            listgalo.remove(player1)
            listgalo.remove(player2) 
            storeXP(str(player1.id),50)
            return await ctx.send(f"Vencedor {player1.mention}, " + randomline(".txt/msgsPositivas.txt").lower())
        elif(check_end_galo(array,numjogadas)==2):
            listgalo.remove(player1)
            listgalo.remove(player2) 
            storeXP(str(player2.id),50)
            return await ctx.send(f"Vencedor {player2.mention}, " + randomline(".txt/msgsPositivas.txt").lower())
        elif(check_end_galo(array,numjogadas)==0):
            listgalo.remove(player1)
            listgalo.remove(player2) 
            storeXP(str(player1.id),15)
            storeXP(str(player2.id),15)
            return await ctx.send(f"Empate entre {player1.mention} e {player2.mention}, Tentem de novo!!!")      
def check_end_galo(array,numjogadas):
    #return 0 empate
    #return 1 player1 win
    #return 2 player 2 win
    #return -1 continue
    end = -1
    if(array[0][0] == array[0][1] == array[0][2]  and array[0][0]!="⬛"):
        end = getjogada(array,0,0)
    elif(array[1][0] == array[1][1] == array[1][2]and array[1][0]!="⬛"):
        end = getjogada(array,1,0)
    elif(array[2][0] == array[2][1] == array[2][2]and array[2][0]!="⬛"):
        end = getjogada(array,2,0)
    elif(array[0][0] == array[1][0] == array[2][0]and array[0][0]!="⬛"):
        end = getjogada(array,0,0)
    elif(array[0][1] == array[1][1] == array[2][1]and array[0][1]!="⬛"):
        end = getjogada(array,0,1)
    elif(array[0][2] == array[1][2] == array[2][2]and array[0][2]!="⬛"):
        end = getjogada(array,0,2)
    elif(array[0][0] == array[1][1] == array[2][2]and array[0][0]!="⬛"):
        end = getjogada(array,0,0)
    elif(array[0][2] == array[1][1] == array[2][0]and array[0][2]!="⬛"):
        end = getjogada(array,0,2)
    elif numjogadas == 9:
        return 0
    return end
def getjogada(array,x,y):
    if array[x][y] == '🟢':
        return 1
    elif array[x][y] == '❌':
        return 2
    else:
        return print("Erro interno")
def check_empty_pos_galo(array, pos):
    x = int(pos/3)
    y = int(pos%3)
    if(array[x][y] == '⬛'):
        return True
    return False
def init_galo():
    n = 3
    array = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            array[i][j] = '⬛'
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
@client.command(brief='cara ou coroa',help=f"Usar: {prefix}coin para girar uma moeda") #Flip that coin sis
async def coin(ctx):
    smile = '\N{SLIGHTLY SMILING FACE}'
    coroa = '\N{CROWN}'
    choice = ran.randint(1,2)
    if(choice == 1):
        return await ctx.message.add_reaction(smile)
    else:
        return await ctx.message.add_reaction(coroa)

###########----OFF----#############  
@client.command(brief='Admin CMD: SHUT DOWN',help='CMD para os desenvolvedores') #Disconnect
async def off(ctx):
    # amaral e bruno autorizados
    if(ctx.author.id == 431857111018897409 or ctx.author.id == 366292034669248514):
        await ctx.send("BOT MOCS OFFLINE 🔴")
        server = ctx.message.guild.voice_client
        try:
            try:
                await server.disconnect()
            except:
                print("Not in a voice channel")
            await client.logout()
        except:
            print("Não consegui sair")
    else:
        await ctx.send("Não tens acesso a este codigo bem potente")

##############----DICE----#################
@client.command(brief ='Guess the dice :p',help=f'Usar: {prefix}dice para começar o jogo') #JOGA ESSE DADO
@commands.cooldown(1, 2, commands.BucketType.user)
async def dice(ctx):

        def is_correct(m):
            return m.author == ctx.author

        answer = ran.randint(1,6)
        try:
            await ctx.send(f"{ctx.author.mention} chuta um numero de 1 a 6 e vê se adivinhas")
            guess = await client.wait_for('message', check = is_correct, timeout=10.0)
        except asyncio.TimeoutError:
            return await ctx.send("Ès buèDA LENto ya")
        
        if (guess.content.isdigit()):
            if(int(guess.content) == answer):
                xp = 20
                storeXP(str(ctx.author.id),xp)
                frase = randomline(".txt/msgsPositivas.txt")
                return await ctx.send(f"{frase}, GANHASTE `{xp}XP` ") 
            else:
                frase = randomline(".txt/msgsNegativas.txt")
                return await ctx.send(frase + f"O número era o `{answer}` seu burro")
        else:
            return await ctx.send(f"{ctx.author.mention} isso não é um numero nabo")

#############----hello----################
@client.command(brief='Saudações amigão',help=f'Usar: {prefix}hello | {prefix}hello @user') #Boas jovem
async def hello(ctx):
    try:
        member = ctx.message.mentions[0]
        await ctx.send(f'Olá, {member.mention}  :nerd:')
    except:
        await ctx.send(f'Olá, {ctx.author.mention}  :nerd:')

############----CONS(C)ELHO----#################
@client.command(brief='Recebe ganda conselho',help=f"Usar: {prefix}conselho para receber um conselho") #Concelho master
async def conselho(ctx):
    frase = randomline(".txt/messages.txt")
    return await ctx.send(frase)

#################----ping----#####################~
@client.command(brief='ping do BOTMOCS', help=f"Usar: {prefix}ping para ver o ping do botMOCS") 
async def ping(ctx):
    await ctx.send(f'**Ping??** **Pong!** Latency: {round(client.latency * 1000)}ms')


client.run(TOKEN_KEY) 
