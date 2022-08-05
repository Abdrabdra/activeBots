# coding=utf-8
from aiogram.utils import executor

import handlers
from main import dp
from utils.help_functions import on_startup


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)