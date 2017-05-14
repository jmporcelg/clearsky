# clearsky
Client for the CloudDNS.net nameserver management service

*This code is a work in progress*, but it implements most of the API functionality offered by www.cloudns.net for managing nameservers. Clearsky can be used as a CLI tool or as a library for any Python script.

**Important**, you must have an account on cloudns.net, fill auth.ini with your username and password.

## requirements

* python3
* docopt
* configparser
* pprint
* requests
* json

## basic usage

You can see all options available by just running 

```clearsky -h```

**Examples**

Working with zones:

* Add a new zone of type master

```clearsky zone new domainname --ztype=master```

* Remove a zone

```clearsky zone remove domainname```

* Dump a zone in BIND format

```clearsky zone dump domainname```

Adding new record to a zone:

```clearsky.py record add A 192.168.1.1 --host=subomain.domaintest-21.net domaintest-21.net```

Adding new record to a zone with 1h TTL:

```clearsky.py record add A 192.168.1.1 --host=subomain.domaintest-21.net --ttl=3600 domaintest-21.net```

### clearsky CLI

![gif](http://i.imgur.com/24vS6VE.gif)
