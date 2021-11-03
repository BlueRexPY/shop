from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import time
import sqlite3
import random

from config import TOKEN,MY_ID,CARD

from data import VOICES,IMG,PRICE_ELF_BAR_2500,PRICE_ELF_BAR_2000,PRICE_ELF_BAR_1500,PRICE_ELF_BAR_800,PRICE_ELF_BAR_550,PRICE_ELF_BAR_LUX_1500,PRICE_ELF_BAR_LUX_800,FAQ,START
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


#elf_bar
@dp.callback_query_handler(lambda c: c.data == 'elf_bar_lux_1500')
async def process_callback_elf_bar_lux(callback_query: types.CallbackQuery):
    global current_price
    current_price = PRICE_ELF_BAR_LUX_1500
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text="🌺 Выберите Вкус",reply_markup=kb.markup_elf_bar_lux)

@dp.callback_query_handler(lambda c: c.data == 'elf_bar_lux_800')
async def process_callback_elf_bar_lux(callback_query: types.CallbackQuery):
    global current_price
    current_price = PRICE_ELF_BAR_LUX_800
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text="🌺 Выберите Вкус",reply_markup=kb.markup_elf_bar_lux)

@dp.callback_query_handler(lambda c: c.data == 'elf_bar_2500')
async def process_callback_elf_bar(callback_query: types.CallbackQuery):
    global current_price
    current_price = PRICE_ELF_BAR_2500
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text="🌺 Выберите Вкус",reply_markup=kb.markup_elf_bar)

@dp.callback_query_handler(lambda c: c.data == 'elf_bar_2000')
async def process_callback_elf_bar(callback_query: types.CallbackQuery):
    global current_price
    current_price = PRICE_ELF_BAR_2000
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text="🌺 Выберите Вкус",reply_markup=kb.markup_elf_bar)


@dp.callback_query_handler(lambda c: c.data == 'elf_bar_1500')
async def process_callback_elf_bar(callback_query: types.CallbackQuery):
    global current_price
    current_price = PRICE_ELF_BAR_1500
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text="🌺 Выберите Вкус",reply_markup=kb.markup_elf_bar)


@dp.callback_query_handler(lambda c: c.data == 'elf_bar_800')
async def process_callback_elf_bar_lux(callback_query: types.CallbackQuery):
    global current_price
    current_price = PRICE_ELF_BAR_800
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text="🌺 Выберите Вкус",reply_markup=kb.markup_elf_bar)


@dp.callback_query_handler(lambda c: c.data == 'elf_bar_550')
async def process_callback_elf_bar_lux(callback_query: types.CallbackQuery):
    global current_price
    current_price = PRICE_ELF_BAR_550
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.edit_text(text="🌺 Выберите Вкус",reply_markup=kb.markup_elf_bar)


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

if __name__ == '__main__':
    executor.start_polling(dp)
