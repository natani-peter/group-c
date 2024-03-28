from CommandsChoice import action_mapper
import views

commands = ('[A]dd', '[D]isplay', '[R]emove', '[S]earch', '[H]elp', '[Q]uit')
my_commands = set(command[1].lower() for command in commands)


def welcome() -> str:
    """Display a welcoming message"""
    return 'WELCOME TO UTAMU LIBRARY\nYou can type "H" to see available commands\nYou can use the first letters only'


def get_user_input(my_prompt='Enter Your Command:\t'):
    """get the user commands"""
    while True:
        user_command = input(my_prompt).lower()
        if user_command[0] in my_commands:
            action_mapper(user_command[0])
            return
        else:
            print('Unknown Command. Please Check Your Spellings')


def book_details():
    """Collect all details of the book you want to add to the library"""
    title = input('Enter Book title:    ')
    author_ids = views.DisplayBook().show_all_author()
    author_detail = views.DisplayBook.handle_missing_author(title)
    if not author_details:
        while True:
            try:
                author_id = int(input(":    "))
                if author_id in author_ids:
                    break
                else:
                    print('Please select a valid ID')
            except ValueError:
                print('Enter a valid digit ID')
    else:
        author_id = views.BookTransaction().add_author(author_detail)
    genre = input('Enter Book genre:    ')
    year = input('Enter publication year of the book:   ')

    return {'id': author_id, 'title': title, 'genre': genre, 'year': year}


def author_details():
    f_name = input('Enter the author first name: ')
    l_name = input('Enter the author last name: ')
    email = input('Enter the author email: ')
    nationality = input('Enter the author\'s nationality: ')
    gender = input('Enter author\'s gender: ')
    birth_day = input('Enter the author birthday like 01/jan/1970: ')
    answer = input('Is the author dead? Y/N ').lower()
    while True:
        if answer[0] == 'y':
            death_day = input('Enter author death day like 01/jan/1970: ')
            break
        elif answer[0] == 'n':
            death_day = ''
            break
        else:
            print('make a correct choice please! ')

    return {'a': f_name, 'b': l_name, 'c': email, 'd': nationality, 'e': gender, 'f': birth_day, 'g': death_day}


def remove_book():
    """select a book to remove using its ID"""
    book_ids = views.DisplayBook().display()
    print('Please Select the Book you want to remove using its ID')
    while True:
        try:
            book_id = int(input(":    "))
            if book_id in book_ids:
                break
            else:
                print('Please select a valid ID')
        except ValueError:
            print('Enter a valid digit ID')
    consent = input('Are you sure you want to remove this book ? Y/N: ').lower()
    if consent[0] == 'y':
        views.BookTransaction().remove_book(book_id)
    else:
        print('Book removal has been aborted.')
