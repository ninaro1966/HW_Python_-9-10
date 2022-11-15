
import handlers
from create_bot import dp
from aiogram import executor

async def onStart(_):
    print('Гусёна, в игре с конфетами побеждает последний взявший. Ну-ка, от винта!')

handlers.registred_handlers(dp)


executor.start_polling(dp, skip_updates=True, on_startup=onStart)
