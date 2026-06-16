import pytest
from books_collector import BooksCollector

class TestBooksbooks_collector:
    
    def ttest_add_new_book_name_too_long_result_not_add(self, books_collector):
        long_name = "А" * 42
        books_collector.add_new_book(long_name)
        assert long_name not in books_collector.books_genre

       
    def test_book_genre_success_return_not_genre(self, books_collector):
        books_collector.add_new_book("Сияние")
        assert books_collector.books_genre["Сияние"] == ""

    @pytest.mark.parametrize("book_name, gener",[["Винни-Пух", "Мультфильмы"], ["Сияние", "Ужасы"]])
    def test_set_book_genre_success(self, books_collector, book_name, gener ):
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, gener)
        assert books_collector.books_genre[book_name] == gener
    
    
    def test_set_book_genre_book_not_exists(self, books_collector):
        books_collector.set_book_genre("Несуществующая книга", "Фантастика")
        assert "Несуществующая книга" not in books_collector.books_genre
    
    
    @pytest.mark.parametrize("book_name, gener",[["Винни-Пух", "Мультфильмы"], ["Сияние", "Ужасы"]])
    def test_get_book_genre_existing_book(self, books_collector, book_name, gener):
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, gener)
        assert books_collector.get_book_genre(book_name) == gener
        
    
    def test_get_books_with_specific_genre_success(self, books_collector, books_collector_add, books_collector_genre):        
        result = books_collector.get_books_with_specific_genre("Фантастика")
        assert result == ["Дюна"]
    
    
    def test_get_books_genre_return_good_result_retern_list(self, books_collector, books_collector_add, books_collector_genre):
        result = books_collector.get_books_genre()
        assert result == { "Дюна":'Фантастика', "Трое в лодке, не считая собаки":"Комедии", "Винни-Пух":"Мультфильмы","Сияние":"Ужасы"}
    
        
    @pytest.mark.parametrize("book_name, gener",[["Винни-Пух", "Мультфильмы"], ["Трое в лодке, не считая собаки", "Комедии"]]) 
    def test_get_books_for_children_good_list_return_result(self, books_collector, book_name, gener ):        
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, gener)
        books_for_children = books_collector.get_books_for_children()
        assert book_name in books_for_children
        
    @pytest.mark.parametrize("book_name, gener",[["Убийство в Восточном экспрессе", "Детективы"], ["Сияние", "Ужасы"]])  
    def test_get_books_for_children_bad_list_not_return(self, books_collector, book_name, gener ):        
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, gener)
        books_for_children = books_collector.get_books_for_children()
        assert book_name not in books_for_children
                   
    
    def test_add_book_in_favorites_return_result_found(self, books_collector, books_collector_add):
        name = "Винни-Пух"
        books_collector.add_book_in_favorites(name)
        assert name in books_collector.favorites
    
        
    def test_add_book_in_favorites_return_result_notfound(self, books_collector, books_collector_add):
        name = "Винни-Пух"
        books_collector.add_book_in_favorites("Дюна")
        assert name not in books_collector.favorites
        
        
    def test_delete_book_in_favorites_return_bad_result(self, books_collector, books_collector_add):
        name = "Винни-Пух"
        books_collector.add_book_in_favorites(name)
        books_collector.delete_book_from_favorites(name)
        assert name not in books_collector.favorites
        
        
    def test_get_list_of_favorites_books_result(self, books_collector, books_collector_add):
        books_collector.add_book_in_favorites("Дюна")
        books_collector.add_book_in_favorites("Винни-Пух")
        result = books_collector.get_list_of_favorites_books()
        assert result == ["Дюна", "Винни-Пух"]
  