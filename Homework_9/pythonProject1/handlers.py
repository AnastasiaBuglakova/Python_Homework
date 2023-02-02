import random
import os.path
from aiogram import types
from loader import dp
max_count = 150
total = 0
new_game = False
duel = []
first = 0
current = 0


@dp.message_handler(commands=['start', 'старт'])
async def mes_start(message: types.Message):
    MESSAGE_CANDY_GAME = "Для игры с конфетами человек против бота введи /game.\nУсловия игры: " \
                         "На столе лежит заданное количество конфет.\n" \
                         "Играют два игрока, делая ход друг после друга. Первый ход определяется случайно. \n" \
                         "За один ход можно забрать не более чем 28 конфет. \n" \
                         "Все конфеты оппонента достаются сделавшему последний ход. \n" \
                         "Можно до начала игры выбрать количество конфет командой /set 000, где 000 - количество конфет цифрами.\n" \
                         "По умолчанию 150. Могу сказать заранее, при любом количестве конфет, если бот ходит первым, шансов у тебя нет)." \
                         "\nДля игры с оппонентом введи /duel и id оппонента, для игры вдвоем."

    name = message.from_user.first_name
    await message.answer(f'{name}, привет!\n{MESSAGE_CANDY_GAME}')
    print(message.from_user.id)


@dp.message_handler(commands=['new_game'])
async def mes_new_game(message: types.Message):
    global new_game
    global total
    global max_count
    global first
    new_game = True

    # здесь предлагаю считывать из файла сохраненное значение по команде /set. Если файла там нет, то берем max_count
    if os.path.isfile('count.txt'):
        with open('count.txt', 'r') as data:
            count = data.read().strip()
        total = int(count)
    else:
        total = max_count

    first = random.randint(0,1)
    if first:
        await message.answer(f'Игра началась. На столе {total} конфет. По жребию первым ходит {message.from_user.first_name}! Бери конфеты...')
    else:
        await message.answer(f'Игра началась. На столе {total} конфет. По жребию первым ходит Ботяо')
        await bot_turn(message)


@dp.message_handler(commands=['duel'])
async def mes_duel(message: types.Message):
    global new_game
    global total
    global max_count
    global duel
    global first
    global current
    duel.append(int(message.from_user.id))
    # проверяем ввел ли игрок, запрашивающий дуэль, айди оппонента, и только тогда выполняем программу
    print(len(message.text.split()))
    name = message.from_user.first_name
    if len(message.text.split()) < 2:
        await message.answer(f"{name}, Введи ID оппонента в команде '/duel ID'")
    else:
        duel.append(int(message.text.split()[1]))

        # здесь тоже предлагаю считывать из файла сохраненное значение по команде /set. Если файла там нет, то берем max_count
        if os.path.isfile('count.txt'):
            with open('count.txt', 'r') as data:
                count = data.read().strip()
            total = int(count)
        else:
            total = max_count

        total = max_count
        first = random.randint(0,1)
        if first:
            await dp.bot.send_message(duel[0], f'Первый ход за тобой, на столе {total} конфет, бери конфеты')
            await dp.bot.send_message(duel[1], f'Первый ход за твоим противником! На столе {total} конфет. Жди своего хода')
        else:
            await dp.bot.send_message(duel[1], f'Тебя на дуэль вызывает {name}. Первый ход за тобой,на столе {total} конфет, бери конфеты')
            await dp.bot.send_message(duel[0], f'Первый ход за твоим противником! На столе {total} конфет. Жди своего хода')
        current = duel[0] if first else duel[1]
        new_game = True


@dp.message_handler(commands=['set'])
async def mes_set(message: types.Message):
    global max_count
    global new_game
    name = message.from_user.first_name
    count = message.text.split()[1]
    if not new_game:
        # добавила and int(count) > 28 чтобы вводили не мнее 29 конфет, иначе с 0 первый походивший выигрывал
        if count.isdigit() and int(count) > 28:
            max_count = int(count)
            await message.answer(f'Конфет теперь будет {max_count} ')
            # предлагаю сохранить значение в файл, чтобы оно не терялось при перезапуске бота
            with open('count.txt', 'w') as data:
                data.write(count)
        else:
            # уточнила текст в связи с изменением в строке 69
            await message.answer(f'{name}, напиши цифрами число не менее 29.')
    else:
        await message.answer(f'{name}, нельзя менять правила во время игры')


@dp.message_handler()
async def mes_take_candy(message: types.Message):
    global new_game
    global total
    global max_count
    global duel
    global first
    name = message.from_user.first_name
    count = message.text
    if len(duel) == 0:
        if new_game:
            if message.text.isdigit() and 0 < int(message.text) < 29:
                total -= int(message.text)
                if total <= 0:
                    await message.answer(f'Ура! {name} ты победил!')
                    new_game = False
                else:
                    await message.answer(f'{name} взял {message.text} конфет. На столе {total} конфет. '
                                         f'На столе осталось {total}')
                    await bot_turn(message)
            else:
                await message.answer(f'{name}, надо указать ЧИСЛО от 1 до 28!')
    else:
        if current == int(message.from_user.id):
            name = message.from_user.first_name
            count = message.text
            if new_game:
                if message.text.isdigit() and 0 < int(message.text) < 29:
                    total -= int(message.text)
                    if total <= 0:
                        await message.answer(f'Ура! {name} ты победил!')
                        await dp.bot.send_message(enemy_id(), 'К сожалению ты проиграл! Твой оппонент оказался умнее! :)')
                        new_game = False
                    else:
                        await message.answer(f'{name} взял {message.text} конфет. На столе {total} конфет. '
                                             f'На столе осталось {total}')
                        await dp.bot.send_message(enemy_id(), f'Теперь твой ход, бери конфеты! На столе осталось ровно {total}')
                        switch_players()
                else:
                    await message.answer(f'{name}, надо указать ЧИСЛО от 1 до 28!')


async def bot_turn(message: types.Message):
    global total
    global new_game
    bot_take = 0
    if 0 < total < 29:
        bot_take = total
        total -= bot_take
        await message.answer(f'Бот взял {bot_take} конфет. '
                             f'На столе осталось {total} и бот одержал победу')
        new_game = False
    else:
        remainder = total%29
        bot_take = remainder if remainder != 0 else 28
        total -= bot_take
        await message.answer(f'Бот взял {bot_take} конфет. '
                             f'На столе осталось {total}')

def switch_players():
    global duel
    global current
    if current == duel[0]:
        current = duel[1]
    else:
        current = duel[0]


def enemy_id():
    global duel
    global current
    if current == duel[0]:
        return duel[1]
    else:
        return duel[0]