from locust import HttpUser, task, between, constant
import random
import time

from DMOJ_answer import problem_data
from DMOJ_failed import failed_data

class AlgorithmTest(HttpUser):
    start_time = time.time()
    
    @property
    def wait_time(self):
        elapsed_time = time.time() - self.start_time  # 경과 시간 계산 (초 단위)

        # 10분 단위로 대기 시간 변경
        if elapsed_time < 5 * 60:  # 0~10분: 0.01초 대기
            return constant(0.01)
        elif elapsed_time < 10 * 60:  # 10~20분: 0.1초 대기
            return constant(0.1)
        elif elapsed_time < 15 * 60:  # 20~30분: 1초 대기
            return constant(0.5)
        elif elapsed_time < 20 * 60:  # 30~40분: 5초 대기
            return constant(1)
        elif elapsed_time < 25 * 60:  # 40~50분: 10초 대기
            return constant(5)
        else:  # 50~60분: 20초 대기
            return constant(10)

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
                                data=pro_data,
                                headers=self.headers) as response:
             print(response.status_code)


class StudentUser(HttpUser):
    #wait_time =  lambda self: random.expovariate(1/360)
    tasks = [AlgorithmTest]            