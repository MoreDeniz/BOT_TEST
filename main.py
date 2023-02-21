from aiogram import Bot, Dispatcher, executor, types
from loader import dp, db


async def on_start(_):
    print('Бот запущен.')
    await dp.bot.send_message(chat_id=1468741015, text='Хозяин! Бот запущен!')
    try:
        db.create_table_users()
        db.create_table_events()
        db.create_table_locations()
        print('DB connected ... OK!')
    except:
        print('DB failure!')


async def on_shutdown(_):
    print('Бот упал.')
    db.disconnect()
    await dp.bot.send_message(chat_id=1468741015, text='Хозяин! Бот упал!')


@dp.message_handler()
async def mes_all(message: types.Message):
    await message.reply(text='Поймал всё!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start, on_shutdown=on_shutdown)
