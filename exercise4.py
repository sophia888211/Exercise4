import sqlite3
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Create the Books table
cursor.execute('''CREATE TABLE IF NOT EXISTS Books (
 BookID INTEGER PRIMARY KEY,
 Title TEXT,
 Author TEXT,
 ISBN TEXT,
 Status TEXT)''')

# Create the Users table
cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
 UserID INTEGER PRIMARY KEY,
 Name TEXT,
 Email TEXT)''')

# Create the Reservations table
cursor.execute('''CREATE TABLE IF NOT EXISTS Reservations (
 ReservationID INTEGER PRIMARY KEY,
 BookID INTEGER,
 UserID INTEGER,
 ReservationDate TEXT,
 FOREIGN KEY (BookID) REFERENCES Books(BookID),
 FOREIGN KEY (UserID) REFERENCES Users(UserID))''')

# Function to add a new book to the database
def add_book():
 title = input("Enter the title of the book: ")
 author = input("Enter the author of the book: ")
 isbn = input("Enter the ISBN of the book: ")
