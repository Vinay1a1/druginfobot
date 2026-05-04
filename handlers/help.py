from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("help"))
async def help(message: Message):
    help_text = (
        "<b>💊 Drug Information Command Menu</b>\n\n"
        
        "<b>🔹 Basic Commands:</b>\n"
        "• /start - Start the bot\n"
        "• /help - Display this help menu\n\n"

        "<b>🔹 Dosage & Safety:</b>\n"
        "• /adult_dose <code>drugname</code> - Adult dosage info\n"
        "• /ped_dose <code>drugname</code> - Pediatric dosage info\n"
        "• /dosage_adjustments <code>drugname</code> - Adjustments (Renal/Hepatic)\n"
        "• /contraindications <code>drugname</code> - When not to use\n\n"

        "<b>🔹 Clinical Details:</b>\n"
        "• /moa <code>drugname</code> - Mechanism of Action (How it works)\n"
        "• /adr <code>drugname</code> - Adverse Drug Reactions (Side effects)\n"
        "• /interactions <code>drugname</code> - Drug-Drug interactions\n\n"

        "<b>🔹 Special Considerations:</b>\n"
        "• /considerations <code>drugname</code> - General clinical considerations\n"
        "• /monitor <code>drugname</code> - Parameters to monitor\n"
        "• /pregnancy <code>drugname</code> - Pregnancy & Lactation safety\n\n"

        "<b>🔍 Quick Search:</b>\n"
        "Simply type the drug name (e.g., <code>Paracetamol</code>) to get the clinical introduction."
    )
    
    print(f"User {message.from_user.full_name} is requesting help.")
    await message.answer(help_text, parse_mode="HTML")