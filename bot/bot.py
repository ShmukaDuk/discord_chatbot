import discord
from discord import app_commands
from discord.ext import commands
import os

from olama_api import OlamaAPI

from dotenv import load_dotenv
load_dotenv()


TOKEN = os.getenv('BOT_TOKEN')
FRIEND_NAME = os.getenv('FRIEND_NAME')
OLAMA_ADD = os.getenv('OLAMA_ADD')

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)
if (OLAMA_ADD is not None):
    olama = OlamaAPI(OLAMA_ADD)

@bot.event
async def on_ready():
    print("bot is running")
    try:
        synced = await bot.tree.sync()
    except Exception as e:
        print(e)

@bot.event
async def on_voice_state_update(member, before, after):
    if member.name == "shmuk" and before.channel is None and after.channel is not None:
        if (OLAMA_ADD):
            message_response = olama.greetUser("User dmc has joined the voice channel")
        else:
            message_response = "dmc gay"
        if member.guild.system_channel is not None:
            await member.guild.system_channel.send(message_response)
        else:
            # Alternatively, you can specify a channel by ID
            channel = member.guild.get_channel(CHANNEL_ID)
            if channel is not None:
                await channel.send(message_response)

@bot.tree.command(name="hello")
async def hello1(interaction: discord.Interaction):
    print(interaction.data)
    await interaction.response.send_message(":)")

@bot.tree.command(name="help")
@app_commands.describe(user_message="help with what?")
async def talk(interaction: discord.Interaction, user_message: str):    
    if olama:
        message_response = olama.run_lama(user_message)
    else:
        message_response = "This response is not from ai 🤣🤣🤣🤣, \nplease config your olama"
    await interaction.response.send_message(message_response)

bot.run(TOKEN)
