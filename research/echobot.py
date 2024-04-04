from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import logging


load_dotenv()
# OPENAI_API_TOKEN = os.getenv("OPENAI_API_TOKEN")
TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")


# configuration of logging
logging.basicConfig(level=logging.INFO)


# Initializing bot 
bot = Bot(token=TELEGRAM_API_TOKEN)

# Dispatcher the bot
dp = Dispatcher(bot)


@dp.message_handler(commands=['start','help'])
async def command_start_handler(message: types.Message):
    """This handler receives messages with `/start` or  `/help `command

    Args:
        message (types.Message): _description_
    """
    await message.reply("Hi!\n I am an Echo Bot!\n Powered by TeligraBot version: 0.0.3")



@dp.message_handler()
async def echo(message: types.Message):
    """This will return echo message

    Args:
        message (types.Message): _description_
    """

    await message.reply(message.text)
    




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)