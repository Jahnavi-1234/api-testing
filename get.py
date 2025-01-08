import requests
from constant_values import API_KEY, TOKEN, BASE_URL

def test_get_boards():
    url = f"{BASE_URL}/members/me/boards"
    params = {"key": API_KEY, "token": TOKEN}
    response = requests.get(url, params=params)

    assert response.status_code == 200, "Failed to fetch boards"
    assert isinstance(response.json(), list), "Response is not a list"
    # print("GET Boards Response:", response.json())

if __name__ == "__main__":
    try:
        test_get_boards()
        print("GET Test Passed!")
    except AssertionError as e:
        print(f"GET Test Failed: {e}")
