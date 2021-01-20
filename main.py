import discord
import token_file
import config
import os
from discord.ext import commands

client = commands.Bot(command_prefix=',')
manul_list = ['манул', 'манулов', 'манул', 'манула']
olenf = "C:\\Users\\MinuteX\\Desktop\\Код\\Python\\AutoCounterManul\\files\\olen.png"
olen = os.path.join(os.path.dirname("oleg.png"), "images/")

@client.command()
async def олень(ctx, **kwargs):
    await ctx.send(content="Олень обыкновенный", file=discord.File("C:\\Users\\MinuteX\\Desktop\\Код\\Python\\AutoCounterManul\\files\\olen.png"))

@client.event
async def on_ready():
    print("Connect Successfullyct")

@client.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'Хей, {author.mention}, тебя приветсвует счетчик манулов')


@client.command()
async def bind(ctx):
    channel_file = open('channel.txt', 'w')
    print(ctx.channel)
    channel_id = ctx.message.channel
    channel_id = str(channel_id)
    channel_file.write(channel_id)
    channel_file.close()
    print(config.bind_successfully)
    await ctx.send(config.bind_successfully)

@client.event
async def manul(ctx, message):
    num_manul = 0
    msg = ctx.content.lower()
    not_num_msg = msg
    if msg in manul_list:
        await ctx.send('debug massage')
        

    await ctx.send(f'Уже {num_manul} манулов')

client.run(token_file.token)