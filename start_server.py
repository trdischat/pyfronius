#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyfronius.tests.mock_server import start_server

if __name__ == '__main__':
    start_server('localhost', 33442)
    input("Press any key to stop\n")
