import time

start_time = time.time()

def wait_time(self):
        
        quarter_hour = (time.time() - self.start_time) // (2)  # 2분마다 증가
        return between(1, 30)  # 시간이 지날수록 대기 시간 증가