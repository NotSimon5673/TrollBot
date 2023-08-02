import autoupdate


import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
token = ""



@tree.command(name="die",description="test")
async def command(interaction):
    await interaction.response.send_message("AAA")

@tree.command(name="update",description="updates to the most recent version of the branch that the bot is running on")
async def update():
    autoupdate.branchUpdate()

@client.event
async def ready():
    await tree.sync(guild=discord.Object(id=963784293933535252))
    print("It's trolling time")

client.run(token)