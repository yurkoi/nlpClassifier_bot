from re import compile

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.deep_linking import get_start_link

from filters import IsPrivate
from loader import dp
from utils.db_api import User
from utils.misc import rate_limit


@rate_limit(limit=10)
@dp.message_handler(CommandStart(deep_link=compile(r"\w+"), encoded=True), IsPrivate())
async def bot_start_deeplink(message: types.Message):
    deep_link_args = message.get_args()

    await message.answer(f'Hi, {message.from_user.full_name}. you have deep link {deep_link_args}!')


# @rate_limit(limit=10)
# @dp.message_handler(CommandStart(deep_link=None), IsPrivate())
# async def bot_start(message: types.Message):
#
#     deep_link = await get_start_link("123", encode=True)
#     await message.answer(f'Hi, {message.from_user.full_name}. '
#                          f'you have no deep link {deep_link}!')


@rate_limit(limit=10)
@dp.message_handler(CommandStart())
async def bot_starter(message: types.Message, user: User):
    await message.answer(f'Hi, {message.from_user.full_name}. '
                         f'user from middleware: {user.__dict__}!')
