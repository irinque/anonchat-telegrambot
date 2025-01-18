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
from handlers.message_handler.stop import handler_stop
from handlers.message_handler.profile import handler_profile
from handlers.message_handler.private_chat import handler_private_chat
from handlers.callback_handler.rules_accept import callback_rules_accept
from handlers.callback_handler.complaint_send import callback_complaint_send
from handlers.callback_handler.ban_user import ban_user
from handlers.callback_handler.justify_user import justify_user
from handlers.other_handler.check_subscription import check_subscription, warning
from handlers.photo_handler.download import download
from handlers.photo_handler.send_photo import send_photo
from config import TOKEN, CHAT_ID

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
    if check_subscription(await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)):
        if message.text == "🔎 Поиск":
            await handler_search(message=message, bot=bot)
        elif message.text == "⛔ Стоп":
            await handler_stop(message=message, bot=bot)
        elif message.text == "👀 Профиль":
            await handler_profile(message=message, bot=bot)
        elif message.text != "🔎 Поиск" and message.text != "⛔ Стоп" and message.text != "👀 Профиль":
            await handler_private_chat(message=message, bot=bot)
    else:
        await warning(message=message, bot=bot)

@dp.message_handler(content_types=['photo'])
async def menu(message: Message, state: FSMContext):
    photo_id = await download(message=message)
    await send_photo(message=message, bot=bot, photo_id=photo_id)

@dp.callback_query_handler()
async def query_handler(call: CallbackQuery, state: FSMContext):
    if call.data == "markup_rules_accept":
        await callback_rules_accept(call=call, bot=bot)
    if call.data == "markup_сomplaint_send":
        await callback_complaint_send(call=call, bot=bot)
    if call.data == "markup_admin_ban":
        await ban_user(call=call, bot=bot)
    if call.data == "markup_admin_justify":
        await justify_user(call=call, bot=bot)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)