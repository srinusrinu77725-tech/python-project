# ---- Library Management System ----

library = []  # List to store books

def show_menu():
    print("\n----- LIBRARY MENU -----")
    print("1. Add a new book")
    print("2. View all books")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Search book")
    print("6. Exit")

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    
    # Each book is a dictionary
    library.append({
        "title": title,
        "author": author,
        "available": True
    })

    print("Book added successfully!")

def view_books():
    if len(library) == 0:
        print("No books available.")
    else:
        print("\n----- All Books -----")
        for i, book in enumerate(library):
            status = "Available" if book["available"] else "Not Available"
            print(f"{i+1}. {book['title']} by {book['author']} - {status}")

def borrow_book():
    view_books()
    if len(library) > 0:
        num = int(input("Enter book number to borrow: "))
        if 1 <= num <= len(library):
            if library[num-1]["available"]:
                library[num-1]["available"] = False
                print("Book borrowed successfully!")
            else:
                print("Sorry, book is already borrowed.")
        else:
            print("Invalid book number.")

def return_book():
    view_books()
    if len(library) > 0:
        num = int(input("Enter book number to return: "))
        if 1 <= num <= len(library):
            if library[num-1]["available"] == False:
                library[num-1]["available"] = True
                print("Book returned successfully!")
            else:
                print("This book is already available in library!")
        else:
            print("Invalid book number.")

def search_book():
    keyword = input("Enter title or author to search: ").lower()
    
    print("\nSearch Results:")
    found = False

    for book in library:
        if keyword in book["title"].lower() or keyword in book["author"].lower():
            status = "Available" if book["available"] else "Not Available"
            print(f"{book['title']} by {book['author']} - {status}")
            found = True

    if not found:
        print("No books found with that keyword.")

# ---- MAIN PROGRAM ----
while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        borrow_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        search_book()
    elif choice == "6":
        print("Exiting Library. Goodbye!")
        break
    else:
        print("Invalid choice! Please choose from 1–6.")