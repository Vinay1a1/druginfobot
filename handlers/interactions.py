from aiogram import Router
import html
from aiogram.filters import Command
from database import get_drug_data
from .split import split

router = Router()

@router.message(Command("interactions"))
async def interactions_handler(message, command):
    if not command.args:
        return await message.answer("Usage: /interactions paracetamol.")
    interactions = command.args.strip()
    data = await get_drug_data(interactions ,"interactions")
    if not data:
        return await message.answer("Drug not found")
    interactions_text = data[0]
    interactions_text_edited = html.escape(interactions_text).strip()
    parts = await split(interactions_text_edited)


    for part in parts:
        await message.answer(part, parse_mode="HTML")