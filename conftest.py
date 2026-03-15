import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

@pytest.fixture(params=['Книга','A' * 40,'Короткое название']) 
#Валидная длина названия книг (1-40 символов)
def valid_book_names(request):
    return request.param

@pytest.fixture(params=['','A' * 41,])
#Невалидная длина названия книг (1-41 символов)
def invalid_book_names(request):
    return request.param

@pytest.fixture #Коллектор с книгами и жанрами 
def collector_with_books_and_genres(collector):
    books = [
        ('Книга 1', 'Фантастика'),
        ('Книга 2', 'Ужасы'),
        ('Книга 3', 'Детективы'),
        ('Книга 4', 'Мультфильмы'),
        ('Книга 5', 'Комедии')
    ]
    for name, genre in books:
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    return collector

@pytest.fixture #Коллектор с книгами в избранном
def collector_with_favorites(collector_with_books_and_genres):
    collector_with_books_and_genres.add_book_in_favorites('Книга 1')
    collector_with_books_and_genres.add_book_in_favorites('Книга 3')
    return collector_with_books_and_genres