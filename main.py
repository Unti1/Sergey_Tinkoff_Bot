import asyncio
import datetime
from settings import *
from tools import *


async def start_bot():
    """
    Сопрограмма конфигурации и запуск бота
    :return: NoReturn
    """
    bot = Bot(token=config['Telegram']['api'], parse_mode=ParseMode.HTML)  # создаём экземпляр бота
    dp = Dispatcher(bot=bot, storage=MemoryStorage())  # создаём экземпляр диспетчера
    dp.include_router(router)  # подключаем роутер к диспетчеру
    await bot.delete_webhook(drop_pending_updates=True)  # игнорируем ранее поданные боту запросы
    await dp.start_polling(bot)  # запускаем асинхронного бота


async def monitoring_exchange(actual_shares):
    """
    Сопрограмма мониторинга расписаний и акций Мосбиржи, запускающаяся по расписанию.
    :param actual_shares: экземпляр класса актуального расписания и параметров акций Мосбиржи.
    :return: NoReturn
    """
    while True:
        # Проверяем время для запуска по расписанию актуализации расписания и параметров акций Мосбиржи
        if utc3(now()).strftime('%H') == '10':
            await actual_shares.fit()
            print(actual_shares.message_shedulers)
            #actual_shares.prn_exchanges()
            #actual_shares.prn_shares()
            #actual_shares.prn_shedulers()

            await asyncio.sleep(60)


async def main(actual_shares):
    """
    Сопрограмма конфигурации асинхронных задач
    :param actual_shares: экземпляр класса актуального расписания и параметров акций Мосбиржи.
    :return: NoReturn
    """
    # Конфигурация и запуск бота
    task1 = asyncio.create_task(start_bot())
    # Мониторинг расписаний Мосбиржи и формирование базы
    task2 = asyncio.create_task(monitoring_exchange(actual_shares))
    # Запускаем задачи асинхронно
    await asyncio.gather(task1, task2)


# Запускаем бота и опрос рынка
if __name__ == '__main__':

    # Создаём журнал логирования  ###---  ВОПРОС: как направлять в разные файлы потоки из разных модудей? ---###
    logger.add(LOG_SCHEDULE_PATH, rotation="1 MB", enqueue=True)

    # Создаём экземпляр расписания
    actual_shares = ActualInstruments()  # Создан в основном теле, чтобы иметь возможность передавать в любое место

    # Запускаем асинхронные задачи (бот, мониторинг расписания рынка)
    asyncio.run(main(actual_shares))

