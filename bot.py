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
        await message.channel.send(f'Hi {message.author.mention}')
    if message.content == 'bye knee':
        await message.channel.send(f'Goodbye {message.author.mention}')

    if message.content == 'pineapple on':
        await message.channel.send(f'{message.author.mention} thinks pineapple belongs on pizza!')
        #await channel.send(file=discord.File('Pineapple on pizza.png'))
        await message.channel.send('https://imgur.com/a/vms5Ti2')

    if message.content == 'no pineapple':
        await message.channel.send(f'{message.author.mention} thnks pineapple does not belong on pizza!')
        #await channel.send(file=discord.File('no pineapple pizza.png'))
        await message.channel.send('https://imgur.com/a/4eMOjNK')

    await bot.process_commands(message)


@bot.event
async def on_message_delete(message):
    await message.channel.send(f'The message "{message.content}" was just deleted by {message.author.mention} (or by a mod!)')


@bot.event
async def on_message_edit(before, after):
    await before.channel.send(f'You changed "{before.content}" to "{after.content}" by {before.author.mention}')


@bot.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f"A Reaction was added by {user.mention} to {reaction.message.content}")

@bot.event
async def on_reaction_remove(reaction, user):
    await reaction.message.channel.send(f"A Reaction was removed by {user.mention} to {reaction.message.content}")
    
'''
@bot.event
async def on_member_join(member):
    await
'''


@bot.command()
async def echo(ctx, arg): # The name of the function is the name of the command
    #print(arg) # this is the text that follows the command
    await ctx.send(arg) # ctx.send sends text in chat

@bot.command()
async def rickroll(ctx): # The name of the function is the name of the command
    #print(arg) # this is the text that follows the command
    await ctx.send('https://imgur.com/gallery/yed5Zfk') # ctx.send sends text in chat

@bot.command()
async def helpknee(ctx):
    await ctx.send("Hi I'm knee bot! I was created by gimmegold500 some of the current commands supported are \n !rickroll \n ! echo __ \n hi knee \n bye knee \n pineapple on \n pineapple off \n You can also try editing, reacting or deleting a message! Happy Discording!")

bot.run(TOKEN)
