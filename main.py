token = '6374777423:AAF2b0Vli9Xdf3Y_oIgjITcCkFFi7PlewkM'

from aiogram import Bot,Dispatcher,types
from aiogram.utils import executor
from translator import tarjimon
bot= Bot(token=token)
dp = Dispatcher(bot=bot)
@dp.message_handler(commands='start')
async def start_command(message:types.Message):
    await message.answer("Men tarjimon Botman xohlagan so'zingizni yozing inglizcha variantini chiqarib beraman")
@dp.message_handler(content_types='text')
async def message_send(message: types.Message):
    text = message.text
    tarjima= tarjimon(text=text)

    await message.answer(tarjima)
if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)