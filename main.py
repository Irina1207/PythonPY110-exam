from faker import Faker
import random
import json
from conf import MODEL
# fixme разбить импорт по PEP8
# fixme аннотация типов

OUTPUT_FILE = "strjson.json"


def main():
    gen = my_gen()
    list_book = []
    for _ in range(1, 10):  # fixme list comprehension
        python_object = next(gen) # mext от gen
        print(python_object)
        list_book.append(python_object)
    to_json_file(list_book)

def my_gen(pk=1):
    """ функция генератор"""
    while True:
        yield {
            "model": MODEL,
            "pk": 1,  # fixme статический pk
            "fields": {
                "title": get_books(),
                "year": get_year(),
                "pages": get_pages(),
                "isbn13": get_isbn13(),
                "rating": get_rating(),
                "price": get_price(),
                "author": [
                    get_author(),
                    get_author()
                ]
            }
        }
        pk += 1
        print(pk)



def get_books():
    """ функция считывающая список книг"""
    f = open('books.txt', 'r', encoding='utf8')
    book = random.choice(f.readlines())      # str  # fixme очистить от \n
    #f.close()
    return book

def get_year():
    """функция выбирающая случаный год"""
    year = random.randint(1900, 2021)        # int
    return year

def get_pages():
    """функция выбриющая случайную страницу"""
    page = random.randint(1, 1000)           #int
    return page

def get_isbn13():
    """функия выбирающая случайный код isbn13"""
    fake = Faker()
    Faker.seed(0)
    isbn13 = fake.isbn13()                   #str
    return isbn13

def get_rating():
    """функция выбирающая рейтинг"""
    rating = random.uniform(0, 6)           #float
    return rating

def get_price():
    """функция выбирающая цену"""
    price = random.uniform(0, 5000)         #float
    return price

def get_author():
    """функция выбирающая автора"""
    fake = Faker()
    list_ = []                              #list
    for _ in range(random.randint(1,3)):
        list_.append(fake.name())
    return list_

def to_json_file(python_object):
    """функция записывающая в json файл"""
    with open(OUTPUT_FILE, "w") as f:
        json.dump(python_object, f, indent=4, ensure_ascii=False)
        # print(json.dump(python_object, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()
# ссылка на задание https://docs.google.com/document/d/1xLJWOT_luNtUEWkM8WE4AQDiN_vLWV46Qn09jXNLCbc/edit#

