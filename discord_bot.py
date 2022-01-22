import discord
from discord import channel
from discord import embeds
from discord import member
from discord.ext import commands
import os
import re
import random
import asyncio
import itertools
import sys
from discord_components import Button, ButtonStyle
from math import *
import asyncio
import traceback
import time
from async_timeout import timeout
from functools import partial
import youtube_dl
from discord.ext.commands import Bot
from youtube_dl import YoutubeDL
import colorama
from colorama import Fore
from msvcrt import getch

os.system('cls')
user_discord_name = input(f'\r{Fore.RESET}Enter discord name bot {Fore.LIGHTBLUE_EX}>> {Fore.LIGHTYELLOW_EX}')
print("")
while user_discord_name == '':
    os.system('cls')
    print(f'{Fore.LIGHTRED_EX}Name Is Invalid, Please try again!')
    print("")
    user_discord_name = input(f'\r{Fore.RESET}Enter discord name bot {Fore.LIGHTBLUE_EX}>> {Fore.LIGHTYELLOW_EX}')

while not user_discord_name == "Gizzy's":
    os.system('cls')
    print(f'{Fore.LIGHTRED_EX}Name Is Invalid, Please try again!')
    print("")
    user_discord_name = input(f'\r{Fore.RESET}Enter discord name bot {Fore.LIGHTBLUE_EX}>> {Fore.LIGHTYELLOW_EX}')

print("")
print('\rReading Token ...')
time.sleep(1.5)
TOKEN = "" # Token for discord_bot
print("")
os.system('cls')
print(Fore.LIGHTGREEN_EX + 'Verification token ... /')
time.sleep(0.9)
os.system('cls')
print(Fore.LIGHTGREEN_EX + 'Verification token ... -')
time.sleep(0.4)
os.system('cls')
print(Fore.LIGHTGREEN_EX + 'Verification token ... |')
time.sleep(0.2)
os.system('cls')
os.system('cls')
print(Fore.LIGHTGREEN_EX + 'Verification token ... \\')
time.sleep(0.9)
os.system('cls')
print(Fore.LIGHTGREEN_EX + 'Verification token ... /')
time.sleep(0.4)
os.system('cls')
print(Fore.LIGHTGREEN_EX + 'Verification token ... -')
time.sleep(0.2)
os.system('cls')
os.system('cls')
print(Fore.LIGHTGREEN_EX + 'Verification token ... \\')
time.sleep(0.9)
os.system('cls')
print(Fore.LIGHTGREEN_EX + 'Verification token ... /')
time.sleep(0.4)
os.system('cls')
print(Fore.LIGHTGREEN_EX + 'Verification token ... -')
time.sleep(0.2)
os.system('cls')
print(Fore.LIGHTGREEN_EX + 'Verification token ... \\')
time.sleep(1.4)
os.system('cls')
print(Fore.LIGHTGREEN_EX + 'Verification token ... |')
time.sleep(0.2)
os.system('cls')
print(Fore.LIGHTGREEN_EX + 'Verification token ... -')
time.sleep(0.2)
os.system('cls')
time.sleep(3)
if TOKEN == '':
    print("")
    print(Fore.LIGHTRED_EX + '❌ Verification Is Failed')
    print("")
    TOKEN = input(f'{Fore.YELLOW}Enter your token {Fore.GREEN}>> {Fore.LIGHTMAGENTA_EX}')

if not TOKEN == 'OTMwMDc3ODY3NjU0NjcyNDA0.Ydwogw.BP3YgndU4qcpnofDXOxgL_UhEB0':
    print("")
    print(Fore.LIGHTRED_EX + 'TOKEN IS INVALID, PLEASE ENTER YOUR TOKEN IN >>>>>>>>>>>>>>> [ TOKEN = "" # Token for discord_bot! ]')
    print("")
    print(f'                                     {Fore.LIGHTBLUE_EX}Detected By :{Fore.LIGHTWHITE_EX} Giuseppe{Fore.LIGHTRED_EX} | ERROR:   ⬆️ {Fore.LIGHTWHITE_EX} Missing on line 37!')
    print("")
    print(Fore.WHITE + "Press any key to exit...")
    print(Fore.WHITE)
    junk = getch() # Assign to a variable just to suppress output. Blocks until key press.
    sys.exit()

print("")
print(f'\r{Fore.WHITE}TOKEN : {TOKEN}')
print("")
print(Fore.LIGHTGREEN_EX + 'Verification Is Success ✔')

time.sleep(1.5)

os.system('cls')
print('Connecting to discord server! ...')
time.sleep(3)
os.system('cls')
print(Fore.LIGHTBLUE_EX)
print("Connecting 35%")
time.sleep(1) #do some work here...
os.system('cls')
print("Connecting 79%")
time.sleep(0.4) #do some more work here...
os.system('cls')
print("Connecting 91%")
time.sleep(1) #do even more work...
os.system('cls')

print("Connecting 100%")
time.sleep(4) #gratuitious amounts of work...
os.system('cls')

print(Fore.LIGHTWHITE_EX)

bot = commands.Bot(command_prefix=".")

intents = discord.Intents.default()

intents.members=True

invites = {}

replace_with = '!@#$%^&*()\':;.,><UwU--_--=+`~\|][}{[/?'

print(f'Connecting To Discord ... ')

client = discord.Client(intents=intents)
time.sleep(1.3)
os.system('cls')

@bot.event
async def on_ready():
    # Get the size of the file
    size = os.stat("discord_bot.py").st_size

    # Convert to familiar units
    kb = size / 1024
    mb = size / 1024 / 1024

    # print the results to the console
    print('WARNING')
    print('File Size')
    print("size in kb:", kb)
    print("size in mb:", mb)
    print("")
    print(f'{bot.user} succesfully logged in!')
    # Getting all the guilds our bot is in
    for guild in bot.guilds:
        # Adding each guild's invites to our dict
        invites[guild.id] = await guild.invites()
        
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # L O G G I N G
    username = message.author.display_name
    msg = message.content
    with open('BadWords.txt', 'r') as f:
        blacklist = f.read()
    if message.author.bot:
      return
    elif msg.lower() in blacklist:
      await message.delete()
      embed=discord.Embed(title=f"⚠️WARNING⚠️", description=f"{message.author} Do not say that words!", color=0xe74c3c)
      embed.set_footer(text=f"Detected by Gizzy#0857 Bot (G)")
      print(f"Gizzy's Bot has detected bad words from {message.author} (Message Has Deleted)")
      await message.channel.send(embed=embed)
    else:
      await bot.process_commands(message)

    if message.content == 'hello':
        await message.channel.send(f'Hi! {message.author}')
        print(f"\rBot :: Hi! {message.author}")
    if message.content == 'Hello':
        await message.channel.send(f'Hi! {message.author}')
        print(f"\rBot :: Hi! {message.author}")
    if message.content == 'bye':
        await message.channel.send(f'Goodbye {message.author}')
        print("\rBot :: Goodbye")
    if message.content == 'fuck':
        print(f"Bot detected bad words from {message.author}!")
    if message.content == 'FUCK':
        print(f"Bot detected bad words from {message.author}!")
    if message.content == 'shutdown_bot':
        await message.channel.send(f'I am exiting (Bye!)')
        await bot.close()
        print('Bot is disconnected from the server!')
        os.system('cls')
        print(Fore.WHITE + "Press any key to exit...")
        print(Fore.WHITE)
        junk = getch() # Assign to a variable just to suppress output. Blocks until key press.
        os.system('cls')
        sys.exit()

        # Get the size of the file
        size = os.stat("discord_bot.py").st_size

        # Convert to familiar units
        kb = size / 1024
        mb = size / 1024 / 1024

        # print the results to the console
        print('WARNING')
        print('File Size')
        print("size in kb:", kb)
        print("size in mb:", mb)
        print("")
        print(f'{bot.user} succesfully logged in!')
        print('\rBot is disconnected from the server!')
    await bot.process_commands(message)

@bot.event
async def on_message_join(member):
    channel = client.get_channel('930085038345814050')
    embed=discord.Embed(title=f"Welcome {member.name}", description=f"Thanks for joining {member.guild.name}!") # F-Strings!
    embed.set_thumbnail(url=member.avatar_url) # Set the embed's thumbnail to the member's avatar image!
    await channel.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used!')

@bot.event
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

@bot.event
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify an amount of messages to delete!')

def find_invite_by_code(invite_list, code):
    
    # Simply looping through each invite in an
    # invite list which we will get using guild.invites()
    
    for inv in invite_list:
        
        # Check if the invite code in this element
        # of the list is the one we're looking for
        
        if inv.code == code:
            
            # If it is, we return it.
            
            return inv

@bot.event
async def on_member_join(member):

    print(f"{member} Has joined to Server!")

    # Getting the invites before the user joining
    # from our cache for this specific guild

    invites_before_join = invites[member.guild.id]

    # Getting the invites after the user joining
    # so we can compare it with the first one, and
    # see which invite uses number increased

    invites_after_join = await member.guild.invites()

    # Loops for each invite we have for the guild
    # the user joined.

    for invite in invites_before_join:

        # Now, we're using the function we created just
        # before to check which invite count is bigger
        # than it was before the user joined.
        
        if invite.uses < find_invite_by_code(invites_after_join, invite.code).uses:
            
            # Now that we found which link was used,
            # we will print a couple things in our console:
            # the name, invite code used the the person
            # who created the invite code, or the inviter.
            
            print(f"Member {member.name} Joined")
            print(f"Invite Code: {invite.code}")
            print(f"Inviter: {invite.inviter}")
            
            # We will now update our cache so it's ready
            # for the next user that joins the guild

            invites[member.guild.id] = invites_after_join
            
            # We return here since we already found which 
            # one was used and there is no point in
            # looping when we already got what we wanted
            return

@bot.event
async def on_message_delete(message):
  if message.author.bot:
    return
  await bot.send_message(message.channel, "<@{}>'s message was deleted".format(message.author.id))

@bot.event
async def on_member_remove(member):
    
    # Updates the cache when a user leaves to make sure
    # everything is up to date
    
    invites[member.guild.id] = await member.guild.invites()

@bot.command()
async def message_id(ctx):
    '''
    See Message ID In Server
    
    .message_id

    '''
    await ctx.send_message(message_id)

bot.run(TOKEN) #you get a token if you create a bot on the discord developer page
