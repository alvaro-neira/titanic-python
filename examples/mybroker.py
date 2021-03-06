# -*- coding: utf-8 -*-

__license__ = """
    This file is part of MDP.

    MDP is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    MDP is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with MDP.  If not, see <http://www.gnu.org/licenses/>.
"""
__author__ = 'Guido Goldstein'
__email__ = 'gst-py@a-nugget.de'

import zmq
from zmq.eventloop.ioloop import IOLoop

from mdp.broker import MDPBroker

###

class MyBroker(MDPBroker):

    pass
#
###

if __name__ == '__main__':
    context = zmq.Context()
    broker = MyBroker(context, "tcp://127.0.0.1:5555")
    IOLoop.instance().start()
    broker.shutdown()


### Local Variables:
### buffer-file-coding-system: utf-8
### mode: python
### End:
