.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Cyb3rhq 3.2.3 has been released. Check out our release notes to discover the changes and additions of this release.
  
.. _release_3_2_3:

3.2.3 Release notes - 28 May 2018
=================================

This section shows the most relevant improvements and fixes in version 3.2.3. More details about these changes are provided in each component changelog.

- `cyb3rhq/cyb3rhq <https://github.com/cyb3rhq/cyb3rhq/blob/v3.2.3/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-api <https://github.com/cyb3rhq/cyb3rhq-api/blob/v3.2.3/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-ruleset <https://github.com/cyb3rhq/cyb3rhq-ruleset/blob/v3.2.3/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-kibana-app <https://github.com/cyb3rhq/cyb3rhq-kibana-app/blob/v3.2.3-6.2.4/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-kibana-splunk <https://github.com/cyb3rhq/cyb3rhq-splunk/blob/v3.2.3-7.1.0/CHANGELOG.md>`_

GDPR Support
------------

The `General Data Protection Regulation <https://www.eugdpr.org/>`_ took effect on 25th May 2018. Cyb3rhq helps with most technical requirements, taking advantage of features such as File Integrity or Policy monitoring. In addition, the entire Ruleset has been mapped following the GDPR regulation, enriching all the alerts related to this purpose.

You can read more information about the GDPR regulation and how Cyb3rhq faces it on the this section: :doc:`/compliance/gdpr/index`.

Cyb3rhq cluster
-------------

This version fixes several performance issues (like CPU usage) and synchronization errors. The communications and synchronization algorithm have been redesigned in order to improve the cluster performance and reliability.

Now, the client nodes initialize the communication and only the master node is included in the client configuration.

The number of daemons has been reduced to one: ``cyb3rhq-clusterd``.

You can check our documentation for Cyb3rhq cluster in the following :doc:`Cluster basics </user-manual/manager/cyb3rhq-server-cluster>`.

Core improvements
-----------------

These are the most relevant changes in the Cyb3rhq core:

- :doc:`Vulnerability-detector </user-manual/capabilities/vulnerability-detection/index>` continues to expand its scope, now adding support for Amazon Linux. A bug when comparing epoch versions has also been fixed.
- The agent limit has been increased to ``14000`` by default, improving the manager availability in large environments.
- More internal bugs reported by the community have been fixed for this version.

Cyb3rhq app for Splunk
--------------------

New section describing the installation process for the `Cyb3rhq app for Splunk <https://cyb3rhq.github.io/documentation/3.13/installation-guide/installing-splunk/index.html>`_.

Cyb3rhq app for Kibana
--------------------

The **Dev tools** tab has been added in this version. You can use it to interact with the managers by API requests.

Similar to PCI DSS, a new tab for **GDPR** is included in order to visualize the related alerts.

Other relevant changes in the Cyb3rhq app are:

- New button for downloading lists on a *CSV* format. Currently available for the Ruleset, Logs and Groups sections on the Manager tab and also the Agents tab.
- New option on the configuration file for enabling or disabling the ``cyb3rhq-monitoring`` indices creation/visualization.
- Design improvements for the Ruleset tab.
- Performance improvements on visualization filters.
- And many bugfixes for the overall app.
