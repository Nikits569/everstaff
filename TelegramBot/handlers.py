from aiogram import Router
from aiogram.filters import Command
from .db import *

router = Router()

@router.message(Command("start"))
async def start(message):
    add_subscriber(message.from_user.id)
    await message.answer("Повідомлення запущені")


@router.message(Command("stop"))
async def stop(message):
    await message.answer("Повідомлення зупинені")
    remove_subscriber(message.from_user.id)