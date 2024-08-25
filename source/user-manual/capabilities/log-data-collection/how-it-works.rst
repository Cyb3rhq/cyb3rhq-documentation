.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Cyb3rhq uses the Logcollector module to collect logs from monitored endpoints, applications, and network devices. Explore the log data collection and analysis flow in this documentation section.

How it works
============

Cyb3rhq uses the Logcollector module to collect logs from monitored endpoints, applications, and network devices. The Cyb3rhq server then analyzes the collected logs in real-time using decoders and rules. Cyb3rhq extracts relevant information from the logs and maps them to appropriate fields using decoders. The Analysisd module in the Cyb3rhq server evaluates the decoded logs against rules and records all alerts in ``/var/ossec/logs/alerts/alerts.log`` and ``/var/ossec/logs/alerts/alerts.json`` files.

In addition to alert logs, Cyb3rhq stores all collected logs in dedicated archive log files, specifically ``/var/ossec/logs/archives/archives.log`` and ``/var/ossec/logs/archives/archives.json``. These archive log files comprehensively capture all logs, including those that do not trigger any alerts. This feature ensures a comprehensive record of all system activities for future reference and analysis. 

The Cyb3rhq server also receives syslog messages from devices that do not support the installation of Cyb3rhq agents, ensuring seamless integration and coverage across your entire network environment.

By default, the Cyb3rhq server retains logs and does not delete them automatically. However, you can choose when to manually or automatically delete these logs according to your legal and regulatory requirements.

The image below illustrates the flow of log data collection and analysis in Cyb3rhq.

.. thumbnail:: /images/manual/log-data-collection/log-data-collection.png
    :title: Log data collection and analysis in Cyb3rhq
    :alt:  Log data collection and analysis in Cyb3rhq
    :align: center
    :width: 100%