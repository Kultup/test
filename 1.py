import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "6386051313:AAGHLs1e_lJAtXOYF85F_d5I8KN73VAuFhc"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Привет! Я бот, напиши мне что-нибудь.")

@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer("Я умею отвечать на сообщения и выполнять команды: \n/start - начать \n/help - помощь")

@dp.message()
async def echo(message: types.Message):
    if message.text.lower() in ["привет", "здравствуй"]:
        await message.answer("Привет! Как дела?")
    elif message.text.lower() in ["пока", "до свидания"]:
        await message.answer("Пока! Хорошего дня!")
    else:
        await message.answer(f"Ты сказал: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())