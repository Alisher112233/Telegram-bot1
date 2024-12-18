from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import F
import logging
import asyncio

API_TOKEN = "7921515467:AAFBIpnFz2I5AxLguOQBweNfcMDUIWxcXy8"  # Замените на ваш токен

# Настройка логирования
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# --- ГЛАВНОЕ МЕНЮ --- #
def main_menu():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="\U0001F4C5 Устроиться", callback_data="hire"),
        InlineKeyboardButton(text="\U0001F4B8 График выплат", callback_data="payments")
    )
    builder.row(
        InlineKeyboardButton(text="\U0001F4DA База знаний для скаутов", url="https://yshz.tilda.ws/")
    )
    builder.row(
        InlineKeyboardButton(text="\U0001F4F0 Новости", url="https://t.me/+Kxie3mQpivhiMzFi")
    )
    builder.row(
        InlineKeyboardButton(text="\U0001F5E3️ Чат для исполнителей", url="https://t.me/+TG6btcG-SbA3Yjky")
    )
    builder.row(
        InlineKeyboardButton(text="\U0001F4BB Приложение 'Yandex Pro'", callback_data="apps")
    )
    builder.row(
        InlineKeyboardButton(text="\U0001F6E0️ Тех. проблемы", callback_data="tech_issues")
    )
    builder.row(
        InlineKeyboardButton(text="\U0001F4DD Вопросы по выплатам, корректировкам и прочему", callback_data="questions")
    )
    return builder.as_markup()

# Стандартная клавиатура с кнопкой "Меню"
def get_default_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton(text="Меню"))
    return keyboard

# Клавиатура для выбора вендора
def questions_menu():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Creon", url="https://t.me/creonhelper"),
        InlineKeyboardButton(text="Service Pro", url="https://t.me/TopDoerHelpBot")
    )
    return builder.as_markup()

# --- ОБРАБОТЧИКИ --- #
@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.answer("\U0001F44B Привет! Выберите нужный раздел:", reply_markup=main_menu())
    await message.answer("Используйте кнопку 'Меню' внизу слева для вызова меню.", reply_markup=get_default_keyboard())

@dp.message(F.text.lower() == "меню")
async def show_main_menu(message: types.Message):
    await message.answer("\U0001F44B Выберите нужный раздел:", reply_markup=main_menu())

@dp.callback_query(F.data == "hire")
async def hire_menu(callback_query: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Creon", url="https://t.me/creonhelper"),
        InlineKeyboardButton(text="Service Pro", url="https://t.me/TopDoerHelpBot")
    )
    await callback_query.message.answer("\U0001F4BC Выберите вендор:", reply_markup=builder.as_markup())
    await callback_query.message.answer("Используйте кнопку 'Меню' внизу слева для вызова меню.", reply_markup=get_default_keyboard())

@dp.callback_query(F.data == "payments")
async def payments_menu(callback_query: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Creon", callback_data="payments_kreon"),
        InlineKeyboardButton(text="Service Pro", callback_data="payments_servicepro")
    )
    await callback_query.message.answer("\U0001F4B5 Выберите вендор:", reply_markup=builder.as_markup())
    await callback_query.message.answer("Используйте кнопку 'Меню' внизу слева для вызова меню.", reply_markup=get_default_keyboard())

@dp.callback_query(F.data == "payments_kreon")
async def payments_kreon(callback_query: types.CallbackQuery):
    text = ("\U0001F4B5 *Выплаты Creon*:\n\n"
            "Каждую неделю, например:\n"
            "Слоты с 30.09 по 6 октября - выплата 10 октября\n"
            "Слоты с 7 по 13 октября - выплата 17 октября\n"
            "Слоты с 14 по 20 октября - выплата 24 октября\n"
            "Слоты с 21 по 27 октября - выплата 31 октября")
    await callback_query.message.answer(text, parse_mode="Markdown")
    await callback_query.message.answer("Используйте кнопку 'Меню' внизу слева для вызова меню.", reply_markup=get_default_keyboard())

@dp.callback_query(F.data == "payments_servicepro")
async def payments_servicepro(callback_query: types.CallbackQuery):
    text = ("\U0001F4B5 *Выплаты Service Pro*:\n\n"
            "Понедельник - среда\n"
            "Вторник - четверг\n"
            "Среда - пятница\n"
            "Четверг, пятница - понедельник\n"
            "Суббота, воскресенье - вторник")
    await callback_query.message.answer(text, parse_mode="Markdown")
    await callback_query.message.answer("Используйте кнопку 'Меню' внизу слева для вызова меню.", reply_markup=get_default_keyboard())

@dp.callback_query(F.data == "apps")
async def apps(callback_query: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Android", url="https://play.google.com/store/apps/details?id=ru.yandex.taximeter&hl=ru"),
        InlineKeyboardButton(text="iOS", url="https://apps.apple.com/ru/app/яндекс-про-водители-и-курьеры/id1496904594")
    )
    await callback_query.message.answer("\U0001F4F1 Выберите ос:", reply_markup=builder.as_markup())
    await callback_query.message.answer("Используйте кнопку 'Меню' внизу слева для вызова меню.", reply_markup=get_default_keyboard())

@dp.callback_query(F.data == "tech_issues")
async def tech_issues(callback_query: types.CallbackQuery):
    text = ("\U0001F527 *Технические проблемы*:\n\n"
            "🔍 Что делать если не удается начать слот\n\n"
            "Почистить кэш, проверить гео, удалить и заново скачать приложение, если не помогает - пишите супервайзеру👇\n\n")
    await callback_query.message.answer(text, parse_mode="Markdown")
    await callback_query.message.answer("Используйте кнопку 'Меню' внизу слева для вызова меню.", reply_markup=get_default_keyboard())

@dp.callback_query(F.data == "questions")
async def questions_menu(callback_query: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Creon", url="https://t.me/creonhelper"),
        InlineKeyboardButton(text="Service Pro", url="https://t.me/TopDoerHelpBot")
    )
    await callback_query.message.answer("\U0001F4BC Выберите вендор:", reply_markup=builder.as_markup())
    await callback_query.message.answer("Используйте кнопку 'Меню' внизу слева для вызова меню.", reply_markup=get_default_keyboard())

# --- ЗАПУСК --- #
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


