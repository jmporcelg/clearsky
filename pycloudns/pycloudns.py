# -*- coding: UTF-8 -*-
import requests,json
import sys

class ClouDNS:
 _api_username = None
 _api_password = None
 _api_url      = None

 def __init__(self, api_json_url,api_username,api_password):
  requests.packages.urllib3.disable_warnings()
  params = {
            'auth-id':api_username,
            'auth-password':api_password
           }
  resp = requests.get(url=api_json_url+"/login.json", params=params,verify=False)
  data = json.loads(resp.text)
  if not data['status'] == 'Success':
      print("Could not login into the API, exiting")
      sys.exit()
  else:
   self._api_url      = api_json_url
   self._api_username = api_username
   self._api_password = api_password

 def _do_request(self,api_action,api_params):
   auth = {
            'auth-id':self._api_username,
            'auth-password':self._api_password,
          }
   api_params.update(auth)
   resp = requests.get(url=str(self._api_url)+str(api_action),
                       params=api_params,
                       verify=False)
   data = json.loads(resp.text)
   return data

 def get_pages_count(self,rowsperpage=100,search=None):
   params = {
                'rows-per-page':rowsperpage,
                'search':search
            }
   return self._do_request('get-pages-count.json',params)

 def list_zones(self,page=1,rowsperpage=100,search=None):
   params = {
             'page':page,
             'rows-per-page':rowsperpage,
             'search':search
            }
   return self._do_request('list-zones.json',params)

 def is_updated(self,domain_name):
  params = { 'domain-name':domain_name }
  return self._do_request('is-updated.json',params)

 def update_status(self,domain_name):
  params = { 'domain-name':domain_name }
  return self._do_request('update-status.json',params)

 def update_zone(self,domain_name):
  params = { 'domain-name':domain_name }
  return self._do_request('update-zone.json',params)

 def change_status(self,domain_name,status):
  params = {
            'domain-name':domain_name,
            'status':status
           }
  return self._do_request('change-status.json',params)

 def register_zone(self,domain_name,zone_type='master',ns=None,master_ip=None):
  params = {
             'domain-name':domain_name,
             'zone-type': zone_type,
             'ns': ns,
             'master-ip': master_ip
            }
  return self._do_request('register.json',params)

 def remove_zone(self,domain_name):
  params = { 'domain-name':domain_name }
  return self._do_request('delete.json',params)

 def list_records(self,domain_name):
  params = { 'domain-name':domain_name }
  return self._do_request('records.json',params)

 def add_record(self,
                domain_name,
                record_type,
                host,
                record,
                ttl,
                **kwargs):
   params = {
              'domain-name':domain_name,
              'record-type':record_type,
              'host':host,
              'record':record,
              'ttl':ttl,
            }
   if kwargs:
    params.update(kwargs)
   return self._do_request('add-record.json',params)

 def modify_record(self,
                domain_name,
                record_id,
                host,
                record,
                ttl,
                **kwargs):
   params = {
              'domain-name':domain_name,
              'record-id':record_id,
              'host':host,
              'record':record,
              'ttl':ttl,
            }
   if kwargs:
    params.update(kwargs)
   return self._do_request('mod-record.json',params)

 def copy_records(self,domain_name,from_domain,delete_current_records=0):
   params = {
              'domain-name':domain_name,
              'from-domain':from_domain,
              'delete_current_records': delete_current_records
            }
   return self._do_request('copy-records.json',params)

 def delete_record(self,domain_name,record_id):
   params = {
              'domain-name':domain_name,
              'record-id':record_id
            }
   return self._do_request('delete-record.json',params)

 def export_records(self,domain_name):
  params = { 'domain-name':domain_name }
  return self._do_request('records-export.json',params)

 def get_available_record_types(self,zone_type):
  params = { 'zone-type':zone_type }
  return self._do_request('get-available-record-types.json',params)

 def get_soa_details(self,domain_name):
   params = { 'domain-name':domain_name }
   return self._do_request('soa-details.json',params)

 def get_zone_stats(self,domain_name):
    params = { 'domain-name':domain_name }
    return self._do_request('get-zones-stats.json',params)

 def modify_soa_details(self,
                        domain_name,
                        primary_ns,
                        admin_mail='info@ClouDNS.net',
                        refresh=1200,
                        retry=180,
                        expire=1209600,
                        default_ttl=2400,
                        ):
    params = {
               'domain-name':domain_name,
               'primary-ns':primary_ns,
               'admin-mail':admin_mail,
               'refresh':refresh,
               'retry':retry,
               'expire':expire,
               'default-ttl':default_ttl
             }
    return self._do_request('modify-soa.json',params)

 def axfr_import(self,domain_name,server):
    params = {
               'domain-name':domain_name,
               'server':server
             }
    return self._do_request('axfr-import.json',params)

 def add_master_server(self,domain_name,master_ip):
    params = {
                'domain-name':domain_name,
                'master-ip':master_ip
             }
    return self._do_request('add-master-server.json',params)

 def delete_master_server(self,domain_name,master_id):
    params = {
                'domain-name':domain_name,
                'master-id':master_id
             }
    return self._do_request('delete-master-server.json',params)

 def list_master_servers(self,domain_name,master_ip):
    params = { 'domain-name':domain_name }
    return self._do_request('master-servers.json',params)

 def available_name_servers(self,domain_name):
    params = { 'domain-name':domain_name }
    return self._do_request('available-name-servers.json',params)

 def get_zones_statistics(self):
   return self._do_request('get-zones-stats.json',{})

 def get_dynamic_url(self,domain_name,record_id):
    params = {
               'domain-name': domain_name,
               'record-id': record_id
             }
    return self._do_request('get-dynamic-url.json',params)
