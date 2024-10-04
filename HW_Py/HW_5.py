class Human:
    def __init__(self, gender, age, weight, height, eyes_color):
        self.gender = gender
        self.__age = age
        self.weight = weight
        self.height = height
        self.eyes_color = eyes_color
        
        

    def move(self):
        print('I can walk and run')

    def get_age(self):
        print(self.__age)

    def set_age(self, new_age):
        self.__age = new_age

    def super_mother(self):
        print('I can feed my family')

    def super_father(self):
        print('I can help my family')


person1 = Human('f', 36, 54, 154, 'brown')
person1.move()
print(person1.get_age())
print(person1.__dict__)
print(person1._Human__age)
person1.set_age(18)
print(person1.__dict__)
person1.weight = 45
person1._Human__age = 21
print(person1.__dict__)

########################

import requests
import pytest

BASE_URL = "https://release-gs.qa-playground.com/api/v1"
AUTH_HEADER = {
    "Authorization": "YOUR TOKEN"
}

def headers(x_task_id):
    return {
        "Authorization": "YOUR TOKEN",
        "X-Task-Id": x_task_id
    }

@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    response = requests.post(f"{BASE_URL}/setup", headers=AUTH_HEADER)
    assert response.status_code == 205

def test_delete_user(x_task_id):
    # Step 1: Get user list
    response = requests.get(f"{BASE_URL}/users", headers=headers(x_task_id))
    assert response.status_code == 200
    users = response.json()
    assert len(users) > 0, "No users found"

    # Step 2: Choose a user and get user uuid
    user_uuid = users[0]['uuid']

    # Step 3: Send DELETE request to delete the user
    response = requests.delete(f"{BASE_URL}/users/{user_uuid}", headers=headers(x_task_id))
    assert response.status_code == 204

    # Step 5: Validate that the user was deleted from the user list
    response = requests.get(f"{BASE_URL}/users", headers=headers(x_task_id))
    assert response.status_code == 200
    users = response.json()
    assert not any(user['uuid'] == user_uuid for user in users), "User not deleted"

    # Step 6: Verify that user information doesn't return
    response = requests.get(f"{BASE_URL}/users/{user_uuid}", headers=headers(x_task_id))
    assert response.status_code == 404



