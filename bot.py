import discord
from discord.ext import commands

import os
from dotenv import load_dotenv



intents = discord.Intents.default()
intents.message_content = True  


bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command()
async def ping(ctx):
    await ctx.send('Hello We are the Task Manager Discord Bot!')


load_dotenv('tokenDis.env')
bot.run(os.getenv('DISCORD_BOT_TOKEN'))
