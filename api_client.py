# api_client.py
# This file contains the TrelloAPI class which provides methods to interact with the Trello API.
import requests
from constant_values import API_KEY, TOKEN, BASE_URL

class TrelloAPI:

    # A class to interact with the Trello API, providing methods to manage boards.
    def __init__(self, api_key=API_KEY, token=TOKEN):

        self.api_key = api_key
        self.token = token
        self.base_url = BASE_URL

    def _make_request(self, method, url, params=None):

        # Define headers for the request
        headers = {'Accept': 'application/json'}
        # If no parameters are provided, initialize an empty dictionary
        if params is None:
            params = {}

        # Add the API key and token to the request parameters
        params.update({"key": self.api_key, "token": self.token})
        try:
            # Make the HTTP request
            response = requests.request(method, url, headers=headers, params=params)
            # Raise an exception for HTTP errors
            response.raise_for_status()  
            # Return the response if successful
            return response
        except requests.exceptions.HTTPError as err:
            # Print the HTTP error if one occurs
            print(f"HTTP error occurred: {err}")
        except requests.exceptions.RequestException as err:
            # Print any general request errors
            print(f"Error occurred: {err}")

    def create_board(self, board_name):
        # Define the API endpoint for creating boards
        url = f"{self.base_url}/boards/"
        # Set the board name as a parameter
        params = {"name": board_name}
        # Send the POST request to create the board
        return self._make_request("POST", url, params)

    def get_boards(self):
        # Define the API endpoint for retrieving boards
        url = f"{self.base_url}/members/me/boards"
        # Send the GET request to fetch the boards
        return self._make_request("GET", url)

    def update_board(self, board_id, new_name):
        # Define the API endpoint for updating a board
        url = f"{self.base_url}/boards/{board_id}"
        # Set the new board name as a parameter
        params = {"name": new_name}
        # Send the PUT request to update the board name
        return self._make_request("PUT", url, params)

    def delete_board(self, board_id):
        # Define the API endpoint for deleting a board
        url = f"{self.base_url}/boards/{board_id}"
        # Send the DELETE request to remove the board
        return self._make_request("DELETE", url)
