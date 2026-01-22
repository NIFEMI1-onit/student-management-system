import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    department TEXT
)
""")

def add_student(name, age, department):
    cursor.execute("INSERT INTO students (name, age, department) VALUES (?, ?, ?)", (name, age, department))
    conn.commit()
    print(f"Student {name} added successfully!")

def view_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)

# Example usage
add_student("Nifemi", 21, "Computer Science")
view_students()

conn.close()
