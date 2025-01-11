from aiogram.types import CallbackQuery
from aiogram import Bot
from database.db import db
from settings.messages import message_rules_accept
from settings.markups import markup_menu

async def callback_rules_accept(call: CallbackQuery, bot: Bot):
    db.insert_user(user_name=call.from_user.full_name, user_id=call.from_user.id)
    await bot.send_message(call.from_user.id, message_rules_accept, parse_mode="Markdown", reply_markup=markup_menu)