# post.py

from api_client import TrelloAPI

def test_create_board():
    # Initialize the TrelloAPI client
    trello = TrelloAPI()
    # Define the name for the new board
    board_name = "Jahnavi"
    # Call the create_board method to create a new board
    response = trello.create_board(board_name)
     
    # Check if the response object is valid
    if response:
        # Extract the board name from the response JSON
        board_name = response.json().get("name")
        # Assert that the HTTP response status code is 200 (success)
        assert response.status_code == 200, "Failed to create board"
        # Assert that the created board name matches the expected board name
        assert board_name == "Jahnavi", "Board name mismatch"
        # Print the created board's ID and name for verification
        print("Created Board ID:", response.json().get("id"))
        print(f"Board name: {board_name}")
    else:
        # Print an error message if the board creation failed
        print("Failed to create board due to an error.")

if __name__ == "__main__":  
    # Run the test function and handle any assertion errors
    try:
        test_create_board()
        print("Create Test Passed!") # Print success message if all assertions pass
    except AssertionError as e:
        print(f"Create Test Failed: {e}") # Print failure message with the assertion error details
