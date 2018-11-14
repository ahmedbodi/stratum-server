from stratum.irc import IRCClientFactory, log
from .client import IRCBot

class IRCClientFactory(IRCClientFactory):
    protocol = IRCBot
