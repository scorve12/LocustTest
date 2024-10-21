from locust import HttpUser, task, between, constant
from locust import LoadTestShape
import random
from bs4 import BeautifulSoup
import time


class AlgorithmTest(HttpUser):
    # start_time = time.time()
    wait_time = lambda self: int(random.expovariate(1/100)) 
    def get_csrf(self):
        
        self.sessionid = None
        self.csrftoken = None
        
        response = self.client.get("/login")
        self.phpsessid = response.cookies.get("PHPSESSID")
        self.headers = {'X-CSRFToken': self.csrftoken, "Content-Type": "application/x-www-form-urlencoded"}
        
        soup = BeautifulSoup(response.text, 'html.parser')
        token_input = soup.find('input', {'name': '_csrf_token'})
        self.csrf_token = token_input['value']
        
    def on_start(self):
        self.get_csrf()

        # 로그인 정보 설정
        user_id = random.randint(1, 100)
        username = f"test{user_id}"
        password = "test000000"
        
        # 로그인 폼 데이터
        login_data = {
            "_username": username,
            "_password": password,
            "_csrf_token": self.csrf_token
        }

        # 로그인 요청 보내기
        response = self.client.post("/login", data=login_data)
        self.phpsessid = response.cookies.get("PHPSESSID")
        self.headers = {'PHPSESSID':self.phpsessid}
        if response.ok:
            print("로그인 성공!")
        else:
            print("로그인 실패!", response.status_code)

    @task
    def submit_ok(self):
        
        
        response = self.client.get("/team/submit")
        
        soup = BeautifulSoup(response.text, 'html.parser')
        token_input = soup.find('input', {'name': 'submit_problem[_token]'})
        self.submit_problem = token_input['value']
        
        files = {
            'submit_problem[code][]': ('./test1.py', open('DOM/test1.py', 'rb'), 'text/x-python')
        }
        data = {
            'submit_problem[problem]': '1',
            'submit_problem[language]': 'py3',
            'submit_problem[entry_point]': '',
            'submit_problem[_token]': self.submit_problem
        }

        
        with self.client.post("/team/submit", files=files, data=data, headers=self.headers)as response:
            print("Response status code:", response.status_code)
            print("Response status code:", response.text)