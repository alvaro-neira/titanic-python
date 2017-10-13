import zmq
from zmq.eventloop.ioloop import IOLoop
from mdp.client import MDPClient


class MajorDomoClient(MDPClient):
    def __init__(self, endpoint, verbose):
        self.context = zmq.Context()
        super(MajorDomoClient, self).__init__(self.context, endpoint, b"echo")
        return

    def on_message(self, msg):
        print("Received:", repr(msg))
        IOLoop.instance().stop()
        return

    def on_timeout(self):
        print('TIMEOUT!')
        IOLoop.instance().stop()
        return
