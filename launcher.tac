# Run me with "twistd -ny launcher.tac -l -"

# Add conf directory to python path.
# Configuration file is standard python module.
import os, sys
sys.path = [os.path.join(os.getcwd(), 'conf'),] + sys.path + [os.path.join(os.getcwd(), '.'), ]

from twisted.internet import defer
from twisted.internet.defer import setDebugging
setDebugging(True)

from twisted.application.service import Application, IProcess

# Run listening when services service is ready
on_startup = defer.Deferred()

import stratum
import lib.settings as settings

# Bootstrap Stratum framework
application = stratum.setup(on_startup)
IProcess(application).processName = settings.STRATUM_SERVER_PROCESS_NAME

# Load services service into stratum framework
import services
from services.interfaces import Interfaces, TimestamperInterface

Interfaces.set_timestamper(TimestamperInterface())
services.setup(on_startup)
