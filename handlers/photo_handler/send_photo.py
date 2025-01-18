from aiogram import Bot
from aiogram.types import Message, InputFile
from settings.messages import message_registration, message_ban
from database.db import db

async def send_photo(message: Message, bot: Bot, photo_id):
    if db.user_exists(message.from_user.id):
        if db.user_check_ban(message.from_user.id):
            await bot.send_message(message.from_user.id, message_ban, parse_mode="Markdown")
        else:
            if db.check_session(message.from_user.id):
                interlocutor = db.get_user_from_session(message.from_user.id)
                await bot.send_photo(interlocutor, InputFile(f"img/users/{photo_id}.jpg"))
    else:
        await bot.send_message(message.from_user.id, message_registration, parse_mode="Markdown")