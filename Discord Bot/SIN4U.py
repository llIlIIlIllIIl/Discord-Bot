import discord
from discord.ext import commands
from discord import Colour
import asyncio
from discord.ext import tasks


app = commands.Bot(command_prefix='!')

# Status
@app.event
    # 프로그램이 처음 실행되었을 때 초기 구성
async def on_ready():
    """
    봇이 로딩되었거나 재로딩 되는 경우 실행되는 이벤트
    
    :return: None
    """

    # 'comment'라는 게임 중으로 설정합니다.
    game = discord.Game("!도움말")
    await app.change_presence(status=discord.Status.online, activity=game)
    print("READY")

        
    print(app.guilds)
    g = app.guilds[0]  
    r = g.roles[1]      

# join 
@app.command()
async def join(ctx):
    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send(embed = discord.Embed(title="Error", description = "채널에 유저가 접속하고 있지 않습니다.", color=0xFF0000))
            
# Leave
@app.command()
async def leave(ctx):
    try:
        await vc.disconnect()
    except:
        await ctx.send(embed = discord.Embed(title="Error", description = "채널에 접속하고 있지 않습니다.", color=0xFF0000))
     
# Play


# Greeting
@app.command(aliases=['반가워'])
async def 안녕(ctx):
    await ctx.send(f'{ctx.author.mention}님 안녕하세요!')
    
# Vote
@app.command()
async def 투표(ctx, *args):

    await ctx.send("투표 시작!!")
    for arg in args:
        # print(msg)
        code_block = await ctx.send("```" + arg + "```")
        await code_block.add_reaction("👍")
        
# Neonsign
@app.command()
async def 반짝반짝(ctx):
    g = app.guilds[0]
    r = g.roles[1]
    if neonsign_nickname.is_running():
        neonsign_nickname.stop()
    else:
        neonsign_nickname.start(r)
        
@tasks.loop(seconds=1)
async def neonsign_nickname(role):
    await role.edit(colour=Colour.random())


# Help    
@app.command()
async def 도움말(ctx):
        embed = discord.Embed(title="Sin4U", description="노래하는 봇", color=0x4432a8)
        embed.add_field(name="1. 인사", value="!안녕", inline = False)
        embed.add_field(name="2. 투표", value="!투표", inline = False)
        embed.add_field(name="3. 네온사인", value="!반짝반짝 (역할 필요)", inline=False)
        embed.add_field(name="4. 음성채널 입장/퇴장", value="!join / !leave (초대자가 입장된 상태에만 가능)", inline = False)
        embed.add_field(name="5. 음악", value="!play [Youtube URL] : 음악을 재생\n!pause : 일시정지 \n!resume :다시 재생 \n!stop : 중지", inline = False)
        embed.set_image(url="https://blog.kakaocdn.net/dn/WsyUB/btre7ur4HG7/HSR4G7FZCoTAig48akq8K0/img.jpg")
        await ctx.send(embed=embed)
        
# Token
app.run('OTIwNjUzMTcyMTUyODY4ODg1.YbnfFQ.TZXlHSQkKMX50cpd-HPR20cJDvg')
