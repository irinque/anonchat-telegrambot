from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

markup_rules = InlineKeyboardMarkup(row_width=1)
markup_rules_accept = InlineKeyboardButton("Ознакомлен(а)", callback_data="markup_rules_accept")
markup_rules.row(markup_rules_accept)

markup_menu = ReplyKeyboardMarkup(resize_keyboard=True)
markup_menu_dialog = KeyboardButton(text="🔎 Поиск")
markup_menu_stop = KeyboardButton(text="⛔ Стоп")
markup_menu_profile = KeyboardButton(text="👀 Профиль")
markup_menu.row(markup_menu_dialog, markup_menu_stop)
markup_menu.row(markup_menu_profile)