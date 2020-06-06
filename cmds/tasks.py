import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, asyncio, datetime

with open('settings.json', 'r', encoding='utf8') as settings:
	botconfig = json.load(settings)

class Tasks(Cog_Extension):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		async def interval():
			await self.bot.wait_until_ready()
			self.channel = self.bot.get_channel(710718810470088712)
			while not self.bot.is_closed():
				await self.channel.send('shut the f**k up')
				await asyncio.sleep(5)

		self.bg_task = self.bot.loop.create_task(interval())

	@commands.command
	async def set_channel(self, ctx, ch:int):
		self.channel = self.bot.get_channel(ch)
		await ctx.send(f'Set Channel : {self.channel.mention}')

def setup(bot):
	bot.add_cog(Tasks(bot))