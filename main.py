from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types.message import ContentType
from aiogram.types import InputFile, InputMedia, Message, CallbackQuery
from aiogram import Bot, Dispatcher, executor

from database.db import db
from settings.markups import *
from settings.messages import *
from commands.start import command_start
from commands.menu import command_menu
from handlers.message_handler.search import handler_search
from handlers.callback_handler.rules_accept import callback_rules_accept
from config import TOKEN

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def start(message: Message, state: FSMContext):
    await command_start(message=message, bot=bot)

@dp.message_handler(commands=['menu'])
async def menu(message: Message, state: FSMContext):
    await command_menu(message=message, bot=bot)

@dp.message_handler(content_types=['text'])
async def message_handler(message: Message):
    if message.text == "🔎 Поиск":
        await handler_search(message=message, bot=bot)

@dp.callback_query_handler()
async def query_handler(call: CallbackQuery, state: FSMContext):
    if call.data == "markup_rules_accept":
        await callback_rules_accept(call=call, bot=bot)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)