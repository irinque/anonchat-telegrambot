from aiogram import Bot
from aiogram.types import Message
from settings.messages import message_registration, message_ban, message_search_queue, message_search_session_started, message_search_queue_duplicated
from database.db import db

async def handler_search(message: Message, bot: Bot):
    if db.user_exists(message.from_user.id):
        if db.user_check_ban(message.from_user.id):
            await bot.send_message(message.from_user.id, message_ban, parse_mode="Markdown")
        else:
            if db.check_queue_duplicated(message.from_user.id):
                await bot.send_message(message.from_user.id, message_search_queue_duplicated, parse_mode="Markdown")
            else:
                if db.check_queue():
                    random_user = db.random_user_from_queue()
                    db.remove_queue(random_user)
                    db.add_session(message.from_user.id, random_user)
                    await bot.send_message(message.from_user.id, message_search_session_started, parse_mode="Markdown")
                    await bot.send_message(random_user, message_search_session_started, parse_mode="Markdown")
                else:
                    db.add_queue(message.from_user.id)
                    await bot.send_message(message.from_user.id, message_search_queue, parse_mode="Markdown")


    else:
        await bot.send_message(message.from_user.id, message_registration, parse_mode="Markdown")