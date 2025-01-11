from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types.message import ContentType
from aiogram.types import InputFile, InputMedia, Message
from aiogram import Bot, Dispatcher, executor

from database.db import db
from settings.markups import *
from settings.messages import *
from commands.start import command_start
from config import TOKEN

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def start(message: Message, state: FSMContext):
    await command_start(message=message, bot=bot)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)