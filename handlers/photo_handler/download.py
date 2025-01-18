from aiogram.types import Message

async def download(message: Message):
    await message.photo[-1].download(destination_file="img/users/" + message.photo[-1].file_unique_id + ".jpg")
    return message.photo[-1].file_unique_id