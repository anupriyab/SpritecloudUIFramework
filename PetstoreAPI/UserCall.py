import requests

from Models import user
from Models.user import User
from utilities import ConfigReader


class UserOperations:
    BASE_URL = ConfigReader.readconfig("basic info", "ApiBaseUrl")

    @staticmethod
    def add_user(user):
        endpoint = f"{UserOperations.BASE_URL}/user"
        user_data = user.__dict__
        response = requests.post(endpoint, json=user_data)
        if response.status_code == 200:
            print("User added successfully!", response.status_code)
        else:
            print(f"Failed to add user. Status code: {response.status_code}, Message: {response.json()['message']}")

    @staticmethod
    def get_user(username):
        endpoint = f"{UserOperations.BASE_URL}/user/{username}"
        response = requests.get(endpoint)
        if response.status_code == 200:
            print("User retrieved successfully!", response.status_code)
        else:
            print(
                f"Failed to retrieve user. Status code: {response.status_code}, Message: {response.json()['message']}")
        # Check if the returned user has the expected username
        resp = response.json()

        # Check if the returned user has the expected username
        assert resp['username'] == username
