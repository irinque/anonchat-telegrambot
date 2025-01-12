from aiogram.types import CallbackQuery
from aiogram import Bot
from database.db import db
from settings.messages import message_search_session_complaint, message_registration, message_error, message_stop_session_ended, message_stop_session_ended_byinterlocutor

async def callback_complaint_send(call: CallbackQuery, bot: Bot):
    if db.user_exists(call.from_user.id):
        if db.check_session(call.from_user.id):
            target = db.get_user_from_session(call.from_user.id)
            db.add_complaint(sender_id=call.from_user.id, target_id=target, reason="Не Указана")
            await bot.send_message(call.from_user.id, message_search_session_complaint, parse_mode="Markdown")
            db.remove_session(call.from_user.id)
            await bot.send_message(call.from_user.id, message_stop_session_ended, parse_mode="Markdown")
            await bot.send_message(target, message_stop_session_ended_byinterlocutor, parse_mode="Markdown")
        else:
            await bot.send_message(call.from_user.id, message_error, parse_mode="Markdown")
    else:
        await bot.send_message(call.from_user.id, message_registration, parse_mode="Markdown")