## SplunkToEncase


#### Description

A python script that can be used by a Splunk custom command to query the EnCase API.

#### Requirements

1. Splunk 6.0+ 
2. Internet connection

#### Installation

1. Add the following to your Splunk apps `$SPLUNK_HOME/etc/apps/<app_name>local/commands.conf`
```python
[encase]
filename = splunk_to_encase.py
```
2. Add splunk_to_encase.py to `$SPLUNK_HOME/etc/apps/<app_name>/bin/`

#### Usage
#####To query an IP
From Splunk search run `| encase __EXECUTE__ 10.1.2.3`

##### To query a domain
From Splunk search run `| encase __EXECUTE__ myDesktop `

#### ToDo

- [ ] Add support for others parameters
- [ ] Test proxy settings

##### Credits
Used most of https://github.com/xg5-simon/Splunk_Cymon.io - thanks xg5-simon !

