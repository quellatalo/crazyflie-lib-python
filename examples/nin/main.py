from examples.nin.cmd.commander import Commander
from examples.nin.cmd.example_cmd import ExampleCmd
from examples.nin.cf.cmd_hover import CmdHover
from examples.nin.cf.cmd_land import CmdLand
from examples.nin.cfcom import CfCom

URI = 'radio://0/80/2M'

class Main:
    def __init__(self):
        self.com = CfCom(URI)
        self.commander = Commander()
        self.choices = {
            'start': self.cmd_start,
            'stop': self.cmd_stop,
            'queue': self.cmd_queue,
            'next':self.cmd_next
        }
        self.loop = True

    def cmd_start(self):
        self.commander.start()

    def cmd_stop(self):
        self.commander.stop()

    def cmd_queue(self):
        self.commander.queue_command(CmdLand(self.com.scf.cf,0.4))

    def cmd_next(self):
        self.commander.next_command()

    def quit(self):
        self.loop = False
        self.commander.stop()

    def get_cmd(self, str):
        return self.choices.get(str, self.quit)

    def main(self):
        with self.com:
            self.commander.queue_command(CmdHover(self.com.scf.cf,0.4))
            while self.loop:
                print('Commands: start | stop | queue | next')
                print('Instructions: hover | stop | queue | next')
                self.get_cmd(input('your command?'))()


if __name__ == '__main__':

    Main().main()