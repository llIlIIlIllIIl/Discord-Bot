import discord
from discord.ext import commands
from discord import Colour
import asyncio
from discord.ext import tasks
import youtube_dl

app = commands.Bot(command_prefix='!')


@app.event
    # 프로그램이 처음 실행되었을 때 초기 구성
async def on_ready():
    """
    봇이 로딩되었거나 재로딩 되는 경우 실행되는 이벤트
    
    :return: None
    """

    # 'comment'라는 게임 중으로 설정합니다.
    game = discord.Game("!설명서")
    await app.change_presence(status=discord.Status.online, activity=game)
    print("READY")

        
    print(app.guilds)
    g = app.guilds[0]  
    r = g.roles[1] 

async def song_start(voice, url):
    try:
        if not voice.is_playing() and not voice.is_paused():
            ydl_opts = {'format': 'bestaudio'}
            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': 'vn'}
            

@app.command(aliases=['반가워'])
async def 안녕(ctx):
    await ctx.send(f'{ctx.author.mention} 안녕하세요!')
    
@app.command() 
async def 따라말해(ctx, *args):
    await ctx.send(' '.join(args))
    
@app.command()
async def vote(ctx, *args):

    await ctx.send("투표 시작!!")
    for arg in args:
        # print(msg)
        code_block = await ctx.send("```" + arg + "```")
        await code_block.add_reaction("👍")

@app.command()
async def change(ctx):
    g = app.guilds[0]
    r = g.roles[1]
    if neonsign_nickname.is_running():
        neonsign_nickname.stop()
    else:
        neonsign_nickname.start(r)
        
@tasks.loop(seconds=1)
async def neonsign_nickname(role):
    await role.edit(colour=Colour.random())
    
@app.command()
async def 설명서(ctx):
        embed = discord.Embed(title="Sin4U", description="노래하는 봇", color=0x4432a8)
        embed.add_field(name="1. 인사", value="!안녕", inline = False)
        embed.add_field(name="2. 따라쟁이", value="!따라말해", inline = False)
        embed.add_field(name="3. 음성채널 입장/퇴장", value="!join / !leave (초대자가 입장된 상태에만 가능", inline = False)
        embed.add_field(name="4. 음악", value="!play [Youtube URL] : 음악을 재생\n!pause : 일시정지 \n!resume :다시 재생 \n!stop : 중지", inline = False)
        embed.set_image(url="https://pbs.twimg.com/media/EZMDOe4UwAAgzrG.jpg:small")
        await ctx.send(embed=embed)
        
        
app.run('OTIwNjUzMTcyMTUyODY4ODg1.YbnfFQ.rpN22J3wt30ZH6Xa4mIEo5QEg_M')
