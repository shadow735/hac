import discord
from discord.ext import commands
from twilio.rest import Client

# Discord bot token and server ID
server_id = "1262477641676750980"
token = "MTI2MjY5ODgzMjAzOTUxMDAzNw.Gj1HpW.geCvt6Ms4EZq4TNe5mBmZkxxNyyBeYIRUxG5i4"  # Replace with your bot token

# Twilio setup
account_sid = 'AC47a864c9272de0ca6ec1318282c2b5d2'
auth_token = 'b1e1f02639c8a60ed37436e666e15e4f'
client = Client(account_sid, auth_token)

def send_whatsapp_message(message):
    try:
        client.messages.create(
            from_='whatsapp:+14155238886',  # Twilio-provided WhatsApp number
            body=message,
            to='whatsapp:+918433767254'  # Your WhatsApp number
        )
        print("WhatsApp message sent successfully.")
    except Exception as e:
        print(f"Failed to send WhatsApp message: {e}")

# Discord bot setup
intents = discord.Intents.default()
intents.guilds = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_guild_channel_create(channel):
    if isinstance(channel, discord.TextChannel):
        message = f"A new channel named '{channel.name}' has been created."
        send_whatsapp_message(message)

# Run the bot with your token
bot.run(token)
