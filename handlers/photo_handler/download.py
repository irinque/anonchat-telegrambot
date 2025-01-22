from aiogram.types import Message
from exif import Image

async def download(message: Message):
    await message.photo[-1].download(destination_file="img/users/" + message.photo[-1].file_unique_id + ".jpg")
    with open("img/users/" + message.photo[-1].file_unique_id + ".jpg", "rb") as image:
        image = Image()
        if image.has_exif:
            image.delete_all()      
    return message.photo[-1].file_unique_id