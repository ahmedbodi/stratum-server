'''
This module contains interfaces for interacting with the rest of the world
'''
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()

from builtins import object
from thimble import Thimble
from twisted.python.threadpool import ThreadPool
from twisted.internet import reactor, defer, task, threads, _sslverify
from stratum.custom_exceptions import RemoteServiceException
from cachetools import cached, TTLCache
import lib.settings as settings
import lib.logger
from lib.utils import slugify, as_deferred
import time

_the_thread_pool = ThreadPool()
_sslverify.platformTrust = lambda : None
log = lib.logger.get_logger('interfaces')

class TimestamperInterface(object):
    ''' Provide Time as a UNIX Timestamp for API Users '''

    @cached(cache=TTLCache(maxsize=1024, ttl=2))
    def time(self):
        return time.time()

class Interfaces(object):
    redisConn = None
    timestamper = None

    @classmethod
    def set_redis_connection(cls, connection):
        cls.redisConn = connection

    @classmethod
    def set_timestamper(cls, manager):
        cls.timestamper = manager

