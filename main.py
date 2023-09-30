from settings import *
from tools import *


async def main_run():
    bot = Bot(token=config['Telegram']['API'], parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    # print(config['Telegram']['API'])
    asyncio.run(main_run())