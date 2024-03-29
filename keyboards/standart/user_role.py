from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from .cancel import btn_cancel

kb_user_role = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

btn_admin = KeyboardButton(text='Организатор')
btn_acro = KeyboardButton(text='Акро')
btn_guest = KeyboardButton(text='Гость')

kb_user_role.add(btn_admin, btn_acro, btn_guest)
kb_user_role.add(btn_cancel)