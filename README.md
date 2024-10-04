# Discord_botCIS3296


Before running the bot, make sure you have the following:

Python 3.x installed on your system.
A Discord account and server.
A Discord bot token which can be created in Discord Developer Portal


Step 1. Clone the repo and cd to it.

Step 2. Install the following libraries: 
pip3 install discord.py
pip3 install python-dotenv

Step 3. in the cloned repo create a .env file with your discord bot token in it 

DISCORD_BOT_TOKEN=your-discord-bot-token-here

Step 4. Run the bot

python3 bot.py

Step 5. Go to Discord Developer Portal, in OAuth2 URL Generator, check off the boxes: bot, messages.read

Step 6. copy the URL of the OAuth2 and paste into your browser then select your server to add the bot. 

Step 7. Type !ping and the bot should reply. 



System Requirements

Supported OS: macOS, Linux, or Windows
Tested On:
macOS Ventura 13.x
Python version: 3.12.x
Compiler: Python Interpreter (No additional compiler required, Python interpreter compiles and runs the script automatically)


Python Version: python3 --version
