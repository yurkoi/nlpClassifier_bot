from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("help", "Помощь"),
        types.BotCommand("btn_menu", "Pass the test"),
        types.BotCommand("questions", "Pass the test"),
        types.BotCommand("btn_item", "Button items"),
    ])
