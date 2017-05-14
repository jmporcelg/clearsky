# -*- coding: UTF-8 -*-
class DnsRecord():
    _api = None
    _args = None

    def __init__(self,api,args):
        self._api = api
        self._args = args

    def add_record(self):
        domain = self._args['<domain>']
        host = str(self._args['--host']) if self._args['--host'] else None
        record_type = self._args['<record_type>']
        record = self._args['<record>']
        ttl = str(self._args['--ttl']) if self._args['--ttl'] else 300
        response = self._api.add_record(domain,record_type,host,record,ttl)
        return response['statusDescription']

    def remove_record(self):
        response = self._api.delete_record(self._args['<domain>'],self._args['<id>'])
        return response['statusDescription']

    def list_records(self):
        response = self._api.get_available_record_types(self._args['--rztype'])
        return response

    def repr(self):
        return "dns record helper class"
