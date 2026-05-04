from aiogram import Router
import html
from aiogram.filters import Command
from database import get_drug_data
from .split import split

router = Router()

@router.message(Command("monitor"))
async def monitoring_parameters_handler(message, command):
    if not command.args:
        return await message.answer("Usage: /monitor paracetamol.")
    drug_name = command.args.strip()
    data = await get_drug_data(drug_name ,"monitoring_parameters")
    print(f"User {message.from_user.full_name} is requesting monitoring_parameters for {drug_name}")

    if not data:
        return await message.answer("Drug not found")
    dosage_text = data[0]
    dosage_text_edited = html.escape(dosage_text).strip()


    parts = await split(dosage_text_edited)


    for part in parts:
        await message.answer(part, parse_mode="HTML")