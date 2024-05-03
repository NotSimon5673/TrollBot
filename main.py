import discord
from discord import app_commands
from discord import Intents
import random as rand

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@tree.command(name="getrandommember", description="It do what it say 8==D")
async def getmember(interaction):
    memberlist = interaction.guild.members
    victim = rand.choice(memberlist)
    user = victim.display_avatar
    id = victim.id
    name = victim.name
    nick = victim.nick

    yok = discord.Embed(title="User info:", color=0xE8D3B9)
    yok.set_image(url=user)
    if nick != None:
        yok.add_field(name="Display Name", value="**" + str(nick) + "**")
    yok.add_field(name="Username", value="**" + str(name) + "**")
    yok.add_field(name="Id", value="**" + str(id) + "**")

    await interaction.response.send_message(embed=yok)


@tree.command(name="spamping", description="Let's have some fun >:3")
async def spamPing(interaction, user: str, amount: int, msg: str = None):
    memberlist = interaction.guild.members
    for member in memberlist:
        if member.name == user:
            id = member.id
    for i in range(amount):
        await interaction.channel.send("<@" + str(id) + "> " + msg)


@tree.command(name="destruct", description="Die")
async def explode(interaction):
    await interaction.response.send_message("AHHHHHHHHHHHHHHHHHHHHHH")
    quit()


@client.event
async def on_ready():
    await tree.sync()
    print("It's trolling time")


client.run("")
