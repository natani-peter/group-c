import models
from database import session


class DisplayBook:
    """deals with any to do with displaying data"""

    @staticmethod
    def display():
        """show that available books in the library that are not removed"""
        books = session.query(models.Book).filter(models.Book.state).all()
        if books:
            print('ID\tTITLE\t\tAUTHOR\t\t\tPUBLICATION YEAR')
        [print(f"{book.id}\t{book.title}\t\t{book.authors}{(22 - len(book.authors)) * ' '}{book.publication_year}") for
         book in sorted(books)]
        return set([my_book.id for my_book in books])

    @staticmethod
    def search(query: str):
        """search for books in the library using its title and its author"""
        book_title = session.query(models.Book).filter(models.Book.title.ilike(f'%{query.lower()}%')).all()
        book_f_author = session.query(models.Book).join(models.Author).filter(
            models.Author.f_name.ilike(f'%{query.lower()}%'), models.Book.state).all()
        book_l_author = session.query(models.Book).join(models.Author).filter(
            models.Author.l_name.ilike(f'%{query.lower()}%'), models.Book.state).all()

        wanted_books = set(book_title + book_f_author + book_l_author)
        if wanted_books:
            print('ID\tTITLE\t\tAUTHOR\t\t\tPUBLICATION YEAR')
            return [print(
                f"{book.id}\t{book.title}\t\t{book.authors}{(22 - len(book.authors)) * ' '}{book.publication_year}") for
                    book in
                    sorted(wanted_books)]
        else:
            print('No books with such title or author')
            return

    @staticmethod
    def show_all_author():
        """show available authors during new book addition"""
        authors = session.query(models.Author).all()
        print('List of available Authors With Their IDs')
        print('ID\t|\tName\n============================================================')
        [print(f"{author.id}\t|\t{author}") for author in authors]
        print('============================================================')
        return set([int(auth.id) for auth in authors])

    @staticmethod
    def handle_missing_author(title):
        import utility
        """Handle cases where the user tries to add book whose author is not in our library data"""

        while True:
            answer = input(f'Is the author of {title} listed? Y/N:  ').lower()
            if answer[0] == 'y':
                print('Please select that author using the ID')
                break
            elif answer[0] == 'n':
                print('Lets us Add that author !')
                author_details = utility.author_details()
                return author_details
            else:
                print('please make a proper choice'.title())


class BookTransaction:
    """Handle any anything to do with changing the database"""

    @staticmethod
    def add_book(book_details: dict):
        """add a book to the library"""
        try:
            author_id, title, genre, year = book_details.values()
            new_book = models.Book(author_id=author_id, title=title, genre=genre, publication_year=year)
            session.add(new_book)
            session.commit()
            print('Book successfully added')
        except Exception as e:
            print('Book was not added because Error occurred')
            return e

    @staticmethod
    def add_author(author_details: dict):
        """add and return an author"""
        try:
            f_name, l_name, email, nationality, gender, birth_day, death_day = author_details.values()
            new_author = models.Author(
                f_name=f_name,
                l_name=l_name,
                email=email,
                nationality=nationality,
                gender=gender,
                birth_day=birth_day,
                death_day=death_day
            )
            session.add(new_author)
            session.commit()
            session.refresh(new_author)
            print(f'{new_author} was created')
            return new_author.id
        except Exception as e:
            print('Author was not created due to an error')
            return e

    @staticmethod
    def remove_book(book_id):
        """remove books from the library by changing their state to 0"""
        wanted_book = session.query(models.Book).filter(models.Book.id == book_id).first()
        wanted_book.state = 0
        session.commit()
        print(f'The Book " {wanted_book} " has Been Removed')
