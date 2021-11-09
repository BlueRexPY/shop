from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from data import CALLBACKS_ELF
#Start
markup_start = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Каталог 🗄', callback_data='сatalog')
).add(
    InlineKeyboardButton('F.A.Q ❓', callback_data='faq')
)

#shop
markup_shop = InlineKeyboardMarkup().add(
    InlineKeyboardButton(f'❤️ ELF BAR 2500 {CALLBACKS_ELF[1][0]} грн', callback_data='elf_bar_2500')
).add(
    InlineKeyboardButton(f'🧡 ELF BAR 2000 {CALLBACKS_ELF[1][1]} грн', callback_data='elf_bar_2000')
).add(
    InlineKeyboardButton(f'💛 ELF BAR 1500 {CALLBACKS_ELF[1][2]} грн', callback_data='elf_bar_1500')
).add(
    InlineKeyboardButton(f'💚 ELF BAR 800 {CALLBACKS_ELF[1][3]} грн', callback_data='elf_bar_800')
).add(
    InlineKeyboardButton(f'💙 ELF BAR 550 {CALLBACKS_ELF[1][4]} грн', callback_data='elf_bar_550')
).add(
    InlineKeyboardButton(f'💜 ELF BAR LUX 1500 {CALLBACKS_ELF[1][5]} грн', callback_data='elf_bar_lux_1500')
).add(
    InlineKeyboardButton(f'🖤 ELF BAR LUX 800 {CALLBACKS_ELF[1][6]} грн', callback_data='elf_bar_lux_800')
).add(
    InlineKeyboardButton('Назад ⬅️', callback_data='start')
)


markup_elf_bar_lux = InlineKeyboardMarkup().add(
    InlineKeyboardButton('🫐 Черника', callback_data='city')
).add(
    InlineKeyboardButton('🍑🥭🍍 Ананас, персик и манго ', callback_data='city')
).add(
    InlineKeyboardButton('🍹 Розовый Лимонад ', callback_data='city')
).add(
    InlineKeyboardButton('🥭 Манго ', callback_data='city')
).add(
    InlineKeyboardButton('🍏🍑 Яблоко с персиком ', callback_data='city')
).add(
    InlineKeyboardButton('🍌🧊 Ледяной Банан ', callback_data='city')
).add(
    InlineKeyboardButton('🍓🍌 Клубника с Бананом ', callback_data='city')
).add(
    InlineKeyboardButton('🍈 Киви, Маракуйя, Гуава', callback_data='city')
).add(
    InlineKeyboardButton('Назад ⬅️', callback_data='сatalog')
)


markup_elf_bar = InlineKeyboardMarkup().add(
    InlineKeyboardButton('🫐 Черника ', callback_data='city')
).add(
    InlineKeyboardButton('🍒 Вишня', callback_data='city')
).add(
    InlineKeyboardButton('🍌 Банан', callback_data='city')
).add(
    InlineKeyboardButton('🍉 Арбуз', callback_data='city')
).add(
    InlineKeyboardButton('🍑 Персик', callback_data='city')
).add(
    InlineKeyboardButton('🍇 Виноград', callback_data='city')
).add(
    InlineKeyboardButton('🍎 Яблоко', callback_data='city')
).add(
    InlineKeyboardButton('🥭 Манго', callback_data='city')
).add(
    InlineKeyboardButton('🍊 Апельсин', callback_data='city')
).add(
    InlineKeyboardButton('🍈 Дыня', callback_data='city')
).add(
    InlineKeyboardButton('🍓🍇 Мультифрукт', callback_data='city')
).add(
    InlineKeyboardButton('🍍 Ананас', callback_data='city')
).add(
    InlineKeyboardButton('🍋 Лимонный пирог', callback_data='city')
).add(
    InlineKeyboardButton('🏺 Корица', callback_data='city')
).add(
    InlineKeyboardButton('🍬 Жвачка', callback_data='city')
).add(
    InlineKeyboardButton('🥬 Мята, хвоя и лесные ягоды', callback_data='city')
).add(
    InlineKeyboardButton('🍹 Кола', callback_data='city')
).add(
    InlineKeyboardButton('🍸 Розовый лимонад', callback_data='city')
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

markup_city = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Киев', callback_data='buy')
).add(
    InlineKeyboardButton('Харьков', callback_data='buy')
).add(
    InlineKeyboardButton('Одесса', callback_data='buy')
).add(
    InlineKeyboardButton('Днепр', callback_data='buy')
).add(
    InlineKeyboardButton('Запорожье', callback_data='buy')
).add(
    InlineKeyboardButton('Львов', callback_data='buy')
).add(
    InlineKeyboardButton('Кривой Рог', callback_data='buy')
).add(
    InlineKeyboardButton('Николаев', callback_data='buy')
).add(
    InlineKeyboardButton('Мариуполь', callback_data='buy')
).add(
    InlineKeyboardButton('Назад ⬅️', callback_data='сatalog')
)
