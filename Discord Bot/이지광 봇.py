import discord
from discord.ext import commands
from discord import Colour
import asyncio
from discord.ext import tasks

app = commands.Bot(command_prefix='!')

@app.command()
async def 노예야(ctx):
    await ctx.send('네 주인님!')
    
@app.command() 
async def 따라해봐(ctx, *args):
    await ctx.send(' '.join(args))
    
@app.command()
async def vote(ctx, *args):
    # print(ctx)
    # print(type(ctx))
    # print(dir(ctx))

    await ctx.send("투표 시작!!")
    for arg in args:
        # print(msg)
        code_block = await ctx.send("```" + arg + "```")
        await code_block.add_reaction("👍")

@app.event
async def on_ready():
    print(f'{app.user.name} 연결 완료!')
    print(app.guilds)
    #892724718958956565
    g = app.guilds[0]
    
    #print(g.roles)
    r = g.roles[1]
    
    await app.change_presence(status=discord.Status.online, activity=None)     
    
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
     
app.run('OTIwNjUzMTcyMTUyODY4ODg1.YbnfFQ.rpN22J3wt30ZH6Xa4mIEo5QEg_M')
