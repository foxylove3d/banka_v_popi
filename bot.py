import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, URLInputFile
from aiohttp import web
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

# Токен твоего бота
BOT_TOKEN = "8891218010:AAEGuU9-6zT6fAWSKvJBHsWPzVDEQOSA2IE"

# Ссылка на саму игру (если index.html лежит в новом репозитории, обнови ее тоже, если нужно)
WEB_APP_URL = "https://foxylove3d.github.io/banka_v_popi/"

# Ссылка на твой веб-сервис на Render
RENDER_EXTERNAL_URL = os.getenv("RENDER_EXTERNAL_URL", "https://banka-v-popi.onrender.com")

WEBHOOK_PATH = f"/bot/{BOT_TOKEN}"
WEBHOOK_URL = f"{RENDER_EXTERNAL_URL}{WEBHOOK_PATH}"

# Порт, который выделяет Render
PORT = int(os.getenv("PORT", 8080))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    # Кнопка для запуска Mini App
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="присесть", 
            web_app=WebAppInfo(url=WEB_APP_URL)
        )]
    ])
    
    # Загружаем приветственную картинку по прямой ссылке из публичного репозитория
    photo_url = "https://raw.githubusercontent.com/foxylove3d/banka_v_popi/main/privetstvie.jpg"
    photo = URLInputFile(photo_url)
    
    # Отправляем фото и кнопку
    await message.answer_photo(
        photo=photo,
        reply_markup=kb
    )

async def on_startup(bot: Bot):
    # Автоматически регистрируем вебхук в Телеграме при старте сервера
    await bot.set_webhook(WEBHOOK_URL)
    print(f"Вебхук успешно установлен на: {WEBHOOK_URL}")

def main():
    logging.basicConfig(level=logging.INFO)
    
    # Создаем aiohttp приложение
    app = web.Application()
    
    # Регистрируем обработчик вебхуков aiogram
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    )
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)
    
    setup_application(app, dp, bot=bot)
    dp.startup.register(on_startup)
    
    print(f"Запуск веб-сервера на порту {PORT}...")
    # Запускаем веб-сервер, который ждет входящие запросы от Render и Telegram
    web.run_app(app, host="0.0.0.0", port=PORT)

if __name__ == "__main__":
    main()
