import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, FSInputFile

# Твой токен от @BotFather
BOT_TOKEN = "8891218010:AAEGuU9-6zT6fAWSKvJBHsWPzVDEQOSA2IE"

# Ссылка на твой GitHub Pages
WEB_APP_URL = "https://foxylove3d.github.io/banka_v_popi/"

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
    
    # Загружаем приветственную картинку
    photo = FSInputFile("privetstvie.jpg")
    
    # Отправляем фото и кнопку
    await message.answer_photo(
        photo=photo,
        reply_markup=kb
    )

async def main():
    print("Бот запущен и готов к работе!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
