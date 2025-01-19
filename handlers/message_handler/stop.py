import os
from aiogram import Bot
from aiogram.types import Message
from settings.messages import message_registration, message_stop_session_ended, message_stop_queue_removed, message_error,message_stop_session_ended_byinterlocutor
from database.db import db

async def handler_stop(message: Message, bot: Bot):
    if db.user_exists(message.from_user.id):
        if db.check_queue_duplicated(message.from_user.id):
            db.remove_queue(message.from_user.id)
            await bot.send_message(message.from_user.id, message_stop_queue_removed, parse_mode="Markdown")
        elif db.check_session(message.from_user.id):
            interlocutor = db.get_user_from_session(message.from_user.id)
            images = db.get_user_images(user_id=message.from_user.id)
            for i in images:
                os.remove(f"img/users/{i}.jpg")
            images = db.get_user_images(user_id=interlocutor)
            for i in images:
                os.remove(f"img/users/{i}.jpg")
            db.remove_session(message.from_user.id)
            await bot.send_message(message.from_user.id, message_stop_session_ended, parse_mode="Markdown")
            await bot.send_message(interlocutor, message_stop_session_ended_byinterlocutor, parse_mode="Markdown")
        else:
            await bot.send_message(message.from_user.id, message_error, parse_mode="Markdown")
    else:
        await bot.send_message(message.from_user.id, message_registration, parse_mode="Markdown")