from locust import HttpUser, TaskSet, task, between, constant
from locust import LoadTestShape
import random

import time

from Qing_answer import problem_data
from Qing_failed import failed_data

#김재호 코드

class AlgorithmTest(TaskSet):
    start_time = time.time()

    def wait_time(self):
        elapsed_time = time.time() - self.start_time
        dynmaic_wait_time = min(0.1 + (elapsed_time / 20), 300)
        
        print(f"Cuurent wait time: {dynmaic_wait_time:.2f}")
        return dynmaic_wait_time
        
        

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
    @task(5)
    def submit_ok(self):
        
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
            
    @task(5)
    def submit_failed(self):
       
       problem = random.choice(failed_data)
       
       self.headers = {
           'Cookie': f'sessionid={self.sessionid}; csrftoken={self.csrftoken}',
           'X-CSRFToken': self.csrftoken
       }
       
       with self.client.post("/api/submission", 
                                json=problem, 
                                headers=self.headers,
                                catch_response=True) as response:
           print(response.status_code)

class StudentUser(HttpUser):
    #wait_time =  lambda self: random.expovariate(1 / 360 )
    tasks = [AlgorithmTest]
    
