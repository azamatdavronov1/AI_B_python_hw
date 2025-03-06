import sqlite3

def create_roster_db():
    conn = sqlite3.connect("roster.db")
    cur = conn.cursor()

    # Create table and insert data
    cur.execute("CREATE TABLE IF NOT EXISTS Roster (Name TEXT, Species TEXT, Age INTEGER)")
    cur.executemany("INSERT INTO Roster VALUES (?, ?, ?)", [
        ("Benjamin Sisko", "Human", 40),
        ("Jadzia Dax", "Trill", 300),
        ("Kira Nerys", "Bajoran", 29)
    ])

    # Update name
    cur.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")

    # Get Bajoran characters
    cur.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
    print("Bajoran Characters:", cur.fetchall())

    # Remove characters older than 100
    cur.execute("DELETE FROM Roster WHERE Age > 100")

    # Add Rank column and update data
    cur.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")
    cur.executemany("UPDATE Roster SET Rank = ? WHERE Name = ?", [
        ("Captain", "Benjamin Sisko"),
        ("Lieutenant", "Ezri Dax"),
        ("Major", "Kira Nerys")
    ])

    # Show sorted roster
    cur.execute("SELECT * FROM Roster ORDER BY Age DESC")
    print("Sorted Characters:", cur.fetchall())

    conn.commit()
    conn.close()

create_roster_db()
