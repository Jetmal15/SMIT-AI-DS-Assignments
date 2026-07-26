class Book:
    def __init__(self, title, author, book_id, price, quantity):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.price = price
        self.quantity = quantity

class LibraryManagement:
    def __init__(self):
        self.book_list = []

    # Add Book
    def add_book(self):
        try:
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            book_id = input("Enter Book ID: ")
            price = float(input("Enter Book Price: "))
            quantity = int(input("Enter Quantity: "))

            book = Book(title, author, book_id, price, quantity)
            self.book_list.append(book)

            print("\n----- Book Added Successfully -----\n")

        except ValueError:
            print("Invalid input! Please enter correct values.\n")

    # View All Books
    def view_all_books(self):
        if len(self.book_list) == 0:
            print("\nNo books found.\n")
            return

        print("\n------ Book List ------")

        for book in self.book_list:
            print(f"Book ID : {book.book_id}")
            print(f"Title   : {book.title}")
            print(f"Author  : {book.author}")
            print(f"Price   : {book.price}")
            print(f"Quantity: {book.quantity}")
            print("*" * 30)

    # Search Book by ID
    def search_book(self):
        book_id = input("Enter Book ID: ")

        for book in self.book_list:
            if book.book_id == book_id:
                print("\nBook Found")
                print(f"Book ID : {book.book_id}")
                print(f"Title   : {book.title}")
                print(f"Author  : {book.author}")
                print(f"Price   : {book.price}")
                print(f"Quantity: {book.quantity}")
                return

        print("Book not found.")

    # Update Book
    def update_book(self):
        book_id = input("Enter Book ID to Update: ")

        for book in self.book_list:
            if book.book_id == book_id:

                print("\nEnter New Details")

                book.title = input("Enter New Title: ")
                book.author = input("Enter New Author: ")
                book.price = float(input("Enter New Price: "))
                book.quantity = int(input("Enter New Quantity: "))

                print("\nBook Updated Successfully.\n")
                return

        print("Book not found.")

    # Delete Book
    def delete_book(self):
        book_id = input("Enter Book ID to Delete: ")

        for book in self.book_list:
            if book.book_id == book_id:
                self.book_list.remove(book)
                print("\nBook Deleted Successfully.\n")
                return

        print("Book not found.")


# Object
my_library = LibraryManagement()


# Menu
while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Search Book by ID")
    print("0. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            my_library.add_book()

        elif choice == 2:
            my_library.view_all_books()

        elif choice == 3:
            my_library.update_book()

        elif choice == 4:
            my_library.delete_book()

        elif choice == 5:
            my_library.search_book()

        elif choice == 0:
            print("\nThank you!")
            break

        else:
            print("Invalid Choice.")

    except ValueError:
        print("Please enter a valid number.")