from aiogram import Router
import html
from aiogram.filters import Command
from database import get_drug_data
from .split import split

router = Router()

@router.message(Command("ped_dose"))
async def pedia_dosage_handler(message, command):
    if not command.args:
        return await message.answer("Usage: /ped_dose paracetamol.")
    drug_name = command.args.strip()
    data = await get_drug_data(drug_name ,"pediatric_dosage")
    if not data:
        return await message.answer("Drug not found")
    dosage_text = data[0]
    dosage_text_edited = html.escape(dosage_text).strip()
    user = message.from_user
    print(f"User {user.full_name} is requesting a split for {command.args}")

    parts = await split(dosage_text_edited)
    # await message.answer(dosage_text_edited, parse_mode ="HTML")

    for part in parts:
        await message.answer(part, parse_mode="HTML")
    