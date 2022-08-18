from email.message import Message
import config
from aiogram import Bot, types, executor, Dispatcher

bot = Bot(token=config.token)
dp = Dispatcher(bot)

words = []
with open("mat.txt") as input:
    for word in input:
        words.append("".join(word.split()))

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет!")

@dp.message_handler(commands=["help"])
async def start(message: types.Message):
    await message.answer("Бог поможет")

#Для администрирования фоток
#@dp.message_handler(content_types=["photo"])
#async def handle_file(message):
    #await message.answer('По правилам нельзя присылать фотки')
    #await message.delete()

@dp.message_handler()
async def filter_message(message: types.Message):
    if message.text.lower() in words:
        await message.delete()
        await message.answer("Не ругайтесь!")

@dp.message_handler(content_types=["new_chat_members"])
async def new_chat(message: types.Message):
    await message.answer("Добро пожаловать!")

@dp.message_handler(content_types=["left_chat_member"])
async def left_chat(message: types.Message):
    await message.delete()


if __name__ == "__main__":
    executor.start_polling(dp)
