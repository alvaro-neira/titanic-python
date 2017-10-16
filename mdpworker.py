import zmq
from MajorDomoWorker import MajorDomoWorker
from zmq.eventloop.ioloop import IOLoop


def main():
    worker = MajorDomoWorker("tcp://127.0.0.1:5555", b"echo")
    IOLoop.instance().start()
    worker.shutdown()


if __name__ == '__main__':
    main()
