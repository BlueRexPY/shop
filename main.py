from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import time
import sqlite3

from config import TOKEN,MY_ID

from data import VOICES,IMG
import keyboards as kb


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

dp.middleware.setup(LoggingMiddleware())
#Красивый вывод в терминал
from progress.bar import ShadyBar

with ShadyBar('Loading', max=10) as bar:
    for i in range(10):
        time.sleep(0.05)
        bar.next()
    print("\n")


from colorama import init
init()
from colorama import Fore, Back, Style

#commands
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer_sticker(r'CAACAgIAAxkBAAEDNc5hgaoMOaeItPkEkioLa-9Sfhh4BwACQhAAAjPFKUmQDtQRpypKgiEE')
    await message.reply("Добро пожаловать в магазин-темплейт. Для просмотра каталога напишите /shop ", reply_markup=kb.greet_kb)

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Для просмотра каталога напишите /shop")

@dp.message_handler(commands=['shop'])
async def process_shop_command(message: types.Message):
    await message.reply("Нажмите на одну из кнопок")

#SECRET
@dp.message_handler(commands=['tof'])
async def process_voice_command(message: types.Message):
    for i in range(len(VOICES[0])):
        await bot.send_voice(message.from_user.id, VOICES[1][i], caption=VOICES[0][i])

@dp.message_handler(commands=['ip'])
async def process_ip_command(message: types.Message):
    await message.reply("Пробив по ip", reply_markup=kb.markup_request)

#text
@dp.message_handler()
async def echo_message(msg: types.Message):
    print(f"{Fore.GREEN}{msg.from_user.username}:{Fore.WHITE} {msg.text}")
    await bot.send_message(MY_ID, f"{msg.from_user.username} : {msg.text}",disable_notification=True)

#ответ на мусор





if __name__ == '__main__':
    executor.start_polling(dp)
