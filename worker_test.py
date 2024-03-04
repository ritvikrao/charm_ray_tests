import ray
import time

@ray.remote
class Worker(object):
    def __init__(self):
        return

    def wait_test(self):
        return


def main(args):
    num_workers = 131072
    workers = [Worker.remote() for i in range(num_workers)]
    for i in range(num_workers):
        print("Spawning worker: ", i)
        workers[i].wait_test.remote()


main([])
