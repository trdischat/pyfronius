#!/usr/bin/env python
# -*- coding: utf-8 -*-

# general requirements
from .test_structure.server_control import Server
from .test_structure.fronius_mock_server import FroniusRequestHandler, FroniusServer

# For the server in this case
import time

ADDRESS = 'localhost'


def start_server(url=ADDRESS, port=0):
    # Create an arbitrary subclass of TCP Server as the server to be started
    # Here, it is an Simple HTTP file serving server
    handler = FroniusRequestHandler

    max_retries = 10
    r = 0
    server = None
    while not server:
        try:
            # Connect to any open port
            server = FroniusServer((url, port), handler)
        except OSError:
            if r < max_retries:
                r += 1
            else:
                raise
            time.sleep(1)

    server_control = Server(server)
    port = server_control.get_port()
    url = "http://{}:{}".format(ADDRESS, port)
    server_control.start_server()
    print("Server set up and reachable at")
    print("\t{}".format(url))
