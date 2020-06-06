import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime

class Utilities(Cog_Extension):

	@commands.command()
	async def ping(self, ctx):
		await ctx.send(f'{round(self.bot.latency*1000)} ms')

	@commands.command()
	async def about(self, ctx):
		embed=discord.Embed(title="About", url="https://github.com/james10949/sijingprogram/blob/master/README.md", description="About this bot", color=0xffa500, timestamp=datetime.datetime.utcnow())
		embed.set_author(name="思鏡Project", url="https://yeyunstudio.nctu.me")
		embed.add_field(name="Made By", value="ユキ綾乃", inline=False)
		embed.set_footer(text="Using Python")
		await ctx.send(embed=embed)

	@commands.command()
	async def said(self, ctx, *,msg):
		await ctx.message.delete()
		await ctx.send(msg)

def setup(bot):
	bot.add_cog(Utilities(bot))