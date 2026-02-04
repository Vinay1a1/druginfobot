from aiogram import Router
import html
from aiogram.filters import Command
from database import get_drug_data
from .split import split

router = Router()

@router.message(Command("contraindications"))
async def adult_dosage_handler(message, command):
    if not command.args:
        return await message.answer("Usage: /contraindications paracetamol.")
    drug_name = command.args.strip()
    data = await get_drug_data(drug_name ,"contraindications")
    print(f"User {message.from_user.full_name} is requesting contraindications for {drug_name}")

    if not data:
        return await message.answer("Drug not found")
    dosage_text = data[0]
    dosage_text_edited = html.escape(dosage_text).strip()


    parts = await split(dosage_text_edited)


    for part in parts:
        await message.answer(part, parse_mode="HTML")