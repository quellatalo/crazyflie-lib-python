import queue
import threading
from examples.nin.cmd.cmd_idle import CmdIdle


class Commander:
    def __init__(self):
        self.active = False
        self.commands = queue.Queue()
        self.thread = threading.Thread(target=self.run)
        self.currentCmd = CmdIdle()

    def run(self):
        while self.active:
            if not self.commands.empty():
                self.currentCmd = self.commands.get()
                self.currentCmd.execute()

    def start(self):
        self.active = True
        self.thread.start()

    def stop(self):
        self.active = False
        self.currentCmd.end()

    def queue_command(self, cmd):
        self.commands.put(cmd)

    def next_command(self):
        self.currentCmd.end()