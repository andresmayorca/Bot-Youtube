import discord
from discord.ext import commands

from urllib import parse, request
import re

bot = commands.Bot(command_prefix='>', description="This is a Helper Bot")

@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall( r"watch\?v=(\S{11})", html_content.read().decode())
    #print(search_results)
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[1])


@bot.event
async def on_ready():
    print('Mi Bot esta listo')

bot.run('token')