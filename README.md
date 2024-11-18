# Discord Bot: Responsive Chat Bot

This repository contains a Python-based Discord bot that processes user messages and responds dynamically. The bot is designed with a professional structure, ensuring readability, maintainability, and ease of use.

## Features
- **Public & Private Messaging**: Responds to messages either in a public channel or privately, depending on user input.
- **Dynamic Responses**: Uses the `get_response` function to generate replies based on user messages.
- **Custom Prefix for Private Messages**: Messages prefixed with `?` trigger private replies.
- **Error Handling**: Comprehensive logging for better debugging.
- **Configurable**: Uses environment variables for secure configuration.

## Technologies Used
- **Python**: Main programming language.
- **Discord.py**: Library for interacting with the Discord API.
- **dotenv**: To securely manage environment variables.

## Setup Instructions

### Prerequisites
1. Python 3.8+ installed on your system.
2. A [Discord Bot Token](https://discord.com/developers/docs/intro).
3. The `get_response` function in a `responses.py` module for generating replies.

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/sofe1204/chat_bot.git
   cd discord-bot
2.Install dependencies:
  bash
  pip install -r requirements.txt
3.Create a .env file in the root directory and add your Discord bot token:
  env
  DISCORD_TOKEN=your_discord_token_here
4.Implement the get_response function in a responses.py file. Example:
python
def get_response(message: str) -> str:
    return f"You said: {message}"
    
## Running the Bot
1.Start the bot:
  python bot.py
2.If configured correctly, the bot will be active and log its status to the console.

## How to Use
1.Public Message: Type any message in a channel the bot has access to, and it will respond publicly.
2.Private Message: Prefix your message with ?, and the bot will send a reply to you privately.
3.Example:

  Public: Hello, bot!
  Response: Hello! How can I help you?
  Private: ?Help
  Response (DM): Sure! What do you need help with?
  
##File Structure
discord-bot/
├── bot.py           # Main script for running the bot
├── responses.py     # Custom response logic
├── .env             # Environment variables (not tracked by Git)
├── requirements.txt # Dependencies for the project   
   
