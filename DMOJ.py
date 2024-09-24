from locust import HttpUser, task, between
import random

class UserBehavior(HttpUser):
    wait_time = between(1, 2)

    def get_csrf(self):
        response = self.client.get("/accounts/login")
        self.csrftoken = response.cookies['csrftoken']
        self.headers = {'X-CSRFToken': self.csrftoken, "Content-Type": "application/x-www-form-urlencoded"}

    @task(1)
    def login(self):

        user_id = random.randint(1, 200)
        username = f"test{user_id}"

        self.get_csrf()

        user_data = {
            "username": username,
            "password": "dmoj1234",
            "csrfmiddlewaretoken": self.csrftoken
        }
        # print("Current cookies in Login:" + str(self.client.cookies))

        response = self.client.post("/accounts/login/",
                                data=user_data,
                                headers=self.headers)

        if response.status_code == 200:
            print("로그인 성공!")
            print(response.cookies)
            print(response.text)
        else:
            print("로그인 실패!")
            print(f"상태 코드: {response.status_code}, 응답: {response.text}")

        cookies = self.client.cookies.get_dict()
        self.get_csrf()
        self.headers['sessionid'] = cookies.get('sessionid')

        pro_data = {
            'source': "print('test')",
            'language': 8,
            'judge': '',
            'csrfmiddlewaretoken': self.csrftoken
        }

        response = self.client.post("/problem/test1/submit",
                                data=pro_data,
                                headers=self.headers)

        if response.status_code == 200:
            print("제출 성공!")
            print(response.cookies)
            print(response.text)
        else:
            print("제출 실패!")
            print(f"상태 코드: {response.status_code}, 응답: {response.text}")