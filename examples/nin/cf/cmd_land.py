import time

from examples.nin.cmd.command import Command


class CmdLand(Command):

    def __init__(self, cf, from_z):
        super().__init__()
        self.cf = cf
        self.from_z = from_z

    def pre_task(self):
        for y in range(int(self.from_z*10),2 ,-1):
            self.cf.commander.send_hover_setpoint(0, 0, 0, y / 10)
            time.sleep(0.1)
        self.end()

    def loop_task(self):
        None
