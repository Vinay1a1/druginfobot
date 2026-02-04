import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from handlers.dosage import router as dosage_router
from handlers.introduction import router as intro_router
from handlers.start import router as start_router
from handlers.help import router as help_router

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "Your bot token here"

dp = Dispatcher()


dp.include_router(start_router)
dp.include_router(help_router)

dp.include_router(dosage_router)

dp.include_router(intro_router)



async def main():
    print("Bot is starting...")
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())