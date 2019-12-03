import abc
import time


class Command:

    def __init__(self):
        self.active = False

    def execute(self):
        self.active = True
        self.pre_task()
        while self.active:
            self.loop_task()

    @abc.abstractmethod
    def pre_task(self):
        pass

    @abc.abstractmethod
    def loop_task(self):
        pass

    def end(self):
        self.active = False