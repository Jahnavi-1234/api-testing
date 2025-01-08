import requests
from constant_values import API_KEY, TOKEN, BASE_URL

def test_delete_board(board_id):
    """
    Sends a DELETE request to delete a Trello board and validates the response.
    """
    url = f"{BASE_URL}/boards/{board_id}"
    params = {"key": API_KEY, "token": TOKEN}
    response = requests.delete(url, params=params)

    if response.status_code == 200:
        print(f"Successfully deleted the board with ID: {board_id}")
    elif response.status_code == 404:
        print(f"Board with ID {board_id} not found. Ensure it exists and is accessible.")
    elif response.status_code == 401:
        print("Authentication failed. Check your API key and token.")
    else:
        print(f"Failed to delete the board. Status Code: {response.status_code}, Response: {response.text}")

if __name__ == "__main__":
    board_id = input("Enter the board ID to delete: ")
    test_delete_board(board_id)



