from settings import *


def timeit(func):
    """ Декоратор для измерения времени работы асинхронной и синхронной функции."""

    if asyncio.iscoroutinefunction(func):

        @wraps(func)
        async def measure_time(*args, **kw):
            start_time = time.time()
            result = await func(*args, **kw)

            logger.info(f'Время выполнения асинхронной функции {func.__qualname__}:'
                        f' {(time.time() - start_time):.6f} сек.\n')
            return result

    else:

        @wraps(func)
        def measure_time(*args, **kw):
            start_time = time.time()
            result = func(*args, **kw)

            logger.info(f'Время выполнения синхронной функции {func.__qualname__}:'
                        f' {(time.time() - start_time):.6f} сек.\n')
            return result

    return measure_time


def utc3(utc0):
    """
    Функция перевода времени в Московский часовой пояс
    :return: datetime UTC+3
    """
    return utc0 + timedelta(hours=3)
