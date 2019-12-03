import logging

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie

logging.basicConfig(level=logging.ERROR)


class CfCom:
    def __init__(self, URI):
        cflib.crtp.init_drivers(enable_debug_driver=False)
        self.URI = URI
        self.scf = SyncCrazyflie(self.URI, cf=Crazyflie(rw_cache='./cache'))

    def __del__(self):
        self.scf.close_link()

    def open_link(self):
        self.scf.open_link()

    def close_link(self):
        self.scf.close_link()

    def __enter__(self):
        self.scf.open_link()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.scf.close_link()
