import pymongo
from datetime import date

#Connect mongodb
mclient=pymongo.MongoClient('mongodb://localhost:27017/')
mdb=mclient['bible']

class get_books():
    books=[]
    books_indexes={}
    collection=mdb['summary']
    contents=collection.find().sort('book_code', pymongo.ASCENDING)
    for row in contents:
        book={}
        book['name']=row['cuv_t_name']
        book['abbr'] = row['cuv_t_abbr']
        book['book_code'] = row['book_code']
        books.append(book)
        books_indexes[row['book_code']]=[row['cuv_t_name'],row['cuv_t_abbr']]
    def get_chapters(book_code):
        result=[]
        query={'bookNum':book_code}
        chps=mdb['cuv_t'].find(query).sort('chNum', pymongo.ASCENDING)
        for chp in chps:
            if chp['chNum'] not in result:
                result.append(chp['chNum'])
        return result

    def get_words(book_code,chp_num):
        words={}
        query={'bookNum':book_code,'chNum':chp_num}
        word_contents=mdb['cuv_t'].find(query)
        for word in word_contents:
            words[word['verseNum']]=word['word']
        return words
    def get_book_abbr(book_code):
        row=mdb['summary'].find_one({'book_code':book_code})
        return row['cuv_t_abbr']
    def get_book_name(book_code):
        row=mdb['summary'].find_one({'book_code':book_code})
        return row['cuv_t_name']

class search_bible:
    def get_search_results(key_word,bl_version):
        results=[]
        #key_hl = "\<span class='content_hl'\>" + key_word + "\</span\>"
        if key_word:
            coll_word=mdb[bl_version]
            query={'word':{'$regex':key_word}}
            docs=coll_word.find(query)
            for doc in docs:
                word=doc['word']
                #res_word=word.replace(key_word,key_hl)
                result=[doc['bookNum'],doc['chNum'],doc['verseNum'],word]
                results.append(result)
        return results

class common_info:
    this_year = date.today().strftime("%Y")
