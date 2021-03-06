#!/usr/bin/python3

# Imports for Discord Commands
import time
from datetime import datetime
import pytz
import discord
import os
import random
import requests
import json
import webbrowser
from dadjokes import Dadjoke
from discord.ext import commands
from discord.ext.commands import Context
import string
import asyncpraw
import aiohttp
from aiohttp import ClientSession

#Authentication for Discord and 
TOKEN = os.getenv("TOKEN")
client = discord.Client()
food_list = ["pizza 🍕", "lasagna", "a cheeseburger 🍔", "tacos 🌮", "a burrito 🌯", "spaghetti 🍝", "pad thai", "pho", "barbeque", "fried chicken 🍗", "sushi 🍣", "ice cream 🍦", "curry", "a sandwich 🥪", "steak 🥩", "mac and cheese" ,"a microwave dinner", "nothing (get rekt)", "a PB&J Sandwhich", "a salad 🥗", "Chinese food", "pancakes 🥞", "chicken and waffles", "hot dogs 🌭", "chicken tendies", "enchiladas", "Korean BBQ", "a gyro 🥙", "chicken nuggets", "a cheesesteak sandwich", "a burrito bowl", "a banh mi", "ramen 🍜", "a poke bowl", "fish and chips"]
dadjoke = Dadjoke()
rand_num = range(1,10)
hd_tl = ["Heads", "Tails"]
bot = commands.Bot(command_prefix="!")
embed = discord.Embed()
commands = ("!commands", "!hello", "!lunch", "!dinner", "!number", "!coinflip", "!joke", "!time","!pwmaker","!aww","!memes","!pfd","!wcgw","!youtube","!google")
pizza_counter = 0
activity = discord.Game(name = "Away From Keyboard")



### Time Zones ###

# California Time
tz_CA = pytz.timezone("America/Los_Angeles")
datetime_CA = datetime.now(tz_CA)
dt_CA = datetime_CA.strftime("%Y-%m-%d  | %I:%M:%S %p")

# Colorado Time
tz_CO = pytz.timezone("America/Denver")
datetime_CO = datetime.now(tz_CO)
dt_CO = datetime_CO.strftime("%Y-%m-%d | %I:%M:%S %p")

# Illinois Time
tz_IL = pytz.timezone("America/Chicago")
datetime_IL = datetime.now(tz_IL)
dt_IL = datetime_IL.strftime("%Y-%m-%d   | %I:%M:%S %p")

# New York Time
tz_NY = pytz.timezone("America/New_York")
datetime_NY = datetime.now(tz_NY)
dt_NY = datetime_NY.strftime("%Y-%m-%d    | %I:%M:%S %p")

# Bot Login

@client.event
async def on_ready():
  print("{0.user} has logged into the the server." .format(client))
  await client.change_presence(status=discord.Status.idle, activity = activity)


# Commands for Discord Bot in Server


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  elif message.content.startswith("!commands"):
    await message.channel.send("Check out these commands on this channel: \n!hello \n!memes (This will produce five of the newest memes from r/memes subreddit.) \n!pfd (This will produce five of the newest posts from r/PeopleFuckingDying.) \n!aww (This will provide five of the newest posts from r/aww.) \n!wcgw (This will provide five of the newest posts from r/Whatcouldgowrong.) \n!lunch (This will choose a random food for you to eat for lunch.) \n!dinner (This will choose a random food for you to eat for dinner) \n!number (This will think of a number 1-10.) \n!coinflip (This will flip a coin for you.) \n!joke (This will tell a random dad joke.) \n!time (This will display the current time for 4 American time zones.) \n!pizza (This will show how many pizza slices have been eaten.) \n!pwmaker (This will generate a random 16 character password and send it to you in a private DM.) \n!youtube (This will provide a link to Youtube.) \n!google (This will provide a link to Google.) \nMore commands will be available in the future! Stay tuned!")

  elif message.content.startswith("!dinner"):
    await message.channel.send("{0} is eating {1} for dinner!" .format(message.author, random.choice(food_list)))

  elif message.content.startswith("!lunch"):
    await message.channel.send("{0} will be eating {1} for lunch today!" .format(message.author, random.choice(food_list)))

  elif message.content.startswith("!joke"):
    dadjoke = Dadjoke()
    await message.channel.send(dadjoke.joke)
  
  elif message.content.startswith("!time"):
    await message.channel.send("Current PDT date and time is: {0}. \nCurrent MDT date and time is: {1}. \nCurrent CST date and time is: {2}. \nCurrent EST date and time is: {3}." .format(dt_CA, dt_CO, dt_IL, dt_NY))

 
  elif message.content.startswith("!coinflip"):
    await message.channel.send("The 🪙 landed on {}!" .format(random.choice(hd_tl)))
    
  elif message.content.startswith("!hello"):
    await message.channel.send("Hello {}!👋" .format(message.author))

  elif message.content.startswith("!number"):
    await message.channel.send("The number I am thinking of is {}!" .format(random.choice(rand_num)))

  elif message.content.startswith("!pizza"):
	  global pizza_counter
	  pizza_counter += 1
	  await message.channel.send("{} slices of 🍕 have been eaten so far!" .format(pizza_counter))

    # Embed Links for Youtube and Google
  elif message.content.startswith("!youtube"):
    embed.set_author(name = "Youtube", url="https://www.youtube.com", icon_url="https://i.imgur.com/U2TRVbz.png?1")
    embed.description = "Click above to open Youtube in a new tab."
    await message.channel.send(embed=embed)

  elif message.content.startswith("!google"):
    embed.set_author(name = "Google", url = "https://www.google.com", icon_url = "https://i.imgur.com/PDL9lTM.jpg")
    embed.description = "Click above to open Google in a new tab."
    await message.channel.send(embed=embed)

    # Password Maker
  elif message.content.startswith("!pwmaker"):
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation
    password_characters = letters + digits + punctuation
    password = ''.join(random.choice(password_characters) for i in range(16))
    await message.author.send("Your 16 character password is: **{}** . Please save your password in a text or Word file to prevent its loss. Please do not share your password with anyone else!" .format(password))

    # Reddit Pull Using API
  elif message.content.startswith("!memes"):
    reddit = asyncpraw.Reddit(client_id = os.getenv("rclientid"),client_secret = os.getenv("rclientsecret"),user_agent = os.getenv("ruseragent"),username = os.getenv("rusername"),password = os.getenv("rpassword"))
    subreddit = await reddit.subreddit("memes")
    session = ClientSession()  
    async for submission in subreddit.new(limit=5):
      await message.channel.send(submission.title + " " + submission.url)
    await session.close()
  
  elif message.content.startswith("!pfd"):
    reddit = asyncpraw.Reddit(client_id = os.getenv("rclientid"),client_secret = os.getenv("rclientsecret"),user_agent = os.getenv("ruseragent"),username = os.getenv("rusername"),password = os.getenv("rpassword"))
    subreddit = await reddit.subreddit("PeopleFuckingDying")
    session = ClientSession()  
    async for submission in subreddit.new(limit=5):
      await message.channel.send(submission.title + " " + submission.url)
    await session.close()

  elif message.content.startswith("!aww"):
    reddit = asyncpraw.Reddit(client_id = os.getenv("rclientid"),client_secret = os.getenv("rclientsecret"),user_agent = os.getenv("ruseragent"),username = os.getenv("rusername"),password = os.getenv("rpassword"))
    subreddit = await reddit.subreddit("aww")
    session = ClientSession()  
    async for submission in subreddit.new(limit=5):
      await message.channel.send(submission.title + " " + submission.url)
    await session.close()

  elif message.content.startswith("!wcgw"):
    reddit = asyncpraw.Reddit(client_id = os.getenv("rclientid"),client_secret = os.getenv("rclientsecret"),user_agent = os.getenv("ruseragent"),username = os.getenv("rusername"),password = os.getenv("rpassword"))
    subreddit = await reddit.subreddit("Whatcouldgowrong")
    session = ClientSession()  
    async for submission in subreddit.new(limit=5):
      await message.channel.send(submission.title + " " + submission.url)
    await session.close()
    
  else:
    pass


### TOKEN ###
client.run(os.getenv("TOKEN"))
