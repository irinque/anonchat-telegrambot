from aiogram import Bot
from aiogram.types import Message
from settings.messages import message_registration, message_ban, message_menu_success
from settings.markups import markup_menu
from database.db import db

async def command_menu(message: Message, bot: Bot):
    if db.user_exists(message.from_user.id):
        if db.user_check_ban(message.from_user.id):
            await bot.send_message(message.from_user.id, message_ban, parse_mode="Markdown")
        else:
            await bot.send_message(message.from_user.id, message_menu_success, parse_mode="Markdown", reply_markup=markup_menu)
    else:
        await bot.send_message(message.from_user.id, message_registration, parse_mode="Markdown")