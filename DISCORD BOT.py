import discord
from discord.ext import commands
from asyncio import sleep as s

bot = commands.Bot(commands.when_mentioned_or('/'), help_command=None)

@bot.command()
async def hello(ctx, *, msg):
        await ctx.send(f'{msg}, {ctx.author.mention}')

@bot.command()
async def reminder(ctx, time: int, *, msg):
        await s(time)
        await ctx.send(f'{msg}, {ctx.author.mention}')
        

@bot.command()
async def reminderMinute(ctx, time: int, *, msg):
        await s(60*time)
        await ctx.send(f'{msg}, {ctx.author.mention}')   

@bot.command()
async def reminderHour(ctx, time: int, *, msg):
        await s(3600*time)
        await ctx.send(f'{msg}, {ctx.author.mention}')

@bot.command()
async def reminderDay(ctx, time: int, *, msg):
        await s(86400*time)
        await ctx.send(f'{msg}, {ctx.author.mention}')

@bot.command()
async def stop(ctx):
        await ctx.reply('wait')


bot.run('Input bot token')


        