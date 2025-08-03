from book import Book
from users import Librarian, Member, User


class Library:
    def __init__(self, name) -> None:
        self.name = name
        self.books: list[Book] = []
        self.users: list[User] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def register_user(self, user: User) -> None:
        self.users.append(user)

    def find_book(self, title: str) -> Book | None:
        for book in self.books:
            if title == book.title:
                return book
        return None


new_book = Book("Deep dive into design patterns", "John Doe", "10293dsa9834")
new_user = Member("Leykun")

new_library = Library("New_Library")

new_library.add_book(new_book)
