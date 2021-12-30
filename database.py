import psycopg2
from config import TABLE

def connect(DATABASE, USER):
    conn = psycopg2.connect(
        host = 'localhost',
        database = DATABASE,
        user = USER
    )
    return conn


def insert(cursor, data):
    query = '''
    INSERT INTO crypto_rates (crypto_name, rate, market_cap)
      VALUES ('{}', {}, {})
    '''.format(
        data['crypto_name'],
        data['rate'],
        data['market_cap']
    )
    cursor.execute(query)
    return 'ok'