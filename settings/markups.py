from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

markup_rules = InlineKeyboardMarkup(row_width=1)
markup_rules_accept = InlineKeyboardButton("Ознакомлен(а)", callback_data="markup_rules_accept")
markup_rules.row(markup_rules_accept)