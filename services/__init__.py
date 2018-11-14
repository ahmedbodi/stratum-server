from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from .service import ServerService
from twisted.internet import defer, reactor
from twisted.internet.endpoints import clientFromString
from twisted.internet.protocol import Factory
import txredisapi as redis

@defer.inlineCallbacks
def setup(on_startup):
    u'''Setup services service internal environment.
    You should not need to change this. If you
    want to use another Worker manager or Share manager,
    you should set proper reference to Interfaces class
    *before* you call setup() in the launcher script.'''

    import lib.settings as settings

    # Get logging online as soon as possible
    import lib.logger
    log = lib.logger.get_logger(u'services')

    from .interfaces import Interfaces
    from lib.irc.client import IRCClient
    from lib.irc.factory import IRCClientFactory

    if settings.IRC_NICK:
       log.info("Starting IRC Bot")
       reactor.connectTCP(settings.IRC_SERVER, settings.IRC_PORT, IRCClientFactory(settings.IRC_ROOM, settings.IRC_NICK, settings.IRC_HOSTNAME))


    if settings.REDIS_HOST:
       log.info("Setting Up Redis Connection")
       redisConn = yield redis.lazyConnectionPool(settings.REDIS_HOST, settings.REDIS_PORT, settings.REDIS_DBID, reconnect=True)
       Interfaces.set_redis_connection(redisConn)

    log.info(u"SERVICES IS READY")
    yield on_startup.callback(True)
