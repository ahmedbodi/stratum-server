#!/usr/bin/env python
# Send notification to Stratum mining instance add a new litecoind instance to the pool

import socket
import json
import sys
import time

message = {'id': 1, 'method': 'server.time', 'params': []}

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 3333))
    s.sendall(json.dumps(message)+"\n")
    data = s.recv(200000000)
    s.close()
except IOError:
    print "addlitecoind: Cannot connect to the pool"
    sys.exit()

for line in data.split("\n"):
    print line
