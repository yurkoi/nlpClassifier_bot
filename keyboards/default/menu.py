from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup([
    [
        KeyboardButton(text="button 1")
    ],
    [
        KeyboardButton(text="button 2")
    ],
    [
        KeyboardButton(text="button 3")
    ],
    [
        KeyboardButton(text="button 4")
    ],

], resize_keyboard=True)
