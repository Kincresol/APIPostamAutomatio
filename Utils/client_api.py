import requests


class APIClient:
    base_url = "https://jsonplaceholder.typicode.com"

    def __init__(self):
        self.headers = {
            "Content-Type": "application/json"
        }


    def get(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)
        return response

    def post(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        response1 = requests.post(url, headers=self.headers, json=data)
        return response1

    def put(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        response2 = requests.put(url, headers=self.headers, json=data)
        return response2

    def delete(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response3 = requests.delete(url, headers=self.headers)
        return response3