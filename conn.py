# -*- coding:utf-8 -*-
def connectDB():
    import psycopg2, os, sys
    from insertation import insert

    db_name = "testdb"
    connection = psycopg2.connect(
            host = "XXX.XXX.XXX.XXX",
            database = db_name,
            user = "name",
            password = "******"
    )

    cursor = connection.cursor()

    #テーブルを空にする
    cursor.execute('delete from dicweblio;')

    #テーブルの作成
    os.system('psql {} < {}'.format(db_name, sys.argv[1]))

    insert(cursor)

    connection.commit()
    cursor.close()
    connection.close()
