
'''
Bot development
'''
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command

'''
SQL Database dev
'''
import aiomysql

'''
Other libs
'''
import configparser
import asyncio

config = configparser.ConfigParser()
config.read('settings/settings.ini')

def config_update():
    with open('settings/settings.ini', 'w', encoding='utf-8') as f:
        config.write(f)
    config.read() # обновляем конфигурацию


import logging
logging.basicConfig(
    level=logging.INFO,
    filename="data/logs.log",
    format="%(asctime)s - %(module)s\n[%(levelname)s] %(funcName)s:\n %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
    encoding="utf-8"
)

if __name__ == "__main__":
    try:
        print(config['Telegram']['username'])
    except:
        pass
    config['Telegram']['username'] = 'кто-то'
    # config_update()
