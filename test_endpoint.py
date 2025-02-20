import requests

def test_users_endpoint():
    response = requests.get('http://localhost:8000/users/')
    print("Status Code:", response.status_code)
    print("Response:", response.json())

if __name__ == "__main__":
    test_users_endpoint()
