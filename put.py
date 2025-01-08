import requests
from constant_values import API_KEY, TOKEN, BASE_URL

def test_update_board(board_id):
    url = f"{BASE_URL}/boards/{board_id}"
    params = {"key": API_KEY, "token": TOKEN, "name": "DINU DONNEY"}
    response = requests.put(url, params=params)

    assert response.status_code == 200, "Failed to update board"
    assert response.json().get("name") == "DINU DONNEY", "Board name not updated"
    board_name=response.json().get("name")
    print("updated board name is", board_name)

if __name__ == "__main__":
    board_id = input("Enter the board ID to update: ")
    try:
        test_update_board(board_id)
        print("Update Test Passed!")
    except AssertionError as e:
        print(f"Update Test Failed: {e}")
