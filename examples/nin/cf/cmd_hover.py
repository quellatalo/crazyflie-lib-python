import time

from examples.nin.cmd.command import Command


class CmdHover(Command):

    def __init__(self, cf, to_z, from_z = 0):
        super().__init__()
        self.cf = cf
        self.to_z = to_z
        self.from_z = from_z

    def pre_task(self):
        for y in range(int(self.from_z*10) ,int(self.to_z * 10)):
            self.cf.commander.send_hover_setpoint(0, 0, 0, y / 10)
            time.sleep(0.1)

    def loop_task(self):
        self.cf.commander.send_hover_setpoint(0, 0, 0, self.to_z)
        time.sleep(0.1)
