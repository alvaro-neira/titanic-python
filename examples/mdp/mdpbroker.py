import logging
import sys
import time
from binascii import hexlify
from MajorDomoBroker import MajorDomoBroker
import zmq
from zmq.eventloop.ioloop import IOLoop
from pprint import pprint


def _on_msg(msg):
    print 'broker received:',
    pprint(msg)
    target = msg.pop(0)
    marker_frame = msg.pop(0)
    if msg[1] == b'\x01':  # ready
        print 'READY'
        target = msg[0]
        return
    if msg[1] == b'\x04':  # ready
        print 'HB'
        return
    if msg[1] == b'\x03':  # reply
        IOLoop.instance().stop()
        return
    return


def main():
    broker = MajorDomoBroker()
    IOLoop.instance().start()
    broker.shutdown()


if __name__ == '__main__':
    main()
