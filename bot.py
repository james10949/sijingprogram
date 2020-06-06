import discord
from discord.ext import commands
import json

with open('settings.json', 'r', encoding='utf8') as settings:
    botconfig = json.load(settings)

bot = commands.Bot(command_prefix = "$")

@bot.event

async def on_ready():
    print(">> System Online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(botconfig['Welcome_channel']))
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(botconfig['Leave_channel']))
    await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} ms')

@bot.command()
async def funcname(parameter_list):
    pass

bot.run(botconfig['TOKEN'])