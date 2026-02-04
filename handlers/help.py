from aiogram import Router
from aiogram.filters import Command

router = Router()

@router.message(Command("help"))
async def help(message):
    help_text = (
        "<b>Drug info Command Menu</b>\n\n"
        "<b>🔹 Commands:</b>\n"
        "• /start - Start the bot\n"
        "• /help - Display this help menu\n"
        "• /adult_dose <code>drugname</code> - Get adult dosage info\n\n"
        "<b>🔹 Quick Search:</b>\n"
        "Simply type the drug name (e.g., <code>Paracetamol</code>) to get the clinical introduction."
    )
    
    await message.answer(help_text, parse_mode="HTML")