Simple Python module to permit talking to the aql (www.aql.com) SMS gateway.

Sample usage:

import aqlsms
sms = aqlsms.aqlSMS('username', 'password')
print sms.credit()
sms.sendMessage('Hello, World!', '447788990099, originator='PyAQLSMS')

TODO
----
    * Fix logging (use logger?)
    * Implement sendtime
    * Better error handling/reporting
    * ...?
