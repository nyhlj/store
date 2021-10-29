import pymysql

host = "localhost"
user = "root"
password = ""
database = "salesdatabase"


def update(sql, param):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql, param)

    con.commit()
    cursor.close()
    con.close()


def select(sql, param, mode='one', size=1):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql, param)

    if mode == 'one':
        return cursor.fetchone()
    elif mode == 'all':
        return cursor.fetchall()
    elif mode == 'many':
        return cursor.fetchmany(size)

    con.commit()
    cursor.close()
    con.close()
