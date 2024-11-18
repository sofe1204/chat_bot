from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Configure bot intents
intents: Intents = Intents.default()
intents.message_content = True 

client: Client = Client(intents=intents)

async def send_message(message: Message, user_message: str) -> None:
    if not user_message.strip():
        print("(Message was empty)")
        return

    is_private = user_message.startswith("?")
    if is_private:
        user_message = user_message[1:]  

    try:
        response: str = get_response(user_message)
        if is_private:
            await message.author.send(response)  
        else:
            await message.channel.send(response)  
    except Exception as error:
        print(f"Error while sending message: {error}")

@client.event
async def on_ready() -> None:
    """
    Triggered when the bot successfully connects to Discord.
    """
    print(f"{client.user} is now running.")

@client.event
async def on_message(message: Message) -> None:
    """
    Triggered whenever a message is sent in a channel the bot can access.

    :param message: The Discord message object.
    """
    if message.author == client.user:
        return  

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f"[{channel}] {username}: \"{user_message}\"")
    await send_message(message, user_message)

def main() -> None:
    """
    Entry point for the bot application.
    """
    try:
        client.run(TOKEN)
    except Exception as error:
        print(f"Failed to start the bot: {error}")

if __name__ == "__main__":
    main()
