

1) test_add_new_book_name_too_long_result_not_add(): тест проверяет, что не добавляеться книга с именем более 42 символов;
   
2) test_book_genre_success_return_not_genre(): тест проверяет, что в добавленной книге отсутсвует жанр;

3) test_set_book_genre_success():тест проверяет добавление жанра в список по имени книги;

4) test_set_book_genre_book_not_exists():тест проверяет, если книга отсутсвует в списке, то жанр не добавляеться;

5) test_get_book_genre_existing_book():тест проверяет вывод жанра по имени книги;
            
6) test_get_books_with_specific_genre_success():тест проверяет вывод книг по жанру;        
    
7) test_get_books_genre_return_good_result_retern_list():тест проверяет вывод списка книг ввиде листа, по названию и жанру;

8) test_get_books_for_children_good_list_return_result тест проверяет добавления книг в список для детей;

9) test_get_books_for_children_bad_list_not_return(): тест проверяет отсутсвие добавления книг с жанрами
"Ужасы" и "Детективы" в список для детей;
                   
10) test_add_book_in_favorites_return_result_found() тест проверяет добавление книги в список "избранные";

11) test_add_book_in_favorites_return_result_notfound():тест проверяет отсутсвие не добавленой книги в списоке "избранные";

12) test_delete_book_in_favorites_return_result_not_in_list(): тест проверяет удаление книги из списка "избранные";

13) test_get_list_of_favorites_books_return_list() тест проверяет вывод списка книг из "избранных" 
