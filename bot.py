import discord
from dotenv import load_dotenv
import os
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True  


bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')


load_dotenv('tokenDis')
bot.run(os.getenv('DISCORD_BOT_TOKEN'))
