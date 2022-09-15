import pytest
from app import check_document_existance, get_doc_owner_name, get_all_doc_owners_names, remove_doc_from_shelf, add_new_shelf, append_doc_to_shelf, delete_doc, get_doc_shelf, move_doc_to_shelf, show_document_info, show_all_docs_info, add_new_doc, documents

# def test_check_document_existance():
#     check = "10006"
#     result = check_document_existance(check)
#     etalon = True
#     assert result == etalon

# def test_get_doc_owner_name():
#     check = "10006"
#     result = get_doc_owner_name(check)
#     etalon = "Аристарх Павлов"
#     assert  result == etalon

# def test_get_all_doc_owners_names():
#     result = get_all_doc_owners_names()
#     etalon = {"Василий Гупкин", "Геннадий Покемонов", "Аристарх Павлов"}
#     assert result == etalon

# def test_remove_doc_from_shelf():
#     check = "10006"
#     result = remove_doc_from_shelf(check)
#     etalon = {
#     '1': ['2207 876234', '11-2', '5455 028765'],
#     '2': [],
#     '3': []
# }
#     assert result == etalon

# def test_add_new_shelf():
#     check = '4'
#     result = add_new_shelf(check)
#     etalon = '4',True
#     assert result == etalon

# def test_append_doc_to_shelf():
#     check1 = '10006'
#     check2 = '1'
#     result = append_doc_to_shelf(check1, check2)
#     etalon = {
#         '1': ['2207 876234', '11-2', '5455 028765', '10006'],
#         '2': ['10006'],
#         '3': []
#     }
#     assert result == etalon

# def test_delete_doc():
#     check = '10006'
#     result = delete_doc(check)
#     etalon = check, True
#     assert result == etalon

# def test_get_doc_shelf():
#     check = '10006'
#     result = get_doc_shelf(check)
#     etalon = '2'
#     assert result == etalon

# def test_move_doc_to_shelf():
#     check1 = '10006'
#     check2 = '1'
#     result = move_doc_to_shelf(check1,check2)
#     etalon = {
#             '1': ['2207 876234', '11-2', '5455 028765', '10006'],
#             '2': [],
#             '3': []
#         }
#     assert result == etalon

# def test_show_document_info():
#     check = documents[1]
#     result = show_document_info(check)
#     etalon = 'invoice "11-2" "Геннадий Покемонов"'
#     assert result == etalon

# def test_show_all_docs_info():
#     result = show_all_docs_info()
#     etalon = documents
#     assert result == etalon

# def test_add_new_doc():
#     check_num = '1111'
#     check_type = 'pass'
#     check_name = 'Дора'
#     check_shelf = '3'
#     result = add_new_doc(check_num, check_type, check_name, check_shelf)
#     etalon = '3'
#     assert result == etalon


