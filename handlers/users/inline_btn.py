from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from keyboards.inline.callback_data import btns_callback
from keyboards.inline.choise_btn import choise, btn_keyboard
from loader import dp
from utils.misc import logging


@dp.message_handler(Command("btn_item"))
async def show_inline_button(message: types.Message):
    await message.answer(("Some text inside the button \n"
                          "to exit click on 'cancel'"), reply_markup=choise)


@dp.callback_query_handler(btns_callback.filter(item_name=["btn1", "btn2"]))
async def btn1_fun(call: CallbackQuery, callback_data: dict):
    # await bot.answer_callback_query(callback_query_id=call.id) the same as below
    await call.answer(cache_time=60)
    # logging.info(f"callback_data = {call.data}")
    # logging.info(f"callback_data dict = {callback_data}")
    quantity = callback_data.get("quantity")
    btn_name = callback_data.get("item_name")
    await call.message.answer(f'You choose {btn_name} {quantity}', reply_markup=btn_keyboard)


@dp.callback_query_handler(text="cancel")
async def cancel(call: CallbackQuery):
    await call.answer("You are denied your purchase", show_alert=True)
    await call.message.edit_reply_markup()