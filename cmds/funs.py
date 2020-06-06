import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('settings.json', 'r', encoding='utf8') as settings:
    botconfig = json.load(settings)

class Funs(Cog_Extension):
	@commands.command()
	async def picture(self, ctx):
		random_pic = random.choice(botconfig['pic'])
		await ctx.send(random_pic)

def setup(bot):
	bot.add_cog(Funs(bot))