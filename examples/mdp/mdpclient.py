import zmq
from zmq.eventloop.ioloop import IOLoop

from mdp.client import MDPClient, mdp_request

if __name__ == '__main__':
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.setsockopt(zmq.LINGER, 0)
    socket.connect("tcp://127.0.0.1:5555")
    res = mdp_request(socket, b'echo', [b'TEST'], 2.0)
    if res:
        print "Reply:", repr(res)
    else:
        print 'Timeout!'
    socket.close()
