from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        self.client.get("/api/profile")
        self.csrftoken = self.client.cookies.get('csrftoken')
        print("CSRFTOKEN:", self.csrftoken)

        with self.client.post("/api/login", json={
            "username": "test1",
            "password": "cnlab01"
        }, headers={
            "X-CSRFToken": self.csrftoken
        }, catch_response=True) as response:
            if response.cookies:
                self.sessionid = response.cookies.get('sessionid')
                print("SESSIONID:", self.sessionid)

    @task
    def profile(self):
        with self.client.post("/api/submission", json={
            "problem_id": 1,
            "language": "Python3",
            "code": "print(\"hello\")"
        }, headers={
            'Cookie': f'sessionid={self.sessionid}; csrftoken={self.csrftoken}',
            'X-CSRFToken': self.csrftoken
        }, catch_response=True) as response:
            print(response.text)
