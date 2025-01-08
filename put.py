# put.py

from api_client import TrelloAPI

def test_update_board(board_id):
    # Initialize the TrelloAPI client
    trello = TrelloAPI()
    # Define the new name for the board
    new_name = "DINU DONNEY"
    # Call the update_board method to update the board name
    response = trello.update_board(board_id, new_name)
    
    # Check if the response object is valid
    if response:
        # Assert that the HTTP response status code is 200 (success)
        assert response.status_code == 200, "Failed to update board"
        # Extract the updated board name from the response JSON
        updated_name = response.json().get("name")
        # Assert that the updated board name matches the new name
        assert updated_name == new_name, "Board name not updated"
        print(f"Updated board name is {updated_name}") # Print the updated board name
    else:
        print("Failed to update board due to an error.") # Print an error message if the board update failed

if __name__ == "__main__":
    board_id = input("Enter the board ID to update: ") # Prompt the user to enter a board ID
    try:
        test_update_board(board_id) # Run the test function and handle any assertion errors
        print("Update Test Passed!")
    except AssertionError as e: # Print failure message with the assertion error details
        print(f"Update Test Failed: {e}")

