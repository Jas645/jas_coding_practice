import json

books = []

def load_books():
    global books
    try:
        with open("books.json", "r") as f:
            books = json.load(f)
        print("Library loaded successfully.")
    except FileNotFoundError:
        books = []
        
def save_books():
    with open("books.json", "w") as f:
        json.dump(books, f)
    print("Library saved successfully!")


def get_book_data():
        if not books:
            print("No books in library.")
            return
        sorted_books = sorted(books, key=lambda book: book['Author'].split()[-1])
        for book in sorted_books:
            print(f"""
          Book: {book['Title']}
          Author: {book['Author']}
          Copies Available: {book['Copies Available']}
          """)
          
def add_book():
    new_book = input('Please add a book: ')
    for book in books:
        if new_book == book['Title']:
            book['Copies Available'] += 1
            print(f"One more copy of {book['Title']} available. Total copies: {book['Copies Available']}.")
            break
    else:
        new_author = input('Who is the author? ')
        new_copies = 1
        books.append({'Title': new_book, 
                      'Author': new_author, 
                      'Copies Available': new_copies
                      })
        print(f"{new_book} by {new_author} added. {new_copies} copy now available.")
        
def remove_book():
    removed_book = input("Which book would you like to remove? ")
    for book in books:
        if removed_book == book['Title']:
            book['Copies Available'] -= 1
            print(f"One copy of {book['Title']} removed. Total copies: {book['Copies Available']}.")
            
            if book['Copies Available'] == 0:
                books.remove(book)
                print(f"{book['Title']} completely removed from the library")
            return
        
    print("No book of that name is in the library. Returning to menu.")
    
    
def borrow_book():
    borrowed_book = input("Which book would you like to borrow? ")
    for book in books:
        if borrowed_book == book['Title']: 
            if book['Copies Available'] > 0:
                book['Copies Available'] -= 1
                print(f"One copy of {book['Title']} removed. Total copies: {book['Copies Available']}.")
            
            else:
                print(f"There are no available copies of {book['Title']}. Returning to menu")
                return
    print(f"{borrowed_book} is not in the library. Returning to menu.")
    
def library_menu():
    while True:
        print("""
              === Library Menu ===
              1. View Books
              2. Add or Return Book
              3. Remove Book
              4. Borrow Book
              5.Exit
              """)
        choice = input("Choose an option: ")
        
        if choice == "1":
            get_book_data()
        elif choice == '2':
            add_book()
        elif choice == '3':
            remove_book()
        elif choice == '4':
            borrow_book()
        elif choice == '5':
            print('Goodbye!')
            break
        else:
            print('Invalid. Please try again.')



load_books()

library_menu()

save_books()       
              
