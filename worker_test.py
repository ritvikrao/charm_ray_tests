import ray
import time

@ray.remote
class Worker(object):
    def __init__(self):
        return

    def wait_test(self):
        return 0


def main(args):
    num_workers = 131072
    workers = [Worker.remote() for i in range(num_workers)]
    retvals = [workers[i].wait_test.remote() for i in range(num_workers)]
    for i in range(num_workers):
        print("Worker: ", i, " returned: ", ray.get(retvals[i]))


main([])
