from aiogram import Bot, Dispatcher
import asyncio
import os
from dotenv import load_dotenv
from pathlib import Path

from .handlers import router
from .db import subscribers

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR.parent / ".env")

bot = Bot(token=os.environ.get("BOT_TOKEN"))
dp = Dispatcher()

dp.include_router(router)

subscribers()

if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))


    async def main():
        await dp.start_polling(bot)