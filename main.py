import discord
from discord.ext import commands
import os
import random
import requests


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
images = os.listdir('images')
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.command()
async def ecology(ctx):
    await ctx.send('Окружающая человека среда; условия существования животных и растений в какой-л. местности.')
@bot.command()
async def decay(ctx, object = ""):
    if object == 'plastic':
        index = 0
        await ctx.send('Среднее время разложения пластмассовых изделий, созданных по разным технологиям, колеблется от 6 месяцев до 700 лет.')
    elif object == 'glass':
        index = 1
        await ctx.send('Время разложения стекла - более 1000 лет')
    elif object == "gum":
        index = 2
        await ctx.send('От 30 лет')
    elif object == "metal":
        index = 3
        await ctx.send('От 500 лет')
    else:
        index = 4
        await ctx.send('nu stim inca asa obiecte')
    with open(f'images/{images[index]}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file = picture)   















bot.run("token")




