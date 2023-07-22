from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command('start'))
async def start_handler(msg: Message):
    await msg.answer("Сейчас передам твой id на следующее сообщение")
    
@router.message()
async def get_id_by_message(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")