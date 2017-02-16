# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import tornado.ioloop
import tornado.web
import threading
import time
import webbrowser


class LocalServer(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


server_thread = None
app = 1

def local():
    # 1. start a websocket server in background
    global server_thread
    global app
    app = tornado.web.Application([
        (r"/", LocalServer),
    ])
    app.listen(8888)
    server_thread = threading.Thread(
        target=tornado.ioloop.IOLoop.current().start
    )
    server_thread.start()
    webbrowser.open("http://127.0.0.1:8888")
    # setup a basic server serving all files
    # open the server url in browser
    # register a signal handler or something to cleanup the server


def wait():
    try:
        time.sleep(1e7)
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.current().stop()
    print("Done")
