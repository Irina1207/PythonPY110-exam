import random
import json
from typing import Iterator

from faker import Faker  # pip

from conf import MODEL  # local module
# fixme разбить импорт по PEP8  v
# fixme аннотация типов V

OUTPUT_FILE = "strjson.json"


def main():
    gen = my_gen()
    list_book = []
    for _ in range(1, 10):
        python_object = next(gen)
        print(python_object)
        list_book.append(python_object)
    to_json_file(list_book)


def my_gen(pk=1) -> Iterator[dict]:
    """ функция генератор"""
    while True:
        yield {
            "model": MODEL,
            "pk": pk,  # fixme статический pk V
            "fields": {
                "title": get_books(),
                "year": get_year(),
                "pages": get_pages(),
                "isbn13": get_isbn13(),
                "rating": get_rating(),
                "price": get_price(),
                "author": get_author(),
            }
        }
        pk += 1
        print(pk)


def get_books() -> str:
    """ функция считывающая список книг"""
    book: str
    with open('books.txt', 'r', encoding='utf8') as f:
        book = random.choice(f.readlines()).rstrip()
        return book


def get_year() -> int:
    """функция выбирающая случаный год"""
    # year: int
    year: int = random.randint(1900, 2021)        # int
    return year

def get_pages() -> int:
    """функция выбриющая случайную страницу"""
    page: int
    page = random.randint(1, 1000)           #int
    return page

def get_isbn13() -> str:
    """функия выбирающая случайный код isbn13"""
    isbn13: str
    fake = Faker()
    Faker.seed(0)
    isbn13 = fake.isbn13()                   #str
    return isbn13

def get_rating() -> float:
    """функция выбирающая рейтинг"""
    rating: float
    rating = random.uniform(0, 6)           #float
    return rating

def get_price() -> float:
    """функция выбирающая цену"""
    price: float
    price = random.uniform(0, 5000)         #float
    return price

def get_author() -> list:
    """функция выбирающая автора"""
    list_: list
    fake = Faker()
    list_ = []                              #list
    for _ in range(random.randint(1,3)):  # fixme list comprehension
        list_.append(fake.name())
    return list_

def to_json_file(python_object) -> None:
    """функция записывающая в json файл"""
    with open(OUTPUT_FILE, "w") as f:
        json.dump(python_object, f, indent=4, ensure_ascii=False)
        # print(json.dump(python_object, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()
# ссылка на задание https://docs.google.com/document/d/1xLJWOT_luNtUEWkM8WE4AQDiN_vLWV46Qn09jXNLCbc/edit#

