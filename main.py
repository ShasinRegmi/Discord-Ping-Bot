import discord
from discord.ext import commands #for commands
import asyncio

class Client(discord.Client):
    async def on_ready(self): #async function
        print(f'Logged on as {self.user}.')
   
   
    async def on_message(self, message):
        if message.author == self.user: #we dont want infinite loops
            return
        
        if message.content.startswith('hello'): #bot will reply if the message starts with hello
             await message.channel.send(f'Yo man {message.author.mention}') #pauses the execution of the on_message coroutine until the message is sent.


        if message.content == '1':
            # Loop to mention the user repeatedly
          while True:
             await message.channel.send('Hey ' + "<@{}>".format(530675632741285898) + ' are you here?')#mention specfic user with id
             await asyncio.sleep(1)

intents = discord.Intents.default()
intents.message_content = True

Client = Client(intents=intents)
Client.run('#token') #insert your token here