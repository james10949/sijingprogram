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

bot.remove_command('help')
@bot.command()
async def help(ctx):
	embed=discord.Embed(title="Help Page", url="https://github.com/james10949/sijingprogram/blob/master/README.md#Commands")
	embed.add_field(name="Moderations", value="$clean <int\> 清除訊息", inline=False)
	embed.add_field(name="Utilities", value="$about 顯示關於頁面\n$ping 顯示延遲\n$said <msg\> 機器人代發訊息", inline=False)
	embed.add_field(name="Funs", value="$picture 顯示隨機圖片(滿滿鈴鈴)", inline=False)
	embed.add_field(name="Others", value="$help 顯示此頁面", inline=False)
	await ctx.send(embed = embed)

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
	bot.load_extension(f'cmds.{extension}')
	await ctx.send(f'Loaded {extension} done')

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
	bot.unload_extension(f'cmds.{extension}')
	await ctx.send(f'Unloaded {extension} done')

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
	bot.reload_extension(f'cmds.{extension}')
	await ctx.send(f'Reloaded {extension} done')

@bot.command()
async def menu(ctx):
	embed=discord.Embed(title='Invite', url='https://discord.com/api/oauth2/authorize?client_id=718526610302697492&permissions=8&scope=bot', color=0x39c5bb)
	embed.set_author(name='Menu')
	embed.set_footer(text='Powered By 夜雲工作室：ユキ綾乃')
	await ctx.send(embed=embed)

for filename in os.listdir('./cmds'):
	if filename.endswith('.py'):
		bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
	bot.run(botconfig['TOKEN'])