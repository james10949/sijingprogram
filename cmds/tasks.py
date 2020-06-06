import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, asyncio, datetime

with open('settings.json', 'r', encoding='utf8') as settings:
	botconfig = json.load(settings)

class Tasks(Cog_Extension):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.counter = 0

		# async def interval():
		# 	await self.bot.wait_until_ready()
		# 	self.channel = self.bot.get_channel(710718810470088712)
		# 	while not self.bot.is_closed():
		# 		await self.channel.send('shut the f**k up')
		# 		await asyncio.sleep(5)

		async def time_task():
			await self.bot.wait_until_ready()
			self.channel = self.bot.get_channel(710718810470088712)
			while not self.bot.is_closed():
				now_time = datetime.datetime.now().strftime('%H%M')
				with open('settings.json', 'r', encoding='utf8') as settings:
					botconfig = json.load(settings)
				if now_time == botconfig['time'] and self.counter == 0:
					await self.channel.send("It's time...")
					self.counter = 1
					await asyncio.sleep(1)
				else:
					await asyncio.sleep(1)
					pass

		self.bg_task = self.bot.loop.create_task(time_task())

	@commands.command()
	async def set_channel(self, ctx, ch:int):
		self.channel = self.bot.get_channel(ch)
		await ctx.send(f'Set Channel : {self.channel.mention}')

	@commands.command()
	async def set_time(self, ctx, time):
		with open('settings.json', 'r', encoding='utf8') as settings:
			botconfig = json.load(settings)
		
		botconfig['time'] = time
		with open('settings.json', 'w', encoding='utf8') as settings:
			json.dump(botconfig, settings, indent=4)


def setup(bot):
	bot.add_cog(Tasks(bot))