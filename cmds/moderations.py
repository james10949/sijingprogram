import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Moderations(Cog_Extension):
	@commands.command()
	async def clean(self, ctx, num : int):
		await ctx.channel.purge(limit = num+1)

def setup(bot):
	bot.add_cog(Moderations(bot))