from locust import HttpLocust, TaskSet, task, HttpUser, between
import json


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # 사용자 간 대기 시간

    
    def on_start(self):
        # 로그인 과정을 수행하며, CSRF 토큰과 sessionid를 추출합니다. 
        # CSRF 토큰을 가져오기 위해 /api/profile에 GET 요청을 보냅니다.
        with self.client.get("/api/profile", catch_response=True) as response:
            cookies = response.cookies
            csrftoken = cookies.get('csrftoken', None)
            print("CSRFTOKEN:", csrftoken)
        
        # 추출된 CSRF 토큰을 사용하여 로그인을 시도합니다.
        response = self.client.post("/api/login", json={
            "username": "test1",
            "password": "cnlab01"
        }, headers={
            "X-CSRFToken": csrftoken
        })

        # 응답에서 sessionid를 추출하여 저장합니다.
        if response.cookies:
            self.sessionid = response.cookies.get('sessionid', None)
            print("Extracted SESSIONID:", self.sessionid)
    
    @task
    def profile(self):
        response = self.client.get("/api/profile", cookies={'sessionid': self.sessionid})
        print(response.text)
        
            
        
        
      