from aiogram import Router
import html
from aiogram.filters import Command
from database import get_drug_data
from .split import split

router = Router()

@router.message(Command("dosage_adjustments"))
async def adverse_effects_handler(message, command):
    if not command.args:
        return await message.answer("Usage: /dosage_adjustments paracetamol.")
    drug_name = command.args.strip()
    data = await get_drug_data(drug_name ,"dosage_adjustments")
    if not data:
        return await message.answer("Drug not found")
    dosage_adjustments_text = data[0]
    dosage_adjustments_text_edited = html.escape(dosage_adjustments_text).strip()

    parts = await split(dosage_adjustments_text_edited)


    for part in parts:
        await message.answer(part, parse_mode="HTML")