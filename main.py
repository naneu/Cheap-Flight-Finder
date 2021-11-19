import datetime as dt
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

datamanager = DataManager()
flightsearch = FlightSearch()
notificationmanager = NotificationManager()
sheet_data = datamanager.get_destination_data()
users = datamanager.get_email_address()
ORIGIN_CITY_IATA = "LON"


for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flightsearch.flight_search_data(row["city"])
        datamanager.update_destination_data()

tomorrow = dt.datetime.now() + dt.timedelta(days=1)
six_months_from_today = dt.datetime.now() + dt.timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flightsearch.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
        )
    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:
        emails = [row["email"] for row in users]
        # names = [row["firstName"] for row in users]

        message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            print(message)

        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

        notificationmanager.send_notification(message)
        notificationmanager.send_emails(emails, message, link)

