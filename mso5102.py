#!/usr/bin/env python

import sys
import logging
import usb

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def list_devices():
    """Returns a list of all the MSO5102 and similar devices found"""
    return usb.core.find(idVendor=0x49f, idProduct=0x505a, find_all=True)

class MSO5102(object):
    """Basic class to control an Hantek / Tekway / Voltcraft MSO5xxx oscilloscope"""
    def __init__(self, dev):
        if dev.is_kernel_driver_active(0):
            dev.detach_kernel_driver(0)
        self.dev = dev

    def echo(self):
        pass

if __name__ == '__main__':
    devices = list_devices()

    if not devices:
        logger.debug('No device found')
        sys.exit(1)

    d = MSO5102(devices[0])
