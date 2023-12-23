import sqlite3
import pytest
import requests


# @pytest.fixture()
# def connect_data_base():
#     connection = sqlite3.connect("test.db")
#     print("Мы подключили ДБ")
#     return connection
#
# cursor = connect_data_base().cursor()
# cursor.execute("SELECT *FROM employees")
# cursor.fetchall()  # собери все записи и запринть
# connect_data_base().close()   #закрывает БД

# def connect_database2():
#     connect2 = sqlite3.connect("test2.db")
#     return connect2
#
# cursor2 = connect_database2().cursor()
# cursor2.execute("SELECT * FROM employees")
# print(cursor2.fetchall())
# connect_database2()close()

# GET запрос с path-параметрами

# response = requests.post(
#     url="https://dev-gs.qa-playground.com/api/v1",
#     headers={
#         "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IldGZlRBQ0hzYUhvQ3VML1MiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzAzODM4NzY1LCJpYXQiOjE3MDMyMzg3NjUsImlzcyI6Imh0dHBzOi8vbXlrb3RxYm9ja3p2emFjY2N1Ynouc3VwYWJhc2UuY28vYXV0aC92MSIsInN1YiI6IjE3MWZhN2JjLWRjMDAtNGRjYS05MjE3LWRlYmRkMjY5MzU1MSIsImVtYWlsIjoicG9kNGFzb3ZhMjBAZ21haWwuY29tIiwicGhvbmUiOiIiLCJhcHBfbWV0YWRhdGEiOnsicHJvdmlkZXIiOiJnaXRodWIiLCJwcm92aWRlcnMiOlsiZ2l0aHViIl19LCJ1c2VyX21ldGFkYXRhIjp7ImF2YXRhcl91cmwiOiJodHRwczovL2F2YXRhcnMuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3UvMTY2Njg5MjU_dj00IiwiZW1haWwiOiJwb2Q0YXNvdmEyMEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZnVsbF9uYW1lIjoiTWlsYSBQb2RjaGFzb3ZhIiwiaXNzIjoiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbSIsIm5hbWUiOiJNaWxhIFBvZGNoYXNvdmEiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJwb2RjaGFzb3ZhMTEiLCJwcm92aWRlcl9pZCI6IjE2NjY4OTI1Iiwic3ViIjoiMTY2Njg5MjUiLCJ1c2VyX25hbWUiOiJwb2RjaGFzb3ZhMTEifSwicm9sZSI6ImF1dGhlbnRpY2F0ZWQiLCJhYWwiOiJhYWwxIiwiYW1yIjpbeyJtZXRob2QiOiJvYXV0aCIsInRpbWVzdGFtcCI6MTY5OTI0MzI2MH1dLCJzZXNzaW9uX2lkIjoiZmY5ZThlNGEtYzVhNC00MTEyLTg3OGQtYmEyNThmNjE4ZTVjIn0.HRZipKQ3Hvm3lp_IxUCkCJPlSXiuOztr8OSwjGKzdjM"
#     }
# )
# print(response.json())

# GET запрос без передачи параметров
response = requests.post(
    url="https://petstore.swagger.io/v2/store/inventory",
    headers={
        "api_key": "special-key"
    }
)
print(response.status_code)
assert response.status_code == 200
print(response.json()["available"])
# проверим что ["available"] == 163
assert response.json()["available"] == 163
