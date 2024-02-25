class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability_status = True  # True for available, False for borrowed

    def display_details(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nAvailability: {'Available' if self.availability_status else 'Borrowed'}")


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.books_borrowed = []

    def display_details(self):
        print(f"User ID: {self.user_id}\nName: {self.name}\nBooks Borrowed: {', '.join([book.title for book in self.books_borrowed])}")

    def borrow_book(self, book):
        if book.availability_status:
            self.books_borrowed.append(book)
            book.availability_status = False
            print(f"{self.name} has successfully borrowed {book.title}.")
        else:
            print(f"Sorry, {book.title} is currently not available.")


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.transactions = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def register_user(self, user):
        self.users.append(user)
        print(f"User '{user.name}' registered in the library.")

    def handle_transaction(self, user, book, action):
        transaction = Transaction(user, book, action)
        self.transactions.append(transaction)
        if action == "borrow":
            user.borrow_book(book)
        elif action == "return":
            user.books_borrowed.remove(book)
            book.availability_status = True
            print(f"{user.name} has successfully returned {book.title}.")

    def generate_transaction_report(self):
        if not self.transactions:
            print("No transactions to report.")
        else:
            print("\nTransaction Report:")
            for transaction in self.transactions:
                print(f"{transaction.user.name} {transaction.action}ed {transaction.book.title} on {transaction.timestamp}")
            print("End of Transaction Report")


class Transaction:
    def __init__(self, user, book, action):
        import datetime
        self.user = user
        self.book = book
        self.action = action
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def main():
    library = Library()

    while True:
        print("\nOptions:")
        print("1. Add a book")
        print("2. Register a user")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. View user details")
        print("6. View book details")
        print("7. Generate Transaction Report")
        print("8. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)

        elif choice == "2":
            user_id = int(input("Enter user ID: "))
            name = input("Enter user name: ")
            user = User(user_id, name)
            library.register_user(user)

        elif choice == "3":
            user_id = int(input("Enter user ID: "))
            book_title = input("Enter book title: ")

            # Find the user and book objects
            user = next((u for u in library.users if u.user_id == user_id), None)
            book = next((b for b in library.books if b.title == book_title), None)

            if user and book:
                library.handle_transaction(user, book, "borrow")
            else:
                print("User or book not found.")

        elif choice == "4":
            user_id = int(input("Enter user ID: "))
            book_title = input("Enter book title: ")

            # Find the user and book objects
            user = next((u for u in library.users if u.user_id == user_id), None)
            book = next((b for b in library.books if b.title == book_title), None)

            if user and book:
                library.handle_transaction(user, book, "return")
            else:
                print("User or book not found.")

        elif choice == "5":
            user_id = int(input("Enter user ID: "))
            user = next((u for u in library.users if u.user_id == user_id), None)

            if user:
                user.display_details()
            else:
                print("User not found.")

        elif choice == "6":
            book_title = input("Enter book title: ")
            book = next((b for b in library.books if b.title == book_title), None)

            if book:
                book.display_details()
            else:
                print("Book not found.")

        elif choice == "7":
            library.generate_transaction_report()

        elif choice == "8":
            print("Exiting the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
if __name__ == "__main__":
    main()
