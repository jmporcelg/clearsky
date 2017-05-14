#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""Clearsky manages www.cloudns.net DNS services via command line

Usage:
  clearsky.py zone (new [--zonetype=(master|slave)]| remove | update | dump | chstatus (on|off) | status | getsoa | stats) <domain>
  clearsky.py (list | list [<domain>] | list [--search=key])
  clearsky.py record (add <record_type> <record> [--host=@] [--ttl=seconds] | remove <id>) <domain>
  clearsky.py records [--rztype=(domain|reverse|parked)]
  clearsky.py updatesoa <primaryns> <email> [--refresh=s --retry=s --expire=s --ttl=s] <domain>
  clearsky.py nameservers
  clearsky.py --version

Options:
  -h --help      Show this screen.
  --host=@       Target host or domain (i.e.: subdomain.example.com) [default: None]
  --zonetype=str Master or slave  [default: master].
  --rztype=str   Domain, reverse or parked zone types [default: domain].
  --refresh=int  SOA refresh rate time in seconds, 1200 to 43200 [default: 1200].
  --retry=int    SOA retry rate time in seconds, 180 to 2419200 [default: 180].
  --expire=int   SOA expire time in seconds, 1209600 to 2419200 [default: 1209600].
  --ttl=int      SOA and record ttl time in seconds [default: 300].
  --version      Show version.
"""
from docopt import docopt
from pycloudns import ClouDNS
from dnszone import DnsZone
from dnsrecord import DnsRecord
from pprint import pprint
import configparser

def getapi():
    config = configparser.ConfigParser()
    config.readfp(open("auth.ini"))
    api = ClouDNS(config.get('ClouDNS','api_url'),
        	      config.get('ClouDNS','api_username'),
        	      config.get('ClouDNS','api_password'))
    return api

def getarguments():
    return docopt(__doc__, version='Almost Ready 0.9')

def op_zone():
    args = getarguments()
    api = getapi()
    zone = DnsZone(api,args)
    if args['new']:
        print(zone.register_zone())
    elif args['remove']:
        print(zone.remove_zone())
    elif args['update']:
        print(zone.update_zone())
    elif args['status']:
        pprint(zone.status_zone())
    elif args['chstatus']:
        print(zone.changestatus_zone())
    elif args['dump']:
        pprint(zone.dump_zone())
    elif args['getsoa']:
        pprint(zone.getsoa_zone())
    elif args['updatesoa']:
        print(zone.updatesoa_zone())
    elif args['stats']:
        pprint(zone.stats_zone())
    elif args['nameservers']:
        pprint(zone.nameservers_zone())

def op_zonelisting():
    args = getarguments()
    api = getapi()
    zone = DnsZone(api,args)
    if args['list'] and args['<domain>']:
        pprint(zone.list_zone())
    elif args['list'] and args['--search']:
        pprint(zone.search_zones())
    else:
        pprint(zone.list_zones())

def op_record():
    args = getarguments()
    api = getapi()
    zone = DnsRecord(api,args)
    if args['add']:
        print(zone.add_record())
    if args['remove']:
        print(zone.remove_record())
    if args['records']:
        pprint(zone.list_records())

if __name__ == '__main__':
    args = getarguments()
    if args['zone'] or args['updatesoa'] or args['nameservers']:
        op_zone()
    elif args['list']:
        op_zonelisting()
    elif args['record'] or args['records']:
        op_record()
