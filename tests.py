from main import BooksCollector
import pytest

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('book_name', ['Я', 'Книга', 'КнигаКнигаКнигаКнигаКнигаКнигаКнигаКнига'])
    def test_add_new_book_40_range(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_45_words(self):
        collector = BooksCollector()
        collector.add_new_book('ОченьОченьОченьОченьОченьОченьОченьОченьOчень')
        assert len(collector.get_books_genre()) != 1

    def test_set_book_genre_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Крик')
        collector.set_book_genre('Крик', 'Ужасы')
        assert collector.get_books_genre()['Крик'] == 'Ужасы'

    def test_get_book_genre_by_name(self):
        collector = BooksCollector()
        collector.add_new_book('Крик')
        collector.set_book_genre('Крик', 'Ужасы')
        assert collector.get_book_genre('Крик') == 'Ужасы'

    def test_get_books_with_specific_genre_horror(self):
        collector = BooksCollector()
        collector.add_new_book('Крик')
        collector.set_book_genre('Крик', 'Ужасы')
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 1

    def test_get_books_genre_full(self):
        collector = BooksCollector()
        collector.add_new_book('Золушка')
        collector.add_new_book('Крик')
        collector.set_book_genre('Золушка', 'Мультфильмы')
        collector.set_book_genre('Крик', 'Ужасы')
        assert collector.get_books_genre() == {
            'Золушка': 'Мультфильмы',
            'Крик': 'Ужасы'
        }

    def test_get_books_for_children_comedy(self):
        collector = BooksCollector()
        collector.add_new_book('Один дома')
        collector.set_book_genre('Один дома', 'Комедии')
        assert 'Один дома' in collector.get_books_for_children()

    def test_add_book_in_favorites_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Титаник')
        collector.add_book_in_favorites('Титаник')
        assert 'Титаник' in collector.favorites

    def test_add_book_in_favorites_add_re_adding_book(self):
        collector = BooksCollector()
        collector.add_new_book('Титаник')
        collector.add_new_book('Титаник')
        collector.add_book_in_favorites('Титаник')
        collector.add_book_in_favorites('Титаник')
        assert len(collector.favorites) != 2

    def test_delete_book_from_favorites_book_in_list(self):
        collector = BooksCollector()
        collector.add_new_book('Титаник')
        collector.add_book_in_favorites('Титаник')
        collector.delete_book_from_favorites('Титаник')
        assert 'Титаник' not in collector.favorites


    def test_get_list_of_favorites_books_one_book_in_list(self):
        collector = BooksCollector()
        collector.add_new_book('Титаник')
        collector.add_book_in_favorites('Титаник')
        assert collector.get_list_of_favorites_books() == ['Титаник']







