import time


class Clock:
    def __init__(self, max_fps=60):
        self.max_fps = max_fps
        self.fixed_delta_time = 1.0 / max_fps
        self.last_update_time = time.time()
        self.accumulator = 0

    def get_delta_time(self):
        current_time = time.time()
        delta_time = current_time - self.last_update_time
        self.last_update_time = current_time
        return delta_time

    def sleep(self):
        time.sleep(self.fixed_delta_time)

    def update_accumulator(self, delta_time):
        self.accumulator += delta_time