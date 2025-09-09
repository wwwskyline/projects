import asyncio
import random

from aiogram import types, Dispatcher
from aiogram.filters import CommandStart, Command
import html
from aiogram.fsm.context import FSMContext
from states.state import user

async def start_command(message: types.Message):
    await message.answer(f'<b>{html.escape(message.from_user.full_name)}</b>, привет!\n\n'
                         f'Я бот-игра: <b>"угадай число"</b>!\n'
                         f'Чтобы начать игру напиши /game')


async def game(message: types.Message, state: FSMContext):
    await message.answer(f'Бот загадал число от 1 до 10, попробуй отгадать!')
    await state.set_state(user.number)

async def state_handler(message: types.Message, state: FSMContext):
    random_number = random.randint(1, 10)
    user_message = message.text
    if user_message.isdigit():
        if 10 >= int(user_message) >= 1:
            if int(user_message) == random_number:
                await message.answer('Вы угадали!')
                await state.clear()
                await asyncio.sleep(1)
                await message.answer('Чтобы продолжить играть напишите /game')
            else:
                await message.answer(f'Вы не угадали, загаданное число: {random_number}')
        else:
            await message.answer('Ваше число не входит в диапозон от 1 до 10')
    else:
        await message.answer('Пожалуйста, пришлите число!')
def register_user_messages(dp: Dispatcher):
    dp.message.register(start_command, CommandStart())
    dp.message.register(game, Command('game'))
    dp.message.register(state_handler, user.number)