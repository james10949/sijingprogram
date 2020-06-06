import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "$")


@bot.event

async def on_ready():
    print(">> System Online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(710718810470088709)
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(710718810470088709)
    await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} ms')

bot.run('NzE4NTI2NjEwMzAyNjk3NDky.XtqKOA.oqmcS95eIfgcPUPUqYD0ZBR8BBA')