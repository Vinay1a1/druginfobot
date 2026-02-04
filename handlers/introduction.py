from aiogram import Router, F
import html
from aiogram.filters import Command
from database import get_drug_data
from .split import split

router = Router()

@router.message(F.text, ~F.text.startswith("/"))
async def introduction_handler(message):
    drug_name = message.text.strip()
    data = await get_drug_data(drug_name ,"introduction")
    if not data:
        return await message.answer("Drug not found")
    intro = data[0]
    intro_edited = html.escape(intro).strip()


    parts = await split(intro_edited)
    print(f"User {message.from_user.full_name} is requesting introduction for {drug_name}.")


    for part in parts:
        await message.answer(part, parse_mode="HTML")