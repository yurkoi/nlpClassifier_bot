from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states import Test


@dp.message_handler(Command("questions"))
async def enter_test(message: types.Message):
    await message.answer("You are started testing. \n"
                         "Question 1. \n\n")
    await Test.Q1.set()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(answer1=answer)

    await message.answer("Question 2. \n\n")

    await Test.Q2.set()


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):

    answer = message.text
    await state.update_data(answer2=answer)
    await message.answer("Question 3. \n\n")
    await Test.Q3.set()


@dp.message_handler(state=Test.Q3)
async def answer_q3(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = message.text
    await message.answer("Your answers")

    for idx, ans in enumerate(data.values()):
        await message.answer(f"answers {idx}: {ans}")

    await message.answer(f"answer 3: {answer}")
    await state.reset_state()
    # await state.reset_state(with_data=False) # with save data!!!
