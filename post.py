import requests 
from constant_values import API_KEY, TOKEN, BASE_URL

def test_create_board():
    url = f"{BASE_URL}/boards/"
    params = {"key": API_KEY, "token": TOKEN, "name": "Jahnavi"}
    response = requests.post(url, params=params)

    assert response.status_code == 200, "Failed to create board"
    assert response.json().get("name") == "Jahnavi", "Board name mismatch"
    board_name = response.json().get("name")
    print("Created Board ID:", response.json().get("id"))
    print(board_name)
if __name__ == "__main__":
    try:
        test_create_board()
        print("Create Test Passed!")
    except AssertionError as e:
        print(f"Create Test Failed: {e}")
