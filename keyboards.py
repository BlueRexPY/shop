from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

#SHOP BUTTON
button_shop = KeyboardButton('Каталог 🗄')
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(button_shop)


markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
).add(
    KeyboardButton('Отправить свою локацию 🗺️', request_location=True)
)
