from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from data import PRICE_ELF_BAR_2500,PRICE_ELF_BAR_2000,PRICE_ELF_BAR_1500,PRICE_ELF_BAR_800,PRICE_ELF_BAR_550,PRICE_ELF_BAR_LUX_1500,PRICE_ELF_BAR_LUX_800
#Start
markup_start = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Каталог 🗄', callback_data='сatalog')
).add(
    InlineKeyboardButton('F.A.Q ❓', callback_data='faq')
)

#shop
markup_shop = InlineKeyboardMarkup().add(
    InlineKeyboardButton(f'❤️ ELF BAR 2500 {PRICE_ELF_BAR_2500} грн', callback_data='elf_bar_2500')
).add(
    InlineKeyboardButton(f'🧡 ELF BAR 2000 {PRICE_ELF_BAR_2000} грн', callback_data='elf_bar_2000')
).add(
    InlineKeyboardButton(f'💛 ELF BAR 1500 {PRICE_ELF_BAR_1500} грн', callback_data='elf_bar_1500')
).add(
    InlineKeyboardButton(f'💚 ELF BAR 800 {PRICE_ELF_BAR_800} грн', callback_data='elf_bar_800')
).add(
    InlineKeyboardButton(f'💙 ELF BAR 550 {PRICE_ELF_BAR_550} грн', callback_data='elf_bar_550')
).add(
    InlineKeyboardButton(f'💜 ELF BAR LUX 1500 {PRICE_ELF_BAR_LUX_1500} грн', callback_data='elf_bar_lux_1500')
).add(
    InlineKeyboardButton(f'🖤 ELF BAR LUX 800 {PRICE_ELF_BAR_LUX_800} грн', callback_data='elf_bar_lux_800')
).add(
    InlineKeyboardButton('Назад ⬅️', callback_data='start')
)


markup_elf_bar_lux = InlineKeyboardMarkup().add(
    InlineKeyboardButton('🫐 Черника', callback_data='buy')
).add(
    InlineKeyboardButton('🍑🥭🍍 Ананас, персик и манго ', callback_data='buy')
).add(
    InlineKeyboardButton('🍹 Розовый Лимонад ', callback_data='buy')
).add(
    InlineKeyboardButton('🥭 Манго ', callback_data='buy')
).add(
    InlineKeyboardButton('🍏🍑 Яблоко с персиком ', callback_data='buy')
).add(
    InlineKeyboardButton('🍌🧊 Ледяной Банан ', callback_data='buy')
).add(
    InlineKeyboardButton('🍓🍌 Клубника с Бананом ', callback_data='buy')
).add(
    InlineKeyboardButton('🍈 Киви, Маракуйя, Гуава', callback_data='buy')
).add(
    InlineKeyboardButton('Назад ⬅️', callback_data='сatalog')
)


markup_elf_bar = InlineKeyboardMarkup().add(
    InlineKeyboardButton('🫐 Черника ', callback_data='buy')
).add(
    InlineKeyboardButton('🍒 Вишня', callback_data='buy')
).add(
    InlineKeyboardButton('🍌 Банан', callback_data='buy')
).add(
    InlineKeyboardButton('🍉 Арбуз', callback_data='buy')
).add(
    InlineKeyboardButton('🍑 Персик', callback_data='buy')
).add(
    InlineKeyboardButton('🍇 Виноград', callback_data='buy')
).add(
    InlineKeyboardButton('🍎 Яблоко', callback_data='buy')
).add(
    InlineKeyboardButton('🥭 Манго', callback_data='buy')
).add(
    InlineKeyboardButton('🍊 Апельсин', callback_data='buy')
).add(
    InlineKeyboardButton('🍈 Дыня', callback_data='buy')
).add(
    InlineKeyboardButton('🍓🍇 Мультифрукт', callback_data='buy')
).add(
    InlineKeyboardButton('🍍 Ананас', callback_data='buy')
).add(
    InlineKeyboardButton('🍋 Лимонный пирог', callback_data='buy')
).add(
    InlineKeyboardButton('🏺 Корица', callback_data='buy')
).add(
    InlineKeyboardButton('🍬 Жвачка', callback_data='buy')
).add(
    InlineKeyboardButton('🥬 Мята, хвоя и лесные ягоды', callback_data='buy')
).add(
    InlineKeyboardButton('🍹 Кола', callback_data='buy')
).add(
    InlineKeyboardButton('🍸 Розовый лимонад', callback_data='buy')
).add(
    InlineKeyboardButton('Назад ⬅️', callback_data='сatalog')
)

markup_faq= InlineKeyboardMarkup().add(
    InlineKeyboardButton('Назад ⬅️', callback_data='start')
)

markup_buy= InlineKeyboardMarkup().add(
    InlineKeyboardButton('Я оплатил 💳', callback_data='scam')
)
markup_scam= InlineKeyboardMarkup().add(
    InlineKeyboardButton('На главную 🔥', callback_data='start')
)
