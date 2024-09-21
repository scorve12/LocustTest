from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task(1)
    def login(self):
        # 로그인 요청을 위한 데이터
        payload = {
            'csrfmiddlewaretoken': 'Sr6vmRxSweem7P8bN2wbfTVrjt0wSZAOxD9PK5ZPRZDFaGTj4dzkLoVr7Z3qa7KB',
            'username': 'test1',
            'password': 'dmoj1234',
            'next': '/'
        }
        
        # POST 요청 보내기
        self.client.post(
            "/accounts/login/?next=/",
            data=payload,
            headers={
                "Host": "uncertain.today", #호스트정보
                "Connection": "keep-alive", #연결유지
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Referer": "http://uncertain.today/accounts/login/?next=/",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Cookie": "csrftoken=6aOVkudrl4GAuywR9VJzOGETleHtMyEGLmRfIIFoGP5TxphZq6MIkbET9KKn4GOt"
            }
        )

    @task(2)
    def load_homepage(self):
        self.client.get("/")  # 홈페이지 요청

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)  # 요청 사이의 대기 시간
