#!/usr/bin/python

"""
Quick script from https://github.com/xg5-simon/Splunk_encase.io to query encase from Splunk
"""

import json
import csv
import sys
import requests

import splunk.Intersplunk


API_KEY = ''
HTTP_PROXY  = ''
HTTPS_PROXY = ''
ENDPOINT = 'http://<your host>:8700/Splunk/Handler'


def send_data_to_encase(url, encase_payload):
    # curl equivalent request:
    # curl -v --data \
    # "custodian-name=Test.Custodian&source-name=Splunk&data-store-name=Cyber_Datastore&event-id=splunk-1&event-name=splunk-snapshot&investigation-name=splunk_snapshot&function=snapshot&job-name=splunk_scan&machine-ip=machine-ip=dest&safe-name=<your organization>" http://localhost:8700/Splunk/Handler
    
    #print(encase_payload)
    r = requests.post(url, data=encase_payload)
    print(r.text)
    return r

if __name__ == "__main__":

    #http://docs.splunk.com/Documentation/Splunk/4.3.7/Developer/SearchScripts => see $SPLUNK_HOME/lib/python2.7/site-packages/splunk/Intersplunk.py

    (isgetinfo, sys.argv) = splunk.Intersplunk.isGetInfo(sys.argv)
    if len(sys.argv) < 2:
        splunk.Intersplunk.parseError("Not enough arguments: please provide a destination machine, e.g, ""| encase __EXECUTE__ <your machine>""")
        sys.exit(0)

    dest = sys.argv[1]
    # TODO: sanitize data
    # query_obj = validate_ip(dest)

    custodian_name = "Test.Custodian"
    source_name = "Splunk"
    data_store_name =  "Cyber_Datastore"
    event_id = "splunk_1"
    event_name = "splunk_snapshot"
    investigation_name = "splunk_snapshot"
    function = "snapshot"
    job_name = "splunk_scan"
    safe_name =  "<your organization>"
    machine_ip = dest

    #encase_payload = {"custodian_name": custodian_name, "source_name": source_name, "data_store_name":  data_store_name, "event_id": event_id, "event_name": event_name, "investigation_name": investigation_name, "function": function, "job_name": job_name, "safe_name":  safe_name, "machine_ip": dest}
    encase_payload = "custodian-name="+custodian_name+"&source-name="+source_name+"&data-store-name="+data_store_name+"&event-id="+event_id+"&event-name="+event_name+"&investigation-name="+investigation_name+"&function="+function+"&job-name="+job_name+"&machine-ip="+dest+"&safe-name="+safe_name

    data = send_data_to_encase(ENDPOINT, encase_payload)

    with open("/tmp/splunk_to_encase.log", 'ab') as csvfile:
        stew = csv.writer(csvfile, delimiter=',')
        stew.writerow(data)

