import os
from dotenv import load_dotenv
import discord




load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

def create_client() -> discord.Client:
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)
    return client

def init():
    if not TOKEN:
        raise RuntimeError("TOKEN is missing from .env")

    client = create_client()

   # setup_events(client)
   # setup_commands(client)

    client.run(TOKEN)

if __name__ == "__main__":
    init()