
import inspect
import time
from queue import Queue

def register(worker):
    caller_frame = inspect.currentframe().f_back
    self = caller_frame.f_locals['self']
    if not hasattr(self, "__work__"):
        raise Exception("trying to register subworker to non-worker")
    if not hasattr(self, "__subworkers__"):
        self.__subworkers__ = set()
    if worker not in self.__subworkers__:
        self.__subworkers__.add(worker)

def unregister(worker):
    caller_frame = inspect.currentframe().f_back
    self = caller_frame.f_locals['self']
    if not hasattr(self, "__work__"):
        raise Exception("trying to unregister subworker to non-worker")
    if not hasattr(self, "__subworkers__"):
        self.__subworkers__ = set()
    if worker in self.__subworkers__:
        self.__subworkers__.remove(worker)

class MyClass:
    def __init__(self):
        pass

    def __work__(self):
        print("I am working")   # Runs every tick

class RootWorker:
    def __work__(self):
        if 

root = RootWorker()
while True:
    visited = set()
    targets = Queue()
    targets.put(root)
    while not targets.empty():
        target = targets.get()
        if target in visited:
            continue
        visited.add(target)
        if hasattr(target, "__work__"):
            target.__work__()
        if hasattr(target, "__subworkers__"):
            for subworker in target.__subworkers__:
                targets.put(subworker)
    time.sleep(0.001)

