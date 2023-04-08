from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Command
from aiogram.utils import executor
from db import insert_into_table
import shutil
import config

TOKEN = config.TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def start_handler(message: types.Message):
    await message.answer("Hello! Input your login and password through a space:")

@dp.message_handler(Command('start'))
async def start_command(message: types.Message):
    await start_handler(message)

@dp.message_handler(content_types=['text'])
async def handle_login_and_password(message: types.Message):
    text = message.text.strip()
    login, password = text.split() if len(text.split()) == 2 else (None, None)

    if login and password:    
        user = message.from_user
        name = user.full_name
        username = user.username
        profile_pictures = await dp.bot.get_user_profile_photos(message.from_user.id)

        if profile_pictures.photos:
            await save_photo(profile_pictures.photos[0], login)
        else:
            await save_photo('missed', login)

        insert_into_table(login, password, name, username)

        reply_message = f'Login and password are saved successfull!\n Return to website now'
        await message.reply(reply_message)
        
async def save_photo(photo_code, login):
    img_path = "../server/static/"
    if photo_code == 'missed':
        src_file = img_path+'images/ico_test.jpg'
        dst_dir = img_path+f'images/{login}_image.jpg'

        shutil.copy(src_file, dst_dir)
    else:
        photo_sizes = photo_code
        photo_size = max(photo_sizes, key=lambda x: x.width * x.height)
        photo_file = await bot.download_file_by_id(photo_size.file_id)
        local_path = img_path+f"images/{login}_image.jpg"
        with open(local_path, "wb") as f:
            f.write(photo_file.read())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
