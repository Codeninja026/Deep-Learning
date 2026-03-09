from fastapi import FastAPI, HTTPException
import sqlite3
from backend.database import init_db
from backend.models import Ride, Booking

app = FastAPI(title="Campus Ride Sharing API")

# Initialize DB
init_db()

@app.post("/post_ride")
def post_ride(ride: Ride):
    # Simple college domain check
    if "@college.edu" not in ride.email:  # change to your actual domain
        raise HTTPException(status_code=400, detail="Invalid college email")

    conn = sqlite3.connect("rides.db")
    c = conn.cursor()
    c.execute("""INSERT INTO rides 
                 (driver_name, email, from_loc, to_loc, date, time, seats) 
                 VALUES (?, ?, ?, ?, ?, ?, ?)""",
              (ride.driver_name, ride.email, ride.from_loc, ride.to_loc, ride.date, ride.time, ride.seats))
    conn.commit()
    conn.close()
    return {"message": "Ride posted successfully!"}

@app.get("/get_rides")
def get_rides():
    conn = sqlite3.connect("rides.db")
    c = conn.cursor()
    c.execute("SELECT * FROM rides")
    rides = c.fetchall()
    conn.close()
    return {"rides": rides}

@app.post("/book_ride")
def book_ride(booking: Booking):
    if "@college.edu" not in booking.email:
        raise HTTPException(status_code=400, detail="Invalid college email")

    conn = sqlite3.connect("rides.db")
    c = conn.cursor()
    c.execute("INSERT INTO bookings (ride_id, passenger_name, email) VALUES (?, ?, ?)",
              (booking.ride_id, booking.passenger_name, booking.email))
    conn.commit()
    conn.close()
    return {"message": "Ride booked successfully!"}
