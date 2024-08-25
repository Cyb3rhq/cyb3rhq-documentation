.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Cyb3rhq 3.9.1 has been released. Check out our release notes to discover the changes and additions of this release.

.. _release_3_9_1:

3.9.1 Release notes - 21 May 2019
=================================

This section shows the most relevant improvements and fixes in version 3.9.1. More details about these changes are provided in each component changelog:

- `cyb3rhq/cyb3rhq <https://github.com/cyb3rhq/cyb3rhq/blob/v3.9.1/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-ruleset <https://github.com/cyb3rhq/cyb3rhq-ruleset/blob/v3.9.1/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-kibana-app <https://github.com/cyb3rhq/cyb3rhq-kibana-app/blob/v3.9.1-7.1.0/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-splunk <https://github.com/cyb3rhq/cyb3rhq-splunk/blob/v3.9.1-7.2.6/CHANGELOG.md>`_

Cyb3rhq core
----------

- Log collector: Improved wildcards support for Windows platforms. Now, it is possible to set multiple wildcards per path as is shown below:

  .. code-block:: xml

        <localfile>
            <location>C:\Users\user\Desktop\*test*</location>
            <log_format>syslog</log_format>
            <exclude>C:\Users\user\Desktop\*test*.json</log_format>
        </localfile>

- Fixed crash when an active response command was received and the module was disable
- Fixed crash when collecting large files on Windows.
- Fixed Cyb3rhq manager automatic restart via API on Docker containers.
- Fixed corruption error in cluster agent info files synchronization.
- Reverted five seconds reading timeout in FIM scans.


Cyb3rhq apps
----------

- Added support for Elastic Stack v7.1.0
- Added support for Elastic Stack v6.8.0
- Improve dynamic height for configuration editor in Splunk app.
- Fixed infinite API log fetching, fix a handled but not shown error messages from rule editor in Splunk app.

Cyb3rhq ruleset
-------------

- macOS SCA policies based on CIS benchmarks have been corrected.
- Windows rules for EventLog and Security Essentials have been fixed as well as the field filters are now more restrictive to avoid false positives.
- Fixed typo in Windows NT registries within Windows SCA policies.

Elastic Stack 7
----------------

Cyb3rhq is now compatible with Elastic Stack 7, which includes, between others, new out of the box `Security features <https://www.elastic.co/blog/getting-started-with-elasticsearch-security>`_.

Additionally, since this Cyb3rhq release, Logstash is no longer required, Filebeat will send the events directly to Elasticsearch server.

- `Upgrading to Elastic Stack 7.1 <https://documentation.cyb3rhq.com/3.9/upgrade-guide/upgrading-elastic-stack/elastic_server_rolling_upgrade.html>`__
- `Elastic Stack 7.0.0 release blogpost <https://www.elastic.co/blog/elastic-stack-7-0-0-released>`_


Elastic Stack 6.x is still supported by Cyb3rhq.
