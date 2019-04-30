import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import datetime
import time
from threading import Thread
import youtube_dl

client = discord.Client()

def run():
  app.run(host='0.0.0.0',port=8080)

@app.route('/',methods=["HEAD","GET"])
def home():
  keep_alive()
  return "cool"

bot = commands.Bot(command_prefix='-', status=discord.Status.idle, activity=discord.Game(name="Booting.."))

@bot.event
async def on_ready():
    print ("hello")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)
    listen_list = ["-slime | for help", "- | prefix", "Developed by ×Vēørēs×#0095", "SlimeCrew Server"]
    while True:
        await bot.change_presence(game=discord.Game(name=random.choice(listen_list), type=2))
        await asyncio.sleep(6)

bot.remove_command("help")

players = {}

@bot.event
async def on_message(message):
        await bot.process_commands(message)

    
@bot.command()
async def ping():
	await bot.say('**Pong!**')
@bot.command()
async def ahoj():
	await bot.say('__**Ahoj :D**__')
@bot.command()
async def developer():
	await bot.say('**Deveveloped by ×Vēørēs×#0095**')
@bot.command()
async def yt():
	await bot.say('__**Mukiho kanál máš zde:**__ https://www.youtube.com/channel/UC1NLRqhH9K2hdngHv0QSW') 
@bot.command()
async def help():
	await bot.say('**userinfo [@user], yt, developer, ping, ahoj, number**')
@bot.command(pass_context=True)
async def number(ctx):
	await bot.say(random.randint(1,100))
@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.Member):
    await bot.say("**JMÉNO:** {}".format(user.name))
    await bot.say("**STATUS:** {}".format(user.status))
    await bot.say("**NEJVĚTŠÍ ROLE:** {}".format(user.top_role))
    await bot.say("**PŘIPOJIL SE:** {}".format(user.joined_at))
    print ("id")
    await bot.say("**ID:** {}".format(user.id))

bot.run('NTU2MTkzMDE0NTA3MjQxNDgx.D22Kuw.udW1_dDnQBucL-dXaPbDUUHf7CQ')
