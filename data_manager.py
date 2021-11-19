import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        self.users_api_enpoint = ""
        self.sheety_api_endpoint = ""
        self.headers={
            "Authorization": "",
            "Content-Type": ""
        }
    
    def get_destination_data(self):
        destination_res = requests.get(url=self.sheety_api_endpoint, headers=self.headers)
        self.destination_data = destination_res.json()["prices"]
        return self.destination_data

    def update_destination_data(self):
        for row in self.destination_data:
            row_id = row["id"]
            new_data = {
                "price": {
                    "iataCode": row["iataCode"]
                }
                
            }
            update_res = requests.put(url=f"{self.sheety_api_endpoint}/{row_id}",json= new_data, headers=self.headers)
            
        return update_res.text

    def get_email_address(self):
        response = requests.get(url=self.users_api_enpoint, headers=self.headers)
        users = response.json()["users"]
        return users
