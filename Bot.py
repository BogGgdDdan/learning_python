import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

bot = Bot(token="6931024206:AAHgxyzIAi-4B2rBieCyshNGNughaKXcVDg")
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Это была команда старт')

@dp.message()
async def echo(message: types.Message):
    text = message.text
    text_split = text.split()

    for i in text_split:
        if i in ['Привет', 'привет', 'hi', 'hello']:
            await message.answer('И тебе привет!')
            break
        elif text in ['Выведи стихотворение Зимний вечер', 'выведи стихотворение зимний вечер', 'зимний вечер'] or \
            i in ['зимний',"Зимний","Пушкин"]:
            await message.answer("Буря мглою небо кроет,\n"
                                  'Вихри снежные крутя;\n'
                                  'То, как зверь, она завоет,\n'
                                  'То заплачет, как дитя,\n'
                                  'То по кровле обветшалой\n'
                                  'Вдруг соломой зашумит,\n'
                                  'То, как путник запоздалый,\n'
                                  'К нам в окошко застучит.\n\n'
                                    
                                  'Наша ветхая лачужка\n'
                                  'И печальна и темна.\n'
                                  'Что же ты, моя старушка,\n'
                                  'Приумолкла у окна?\n'
                                  'Или бури завываньем\n'
                                  'Ты, мой друг, утомлена,\n'
                                  'Или дремлешь под жужжаньем\n'
                                  'Своего веретена?\n\n'
    
                                  'Выпьем, добрая подружка\n'
                                  'Бедной юности моей,\n'
                                  'Выпьем с горя; где же кружка?\n'
                                  "Сердцу будет веселей.\n"
                                  "Спой мне песню, как синица\n"
                                  "Тихо за морем жила;\n"
                                  "Спой мне песню, как девица\n"
                                  "За водой поутру шла.\n\n"
    
                                  "Буря мглою небо кроет,\n"
                                  "Вихри снежные крутя;\n"
                                  "То, как зверь, она завоет,\n"
                                  "То заплачет, как дитя.\n"
                                  "Выпьем, добрая подружка\n"
                                  "Бедной юности моей,\n"
                                  "Выпьем с горя; где же кружка?\n"
                                  "Сердцу будет веселей.")
            break
        elif i in ['Пока', 'пока', 'Прощай',"прощай"]:
            await message.answer('И тебе пока!')
            break
        elif text in ['Как дела?','как дела?','Как дела','как дела']:
            await message.answer('Нормально ,но когда написал ты ,настроение поднялось!А у тебя?')
            break
        elif i in ['Плохо',"Нормально","плохо","нормально"]:
            await message.answer('Не грусти и все будет хорошо!')
            break
        elif i in ['Хорошо',"Прекрасно","хорошо","прекрасно"]:
            await message.answer('Я и не сомневался!')
            break
    else:
        await message.answer(message.text)


async def main():
    await dp.start_polling(bot)

asyncio.run(main())