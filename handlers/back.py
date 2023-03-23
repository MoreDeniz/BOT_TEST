from aiogram.types import Message, InputFile, CallbackQuery, InputMediaPhoto
from loader import dp, db
from keyboards.hjk import menu_main
from keyboards.inline import kb_main_menu_acro
from config import system_pictures

@dp.callback_query_handlers(menu_main.filter(button='back'))
async def my_events(call: CallbackQuery):

    name = call.message.chat.full_name
    current_chat_id = call.message.chat.id
    current_message_id = call.message.message_id
    photo = system_pictures.get('main')
    caption = f'Привет, {name}!\n Что будем делать?'
    await dp.bot.edit_message_media(media=InputMediaPhoto(media=photo, caption=caption),
                                    chat_id=current_chat_id,
                                    message_id=current_message_id,
                                    reply_markup=kb_main_menu_acro)