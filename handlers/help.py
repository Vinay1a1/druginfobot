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
        "• /interactions <code>drugname</code>- Get the drug interactions\n"
        "• /dosage_adjustments <code>drugname</code> - Get dosage adjustments for various conditions info\n\n"
        "• /ped_dose <code>drugname</code> - Get pediatric dosage info\n\n"
        "• /contraindications <code>drugname</code> - Get contraindications\n\n"

        "<b>🔹 Quick Search:</b>\n"
        "Simply type the drug name (e.g., <code>Paracetamol</code>) to get the clinical introduction."
    )
    print(f"User {message.from_user.full_name} is requesting help.")
    await message.answer(help_text, parse_mode="HTML")