import pytest

from books_collector import BooksCollector

@pytest.fixture
def books_collector():
        return BooksCollector()

@pytest.fixture
def books_collector_add(books_collector):
        books_collector.add_new_book("Дюна")
        books_collector.add_new_book("Трое в лодке, не считая собаки")
        books_collector.add_new_book("Винни-Пух")
        books_collector.add_new_book("Сияние")
        
@pytest.fixture 
def books_collector_genre(books_collector):
        books_collector.set_book_genre("Дюна", "Фантастика")
        books_collector.set_book_genre("Трое в лодке, не считая собаки", "Комедии")
        books_collector.set_book_genre("Винни-Пух" ,"Мультфильмы")
        books_collector.set_book_genre("Сияние","Ужасы")