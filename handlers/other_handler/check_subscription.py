from aiogram import Bot
from aiogram.types import Message
from settings.messages import message_channel
from settings.markups import markup_channel

def check_subscription(member):
    if member['status'] != 'left':
        return True
    else:
        return False
    
async def warning(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, message_channel, parse_mode="Markdown", disable_web_page_preview=True, reply_markup=markup_channel)