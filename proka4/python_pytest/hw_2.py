# Import necessary libraries
import requests
from faker import Faker


# Define a class for user testing
class TestUsers:

    # Create a Faker object to generate random data
    fake = Faker()
    email = fake.word()
    password = fake.password()
    name = fake.name()
    nickname = fake.word()
    # Define the endpoint for user-related API requests
    base_url = "https://release-gs.qa-playground.com/api/v1"
    # Define the headers for API requests
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IldGZlRBQ0hzYUhvQ3VML1MiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNjk4MjcxMjE0LCJpYXQiOjE2OTgyNjc2MTQsImlzcyI6Imh0dHBzOi8vbXlrb3RxYm9ja3p2emFjY2N1Ynouc3VwYWJhc2UuY28vYXV0aC92MSIsInN1YiI6IjQ1MjUxMTVhLTZhY2EtNDAzYS1hODA1LTAyOWY1YTIxY2U4MSIsImVtYWlsIjoibWFuaWtvc3RvQG91dGxvb2suY29tIiwicGhvbmUiOiIiLCJhcHBfbWV0YWRhdGEiOnsicHJvdmlkZXIiOiJnaXRodWIiLCJwcm92aWRlcnMiOlsiZ2l0aHViIl19LCJ1c2VyX21ldGFkYXRhIjp7ImF2YXRhcl91cGRhdGVkX2F0IjoiMTY4OTYyMzAyNDk1MyIsImF2YXRhcl91cmwiOiJodHRwczovL2F2YXRhcnMuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3UvODAyMjQ5OTM_dj00IiwiZW1haWwiOiJtYW5pa29zdG9Ab3V0bG9vay5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZnVsbF9uYW1lIjoiQWxleGV5IEtvbGVkYWNoa2luIiwiaXNzIjoiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbSIsIm5hbWUiOiJBbGV4ZXkgS29sZWRhY2hraW4iLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJtYW5pa29zdG8iLCJwcm92aWRlcl9pZCI6IjgwMjI0OTkzIiwic3ViIjoiODAyMjQ5OTMiLCJ1c2VyX25hbWUiOiJtYW5pa29zdG8ifSwicm9sZSI6ImF1dGhlbnRpY2F0ZWQiLCJhYWwiOiJhYWwxIiwiYW1yIjpbeyJtZXRob2QiOiJvYXV0aCIsInRpbWVzdGFtcCI6MTY5ODI2NzYxNH1dLCJzZXNzaW9uX2lkIjoiMmFkOTAzODAtN2Q0MS00ZmRiLWE1ZDgtMTY2ZDgxZDU3YzMyIn0.nlUZqdz6wde4uDr-x4LfnVoGjTdDnKON94IjONvuEBA",
        "Content-Type": "application/json; charset=utf-8",
    }
    # Create a payload for creating a new user, using the generated login name
    payload = {
        "email": f"{email}.doe@gmail.com",
        "password": password,
        "name": name,
        "nickname": nickname
    }

    # Test method to verify user creation functionality
    def test_create_new_user(self):
        # Setup test environment
        setup = requests.post(
            url=f"{self.base_url}/setup",
            headers=self.headers
        )
        assert setup.status_code != 401
        # Create new user
        user = requests.post(
            url=f"{self.base_url}/users",
            json=self.payload,
            headers=self.headers
        )
        # Check the status code of the user creation response
        assert user.status_code == 200 or 204
        # Verify the email, name, and nickname of the created user
        assert user.json()["email"] == self.payload["email"]
        assert user.json()["name"] == self.payload["name"]
        assert user.json()["nickname"] == self.payload["nickname"]
        # Retrieve the UUID of the created user
        user_id = user.json()["uuid"]
        # Retrieve the created user data via API
        is_user_created = requests.get(
            url=f"{self.base_url}/users/{user_id}",
            headers=self.headers
        )
        # Check the status code of the user retrieval response
        assert is_user_created.status_code == 200
        # Verify the email of the retrieved user
        assert self.payload["email"] == is_user_created.json()["email"]