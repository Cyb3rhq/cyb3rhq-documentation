.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Cyb3rhq 3.9.3 has been released. Check out our release notes to discover the changes and additions of this release.

.. _release_3_9_3:

3.9.3 Release notes - 9 July 2019
=================================

This section shows the most relevant improvements and fixes in version 3.9.3. More details about these changes are provided in each component changelog:

- `cyb3rhq/cyb3rhq <https://github.com/cyb3rhq/cyb3rhq/blob/v3.9.3/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-ruleset <https://github.com/cyb3rhq/cyb3rhq-ruleset/blob/v3.9.3/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-kibana-app <https://github.com/cyb3rhq/cyb3rhq-kibana-app/blob/v3.9.3-7.2.0/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-splunk <https://github.com/cyb3rhq/cyb3rhq-splunk/blob/v3.9.3-7.3.0/CHANGELOG.md>`_


Cyb3rhq core
----------

- Log collector will not report Windows Eventchannel events bookmarked by default.
- Agent-info that are not generated in utf-8 format will be discarded.
- Fix memory leak in Modules Daemon when your on-demand configuration was requested.
- Fixed a bug that crashed Analysisd and Logtest when trying rules having <different_geoip> and no <not_same_field> stanza.
- Fixed the parser of the Canonical's OVAL feed due to a syntax change.
- Rules with <list lookup="address_match_key" /> produced a false match if the CDB list file is missing.
- Remote configuration was missing the <ignore> stanzas for Syscheck and Rootcheck when defined as sregex.


Cyb3rhq apps
----------

- Added support for Kibana v7.2.0.
- Added support for Kibana v6.8.1.
- Fixed height for the menu directive with Dynamic height.
- Fixed timepicker in cluster monitoring.
- Fixed time offset for reporting table.
- Fixed API call for fetching GDPR requirements in agents.
- Fixed filters which were not applying when refreshing agents search bar.
- Fixed wrong fields in never connected agents.
- Fixed the error message when the App detects an unexpected Cyb3rhq version.
- Fixed invalid date message in some web browsers.
- Fixed missing ignored and ignored_sregex fields in the configuration ondemand.


Cyb3rhq ruleset
-------------

- Changed NGINX decoder to make the field "server" optional. (Credits to `@iasdeoupxe <https://github.com/iasdeoupxe>`_).
- Remove unwanted tailing single quote in Audit decoder. (Credits to `@branchnetconsulting <https://github.com/branchnetconsulting>`_).
- Avoid conflicts between the "uid" and "auid" fields in the Audit decoder. (Credits to `@tokibi <https://github.com/tokibi>`_).
- Exclude the full log field from rules for AWS, Suricata, VirusTotal, OwnCloud, Vuls, CIS-CAT, Vulnerability Detector, MySQL, Osquery and Azure.
