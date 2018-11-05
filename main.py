import os
import bluetooth
import time
from wakeonlan import send_magic_packet
from validators import mac_address

def validateMac(address):
    if mac_address(address):
        return address
    raise ValueError('"'+ address+ '" is not a valid MAC address')

def is_here(addr):
    if bluetooth.lookup_name( addr ) is not None:
        return True
    else:
        return False

def arrived():
    if wol_address is not None:
        send_magic_packet(wol_address)
    #TODO: Add code to play music/give notifications about email

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
        if here is True:
            time.sleep(timeout)

bluetooth_address = validateMac(os.environ['BLUETOOTH_ADDRESS'])
try:
    wol_address = validateMac(os.environ['WOL_ADDRESS'])
except KeyError:
    wol_address = None
try:
    timeout = int(os.environ['TIMEOUT'])
except KeyError:
    timeout = 150

loop()
