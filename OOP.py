class Airport:
    def __init__(self, name, location):
        self.name = name
        self.location = location

class Flight:
    def __init__(self, flight_number, departure_airport, arrival_airport, departure_time, arrival_time, price, airline, seat_capacity=100):
        self.flight_number = flight_number
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.price = price
        self.airline = airline
        self.seat_capacity = seat_capacity
        self.seats_booked = 0

    def display_flight_details(self):
        print(f"Flight {self.flight_number} from {self.departure_airport.name} to {self.arrival_airport.name}")
        print(f"Departure: {self.departure_time}, Arrival: {self.arrival_time}, Price: {self.price}, Airline: {self.airline}")
        print(f"Seats available: {self.seat_capacity - self.seats_booked}")

    def book_seat(self):
        if self.seats_booked < self.seat_capacity:
            self.seats_booked += 1
            return True
        return False

class Customer:
    def __init__(self, name):
        self.name = name

class FlightBookingSystem:
    def __init__(self):
        self.flights = []
        self.bookings = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_flights(self, departure, arrival):
        return [flight for flight in self.flights if flight.departure_airport == departure and flight.arrival_airport == arrival]

    def book_flight(self, customer, flight, meal_option=None, additional_services=[]):
        if flight.book_seat():
            booking_id = len(self.bookings) + 1
            self.bookings.append({
                "booking_id": booking_id,
                "customer": customer.name,
                "flight": flight.flight_number,
                "meal_option": meal_option,
                "additional_services": additional_services
            })
            print(f"Booking successful! Booking ID: {booking_id}")
            return booking_id
        print("Booking failed. No seats available.")
        return None

# Example usage
airport1 = Airport("Borg el Arab Airport", "Borg el Arab")
airport2 = Airport("Cairo International Airport", "Cairo")
flight1 = Flight("AA123", airport1, airport2, "08:00 AM", "02:00 PM", 300, "EgyptAir")
flight2 = Flight("UA456", airport1, airport2, "08:00 AM", "06:00 PM", 250, "Nile Air")

booking_system = FlightBookingSystem()
booking_system.add_flight(flight1)
booking_system.add_flight(flight2)

available_flights = booking_system.search_flights(departure=airport1, arrival=airport2)
for flight in available_flights:
    flight.display_flight_details()

customer1 = Customer("Fares Khaled")
selected_flight = available_flights[0]
booking_system.book_flight(customer1, selected_flight, meal_option="meat", additional_services=["Extra sauce"])
