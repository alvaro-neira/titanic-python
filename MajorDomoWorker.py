import zmq
from zmq.eventloop.ioloop import IOLoop

from mdp.worker import MDPWorker


###

class MajorDomoWorker(MDPWorker):
    HB_INTERVAL = 1000
    HB_LIVENESS = 3

    count = 0

    def __init__(self, endpoint, servicename, verbose=""):
        self.context = zmq.Context()
        super(MajorDomoWorker, self).__init__(self.context, endpoint, servicename)
        return

    def on_request(self, msg):
        self.count = self.count + 1
        self.reply(msg)
        return

    def recv(self,reply):
        print "ERROR: recv not implemented"
        return 0


#
###

if __name__ == '__main__':
    context = zmq.Context()
    worker = MyWorker(context, "tcp://127.0.0.1:5555", b"echo")
    IOLoop.instance().start()
    worker.shutdown()


### Local Variables:
### buffer-file-coding-system: utf-8
### mode: python
### End:
