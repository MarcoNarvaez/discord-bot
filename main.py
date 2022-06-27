from email.quoprimime import quote
import discord
import os
import requests
import json

# class MyClient(discord.Client):
#     async def on_ready(self):
#         print('Logged on as {0}!'.format(self.user))

#     async def on_message(self, message):
#         print('Message from {0.author}: {0.content}'.format(message))

# client = MyClient()
# client.run('my token goes here')

client = discord.Client()

sad_words = ['sad', 'depresion', 'unhappy', 'angry', 'miserable']

def get_api():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' -' + json_data[0]['a']
    return quote
    
@client.event
async def on_ready():
    print('We hace logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    
    if message.content.startswith('$inspire'):
        quote = get_api()
        await message.channel.send(quote)
        
client.run(os.getenv('TOKEN'))