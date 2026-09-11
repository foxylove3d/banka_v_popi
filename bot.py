import os
import asyncio
from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

BOT_TOKEN = "8654383124:AAHyu6EgqsMBtg--yteILcD2r2HCQTLrVcY"
WEB_APP_URL = "https://foxylove3d.github.io/anya/?v=2"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="🎁 Открыть поздравление", 
            web_app=WebAppInfo(url=WEB_APP_URL)
        )]
    ])
    await message.answer("Жми на кнопку ниже, чтобы запустить праздничный кликер!", reply_markup=kb)

# Веб-сервер для порта Render
async def handle(request):
    return web.Response(text="Anya Bot is running!")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

async def main():
    await start_web_server()
    print("Веб-сервер запущен, бот Ани готов к работе!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
