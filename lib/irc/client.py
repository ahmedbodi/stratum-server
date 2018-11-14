from stratum.irc import IRCClient
from twisted.internet import defer

class IRCBot(IRCClient):

    def command_op(self, user, channel, message):
        line = 'MODE %s +o %s' % (channel, user)
        self.sendLine(line)
        return 'Opped!'

    def command_deop(self, user, channel, message):
        self.sendLine('MODE %s -o %s' % (channel, user));
        return 'De Opped!'

    def privmsg(self, user, channel, message):
        nick, _, host = user.partition('!')
        message = message.strip()
        if not message.startswith('!'):  # not a trigger command
            return  # so do nothing
        command, sep, rest = message.lstrip('!').partition(' ')
        # Get the function corresponding to the command given.
        func = getattr(self, 'command_' + command, None)
        # Or, if there was no function, ignore the message.
        if func is None:
            return
        d = defer.maybeDeferred(func, nick, channel, rest)
        d.addErrback(self._showError)
        # Whatever is returned is sent back as a reply:
        if channel == self.nickname:
            # When channel == self.nickname, the message was sent to the bot
            # directly and not to a channel. So we will answer directly too:
            d.addCallback(self._sendMessage, nick)
        else:
            # Otherwise, send the answer to the channel, and use the nick
            # as addressing in the message itself:
            d.addCallback(self._sendMessage, channel, nick)

    def command_ping(self, user, channel, message):
        return 'Pong.'

    def command_fishslap(self, user, channel, message):
        self.say(channel, 'slaps %s round the head' % (message.split(' ')[0]))

