from aiogram import Bot
from aiogram.types import Message
from settings.messages import message_registration, message_profile_normal, message_profile_banned, message_profile_admin
from database.db import db

async def handler_profile(message: Message, bot: Bot):
    if db.user_exists(message.from_user.id):
        user_chats = db.get_user_chats(message.from_user.id)
        user_regdate = db.get_user_regdate(message.from_user.id)
        if db.user_check_ban(message.from_user.id):
            await bot.send_message(message.from_user.id, message_profile_banned % (message.from_user.id, user_chats, user_regdate), parse_mode="Markdown")
        else:
            await bot.send_message(message.from_user.id, message_profile_normal % (message.from_user.id, user_chats, user_regdate), parse_mode="Markdown")
    else:
        await bot.send_message(message.from_user.id, message_registration, parse_mode="Markdown")