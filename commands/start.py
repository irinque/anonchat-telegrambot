from aiogram import Bot
from aiogram.types import Message
from settings.messages import message_ban, message_start_exists, message_start_firstvisit
from settings.markups import markup_rules
from database.db import db

async def command_start(message: Message, bot: Bot):
    if db.user_exists(message.from_user.id):
        if db.user_check_ban(message.from_user.id):
            await bot.send_message(message.from_user.id, message_ban, parse_mode="Markdown")
        else:
            await bot.send_message(message.from_user.id, message_start_exists, parse_mode="Markdown")
    else:
        await bot.send_message(message.from_user.id, message_start_firstvisit, parse_mode="Markdown", disable_web_page_preview=True, reply_markup=markup_rules)