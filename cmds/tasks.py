import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, asyncio, datetime

with open('settings.json', 'r', encoding='utf8') as settings:
	botconfig = json.load(settings)

class Tasks(Cog_Extension):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

def setup(bot):
	bot.add_cog(Tasks(bot))