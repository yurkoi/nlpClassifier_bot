from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = [
        'Список команд: ',
        '/start - Start dialog',
        '/help - Call for help :)',
        '/questions - Check the statements',
        '/buttons_menu - Check buttons',
        '/inline_buttons - Inline buttons',
    ]
    await message.answer('\n'.join(text))
