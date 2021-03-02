import os
import discord
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
from discord.ext.commands import Bot

load_dotenv()
DISCORD_TOKEN = os.getenv("discord_token")

client = discord.Client()
bot = Bot(command_prefix='!')


@client.event
async def on_ready():
    print(f'{client.user} has come to regulate.')


@client.event
async def on_message(message):
    # add role when exact phrase is entered anywhere
    member = message.author
    if message.content == "I, ${member}, pledge to give my body and soul to":
        role = discord.utils.get(member.guild.roles.get('Member'))
        await member.add_roles(role)


# start the bot
bot.run(DISCORD_TOKEN)
