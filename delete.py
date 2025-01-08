# delete.py
from api_client import TrelloAPI

def test_delete_board(board_id):
    # Initialize the TrelloAPI client
    trello = TrelloAPI()
    # Call the delete_board method to delete the specified board
    response = trello.delete_board(board_id)
    
    # Check if the response object is valid and Check the status code of the response
    if response:
        # Assert that the HTTP response status code is 200 (success)
        if response.status_code == 200:
            print(f"Successfully deleted the board with ID: {board_id}")
        #Assert that the HTTP response status code is 404 (not found)
        elif response.status_code == 404:
            print(f"Board with ID {board_id} not found.")
        #Assert that the HTTP response status code is 401 (Authentication failed)
        elif response.status_code == 401:
            print("Authentication failed. Check your API key and token.")
        else:
            print(f"Failed to delete the board. Status Code: {response.status_code}") # Print an error message if the board deletion failed
    else:
        print("Failed to delete board due to an error.") # Print an error message if the board deletion failed

if __name__ == "__main__":
    # Prompt the user to enter the board ID to delete
    board_id = input("Enter the board ID to delete: ")
    test_delete_board(board_id) # Run the test function to delete the specified board



