import streamlit as st
import requests

API_BASE = "http://127.0.0.1:8000"

st.set_page_config(page_title="CampusRide", page_icon="🚗", layout="centered")
st.title("🚗 CampusRide - College Ride Sharing")

# Initialize session state
if "email" not in st.session_state:
    st.session_state.email = ""
if "email_valid" not in st.session_state:
    st.session_state.email_valid = False
if "role" not in st.session_state:
    st.session_state.role = None

# Step 1: Email input and validation
if not st.session_state.email_valid:
    st.session_state.email = st.text_input("Enter your college email:", st.session_state.email)
    if st.session_state.email:
        if "@kitsw.ac.in" in st.session_state.email:
            st.session_state.email_valid = True
        else:
            st.error("Use your college email only!")

# Step 2: Show role selection and forms after valid email
if st.session_state.email_valid:
    st.success(f"Welcome {st.session_state.email}!")

    # Role selection stored in session_state
    st.session_state.role = st.radio("Select Role:", ["Driver", "Passenger"], horizontal=True, key="role_radio")

    # Driver form
    if st.session_state.role == "Driver":
        st.header("🚘 Offer a Ride")
        name = st.text_input("Your Name", key="driver_name")
        from_loc = st.text_input("From (Start Location)", key="from_loc")
        to_loc = st.text_input("To (Destination)", key="to_loc")
        date = st.date_input("Date of Travel", key="date")
        time = st.time_input("Time of Travel", key="time")
        seats = st.number_input("Available Seats", min_value=1, max_value=10, value=3, key="seats")

        if st.button("Post Ride", key="post_ride"):
            ride_data = {
                "driver_name": name,
                "email": st.session_state.email,
                "from_loc": from_loc,
                "to_loc": to_loc,
                "date": str(date),
                "time": str(time),
                "seats": seats
            }
            res = requests.post(f"{API_BASE}/post_ride", json=ride_data)
            if res.status_code == 200:
                st.success("✅ Ride posted successfully!")
            else:
                st.error(res.json().get("detail", "Error posting ride"))

    # Passenger form
    elif st.session_state.role == "Passenger":
        st.header("🧍 Available Rides")
        res = requests.get(f"{API_BASE}/get_rides")
        rides = res.json().get("rides", [])

        if not rides:
            st.info("No rides available right now.")
        else:
            for r in rides:
                with st.container():
                    st.markdown(f"""
                    **Ride ID:** {r[0]}  
                    **Driver:** {r[1]} ({r[2]})  
                    **From → To:** {r[3]} → {r[4]}  
                    **Date/Time:** {r[5]} @ {r[6]}  
                    **Seats:** {r[7]}  
                    """)
                    passenger_name = st.text_input("Your Name", key=f"name_{r[0]}")
                    if st.button(f"Book Ride #{r[0]}", key=f"book_{r[0]}"):
                        booking_data = {
                            "ride_id": r[0],
                            "passenger_name": passenger_name,
                            "email": st.session_state.email
                        }
                        b_res = requests.post(f"{API_BASE}/book_ride", json=booking_data)
                        if b_res.status_code == 200:
                            st.success("🎉 Ride booked successfully!")
                        else:
                            st.error(b_res.json().get("detail", "Error booking ride"))
