import sqlite3

DB_NAME = "data.db"


def setup_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)

    conn.commit()
    conn.close()


def add_record():
    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip().lower()

    if not name or not email or "@" not in email:
        print("Invalid data! Enter a name and valid email.")
        return

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM records WHERE LOWER(email) = ?",
        (email,)
    )

    if cursor.fetchone():
        print("Duplicate detected! Record not saved.")
    else:
        cursor.execute(
            "INSERT INTO records (name, email) VALUES (?, ?)",
            (name, email)
        )
        conn.commit()
        print("Unique record added successfully!")

    conn.close()


def view_records():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, email FROM records")
    records = cursor.fetchall()

    print("\n--- Saved Records ---")
    if records:
        for record in records:
            print(record)
    else:
        print("No records found.")

    conn.close()


def main():
    setup_database()

    while True:
        print("\n=== Data Redundancy Removal System ===")
        print("1. Add Record")
        print("2. View Records")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_record()
        elif choice == "2":
            view_records()
        elif choice == "3":
            print("Project closed.")
            break
        else:
            print("Invalid choice! Select 1, 2, or 3.")


if __name__ == "__main__":
    main()