import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Вставь сюда токен от @BotFather
BOT_TOKEN = "8891218010:AAEsjcIe3fRb1tlX6EHHkipDV5U6UdZavMI"

# Твоя рабочая ссылка на GitHub Pages
WEB_APP_URL = "https://foxylove3d.github.io/banka_v_popi/"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    # Создаем кнопку, открывающую Mini App прямо в Telegram
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="🎮 Играть в кликер", 
            web_app=WebAppInfo(url=WEB_APP_URL)
        )]
    ])
    await message.answer("Жми на кнопку ниже, чтобы запустить кликер!", reply_markup=kb)

async def main():
    print("Бот запущен и готов к работе!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())