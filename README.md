# Cheap-Flight-Finder
### project overview:

Nothing beats a good flight deal. This projects shows how to find cheap flight deals and send  SMS  and/or email notification.

before starting create a Google sheet with two sheets, that contain data as shown below.

![snippet](/imgs/prices1.png)

![snippet](/imgs/prices.png)

![snippet](/imgs/users.png)


### APIs Required

1. Google Sheet Data Management - https://sheety.co/

2. Kiwi Partners Flight Search API (Free Signup, Requires Credit Card Details)

   (Tequila Flight Search API Documentation - https://tequila.kiwi.com/portal/docs/tequila_api)

3. Twilio SMS API - https://www.twilio.com/docs/sms



#### Program Requirements

1. Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with [International Air Transport Association (IATA)](https://en.wikipedia.org/wiki/IATA_airport_code#Cities_with_multiple_airports) codes for each city. Most of the cities in the sheet include multiple airports, you want the city code (not the airport code see [here](https://en.wikipedia.org/wiki/IATA_airport_code#Cities_with_multiple_airports)).
2. Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.
3. If the price is lower than the lowest price listed in the Google Sheet then send an SMS to your own number with the Twilio API.
4. The SMS should include the departure airport IATA code, destination airport IATA code, departure city, destination city, flight price and flight dates. 

