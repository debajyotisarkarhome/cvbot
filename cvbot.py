import discord
import os
import httex2json,cvmaker


token = eval(open("secrets","r").read())
token=token["dckey"]

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
  secure_text=message.content
  for danger in danger_list:
    secure_text=secure_text.replace(danger,"")

  if secure_text.startswith("&help"):
    await message.channel.send(help)

  if secure_text.startswith("&choices"):
    b="".join(choicelist)
    await message.channel.send(b)

  if secure_text.startswith("&1"):
    await message.channel.send("Send your Data in the following format  : ")
    await message.channel.send('''```&start
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

  if secure_text.startswith("&start"):
    print("gotit")
    userdat=secure_text.replace("&start","")
    filename=cvmaker.template1(httex2json.httex2json(userdat))
    await message.channel.send("Here is your cv  🤩📄")
    await message.channel.send(file=discord.File(filename))

    


client.run(token)