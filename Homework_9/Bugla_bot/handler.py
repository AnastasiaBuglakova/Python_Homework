from aiogram import types
from loader import dp
import random

total = 100
game = False
count = 0
MESSAGE_CANDY_GAME = "Для игры с конфетами человек против бота введи /game.\nУсловия игры: "\
                     "На столе лежит заданное количество конфет.\n"\
                     "Играют два игрока, делая ход друг после друга. Первый ход определяется случайно. \n"\
                     "За один ход можно забрать не более чем 28 конфет. \n"\
                     "Все конфеты оппонента достаются сделавшему последний ход. \n"\
                     "Можно до начала игры выбрать количество конфет командой /set 000, где 000 - количество конфет цифрами.\n"\
                     "По умолчанию 100. Могу сказать заранее, при любом количестве конфет, если бот ходит первым, шансов у тебя нет)"


@dp.message_handler(commands = ['start', 'старт'])
async def mes_start(message: types.Message):
    await message.answer('Bugla_bot приветсвует тебя сердечно!\nВыбери /help, чтобы узнать что я умею.')
    print("Teбе сообщение в телегу упало. Смотри какое:")
    print(message)

@dp.message_handler(commands = ['help', 'помоги'])
async def mes_help(message: types.Message):
    await message.answer(f'Я умею выполнять команды:\n /start\n /help\n/game\n{MESSAGE_CANDY_GAME}')
    print('Тебя помочь просят', message)

@dp.message_handler(commands = ['game', 'игра'])
async def mes_game(message: types.Message):
    global game
    global total
    global count
    game = True
    with open('count.txt', 'r') as data:
        count = int(data.read().strip())
    if count != 0:
        total = count
    else:
        total = 100

    starting_gamer = random.choice(['you', 'Bot'])
    if starting_gamer == 'you':
        await message.answer(f'Начинаем играть. На столе {total} конфет\n Первым ходит {message.from_user.first_name}')
    else:
        await message.answer(f'Начинаем играть.На столе {total} конфет\n Первым ходит Bugla_bot')
        if total % 29 != 0:
            bot_step = total % 29
            total -= bot_step
            await message.answer(f'Bugla_bot взял {bot_step} конфет. Теперь твоя очередь брать конфеты. Осталось {total}')
        else:
            total -= 1
            await message.answer(f'Bugla_bot взял 1 конфету. Теперь твоя очередь брать конфеты. Осталось {total}')
    # your_step = 0
    print('Игра в конфеты началась', message)

# set_candy 300
@dp.message_handler(commands = ['set'])
async def mes_set_candy(message: types.Message):
    global total
    global game
    if not game:
        count = message.text.split()[1]
        if count.isdigit():
            total = int(count)
            await message.answer(f'Теперь на столе {total} конфет.)'
                                 f'Для начала игры набери /game.')
            with open('count.txt', 'w') as data:
                data.write(count)

        else:
            await message.answer(f'{message.from_user.first_name}, напишите количетво конфет цифрами')
    else:
        await message.answer(f'{message.from_user.first_name}, не получится изменить количество конфет во время игры.')
# @dp.message_handler()
# async def mes_all(message: types.Message):
#     global total
#     if message.text.isdigit():
#         total -= int(message.text)
#         await message.answer(f'{message.from_user.first_name} взял {message.text} конфет. '
#                          f'На столе осталось {total}')
@dp.message_handler()
async def mes_all(message: types.Message):
    global total
    global game
    if game:
        # шаг человека
        if message.text.isdigit() and 0 < int(message.text) < 29:
            total -= int(message.text)
            await message.answer(f'{message.from_user.first_name} взял {message.text} конфет. '
                                 f'На столе осталось {total}')
            flag = True
        else:
            if message.text.isdigit():
                await message.answer(f'{message.from_user.first_name}, ты можешь взять не менее 1 и не более 28 конфет.')
                await message.answer(f'Напиши количетво конфет от 1 до 28')
            else:
                await message.answer(f'{message.from_user.first_name}, напиши количетво конфет цифрами')
            flag = False
        if total == 0:
            await message.answer(f'{message.from_user.first_name}, победа - твоя!')
            game = False
            # шаг бота
        if game and flag:
            if total % 29 > 0:
                bot_step = total % 29
                total -= bot_step
                await message.answer(f'Бот взял {bot_step}, осталось {total} конфет.')
            else:
                bot_step = random.randint(1, 29)
                total -= bot_step
                await message.answer(f'Бот взял {bot_step} конфет, осталось {total} конфет.')
        if total == 0 and game:
            await message.answer(f'Конфеты закончились. Bugla_bot выиграл.')
            game = False

    else:
        await message.answer(f'{message.from_user.first_name}, зачем пишешь такое, непонятное: '
                             f'Если не знаешь что со мной делать набери /help')