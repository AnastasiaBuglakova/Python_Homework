from aiogram import Bot, Dispatcher
import os

bot = Bot(os.getenv('Bot_TOKEN'))
dp = Dispatcher(bot)