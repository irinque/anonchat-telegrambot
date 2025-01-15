from aiogram.types import CallbackQuery
from aiogram import Bot
from database.db import db
from settings.messages import message_search_session_complaint, message_registration, message_error, message_stop_session_ended, message_stop_session_ended_byinterlocutor, message_ticket
from settings.markups import markup_admin
from config import LOGS

async def callback_complaint_send(call: CallbackQuery, bot: Bot):
    if db.user_exists(call.from_user.id):
        if db.check_session(call.from_user.id):
            target_id = db.get_user_from_session(call.from_user.id)
            db.add_complaint(sender_id=call.from_user.id, target_id=target_id, reason="Не Указана")
            messages = db.get_target_messages(target_id=target_id)
            messages = "\n- ".join(messages)
            db.remove_session(call.from_user.id)
            await bot.send_message(target_id, message_stop_session_ended_byinterlocutor, parse_mode="Markdown")
            await bot.send_message(call.from_user.id, message_search_session_complaint, parse_mode="Markdown")
            await bot.send_message(call.from_user.id, message_stop_session_ended, parse_mode="Markdown")
            await bot.send_message(LOGS, message_ticket % (target_id, target_id, "Не указана", f"```[CHAT_MESSAGES]:\n- {messages}```"), parse_mode="Markdown", reply_markup=markup_admin)
        else:
            await bot.send_message(call.from_user.id, message_error, parse_mode="Markdown")
    else:
        await bot.send_message(call.from_user.id, message_registration, parse_mode="Markdown")