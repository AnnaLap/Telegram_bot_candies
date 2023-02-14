from loader import dp, bot 
from aiogram import types

total = 150

@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.answer(f'Hi {message.from_user.first_name}'
                         f'What is UP?')


@dp.message_handler(commands=['OOP'])
async def mes_oop(message: types.Message):
    await message.answer('Bla-bla')

@dp.message_handler(commands=['set'])
async def mes_set(message: types.Message):
    global total
    count = message.text.split()[1]
    total = int(count)  
    await message.answer(f'New total candies = {total}')


@dp.message_handler(commands=['OOP'])
async def mes_all(message: types.Message):
    if message.text.isdigit():
        total -= int(message.text) 
        await bot.send_message(message.from_user.id, f'{total} candies left')
        await message.answer(f'Look at this - {message.text}')
    else:
        await bot.send_message('Write numbers')
