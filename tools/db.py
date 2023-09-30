from settings import *

    

async def collect_candle(loop,limit = 0):
    pool = await aiomysql.create_pool(host=config['SQL']['host'],
                                      port = 3306,
                                        user = config['SQL']['user'],
                                        password = config['SQL']['password'], 
                                        db=config['SQL']['db_name'], 
                                        loop=loop)
    async with pool.acquire() as con:
        cur = await con.cursor()
        await cur.execute('SELECT * FROM AKRN')
        if limit:
            rows = cur.fetchmany(limit)
        else:
            rows = cur.fetchall()
        print(rows)
    return rows

    