from pydantic import BaseModel, EmailStr

class Ride(BaseModel):
    driver_name: str
    email: EmailStr
    from_loc: str
    to_loc: str
    date: str
    time: str
    seats: int

class Booking(BaseModel):
    ride_id: int
    passenger_name: str
    email: EmailStr
