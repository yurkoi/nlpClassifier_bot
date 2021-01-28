from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import menu
from loader import dp


@dp.message_handler(Command("btn_menu"))
async def show_menu(message: types.Message):
    await message.answer("Choose button below", reply_markup=menu)


@dp.message_handler(text="button 1")
async def get_btn1(message: types.Message):
    await message.answer("You`ve chosen btn1")


@dp.message_handler(Text(equals=["button 2", "button 3", "button 4"])) #endswith="3"
async def get_btn3(message: types.Message):
    await message.answer(f"You`ve got {message.text}", reply_markup=ReplyKeyboardRemove())