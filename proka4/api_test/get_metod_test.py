import pytest
import requests



# GET запрос с path-параметрами

response = requests.post(
    url="https://dev-gs.qa-playground.com/api/v1",
    headers={
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IldGZlRBQ0hzYUhvQ3VML1MiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzAzODM4NzY1LCJpYXQiOjE3MDMyMzg3NjUsImlzcyI6Imh0dHBzOi8vbXlrb3RxYm9ja3p2emFjY2N1Ynouc3VwYWJhc2UuY28vYXV0aC92MSIsInN1YiI6IjE3MWZhN2JjLWRjMDAtNGRjYS05MjE3LWRlYmRkMjY5MzU1MSIsImVtYWlsIjoicG9kNGFzb3ZhMjBAZ21haWwuY29tIiwicGhvbmUiOiIiLCJhcHBfbWV0YWRhdGEiOnsicHJvdmlkZXIiOiJnaXRodWIiLCJwcm92aWRlcnMiOlsiZ2l0aHViIl19LCJ1c2VyX21ldGFkYXRhIjp7ImF2YXRhcl91cmwiOiJodHRwczovL2F2YXRhcnMuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3UvMTY2Njg5MjU_dj00IiwiZW1haWwiOiJwb2Q0YXNvdmEyMEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZnVsbF9uYW1lIjoiTWlsYSBQb2RjaGFzb3ZhIiwiaXNzIjoiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbSIsIm5hbWUiOiJNaWxhIFBvZGNoYXNvdmEiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJwb2RjaGFzb3ZhMTEiLCJwcm92aWRlcl9pZCI6IjE2NjY4OTI1Iiwic3ViIjoiMTY2Njg5MjUiLCJ1c2VyX25hbWUiOiJwb2RjaGFzb3ZhMTEifSwicm9sZSI6ImF1dGhlbnRpY2F0ZWQiLCJhYWwiOiJhYWwxIiwiYW1yIjpbeyJtZXRob2QiOiJvYXV0aCIsInRpbWVzdGFtcCI6MTY5OTI0MzI2MH1dLCJzZXNzaW9uX2lkIjoiZmY5ZThlNGEtYzVhNC00MTEyLTg3OGQtYmEyNThmNjE4ZTVjIn0.HRZipKQ3Hvm3lp_IxUCkCJPlSXiuOztr8OSwjGKzdjM"
    }
)
print(response.json())

# GET запрос без передачи параметров

response = requests.post(
    url="https://petstore.swagger.io/v2/store/inventory",
    headers={
        "api_key": "special-key"
    }
)

assert response.status_code == 200
print(response.json()["available"])
# проверим что ["available"] == 163
assert response.json()["available"] == 163

# Мы методом post активировали окружение, теперь
# будем делать запрос с помощью метода get

# делаем запрос к точке /users которая должна нам вернуть весь список юзеров


response = requests.get(
    url="https://petstore.swagger.io/v2/store/inventory/cd3fa85f64-5717-4562-b3fc-2c963f66afa6",  # сюда добавляем ай-ди -юзера, который нам вернулся после прогона теста : /3fa85f64-5717-4562-b3fc-2c963f66afa6
    headers={
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IldGZlRBQ0hzYUhvQ3VML1MiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzAzODM4NzY1LCJpYXQiOjE3MDMyMzg3NjUsImlzcyI6Imh0dHBzOi8vbXlrb3RxYm9ja3p2emFjY2N1Ynouc3VwYWJhc2UuY28vYXV0aC92MSIsInN1YiI6IjE3MWZhN2JjLWRjMDAtNGRjYS05MjE3LWRlYmRkMjY5MzU1MSIsImVtYWlsIjoicG9kNGFzb3ZhMjBAZ21haWwuY29tIiwicGhvbmUiOiIiLCJhcHBfbWV0YWRhdGEiOnsicHJvdmlkZXIiOiJnaXRodWIiLCJwcm92aWRlcnMiOlsiZ2l0aHViIl19LCJ1c2VyX21ldGFkYXRhIjp7ImF2YXRhcl91cmwiOiJodHRwczovL2F2YXRhcnMuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3UvMTY2Njg5MjU_dj00IiwiZW1haWwiOiJwb2Q0YXNvdmEyMEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZnVsbF9uYW1lIjoiTWlsYSBQb2RjaGFzb3ZhIiwiaXNzIjoiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbSIsIm5hbWUiOiJNaWxhIFBvZGNoYXNvdmEiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJwb2RjaGFzb3ZhMTEiLCJwcm92aWRlcl9pZCI6IjE2NjY4OTI1Iiwic3ViIjoiMTY2Njg5MjUiLCJ1c2VyX25hbWUiOiJwb2RjaGFzb3ZhMTEifSwicm9sZSI6ImF1dGhlbnRpY2F0ZWQiLCJhYWwiOiJhYWwxIiwiYW1yIjpbeyJtZXRob2QiOiJvYXV0aCIsInRpbWVzdGFtcCI6MTY5OTI0MzI2MH1dLCJzZXNzaW9uX2lkIjoiZmY5ZThlNGEtYzVhNC00MTEyLTg3OGQtYmEyNThmNjE4ZTVjIn0.HRZipKQ3Hvm3lp_IxUCkCJPlSXiuOztr8OSwjGKzdjM"
    }
)

print(response.json())

assert response.json()["available"] == 163


# GET-запрос с указанием Query-параметров
response =requests.get(
    url="https://petstore.swagger.io/v2/store/pet/findByStatus",
    headers={
        "api_key": "special-key"
    },
    params={
        "status": "pending"     # можно поставить статус "available"
    }
)
print(response.json())


# Авторизация через login/password:
response =requests.get(
    url="https://petstore.swagger.io/v2/store/pet/findByStatus",
    headers={
        "api_key": "special-key"
    },
    params={
        "status": "available"     # можно поставить статус "available"
    },
    auth={
        "login": "pod@ya.ru",
        "password": "123"
    }
)
