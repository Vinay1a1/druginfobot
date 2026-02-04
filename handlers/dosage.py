from aiogram import Router
import html
from aiogram.filters import Command
from database import get_drug_data
router = Router()

@router.message(Command("adult_dose"))
async def adult_dosage_handler(message, command):
    if not command.args:
        return await message.answer("Usage: /dose paracetamol.")
    drug_name = command.args.strip()
    data = await get_drug_data(drug_name ,"adult_dosage")
    if not data:
        return await message.answer("Drug not found")
    dosage_text = data[0]
    dosage_text_edited = html.escape(dosage_text).strip()
    await message.answer(dosage_text_edited, parse_mode ="HTML")