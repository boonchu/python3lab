import threading
import time

def repeat_every(n, func, *args, **kwargs):
    def and_again():
        func(*args, **kwargs)
        t = threading.Timer(n, and_again)
        t.daemon = True
        t.start()
    t = threading.Timer(n, and_again)
    t.daemon = True
    t.start()


def scheduled_task(msg='hello, world', **kwargs):
    print time.time(), "scheduled_task:", msg, kwargs

repeat_every(.5, scheduled_task )
repeat_every(1, scheduled_task, "Slow", name="Hand luke")

for x in range(5):
    print time.time(), "Main: busy as a bee."
    time.sleep(3)
