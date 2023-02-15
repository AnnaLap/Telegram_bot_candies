from loader import dp, bot 
from aiogram import types
import emoji

total = 150


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f'/help - правила игры\n/set <число> - поменять общее количество конфет в игре\n/new_game - начало новой игры')
    # keyboard = types.InlineKeyboardMarkup()
    # keyboard.add(types.InlineKeyboardButton(text='Правила игры', callback_data='hi'))
    # keyboard.add(types.InlineKeyboardButton(text='Начало новой игры', callback_data='new_game'))
    # keyboard.add(types.InlineKeyboardButton(text='Поменять общее количество конфет в игре', callback_data='set'))
    # await message.answer(emoji.emojize('Нажми на кнопку - получишь результат :thumbs_up:'), reply_markup=keyboard)


@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    global total
    await message.answer(f'Приветствую, {message.from_user.first_name}!\nДавай сыграем в игру в конфеты: всего есть {total} конфет. За один ход игрок может взять не больше 28 конфет. Выигрывает тот, кто делает последний ход. ')


@dp.message_handler(commands=['set'])
async def mes_set(message: types.Message):
    global total
    count = message.text.split()[1]
    total = int(count)  
    await message.answer(f'Общее количество конфет в игре = {total}')


@dp.message_handler(commands=['new_game'])
async def mes_new_game(message: types.Message):
    global total 
    await  message.answer(f'Начинаем. Количество конфет в игре = {total}')
    await bot.send_message(message.from_user.id, 'Ваш ход. Введите количество конфет:')
      
    
@dp.message_handler()
async def mes_all(message: types.Message):
    global total
    if message.text.isdigit():
        if int(message.text) > 28 or int(message.text) < 1:
            await bot.send_message(message.from_user.id,'Введите число от 1 до 28')
        else:
            if int(message.text) > total:
                await bot.send_message(message.from_user.id, f'Вы можете взять только {total} конфет.')
            else: 
                total -= int(message.text) 
                await bot.send_message(message.from_user.id, f'{total}шт. конфет осталось в игре')
                if total == 0:
                    await bot.send_message(message.from_user.id, emoji.emojize(f'Победа за {message.from_user.first_name} :smiling_face_with_horns:'))
                else:
                    taken = total%29
                    if taken == 0:
                        taken = 1
                    if taken > total:
                        await message.answer(emoji.emojize(f'Python_bot забирает {total} конфет. Бот Вас уделал :zany_face:'))
                    else:
                        total -= taken
                        await message.answer(f'Python_bot забирает {taken} конфет. {total}шт. конфет осталось в игре')
                        if total == 0:
                            await message.answer(emoji.emojize(f'Python_bot Вас уделал :zany_face:'))
                        else:
                            await bot.send_message(message.from_user.id,'Ваш ход. Введите количество конфет:')
    else:
        await bot.send_message(message.from_user.id,'Введите число')
    






