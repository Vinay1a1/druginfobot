from aiogram import Router
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def start(message):
    start_text = (
        "<b>Drug Information Bot</b>\n"
        "━━━━━━━━━━━━━━━━━━\n"
        "Search the database by typing any drug name below.\n\n"
        "<b>To get a list of available commands, use /help.</b>\n"
        "<b>Example:</b> Type <code>Ibuprofen</code> for an overview.\n\n"
        "<i>Note: This is a reference tool. Consult a healthcare professional "
        "before making medical decisions.</i>"
    )
    
    await message.answer(start_text, parse_mode="HTML")