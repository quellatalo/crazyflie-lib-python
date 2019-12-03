import time

from examples.nin.cmd.command import Command


class ExampleCmd(Command):

    def __init__(self):
        super().__init__()
        self.i = 0

    def pre_task(self):
        print('pre')

    def loop_task(self):
        self.i += 1
        print(self.i)
        time.sleep(0.1)
