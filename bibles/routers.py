from flask import render_template, request, Blueprint
from bibles.models import get_books, search_bible, common_info

main = Blueprint('main',__name__)

@main.route("/")
@main.route("/home")
def home():
    #page = request.args.get('page',1,type=int)
    #posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=3)
    title={'small':'Bible home','big':'Welcome to Bible Home Page','right':''}
    return render_template('home.html',title=title,hide_footer=True)

@main.route("/words/<int:book_code>/<int:chp_num>/", methods=['GET', 'POST'])
def words_book_chapter(book_code,chp_num):
    title = {'small': 'Bible words', 'big': '繁体中文和合本圣经','right':'search'}
    books = get_books.books
    words = get_books.get_words(book_code,chp_num)
    chapters=get_books.get_chapters(book_code)
    book_abbr=get_books.get_book_abbr(book_code)
    book_name=get_books.get_book_name(book_code)
    chp_info={'book_name':book_name,'book_abbr':book_abbr,'chp_num':chp_num,'book_code':book_code}
    return render_template('words.html',title=title,books=books,words=words,chapters=chapters,chp_info=chp_info,this_year=common_info.this_year)

@main.route("/words/<int:book_code>/", methods=['GET', 'POST'])
def words_book(book_code):
    title = {'small': 'Bible words', 'big': '繁体中文和合本圣经','right':'search'}
    books = get_books.books
    words = get_books.get_words(book_code,1)
    chapters = get_books.get_chapters(book_code)
    book_abbr=get_books.get_book_abbr(book_code)
    book_name=get_books.get_book_name(book_code)
    chp_info={'book_name':book_name,'book_abbr':book_abbr,'chp_num':1,'book_code':book_code}
    return render_template('words.html',title=title,books=books,words=words,chapters=chapters,chp_info=chp_info,this_year=common_info.this_year)

@main.route("/words/", methods=['GET', 'POST'])
def words():
    title = {'small': 'Bible words', 'big': '繁体中文和合本圣经','right':'search'}
    books = get_books.books
    words = get_books.get_words(1,1)
    chapters = get_books.get_chapters(1)
    book_abbr=get_books.get_book_abbr(1)
    book_name=get_books.get_book_name(1)
    chp_info={'book_name':book_name,'book_abbr':book_abbr,'chp_num':1,'book_code':1}
    return render_template('words.html',title=title,books=books,words=words,chapters=chapters,chp_info=chp_info,this_year=common_info.this_year)

@main.route("/search/", methods=['GET', 'POST'])
def search():
    books = get_books.books
    books_indexes=get_books.books_indexes
    key_word = request.form.get('key_word')
    search_results=search_bible.get_search_results(key_word,'cuv_t')
    num_of_results=len(search_results)
    title = {'small': 'Bible search', 'big': '经文查找','right':'search'}
    return render_template('search.html',title=title,books=books,search_results=search_results,key_word=key_word,num_of_results=num_of_results,books_indexes=books_indexes,this_year=common_info.this_year)