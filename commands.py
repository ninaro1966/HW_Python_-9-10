
import asyncio
import random

import view
from create_bot import dp
from aiogram import types

import model
from create_bot import bot


async def start(message: types.Message):
    player = message.from_user
    model.set_player(player)
    await view.hello(message)
    await asyncio.sleep(3)
    dp.register_message_handler(player_turn)
    first_turn = random.randint(0,1)
    if first_turn:
        await await_player(player)
    else:
        await enemy_turn(player)

async def player_turn(message: types.Message):
    player = message.from_user
    model.set_player(player)
    if (message.text).isdigit():
        if 0 < int(message.text) < 29:
            total_count = model.get_total_candies()
            player_take = int(message.text)
            total = total_count - player_take
            await bot.send_message(player.id, f'{player.first_name} взял {player_take} конфет, '
                                              f'и на столе осталось {total}')
            if model.check_win(total):
                await bot.send_message(player.id, f'Победил, естественно, {player.first_name}')
                return
            model.set_total_candies(total)
            await enemy_turn(player)

        else:
            await bot.send_message(message.from_user.id, 'Гусена,, да он считать не умеет!')
    else:
        await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, '
                                                     f'в цифрах, в цифрах, очнись!')

async def enemy_turn(player):
    total_count = model.get_total_candies()
    if total_count < 29:
        enemy_take = total_count
    else:
        enemy_take = (total_count - 1)%28
    total = total_count - enemy_take
    await bot.send_message(player.id, f'взял уже {enemy_take} конфет, '
                                      f'и на столе осталось {total}')
    if model.check_win(total):
        await bot.send_message(player.id, f'{player.first_name} Черный Плащ побеждает, как всегда!,'
                                          f'нюхни газу, злодей!')
        return
    model.set_total_candies(total)
    await asyncio.sleep(1)
    await await_player(player)




async def await_player(player):
    max_take = model.get_max_take()
    await bot.send_message(player.id,
                           f'{player.first_name}, Гусёна, бери как в model написано - не больше {max_take}')

async def set_total_candies(message: types.Message):

    count = int((message.text).split(" ")[1])
    model.set_total_candies(count)
    await bot.send_message(message.from_user.id, f'Максимально количество конфет изменили на'
                                                 f' {count}')
