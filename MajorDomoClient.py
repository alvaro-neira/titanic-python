import zmq
from zmq.eventloop.ioloop import IOLoop
from mdp.client import MDPClient


class MajorDomoClient(MDPClient):
    def __init__(self, context, endpoint, servicename):
        super(MajorDomoClient, self).__init__(context, endpoint, servicename)
        return

    def on_message(self, msg):
        print("Received:", repr(msg))
        IOLoop.instance().stop()
        return

    def on_timeout(self):
        print('TIMEOUT!')
        IOLoop.instance().stop()
        return
