.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Cyb3rhq 3.2.4 has been released. Check out our release notes to discover the changes and additions of this release.
  
.. _release_3_2_4:

3.2.4 Release notes - 1 June 2018
=================================

This section shows the most relevant improvements and fixes in version 3.2.4. More details about these changes are provided in each component changelog.

- `cyb3rhq/cyb3rhq <https://github.com/cyb3rhq/cyb3rhq/blob/v3.2.4/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-api <https://github.com/cyb3rhq/cyb3rhq-api/blob/v3.2.4/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-ruleset <https://github.com/cyb3rhq/cyb3rhq-ruleset/blob/v3.2.4/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-kibana-app <https://github.com/cyb3rhq/cyb3rhq-kibana-app/blob/v3.2.4-6.2.4/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-kibana-splunk <https://github.com/cyb3rhq/cyb3rhq-splunk/blob/v3.2.4-7.1.1/CHANGELOG.md>`_

Cyb3rhq minor fixes
-----------------

Most of the bug fixes in this release are fairly minor, but a few fixes deserve special mention:

 - ``<queue_size>`` setting was not properly parsed by ``maild`` causing the termination of the process.
 - Python 3 incompatibilities in the framework that may affect the correct behavior of the cluster.

Cyb3rhq app for Splunk
--------------------

This release includes:

 - New GDPR tab.
 - Multi-API support.
 - Multi-index support.
 - Several performance improvements and bug fixes.


Cyb3rhq app for Kibana
--------------------

Relevant changes in the Cyb3rhq app are:

 - New reporting feature: Generate reports from Overview and Agents tab.
 - New check included to warn about systems with low RAM (less than 3GB).
 - Several performance improvements and bug fixes.
