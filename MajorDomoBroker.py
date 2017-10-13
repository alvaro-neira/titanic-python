import zmq
from zmq.eventloop.ioloop import IOLoop

from mdp.broker import MDPBroker


###

class MajorDomoBroker(MDPBroker):
    def __init__(self, verbose):
        self.context = zmq.Context()
        super(MajorDomoBroker, self).__init__(self.context, "tcp://127.0.0.1:5555")
        return

