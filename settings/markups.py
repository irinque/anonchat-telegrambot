from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from config import CHAT_LINK

markup_rules = InlineKeyboardMarkup(row_width=1)
markup_rules_accept = InlineKeyboardButton("Ознакомлен(а)", callback_data="markup_rules_accept")
markup_rules.row(markup_rules_accept)

markup_menu = ReplyKeyboardMarkup(resize_keyboard=True)
markup_menu_dialog = KeyboardButton(text="🔎 Поиск")
markup_menu_stop = KeyboardButton(text="⛔ Стоп")
markup_menu_profile = KeyboardButton(text="👀 Профиль")
markup_menu.row(markup_menu_dialog, markup_menu_stop)
markup_menu.row(markup_menu_profile)

markup_сomplaint = InlineKeyboardMarkup(row_width=1)
markup_сomplaint_send = InlineKeyboardButton("⚠️ Пожаловаться ⚠️", callback_data="markup_сomplaint_send")
markup_сomplaint.row(markup_сomplaint_send)

markup_complaint_type = InlineKeyboardMarkup(row_width=1)
markup_complaint_type_insults = InlineKeyboardButton("🤬 Оскорбление(я) 🤬", callback_data="markup_complaint_type_insults")
markup_complaint_type_spam = InlineKeyboardButton("📫 Спам 📫", callback_data="markup_complaint_type_spam")
markup_complaint_type_porno = InlineKeyboardButton("🔞 Порнография 🔞", callback_data="markup_complaint_type_porno")
markup_complaint_type_other = InlineKeyboardButton("💣 Другое 💣", callback_data="markup_complaint_type_other")
markup_complaint_type.row(markup_complaint_type_insults, markup_complaint_type_spam, markup_complaint_type_porno, markup_complaint_type_other)

markup_admin = InlineKeyboardMarkup(row_width=2)
markup_admin_ban = InlineKeyboardButton("❌ Бан", callback_data="markup_admin_ban")
markup_admin_justify = InlineKeyboardButton("✔️ Оправдан", callback_data="markup_admin_justify")
markup_admin.row(markup_admin_ban, markup_admin_justify)

markup_channel = InlineKeyboardMarkup(row_width=1)
markup_channel_link = InlineKeyboardButton("🔗 Подписаться 🔗", url=CHAT_LINK)
markup_channel.row(markup_channel_link)