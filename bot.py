import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("token")

from discord.ext import commands

# Initialize Bot and Denote The Command Prefix
bot = commands.Bot(command_prefix="!")

# Runs when Bot Succesfully Connects
@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

    
@bot.event
async def on_message(message):
    # Make sure the Bot doesn't respond to it's own messages
    if message.author == bot.user: 
        return
    
    if message.content == 'hi knee':
        await message.channel.send(f'Hi {message.author}')
    if message.content == 'bye knee':
        await message.channel.send(f'Goodbye {message.author}')

    if message.content == 'pineapple on':
        await message.channel.send(f'Pineapple belongs on Pizza')
        #await channel.send(file=discord.File('Pineapple on pizza.png'))
        await message.channel.send('https://imgur.com/a/vms5Ti2')

    if message.content == 'no pineapple':
        await message.channel.send(f'Pineapple does not belong on Pizza')
        #await channel.send(file=discord.File('no pineapple pizza.png'))
        await message.channel.send('https://imgur.com/a/4eMOjNK')

    await bot.process_commands(message)


@bot.command()
async def echo(ctx, arg): # The name of the function is the name of the command
    #print(arg) # this is the text that follows the command
    await ctx.send(arg) # ctx.send sends text in chat

@bot.command()
async def rickroll(ctx): # The name of the function is the name of the command
    #print(arg) # this is the text that follows the command
    await ctx.send('https://imgur.com/gallery/yed5Zfk') # ctx.send sends text in chat

bot.run(TOKEN)