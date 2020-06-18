import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('settings.json', 'r', encoding='utf8') as settings:
	botconfig = json.load(settings)

class Events(Cog_Extension):
	# @commands.Cog.listener()
	# async def on_member_join(self, member):
	# 	channel = self.bot.get_channel(int(botconfig['Welcome_channel']))
	# 	await channel.send(f'{member} join!')

	# @commands.Cog.listener()
	# async def on_member_remove(self, member):
	# 	channel = self.bot.get_channel(int(botconfig['Leave_channel']))
	# 	await channel.send(f'{member} leave!')
	
	# @commands.Cog.listener()
	# async def on_message(self, msg):
	# 	Keyword = ['Hi','Hello','HiHi','Hey']
	# 	if msg.content in Keyword and msg.author != self.bot.user:
	# 		await msg.channel.send('hi')

	@commands.cog.listener()
	async def null(self, ctx):
		print('')

def setup(bot):
	bot.add_cog(Events(bot))