from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types.message import ContentType
from aiogram.types import InputFile, InputMedia
from aiogram import Bot, Dispatcher

from database.db import database
from settings.markups import *
from settings.messages import *
from config import TOKEN

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)