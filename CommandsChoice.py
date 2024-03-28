import views
import utility

commands = {'[A]dd', '[D]isplay', '[R]emove', '[S]earch', '[H]elp', '[Q]uit'}


def action_mapper(action: str):
    """call appropriate methods of DisplayBook class and BookTransaction depending on the action of the user"""
    display_object = views.DisplayBook()
    transfer_object = views.BookTransaction()
    if action == 'd':
        display_object.display()
    if action == 'h':
        [print(command) for command in commands]
        utility.get_user_input()
    if action == 's':
        query = input('Enter your search term, you can search by title or author\n:\t')
        display_object.search(query)
    if action == 'a':
        new_book_details = utility.book_details()
        transfer_object.add_book(new_book_details)
    if action == 'q':
        print('Thank You For Visiting UTAMU Library')
        exit()
    if action == 'r':
        utility.remove_book()
