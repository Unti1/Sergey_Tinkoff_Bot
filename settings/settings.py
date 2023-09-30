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
SQL Database development
'''
import aiomysql


'''
Other libs
'''
import configparser
import asyncio
import logging


config = configparser.ConfigParser()
config.read('settings/settings.ini')


def config_update():
    with open('settings/settings.ini', 'w', encoding='utf-8') as file:
        config.write(file)
    config.read(file)  # обновляем конфигурацию


logging.basicConfig(
    level=logging.INFO,
    filename='data/logs.log',
    format="%(asctime)s - %(module)s\n[%(levelname)s] %(funcName)s:\n %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
    encoding="utf-8"
)

if __name__ == "__main__":
    pass
    # try:
    #     print(config['Telegram']['api'])
    # except:
    #     print('не записался')
    #
    # print(config.sections())
    # print(config.items('Telegram'))
    # #config['Telegram']['username'] = 'кто-то'
    # # config_update()
