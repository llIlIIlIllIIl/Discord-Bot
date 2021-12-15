import discord
from discord.ext import commands
from discord import Colour
import asyncio
from discord.ext import tasks

app = commands.Bot(command_prefix='!')

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
async def color(ctx):
    g = app.guilds[0]
    r = g.roles[1]
    if neonsign_nickname.is_running():
        neonsign_nickname.stop()
    else:
        neonsign_nickname.start(r)
        
@tasks.loop(seconds=0.5)
async def neonsign_nickname(role):
    await role.edit(colour=Colour.random())
     
app.run('?')
