import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = 1234567890:AAHkjKjfsdfjhWEOijwoewr23rfsdfJfI


logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer("Привет! Я бот по приему заявок от водителей 🚖")

@dp.message_handler()
async def echo(message: Message):
    await message.answer("Спасибо, скоро с вами свяжется менеджер!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
