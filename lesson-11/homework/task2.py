import sqlite3

def create_library_db():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()

    # Create table and insert data
    cur.execute("CREATE TABLE IF NOT EXISTS Books (Title TEXT, Author TEXT, Year_Published INTEGER, Genre TEXT)")
    cur.executemany("INSERT INTO Books VALUES (?, ?, ?, ?)", [
        ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
        ("1984", "George Orwell", 1949, "Dystopian"),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
    ])

    # Update year of 1984
    cur.execute("UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'")

    # Get Dystopian books
    cur.execute("SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'")
    print("Dystopian Books:", cur.fetchall())

    # Remove books published before 1950
    cur.execute("DELETE FROM Books WHERE Year_Published < 1950")

    # Add Rating column and update data
    cur.execute("ALTER TABLE Books ADD COLUMN Rating REAL")
    cur.executemany("UPDATE Books SET Rating = ? WHERE Title = ?", [
        (4.8, "To Kill a Mockingbird"),
        (4.7, "1984"),
        (4.5, "The Great Gatsby")
    ])

    # Show sorted books
    cur.execute("SELECT * FROM Books ORDER BY Year_Published ASC")
    print("Sorted Books:", cur.fetchall())

    conn.commit()
    conn.close()

create_library_db()
