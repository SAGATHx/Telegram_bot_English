import random
import time
import logging
import os

from Data import question, verb, Time, pronouns
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from dotenv import load_dotenv
load_dotenv()

bot = Bot(token= os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

question_pas = ''.join(random.choice(pronouns) + random.choice(verb) + random.choice(Time) + random.choice(question))


async def on_startup(_):
    print('Тачка завелась, педаль в пол класть стрелку под камерами...')

kb = ReplyKeyboardMarkup(resize_keyboard= True)
b1 = KeyboardButton('Задай вопрос сейчас!')
""" b2 = KeyboardButton('Не знаю пока че тут будет') """
kb.add(b1)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    User_name = message.from_user.first_name
    logging.info(f'{User_name}', time.asctime())
    await message.answer(f'Привет, {User_name}!\nготов покорять Английский? :3\n\nНебольшой экскурс по боту!\nВам прийдет сообщение, например: Она работать Будуще ?\nВ данном случае вы должны задать себе вопрос Она будет работать? Так как форма Будущего времяни и есть знак вопроса... и соотвественно написать ответ на Английском, если вопроса нет то и ответ не вопросительный)', reply_markup=kb)

@dp.message_handler(content_types=['text'])
async def start_handler(message: types.Message):
    User_id = message.from_user.id
    User_name = message.from_user.first_name
    User_full = message.from_user.full_name
    logging.info(f'{User_id} {User_name} {User_full}', time.asctime())
    if message.text == 'Задай вопрос сейчас!':
        await message.answer(question_pas)
    else:
        await message.answer('Не могу проверить правильно или нет, но ты старался я уверен)')

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)

""" python3 Bot.py """

