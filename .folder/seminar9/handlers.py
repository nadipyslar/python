from loader import dp, bot
from aiogram import types
import random
total = 150

@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.answer(f'Hi, {message.from_user.first_name}! Have not seen you for while, press "/turn" to start the game')

@dp.message_handler(commands=['turn'])
async def mes_turn(message: types.Message):
    global total
    whos_turn=random.randint(1,2)
    if whos_turn==1:
            await message.answer(f'this is your turn, {message.from_user.first_name}!how many sweets will you take?')
            await bot.send_message(message.from_id, f'we have {total - int(message.text)} sweets on the table')
    if whos_turn==2:
            bot=random.randint(1,28)
            total-=bot
            await message.answer(f'It is bot turn, bot took {bot} sweets, there are {total} sweets on the table. Now it is your turn')
            whos_turn-=1

while total in range (28,150):
    mes_turn


#@dp.message_handler()
#async def mes_all(message: types.message):
#    global total
#    hod=int(message.text)
#    if hod in range (1,29):
#        total-=hod
#        await bot.send_message(message.from_user.id, f'we have {total} sweets on table')
#    else:
#        await bot.send_message(message.from_user.id, f'enter the number from 1 to 28!')
    #await message.answer('Look what i have got - {message.text}')

#@dp.message_handler(commands=['set'])
#async def mes_set(message: types.Message):
#    global total
#    count = message.text.split()[1]
#    total = int(count)

#    await message.answer('now it is new quantity of sweets - {total}')

#@dp.message_handler(commands=['OOP'])
#async def mes_oop(message: types.Message):
#    await message.answer('What are you saying')
