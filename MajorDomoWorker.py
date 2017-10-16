import zmq
from zmq.eventloop.ioloop import IOLoop
from pprint import pprint
from mdp.worker import MDPWorker


class MajorDomoWorker(MDPWorker):
    HB_INTERVAL = 1000
    HB_LIVENESS = 3

    count = 0

    def __init__(self, endpoint, servicename):
        self.context = zmq.Context()
        super(MajorDomoWorker, self).__init__(self.context, endpoint, servicename)
        return

    def on_request(self, msg):
        print "on request"
        pprint(msg)
        self.count = self.count + 1
        self.reply(msg)
        return

    def recv(self, reply):
        print "ERROR: recv not implemented"
        return 0
