import os
import discord

TOKEN = os.environ['TOKEN']

@client.event
async def on_message(message):
    if client.private_channels and message.author.id != ("1082274007648317452"):
        await client.get_channel("1097156613544091729").send(message.author.name + "(" + str(message.author.id) + "): " + message.content)


    if message.content.startswith("!DM"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)
        
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
