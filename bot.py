import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "$")


@bot.event

async def on_ready():
    print(">> Bot is online <<")

bot.run('NzE4NTI2NjEwMzAyNjk3NDky.XtqKOA.oqmcS95eIfgcPUPUqYD0ZBR8BBA')