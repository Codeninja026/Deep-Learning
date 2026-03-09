import sqlite3


def init_db():
    conn = sqlite3.connect('rides.db')
    c = conn.cursor()

    # Create rides table
    c.execute('''CREATE TABLE IF NOT EXISTS rides (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        driver_name TEXT,
        email TEXT,
        from_loc TEXT,
        to_loc TEXT,
        date TEXT,
        time TEXT,
        seats INTEGER
    )''')

    # Create bookings table
    c.execute('''CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ride_id INTEGER,
        passenger_name TEXT,
        email TEXT
    )''')

    conn.commit()
    conn.close()
