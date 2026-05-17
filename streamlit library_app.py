# class Library:

#     def __init__(self):
#         self.books = {}
#         self.issued_books = {}

#     def add_book(self, name, quantity):

#         if name in self.books:
#             self.books[name] += quantity
#         else:
#             self.books[name] = quantity

#         print(f"{name} added successfully. Total copies: {self.books[name]}")


#     def issue_book(self, student, book):

#         if book in self.books and self.books[book] > 0:

#             self.books[book] -= 1
#             self.issued_books[student] = book

#             print(f"Book '{book}' issued to {student}")

#         else:
#             print(f"Sorry, '{book}' is not available")


#     def return_book(self, student):

#         if student in self.issued_books:

#             book = self.issued_books[student]
#             self.books[book] += 1

#             del self.issued_books[student]

#             print(f"{student} returned '{book}' successfully")

#         else:
#             print("No record found for this student")


#     def show_books(self):

#         print("\nAvailable Books in Library")

#         for book, qty in self.books.items():
#             print(f"{book} | Quantity: {qty}")


#     def show_issued_books(self):

#         print("\nIssued Books")

#         if not self.issued_books:
#             print("No books issued")

#         for student, book in self.issued_books.items():
#             print(f"{student} → {book}")


# library = Library()

# while True:

#     print("\n------ Library Menu ------")
#     print("1 Add Book")
#     print("2 Issue Book")
#     print("3 Return Book")
#     print("4 Show Available Books")
#     print("5 Show Issued Books")
#     print("6 Exit")

#     choice = input("Enter choice: ")

#     if choice == "1":

#         name = input("Enter book name: ")
#         qty = int(input("Enter quantity: "))
#         library.add_book(name, qty)

#     elif choice == "2":

#         student = input("Enter student name: ")
#         book = input("Enter book name: ")
#         library.issue_book(student, book)

#     elif choice == "3":

#         student = input("Enter student name: ")
#         library.return_book(student)

#     elif choice == "4":

#         library.show_books()

#     elif choice == "5":

#         library.show_issued_books()

#     elif choice == "6":

#         print("Exiting library system")
#         break

#     else:
#         print("Invalid choice")

import streamlit as st

# -------------------------------
# Library Class
# -------------------------------
class Library:

    def __init__(self):
        if "books" not in st.session_state:
            st.session_state.books = {}

        if "issued_books" not in st.session_state:
            st.session_state.issued_books = {}

    def add_book(self, name, quantity):

        books = st.session_state.books

        if name in books:
            books[name] += quantity
        else:
            books[name] = quantity

        st.success(f"{name} added successfully. Total copies: {books[name]}")


    def issue_book(self, student, book):

        books = st.session_state.books
        issued_books = st.session_state.issued_books

        if book in books and books[book] > 0:

            books[book] -= 1
            issued_books[student] = book

            st.success(f"Book '{book}' issued to {student}")

        else:
            st.error(f"Sorry, '{book}' is not available")


    def return_book(self, student):

        books = st.session_state.books
        issued_books = st.session_state.issued_books

        if student in issued_books:

            book = issued_books[student]
            books[book] += 1

            del issued_books[student]

            st.success(f"{student} returned '{book}' successfully")

        else:
            st.warning("No record found for this student")


    def show_books(self):

        books = st.session_state.books

        st.subheader("📚 Available Books")

        if not books:
            st.info("No books available in library")
        else:
            for book, qty in books.items():
                st.write(f"**{book}** | Quantity: {qty}")


    def show_issued_books(self):

        issued_books = st.session_state.issued_books

        st.subheader("📖 Issued Books")

        if not issued_books:
            st.info("No books issued")
        else:
            for student, book in issued_books.items():
                st.write(f"{student} → {book}")


# -------------------------------
# Streamlit UI
# -------------------------------

st.title("📚 Library Management System")

library = Library()

menu = st.sidebar.selectbox(
    "Choose Action",
    ["Add Book", "Issue Book", "Return Book", "Show Books", "Issued Books"]
)

# -------------------------------
# Add Book
# -------------------------------

if menu == "Add Book":

    st.header("Add New Book")

    name = st.text_input("Book Name")
    qty = st.number_input("Quantity", min_value=1, step=1)

    if st.button("Add Book"):
        library.add_book(name, qty)


# -------------------------------
# Issue Book
# -------------------------------

elif menu == "Issue Book":

    st.header("Issue Book")

    student = st.text_input("Student Name")
    book = st.text_input("Book Name")

    if st.button("Issue Book"):
        library.issue_book(student, book)


# -------------------------------
# Return Book
# -------------------------------

elif menu == "Return Book":

    st.header("Return Book")

    student = st.text_input("Student Name")

    if st.button("Return Book"):
        library.return_book(student)


# -------------------------------
# Show Books
# -------------------------------

elif menu == "Show Books":

    library.show_books()


# -------------------------------
# Show Issued Books
# -------------------------------

elif menu == "Issued Books":

    library.show_issued_books()
