from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division

from stratum.services import GenericService
from .interfaces import Interfaces
import lib.logger

log = lib.logger.get_logger('mining')

class ServerService(GenericService):
    '''This service provides public API for OpenBlock News'''

    service_type = 'server'
    service_vendor = 'OpenBlock'
    is_default = True

    def time(self):
        return Interfaces.timestamper.time()
    time.help_text = "Get Server Time"
    time.params = []

