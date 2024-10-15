from locust import HttpUser, task, between
import random
from Qing_answer import problem_data

#김재호 코드

class WebsiteUser(HttpUser):
    def wait_time(self):
        lambd = 1 / 30  # 평균 30초 대기
        return random.expovariate(lambd)  # 포아송 분포 기반 대기 시간 반환


    def on_start(self):
        
        self.sessionid = None
        self.csrftoken = None
        
        self.client.get("/api/profile")
        self.csrftoken = self.client.cookies.get('csrftoken')
        self.headers = {'X-CSRFToken': self.csrftoken, "Content-Type": "application/json"}
        
        user_id = random.randint(1, 100)
        username = f"test{user_id}"
        
        user_data = {
            "username": username,
            "password": "cnlab123"
        }
    
        with self.client.post("/api/login",
                              json=user_data, 
                              headers=self.headers,
                              catch_response=True) as response:   
                self.sessionid = response.cookies.get('sessionid')
                self.csrftoken = response.cookies.get('csrftoken')
                print(f"Login status: {response.text}")
    @task
    def submit(self):
        
        problem = random.choice(problem_data)
        
        self.headers = {
            'Cookie': f'sessionid={self.sessionid}; csrftoken={self.csrftoken}',
            'X-CSRFToken': self.csrftoken
        }
        
        with self.client.post("/api/submission", 
                              json=problem, 
                              headers=self.headers,
                              catch_response=True) as response:
            print(f"Submission status: {response.text}")
