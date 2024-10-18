from locust import HttpUser, task, between, constant
from locust import LoadTestShape
import random

import time

from DMOJ_answer import problem_data
from DMOJ_failed import failed_data

class AlgorithmTest(HttpUser):
    # start_time = time.time()
    wait_time = lambda self: int(random.expovariate(1/100)) 

    def get_csrf(self):
        
        self.sessionid = None
        self.csrftoken = None
        
        response = self.client.get("/accounts/login")
        self.csrftoken = response.cookies['csrftoken']
        self.headers = {'X-CSRFToken': self.csrftoken, "Content-Type": "application/x-www-form-urlencoded"}

 
    def on_start(self):
        user_id = random.randint(1, 100)
        username = f"test{user_id}"

        self.get_csrf()

        user_data = {
            "username": username,
            "password": "dmoj1234",
            "csrfmiddlewaretoken": self.csrftoken
        }

        response = self.client.post("/accounts/login/",
                                data=user_data,
                                headers=self.headers)

        if response.status_code == 200:
            print("로그인 성공!")
            print(response.cookies)
            print(response.status_code)
        else:
            print("로그인 실패!")
            print(f"상태 코드: {response.status_code}, 응답: {response.text}")


    @task(5)
    def submit_ok(self):
        cookies = self.client.cookies.get_dict()
        self.get_csrf()
        self.headers['sessionid'] = cookies.get('sessionid')

        problem_number = random.randint(1, 10)
        print(f"Problem Number: {problem_number}")
        pro_data = random.choice(problem_data[problem_number-1])
        pro_data['csrfmiddlewaretoken'] = self.csrftoken
        
        with self.client.post(f"/problem/test{problem_number}/submit",
        #with self.client.post(f"/problem/test1/submit",
                                data=pro_data,
                                headers=self.headers) as response:
             print(response.status_code)
            
    @task(5)
    def submit_failed(self):
        cookies = self.client.cookies.get_dict()
        self.get_csrf()
        self.headers['sessionid'] = cookies.get('sessionid')
        
        problem_number = random.randint(1, 10)
        pro_data = random.choice(failed_data[problem_number-1])
        pro_data['csrfmiddlewaretoken'] = self.csrftoken

        with self.client.post(f"/problem/test{problem_number}/submit",
        #with self.client.post(f"/problem/test1/submit",
                                data=pro_data,
                                headers=self.headers) as response:
             print(response.status_code)


class StudentUser(HttpUser):
    
    tasks = [AlgorithmTest]            