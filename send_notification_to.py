import telepot
import credentials

# Here I've used a Telegram bot but obviously you can use whatever you like...
# Telepot docs are here: https://telepot.readthedocs.io/en/latest/#


bot = telepot.Bot(bot_key)
bot.getMe()

def my_bot(message):
    bot.sendMessage(bot_channel, message)
