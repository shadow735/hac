import os
import discord
from discord.ext import commands
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve values from environment variables
discord_token = os.getenv('DISCORD_TOKEN')
twilio_account_sid = os.getenv('TWILIO_ACCOUNT_SID')
twilio_auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_whatsapp_number = os.getenv('TWILIO_WHATSAPP_NUMBER')
your_whatsapp_number = os.getenv('YOUR_WHATSAPP_NUMBER')

# Twilio setup
client = Client(twilio_account_sid, twilio_auth_token)

def send_whatsapp_message(message):
    try:
        client.messages.create(
            from_=twilio_whatsapp_number,  # Twilio-provided WhatsApp number
            body=message,
            to=your_whatsapp_number  # Your WhatsApp number
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

# Event handler for creating a new channel
@bot.event
async def on_guild_channel_create(channel):
    if isinstance(channel, discord.TextChannel):
        message = f"A new channel named '{channel.name}' has been created."
        send_whatsapp_message(message)

# Run the bot with your token
bot.run(discord_token)
