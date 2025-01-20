from aiogram.types import CallbackQuery
from aiogram import Bot
from database.db import db
from settings.messages import message_ticket

async def ban_user(call: CallbackQuery, bot: Bot):
    if db.check_admin_status(call.from_user.id):
        target_id = call.message.text.split("\n")[0][1:]
        db.update_complaint(target_id, "banned")
        db.ban_user(target_id, call.from_user.id)
        messages = call.message.text.split("\n")[5:]
        messages = "\n- ".join(messages)
        await call.message.edit_text(message_ticket % (f'N{target_id}: ❌ БАН', target_id, "Не указана", f"```[CHAT_MESSAGES]:\n- {messages}```"), parse_mode="Markdown")
