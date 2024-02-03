

#environment variable importing
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the TOKEN variable from the environment
token = os.getenv("TOKEN")

##command bit of code from discord package
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio

#intialize bot; inside bracket is prefix bot will listen on discord server "!" calls the discord bot
#Prefix commands are ones where a bot searches the beginning of a message for a set of characters. 
#It uses this to know if the the message contains a command that it needs to run.

#intents is not enabled in discord.py
intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix='!',intents=intents)

#When a event detects a certain action it will run a certain piece of code
@client.event
#on ready function when the bot is ready to recieve commands it will execute this function
async def on_ready():
    print("The bot is ready to receive commands")
    print("-----------------")


@client.command()
#name of function to call a action
#!hello would be recieved in discord and the message below would send
#ctx taking input from discord
async def hello(ctx):
    await ctx.send("Hello I am Verstappen Bot")

@client.command()
async def goodbye(ctx):
    await ctx.send("Goodbye, Hope you have a great day")

#if member joins
@client.event
#detect when user joins servers and does whats written below
async def on_member_join(member):
    #tells bot to send message to channel with id, guild is server
    server_id = 1189987156102496436
    server = client.get_guild(server_id)
    channel_id = 1189987156102496439
    channel = server.get_channel(channel_id)
    await channel.send(f'Welcome {member.mention} to the server, I am your friendly bot')

#if member leaves
@client.event
async def on_member_remove(member):
    server_id = 1189987156102496436
    server = client.get_guild(server_id)
    channel_id = 1189987156102496439
    channel = server.get_channel(channel_id)
    await channel.send(f'Goodbye {member.mention}, Hope to see you again')

#Bot to join voice channel
@client.command(pass_context = True)
#ctx allows to receive and send messages(input)
async def join(ctx):
    #means user is in the voice channel
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        #plays intro for bot when it joins voice channel
        source = FFmpegPCMAudio("BangBang Oblock SoSa.mp3")
        player = voice.play(source)
    else:
        await ctx.send("You are currently not in a voice channel, you must be in one to run this command!")

#Bot to leave voice channel
@client.command(pass_context = True)
async def leave(ctx):
    #seeing if bot is in channel
    if (ctx.voice_client):
        #go to guild then bot then disconnect is the thought process
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I left the voice channel")
    else:
        await ctx.send("I am not in a voice channel")



#tells the bot to run
#Put token in the brackets which only your bot has
# Use the token in your client.run() function
client.run(token)



