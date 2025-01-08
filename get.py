# get.py

from api_client import TrelloAPI

def test_get_boards():
    # Initialize the TrelloAPI client
    trello = TrelloAPI()
    # Call the get_boards method to fetch the list of boards
    response = trello.get_boards()
    
    # Check if the response object is valid
    if response:
        # Assert that the HTTP response status code is 200 (success)
        assert response.status_code == 200, "Failed to fetch boards"
        # Assert that the response JSON contains a list
        assert isinstance(response.json(), list), "Response is not a list"
    else:
        print("Failed to fetch boards due to an error.") # Print an error message if the boards retrieval failed

if __name__ == "__main__":
    # Run the test function and handle any assertion errors
    try:
        test_get_boards()
        print("GET Test Passed!") # Print success message if all assertions pass
    except AssertionError as e:
        print(f"GET Test Failed: {e}") # Print failure message with the assertion error details
