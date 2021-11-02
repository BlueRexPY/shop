from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN
from data import VOICES,IMG
import sqlite3

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


#commands
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Добро пожаловать в магазин-темплейт. Для просмотра каталога напишите /shop ")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Для просмотра каталога напишите /shop")

@dp.message_handler(commands=['shop'])
async def process_help_command(message: types.Message):
    await message.reply("Нажмите на одну из кнопок")

#SECRET
@dp.message_handler(commands=['tof'])
async def process_voice_command(message: types.Message):
    for i in range(len(VOICES[0])):
        await bot.send_voice(message.from_user.id, VOICES[1][i], caption=VOICES[0][i])




#text
@dp.message_handler()
async def echo_message(msg: "Hi"):
    print(f"{msg.from_user.username}: {msg.text}")
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
