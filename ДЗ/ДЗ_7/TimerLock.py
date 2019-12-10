from contextlib import ContextDecorator
import time


class LockedTimer(ContextDecorator):

    def __init__(self, text):
        self.text = text

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("{}: {}".format(self.text, time.time() - self.start_time))


if __name__ == "__main__":

    with LockedTimer("executing..."):
        for i in range(10000000):
            pass
