import os
import discord
import httex2json
import cvmaker

from dotenv import load_dotenv

load_dotenv()

danger_list=['''"''',"'","\\"]

help='''CVBot Commands Start with a '&'
&help -> Show this help screen
&choices -> Select CV Template
'''

choicelist=["1.SimpleCV"]

client=discord.Client()

@client.event
async def on_ready():
  print("Ready Steady po")
  await client.change_presence(activity=discord.Game(name="  &help"))

@client.event
async def on_message(message):
  # we do not want the bot to reply to itself
  if message.author == client.user:
      return
      
  secure_text=message.content
  for danger in danger_list:
    secure_text=secure_text.replace(danger,"")

  if secure_text.startswith("&help"):
    await message.channel.send(help)

  if secure_text.startswith("&choices"):
    b="".join(choicelist)
    await message.channel.send(b)

  if secure_text.startswith("&1") or secure_text.startswith("&SimpleCV") or secure_text.startswith("&1.SimpleCV"):
    await message.channel.send("Send your Data in the following format  : ")
    await message.channel.send('''```&make1 
<name>{Your Name}</name>
<email>{Your email}</email>
<exp>{experience heading}{experience details}</exp>
<exp>{experience heading}{experience details}</exp>
.
.
<edu>{education heading}{education details}</edu>
<edu>{education heading}{education details}</edu>
.
.
<pro>{project heading}{project details}</pro>
<pro>{project heading}{project details}</pro>
.
.
<link>{Facebook}{www.facebook.com/you}</link>
<link>{Twitter}{www.twitter.com/you}</link>```''')

  if secure_text.startswith("&make1"):
    print("$ Received job")
    userdat=secure_text.replace("&make1","")
    filename=cvmaker.template1(httex2json.httex2json(userdat))
    await message.channel.send("Here is your cv  🤩📄",file=discord.File(filename))

    


client.run(os.getenv('DISCORD_TOKEN'))