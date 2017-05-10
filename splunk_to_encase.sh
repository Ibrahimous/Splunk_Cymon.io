#!/usr/bin/bash

#scriptName = $SPLUNK_ARG_0
#numberEventsReturned = $SPLUNK_ARG_1
#searchTerms = $SPLUNK_ARG_2
#queryString = $SPLUNK_ARG_3
#alert_name = $SPLUNK_ARG_4
#triggerReason = $SPLUNK_ARG_5
#browserUrl = $SPLUNK_ARG_6
#rawEventsFile = $SPLUNK_ARG_8

custodian="Test.Custodian"
source="Splunk"
ds="Cyber_Datastore"
evt_id="splunk-1"
evt_name="splunk-snapshot"
investigation="splunk_snapshot"
function="snapshot"
job="splunk_scan"
safe="<your SAFE>"
machine="<your machine>"
URL="http://<your host>:8700/Splunk/Handler"

#curl -v --data "custodian-name=Test.Custodian&source-name=Splunk&data-store-name=Cyber_Datastore&event-id=splunk-1&event-name=splunk-snapshot&investigation-name=splunk_snapshot&function=snapshot&job-name=splunk_scan&machine-ip=<your machine>&safe-name=<your SAFE>" http://<your host>:8700/Splunk/Handler
DATA="custodian-name=$custodian&source-name=$source&data-store-name=$ds&event-id=$evt_id&event-name=$evt_name&investigation-name=$investigation&function=$function&job-name=$job&machine-ip=$machine&safe-name=$safe"

echo $DATA #OK

curl -v --data $DATA $URL
