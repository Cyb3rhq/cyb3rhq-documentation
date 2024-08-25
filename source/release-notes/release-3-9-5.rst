.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Cyb3rhq 3.9.5 has been released. Check out our release notes to discover the changes and additions of this release.

.. _release_3_9_5:

3.9.5 Release notes - 8 August 2019
===================================

This section shows the most relevant improvements and fixes in version 3.9.5. More details about these changes are provided in each component changelog:

- `cyb3rhq/cyb3rhq <https://github.com/cyb3rhq/cyb3rhq/blob/v3.9.5/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-kibana-app <https://github.com/cyb3rhq/cyb3rhq-kibana-app/blob/v3.9.5-7.3.0/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-splunk <https://github.com/cyb3rhq/cyb3rhq-splunk/blob/v3.9.5-7.3.0/CHANGELOG.md>`_

Cyb3rhq manager
-------------

- Fixed a bug in the Framework that prevented Cluster and API from handling the file *client.keys* if it's mounted as a volume on Docker.
- Fixed a bug in Analysisd that printed the millisecond part of the alerts' timestamp without zero-padding. That prevented Elasticsearch 7 from indexing those alerts.

Cyb3rhq Kibana app
----------------

- Fixed a bug present in Kibana v7.3.0, affecting Firefox browser, which creates an endless loop if two or more query filters are added.
