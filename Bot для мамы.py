import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

bot = Bot(token="6931024206:AAHgxyzIAi-4B2rBieCyshNGNughaKXcVDg")
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Спасибо за подписку.\nВ подарок вам предоставляется полезные материалы для ремонта!\n'
                         '(ссылки на них)\n'
                         "(ссылки на них)\n"
                         "(ссылки на них)\n"
                         'Для консультации и заказа проекта пишите в (ссылка на канал).')