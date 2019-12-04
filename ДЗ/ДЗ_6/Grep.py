import functools
import time


def coroutine(gen):
    @functools.wraps(gen)
    def start(*args, **kwargs):
        cr = gen(*args, **kwargs)
        next(cr)
        return cr
    return start


@coroutine
def grep(pattern, target):
    print("Looking for %s" % pattern)
    try:
        while True:
            line = (yield)
            if pattern in line:
                target.send(line)
    except Exception:
        print("Finished")


@coroutine
def printer():
    while True:
        line = (yield)
        print(line)


@coroutine
def dispenser(targets):
    while True:
        item = (yield)
        for target in targets:
            target.send(item)


def follow(file, target):
    file.seek(0, 2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)
            continue
        target.send(line)


if __name__ == "__main__":

    with open('log.txt') as f_open:
        follow(f_open,
               dispenser([
                   grep('python', printer()),
                   grep('is', printer()),
                   grep('great', printer()),
               ])
               )
