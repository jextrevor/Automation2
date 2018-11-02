import os
import bluetooth
from wakeonlan import send_magic_packet

bluetooth_address = os.environ['BLUETOOTH_ADDRESS']
wol_address = os.environ['WOL_ADDRESS']

def is_here(addr):
    if bluetooth.lookup_name( addr ) is not None:
        return True
    else:
        return False

def arrived():
    send_magic_packet(wol_address)

def left():
    pass

def loop():
    old_here = False
    while True:
        here = is_here(bluetooth_address)
        if old_here is False and here is True:
            old_here = True
            arrived()
        elif old_here is True and here is False:
            old_here = False
            left()

loop()
