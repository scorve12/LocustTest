from locust import HttpUser, task, between

#김재호 코드

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        
        self.sessionid = None
        self.csrftoken = None
        
        self.client.get("/api/profile")
        self.csrftoken = self.client.cookies.get('csrftoken')
        self.headers = {'X-CSRFToken': self.csrftoken, "Content-Type": "application/json"}
        
        user_data = {
            "username": "test1",
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
        problem_data = {
            'problem_id': 1,
            'language': 'Python3',
            'code': 'print("hello")'
        }
        
        self.headers = {
            'Cookie': f'sessionid={self.sessionid}; csrftoken={self.csrftoken}',
            'X-CSRFToken': self.csrftoken
        }
        
        with self.client.post("/api/submission", 
                              json=problem_data, 
                              headers=self.headers,
                              catch_response=True) as response:
            print(f"Submission status: {response.text}")
