from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import btns_callback

choise = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[[
                                  InlineKeyboardButton(
                                      text="inline btn 1",
                                      callback_data=btns_callback.new(item_name="btn1",
                                                                      quantity=1)
                                        ),
                                  InlineKeyboardButton(
                                      text="inline btn 2",
                                      callback_data=btns_callback.new(item_name="btn2",
                                                                      quantity=1)
                                        ),
                                  InlineKeyboardButton(
                                      text="cancel",
                                      callback_data="cancel"
                                        )
                                     ]
                              ])

btn_keyboard = InlineKeyboardMarkup()

BTN_LINK = 'https://www.machinelearningmastery.ru/'
btn_link = InlineKeyboardButton(text="Click here", url=BTN_LINK)

btn_keyboard.insert(btn_link)