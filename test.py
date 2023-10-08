from settings import *
from tools.db import *
from tools.tinkoffAPI import *
from tools.utils import *


async def pr():
    print(config['Tinkoff']['api'])
    print(config['Telegram']['api'])
    print(INVEST_TOKEN)


async def main():
    #task1 = asyncio.create_task(get_exchange_figi_shares())
    tast2 = asyncio.create_task(get_schedules())
    #tast3 = asyncio.create_task(get_info_shares())
    #tast4 = asyncio.create_task(get_last_candle())

    #await task1
    await tast2
    #await tast3
    #await tast4

if __name__ == "__main__":
    print(now())
    asyncio.run(main())
