"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1984184464:AAErugPa5Io_0KzTXOMAyoQb5_0pHrIIpA4'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
def echo_message(msg: types.Message):
    f = open(msg.text)
    bot.send_document(msg.from_user.id, f)
    f.close()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
