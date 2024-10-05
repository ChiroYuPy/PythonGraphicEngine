import inspect

from clock import Clock
from window import Window


class App:
    def __init__(self):
        self.running = True
        self.events = {}
        self.clock = Clock(max_fps=60)

    def run(self):
        while self.running:
            for window in Window.windows:
                window.update()
            self.update()
            self.clock.sleep()

    def event(self, func):
        num_params = len(inspect.signature(func).parameters)

        if func.__name__ == 'update' and num_params != 1:
            raise ValueError("The 'update' event handler must accept exactly 1 parameter (dt).")
        elif func.__name__ == 'fixed_update' and num_params != 1:
            raise ValueError("The 'fixed_update' event handler must accept exactly 1 parameter (fixed_dt).")

        self.events[func.__name__] = func
        return func

    def update(self):
        delta_time = self.clock.get_delta_time()
        self.clock.update_accumulator(delta_time)

        if 'update' in self.events:
            self.events['update'](delta_time)

        while self.clock.accumulator >= self.clock.fixed_delta_time:
            if 'fixed_update' in self.events:
                self.events['fixed_update'](self.clock.fixed_delta_time)
            self.clock.accumulator -= self.clock.fixed_delta_time