def insert(cursor):
    from scraping import searcher
    #日本語リスト
    jp_list = ['サッカー','野球','バスケットボール','バレーボール','卓球','ボクシング','水泳','ラグビー']

    #insert into table
    for i in range(len(jp_list)):
        jp_word = jp_list[i]
        eng_word = searcher(jp_word)
        cursor.execute('insert into dicweblio (id,"japanese","english") values (%s, %s, %s)',(i, jp_word, eng_word))

