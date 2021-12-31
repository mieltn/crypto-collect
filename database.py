import psycopg2
from config import TABLE

def connect(DATABASE, USER):
    '''
    Handles connection to db
    '''
    conn = psycopg2.connect(
        host = 'localhost',
        database = DATABASE,
        user = USER
    )
    return conn


def insert(cursor, data):
    '''
    Handles data inserts
    '''

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