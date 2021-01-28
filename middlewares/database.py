from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types
from utils.db_api import User


class GetDBUser(BaseMiddleware):

    async def on_process_message(self, message: types.Message, data: dict):
        data["user"] = User(id=message.from_user.id, name=message.from_user.full_name)

    async def on_process_callback_user(self, message: types.CallbackQuery, data: dict):
        data["user"] = User(id=message.from_user.id, name=message.from_user.full_name)

