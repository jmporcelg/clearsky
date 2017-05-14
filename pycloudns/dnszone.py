# -*- coding: UTF-8 -*-
class DnsZone():
    _api = None
    _args = None

    def __init__(self,api,args):
        self._api = api
        self._args = args

    def register_zone(self):
        response = self._api.register_zone(self._args['<domain>'],
                                       self._args['--zonetype'])
        return response['statusDescription']

    def remove_zone(self):
        response = self._api.remove_zone(self._args['<domain>'])
        return response['statusDescription']

    def list_zones(self):
        pages = self._api.get_pages_count(10)
        response = dict([(i, self._api.list_zones(i, 10)) for i in range(1, pages)])
        return response

    def search_zones(self):
        search = str(self._args['--search']) if self._args['--search'] else None
        pages = self._api.get_pages_count(10,search)
        response = dict([(i, self._api.list_zones(i, 10, search)) for i in range(1, pages)])
        return response

    def list_zone(self):
        response = self._api.list_records(self._args['<domain>'])
        return response

    def dump_zone(self):
        response = self._api.export_records(self._args['<domain>'])
        return response

    def getsoa_zone(self):
        response = self._api.get_soa_details(self._args['<domain>'])
        return response

    def stats_zone(self):
        response = self._api.get_zone_stats(self._args['<domain>'])
        return response

    def status_zone(self):
        response = {}
        response['is_updated'] = self._api.is_updated(self._args['<domain>'])
        response['update_status'] = self._api.update_status(self._args['<domain>'])
        return response

    def changestatus_zone(self):
        status = 1 if self._args['on'] else 0
        response = self._api.change_status(self._args['<domain>'], status)
        return response

    def update_zone(self):
        response = self._api.update_zone(self._args['<domain>'])
        return response['statusDescription']

    def updatesoa_zone(self):
        domain_name = self._args['<domain>']
        primary_ns = self._args['<primaryns>']
        admin_mail = self._args['<email>']
        refresh =  self._args['--refresh']
        retry = self._args['--retry'],
        expire = self._args['--expire'],
        default_ttl = self._args['--ttl']
        response = self._api.modify_soa_details(domain_name,primary_ns, \
                                admin_mail,refresh,retry,expire,default_ttl)
        return response['statusDescription']

    def nameservers_zone(self):
        response = self._api.available_name_servers(self._args['<domain>'])
        return response

    def repr(self):
        return "dns zone helper class"
