import pytest
from main import BooksCollector

class TestBooksCollector:

    # тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # Тест на добавление книги с допустимой длиной названия
    def test_add_new_book_valid_length(self, collector, valid_book_names):
        collector.add_new_book(valid_book_names)
        assert valid_book_names in collector.get_books_genre()
        assert collector.get_book_genre(valid_book_names) == ''

    # Тест на добавление книги с невалидной длиной названия
    def test_add_new_book_invalid_length(self, collector, invalid_book_names):
        collector.add_new_book(invalid_book_names)
        assert invalid_book_names not in collector.get_books_genre()

    # Тест на установку жанра книге
    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_valid_genre(self, genre):
        collector = BooksCollector()
        book_name = 'Книга'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    # Тест на установку несуществующего жанра
    @pytest.mark.parametrize('genre', ['Роман', 'Триллер', ''])
    def test_set_book_genre_invalid_genre(self, genre):
        collector = BooksCollector()
        book_name = 'Книга'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == ''

    # Тест на получение жанра книги
    def test_get_book_genre(self, collector):
        book_name = 'Книга'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Фантастика')
        genre = collector.get_book_genre(book_name)
        assert genre == 'Фантастика'

    # Тест на получение всего словаря books_genre
    def test_get_books_genre_direct(self):
        collector = BooksCollector()
    
    # добавляем книги
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
    
    # устанавливаем жанры
        collector.set_book_genre('Книга 1', 'Фантастика')
        collector.set_book_genre('Книга 2', 'Ужасы')
    
    # получаем словарь
        books_genre_dict = collector.get_books_genre()
    
    # проверяем
        assert len(books_genre_dict) == 2
        assert books_genre_dict == {
        'Книга 1': 'Фантастика',
        'Книга 2': 'Ужасы'}

    # Тест на получение списка книг с определенным жанром
    def test_get_books_with_specific_genre(self, collector_with_books_and_genres):
        fantastic_books = collector_with_books_and_genres.get_books_with_specific_genre('Фантастика')
        assert len(fantastic_books) == 1
        assert 'Книга 1' in fantastic_books
        assert 'Книга 2' not in fantastic_books

    # Тест на получение книг для детей
    def test_get_books_for_children(self, collector_with_books_and_genres):
        children_books = collector_with_books_and_genres.get_books_for_children()
        assert len(children_books) == 3  # Фантастика, Мультфильмы, Комедии
        assert 'Книга 1' in children_books
        assert 'Книга 4' in children_books
        assert 'Книга 5' in children_books
        assert 'Книга 2' not in children_books
        assert 'Книга 3' not in children_books

    # Тест на добавление книги в избранное
    def test_add_book_in_favorites(self, collector_with_books_and_genres):
        collector_with_books_and_genres.add_book_in_favorites('Книга 2')
        assert 'Книга 2' in collector_with_books_and_genres.get_list_of_favorites_books()
        assert len(collector_with_books_and_genres.get_list_of_favorites_books()) == 1

    # Тест на невозможность добавления дубликата в избранное
    def test_add_duplicate_book_in_favorites(self, collector_with_books_and_genres):
        collector_with_books_and_genres.add_book_in_favorites('Книга 1')
        collector_with_books_and_genres.add_book_in_favorites('Книга 1')
        assert len(collector_with_books_and_genres.get_list_of_favorites_books()) == 1

    # Тест на удаление книги из избранного
    def test_delete_book_from_favorites(self, collector_with_favorites):
        collector_with_favorites.delete_book_from_favorites('Книга 1')
        assert 'Книга 1' not in collector_with_favorites.get_list_of_favorites_books()
        assert len(collector_with_favorites.get_list_of_favorites_books()) == 1

    # Тест на получение списка избранных книг
    def test_get_list_of_favorites_books(self, collector_with_favorites):
        favorites = collector_with_favorites.get_list_of_favorites_books()
        assert isinstance(favorites, list)
        assert len(favorites) == 2
        assert 'Книга 1' in favorites
        assert 'Книга 3' in favorites