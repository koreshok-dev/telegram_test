import asyncio
import logging

from aiogram import Bot,Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import config
from handlers import router

async def main():
    bot =Bot(token=config.BOT_TOKEN,parse_mode=ParseMode.HTML)
    dp=Dispatcher(storage=MemoryStorage())


if __name__=='main':
