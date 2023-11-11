import discord #Imports discord library
import config

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents) #Creates an instance of a client

@client.event #This registers an event
async def on_ready(): #Sends a message when the bot is ready
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message): #Listens for messages
    if message.author == client.user: #Makes sure we ignore messages from the bot itself
        return
    
    if message.content.startswith("!hello"):
        await message.channel.send("Hello!")

client.run(config.access_token)