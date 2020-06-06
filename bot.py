import discord
from discord.ext import commands
import json
import random
import os

with open('settings.json', 'r', encoding='utf8') as settings:
	botconfig = json.load(settings)

bot = commands.Bot(command_prefix = "$")

@bot.event
async def on_ready():
	print(">> System Online <<")

@bot.command()
async def load(ctx, extension):
	bot.load_extension(f'cmds.{extension}')
	await ctx.send(f'Loaded {extension} done')

@bot.command()
async def unload(ctx, extension):
	bot.unload_extension(f'cmds.{extension}')
	await ctx.send(f'Unloaded {extension} done')

@bot.command()
async def reload(ctx, extension):
	bot.reload_extension(f'cmds.{extension}')
	await ctx.send(f'Reloaded {extension} done')

for filename in os.listdir('./cmds'):
	if filename.endswith('.py'):
		bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
	bot.run(botconfig['TOKEN'])