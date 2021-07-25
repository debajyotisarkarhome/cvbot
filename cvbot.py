import discord
import os


token = eval(open("secrets","r").read())
token=token["dckey"]

help='''CVBot Commands Start with a '&'
&help -> Show this help screen
&choices -> Select CV Template
'''

choicelist=["1.SimpleCV"]

client=discord.Client()

@client.event
async def on_ready():
  print("Ready Steady po")

@client.event
async def on_message(message):
  if message.content.startswith("&help"):
    await message.channel.send(help)

  if message.content.startswith("&choices"):
    b="".join(choicelist)
    await message.channel.send(b)

  if message.content.startswith("&1"):
    await message.channel.send("Send your Data in the following format  : ")
    await message.channel.send('''```&Start
<name>{Your Name}</name>
<email>{Your email}</email>
<exp>{expirience heading}{expirience details}</exp>
<exp>{expirience heading}{expirience details}</exp>
.
.
<edu>{education heading}{education details}</edu>
<edu>{education heading}{education details}</edu>
.
.
<pro>{project heading}{project details}</edu>
<pro>{project heading}{project details}</edu>```''')
    


client.run(token)