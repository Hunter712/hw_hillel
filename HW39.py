import time


class Timer:

    def __init__(self, start_time=0, elapsed_time=0):
        self.start_time = start_time
        self.elapsed_time = elapsed_time

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self.elapsed_time += time.time() - self.start_time

    def reset(self):
        self.start_time = 0
        self.elapsed_time = 0


with Timer() as t:
    time.sleep(1)

print(t.elapsed_time)  # ~1 second
time.sleep(1)

with t:
    time.sleep(2)

print(t.elapsed_time)  # ~3 seconds

with Timer() as t2:
    time.sleep(1)

print(t2.elapsed_time)  # ~1 second
t2.reset()

with t2:
    time.sleep(2)

print(t2.elapsed_time)  # ~2 seconds
