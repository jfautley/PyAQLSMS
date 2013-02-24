### Simple Python module to permit talking to the aql (www.aql.com) SMS gateway. ###

Sample usage:
```python
import aqlsms
sms = aqlsms.aqlSMS('username', 'password')
print sms.credit()
sms.sendMessage('Hello, World!', '447788990099, originator='PyAQLSMS')
```

_TODO_
* Fix logging (use logger?)
* Implement sendtime
* Better error handling/reporting
* ...?
