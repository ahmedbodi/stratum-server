'''
This is example configuration for Stratum server.
Please rename it to config.py and fill correct values.
'''
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

# ******************** GENERAL SETTINGS ***************

# Enable some verbose debug (logging requests and responses).
DEBUG = True

# Destination for application logs, files rotated once per day.
LOGDIR = 'log/'

# Main application log file.
LOGFILE = None #'stratum.log'

# Possible values: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOGLEVEL = 'DEBUG'

# How many threads use for synchronous methods (services).
# 30 is enough for small installation, for real usage
# it should be slightly more, say 100-300.
THREAD_POOL_SIZE = 300

# ******************** TRANSPORTS *********************

# Hostname or external IP to expose
HOSTNAME = 'stratum.example.com'

# Port used for Socket transport. Use 'None' for disabling the transport.
LISTEN_SOCKET_TRANSPORT = 3333

# Port used for HTTP Poll transport. Use 'None' for disabling the transport
LISTEN_HTTP_TRANSPORT = 8000

# Port used for HTTPS Poll transport
LISTEN_HTTPS_TRANSPORT = 8001

# Port used for WebSocket transport, 'None' for disabling WS
LISTEN_WS_TRANSPORT = 8002

# Port used for secure WebSocket, 'None' for disabling WSS
LISTEN_WSS_TRANSPORT = 8003

# ******************** SSL SETTINGS ******************

# Private key and certification file for SSL protected transports
# You can find howto for generating self-signed certificate in README file
SSL_PRIVKEY = 'server.key'
SSL_CACERT = 'server.crt'

# ******************** TCP SETTINGS ******************

# Enables support for socket encapsulation, which is compatible
# with haproxy 1.5+. By enabling this, first line of received
# data will represent some metadata about proxied stream:
# PROXY <TCP4 or TCP6> <source IP> <dest IP> <source port> </dest port>\n
#
# Full specification: http://haproxy.1wt.eu/download/1.5/doc/proxy-protocol.txt
TCP_PROXY_PROTOCOL = False

# ******************** HTTP SETTINGS *****************

# Keepalive for HTTP transport sessions (at this time for both poll and push)
# High value leads to higher memory usage (all sessions are stored in memory ATM).
# Low value leads to more frequent session reinitializing (like downloading address history).
HTTP_SESSION_TIMEOUT = 3600 # in seconds

# Maximum number of messages (notifications, responses) waiting to delivery to HTTP Poll clients.
# Buffer length is PER CONNECTION. High value will consume a lot of RAM,
# short history will cause that in some edge cases clients won't receive older events.
HTTP_BUFFER_LIMIT = 10000

# User agent used in HTTP requests (for both HTTP transports and for proxy calls from services)
USER_AGENT = 'Stratum/0.1'

# Provide human-friendly user interface on HTTP transports for browsing exposed services.
BROWSER_ENABLE = True

# Use "./signature.py > signing_key.pem" to generate unique signing key for your server
SIGNING_KEY = None # Message signing is disabled
#SIGNING_KEY = 'signing_key.pem'

# Origin of signed messages. Provide some unique string,
# ideally URL where users can find some information about your identity
SIGNING_ID = None
#SIGNING_ID = 'stratum.somedomain.com' # Use custom string
#SIGNING_ID = HOSTNAME # Use hostname as the signing ID

STRATUM_SERVER_PROCESS_NAME = u'stratum-wamp-server'

