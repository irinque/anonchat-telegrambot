from aiogram import Bot
from aiogram.types import Message
from settings.messages import message_registration, message_ban
from database.db import db

async def handler_private_chat(message: Message, bot: Bot):
    if db.user_exists(message.from_user.id):
        if db.user_check_ban(message.from_user.id):
            await bot.send_message(message.from_user.id, message_ban, parse_mode="Markdown")
        else:
            if db.check_session(message.from_user.id):
                interlocutor = db.get_user_from_session(message.from_user.id)
                db.add_user_message(message.from_user.id, message.text)
                if message.reply_to_message:
                    await bot.send_message(interlocutor, message.text, parse_mode="Markdown", reply_to_message_id=message.reply_to_message.message_id-1)
                else:
                    await bot.send_message(interlocutor, message.text, parse_mode="Markdown")
    else:
        await bot.send_message(message.from_user.id, message_registration, parse_mode="Markdown")