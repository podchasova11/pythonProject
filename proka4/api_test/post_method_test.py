import pytest
import requests


response = requests.post(
    url="https://releas.gs-playground/api/v2/users",
    headers={
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IldGZlRBQ0hzYUhvQ3VML1MiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzAzODM4NzY1LCJpYXQiOjE3MDMyMzg3NjUsImlzcyI6Imh0dHBzOi8vbXlrb3RxYm9ja3p2emFjY2N1Ynouc3VwYWJhc2UuY28vYXV0aC92MSIsInN1YiI6IjE3MWZhN2JjLWRjMDAtNGRjYS05MjE3LWRlYmRkMjY5MzU1MSIsImVtYWlsIjoicG9kNGFzb3ZhMjBAZ21haWwuY29tIiwicGhvbmUiOiIiLCJhcHBfbWV0YWRhdGEiOnsicHJvdmlkZXIiOiJnaXRodWIiLCJwcm92aWRlcnMiOlsiZ2l0aHViIl19LCJ1c2VyX21ldGFkYXRhIjp7ImF2YXRhcl91cmwiOiJodHRwczovL2F2YXRhcnMuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3UvMTY2Njg5MjU_dj00IiwiZW1haWwiOiJwb2Q0YXNvdmEyMEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZnVsbF9uYW1lIjoiTWlsYSBQb2RjaGFzb3ZhIiwiaXNzIjoiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbSIsIm5hbWUiOiJNaWxhIFBvZGNoYXNvdmEiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJwb2RjaGFzb3ZhMTEiLCJwcm92aWRlcl9pZCI6IjE2NjY4OTI1Iiwic3ViIjoiMTY2Njg5MjUiLCJ1c2VyX25hbWUiOiJwb2RjaGFzb3ZhMTEifSwicm9sZSI6ImF1dGhlbnRpY2F0ZWQiLCJhYWwiOiJhYWwxIiwiYW1yIjpbeyJtZXRob2QiOiJvYXV0aCIsInRpbWVzdGFtcCI6MTY5OTI0MzI2MH1dLCJzZXNzaW9uX2lkIjoiZmY5ZThlNGEtYzVhNC00MTEyLTg3OGQtYmEyNThmNjE4ZTVjIn0.HRZipKQ3Hvm3lp_IxUCkCJPlSXiuOztr8OSwjGKzdjM"
    },

    json={
        "email": "dima@gmail.com",
        "password": "123321",
        "name": "Dmitriy",
        "nickname": "Dimon"
    }
)

assert response.status_code == 200

print(response.json())