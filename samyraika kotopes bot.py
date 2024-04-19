import asyncio
import logging
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
session = requests.session()
session.trust_env = False

get_cat = 'https://api.thecatapi.com/v1/images/search'
get_dog = 'https://random.dog/woof.json'

logging.basicConfig(level=logging.INFO)
bot = Bot(token="7049383669:AAEawEhcyEjZO62dmlAUrP5u7dbWD4Bmfvc")
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message:types.Message):
    kb = [
        [
            types.KeyboardButton(text="Котяшки"),
            types.KeyboardButton(text="Собакены")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="У тебя есть выбор!"
    )
    await message.answer("Какую картинку отправить?", reply_markup=keyboard)

@dp.message(F.text.lower() == "Котяшки")
async def with_puree(message: types.Message):
    response_cat = session.get(get_cat).json()
    print(response_cat)
    await message.answer_photo(response_cat[0]["url"])

@dp.message(F.text.lower() == "Собакены")
async def with_puree(message: types.Message):
    response_dog = session.get(get_dog).json()
    print(response_dog)
    await message.answer_photo(response_dog[0]["url"])


async def main():
    await dp.start_polling(bot)
if __name__== "__main__":
    asyncio.run(main())