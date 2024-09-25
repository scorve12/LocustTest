from locust import HttpUser, task, between
import random

#박준걸 코드

class UserBehavior(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        response = self.client.get("/accounts/login")
        self.csrftoken = response.cookies['csrftoken']
        self.headers = {'X-CSRFToken': self.csrftoken, "Content-Type": "application/x-www-form-urlencoded"}
        
        user_id = random.randint(1, 200)
        username = f"test{user_id}"

        user_data = {
            "username": username,
            "password": "dmoj1234",
            "csrfmiddlewaretoken": self.csrftoken
        }
        
        with self.client.post("/accounts/login/",
                                data=user_data,
                                headers=self.headers,
                                catch_response=True) as response:
            if response.cookies:
                self.sessionid = response.cookies.get('sessionid')
                print(response.status_code)


    @task
    def submit(self):
        pro_data = {
            'source': "print('test')",
            'language': 8,
            'judge': '',
            'csrfmiddlewaretoken': self.csrftoken
        }
        
        self.headers = {
            'Cookie': f'sessionid={self.sessionid}; csrftoken={self.csrftoken}',
            'X-CSRFToken': self.csrftoken
        }

        with self.client.post("/problem/test1/submit",
                                data=pro_data,
                                headers=self.headers,
                                catch_response=True) as response:
            print(response.status_code)
            if response.status_code != 200:
                response.failure("Failed to submit")