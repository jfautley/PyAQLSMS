import urllib, urllib2

class aqlSMS(object):
    # Current AQL SMS gateway URL, as of Jan 2013
    AQL_GATEWAY = "http://gw.aql.com/sms/sms_gw.php"

    def __init__(self, username, password, gateway=AQL_GATEWAY, originator=None):
        self.username   = username
        self.password   = password
        self.gateway    = gateway
        self.originator = originator

    def __str__(self):
        return "aql SMS gateway interface, as user [%s] and talking to %s" % (self.username, self.gateway)

    def credit(self):
        """ Get our remaining aql SMS credits """
        request_data = urllib.urlencode({'username': self.username, 'password': self.password, 'cmd': 'credit' })

        # Our request object
        #request = urllib2.Request(self.gateway, request_data)
        # XXX: Due to an issue with the aql API, we have to query our credit balance via the 'old' system... grr.
        request = urllib2.Request('http://gw1.aql.com/sms/postmsg.php', request_data)
        # Make the request...
        try:
            response = urllib2.urlopen(request)
        except urllib2.URLError as e:
            print "Unable to query: [%s]" % e
            return False

        aql_response = response.read()

        if (aql_response.startswith('AQSMS-CREDIT')):
            return aql_response.split('=')[1]
        elif aql_response.startswith('AQSMS-AUTHERROR'):
            raise Exception('Authentication Error')
        else:
            raise Exception('Unknown Response from aql Gateway: [%s]' % aql_response)

    def sendMessage(self, message, destination, originator=None, flash=None):
        """ Send an SMS message via the aql HTTP API """
        if originator == None and self.originator != None:
            originator = self.originator

        # Build our basic query string
        message_data = {'username': self.username, 'password': self.password, 'destination': destination, 'message': message}

        # If we have a different originator specified for our message, use it.
        if originator:
            message_data['originator'] = originator

        # Are we sending this as a flash message?
        if flash:
            message_data['flash'] = 1

        print message_data

        # Build our request object
        request = urllib2.Request(self.gateway, urllib.urlencode(message_data))

        # Attempt our request to aql, trap for errors
        try:
            response = urllib2.urlopen(request)
        except urllib2.URLError as e:
            print "Unable to query: [%s]" % e
            return False

        aql_response = response.read()
        (aql_numresponse, aql_message) = aql_response.split(' ', 1)
        (aql_returncode, aql_creditsused) = aql_numresponse.split(':')

        print aql_response

        print "Num response [%s], return code [%s], credits used [%s], message [%s]" % (aql_numresponse, aql_returncode, aql_creditsused, aql_message)
