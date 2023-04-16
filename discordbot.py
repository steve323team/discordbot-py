from cmath import log
import discord
import os

TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print('login')
    print(client.user.name)
    print(client.user.id)
    print('-----------------')
    await client.change_presence(game=discord.Game(name='DeNi BOT', type=1))
    
@client.event
async def on_message(message):
       if message.channel.is_private and message.author.id != "1082274007648317452":
        await client.send_message(discord.utils.get(client.get_all_members(), id="1063636047436730378"), message.author.name + "(" + message.author.id + ") : " + message.content)
    
       if message.channel.is_private and message.author.id != "1082274007648317452":
        await client.send_message(client.get_channel("1097156613544091729"), message.author.name + "(" + message/author.id + ") : " + message.content)
        
       if message.content.startswith("!DM"):
        member = discord.utils.get(client.get_all_members(), id=message.content[4:22])
        await client.send.message(member, "DeNi : " + message.content[23:])
        
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
