import asyncio
import logging
import sys
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from os import getenv
from aiogram.enums import ParseMode
from aiogram.filters import Command
from handlers.dosage import router as dosage_router
from handlers.introduction import router as intro_router
from handlers.start import router as start_router
from handlers.help import router as help_router
from handlers.contraindications import router as contra_router
from handlers.dosage_adjustment import router as dosAdj_router
from handlers.paedi_dose import router as ped_router
from handlers.adr import router as adr_router
from handlers.monitoring_parameters import router as monitor_router
from handlers.pregnancy_lactation import router as pregnancy_router
from handlers.mode_of_action import router as moa_router
from handlers.general_considerations import router as consider_router



load_dotenv()
TOKEN = getenv("BOT_TOKEN")
if not TOKEN:
    exit("No token found in env file.")

dp = Dispatcher()


dp.include_router(start_router)
dp.include_router(help_router)

dp.include_router(dosage_router)
dp.include_router(ped_router)
dp.include_router(interac_router)
dp.include_router(contra_router)
dp.include_router(dosAdj_router)
dp.include_router(adr_router)
dp.include_router(monitor_router)
dp.include_router(pregnancy_router)
dp.include_router(moa_router)
dp.include_router(consider_router)
dp.include_router(intro_router)



async def main():
    print("Bot is starting...")
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    