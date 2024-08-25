.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Cyb3rhq uses Command and Logcollector modules to execute commands and send output for analysis. Learn how the command monitoring works in this documentation section.
  
How it works
============

The command monitoring capability works on all endpoints where the Cyb3rhq server or agent is installed. Cyb3rhq uses the Command and the Logcollector modules to run commands on the endpoints and forward the output to the Cyb3rhq server for analysis.

The steps below describe the sequence of actions from when a user configures the command monitoring module to when the Cyb3rhq server generates alerts:

#. The user adds the desired command to the local agent configuration file or remotely through the Cyb3rhq server. You can achieve this configuration by using either the Command or the Logcollector module.

#. The Cyb3rhq agent periodically executes the command on the configured endpoint based on the set frequency or interval.

#. The Cyb3rhq agent monitors the command’s execution and forwards its output to the Cyb3rhq server for analysis.

#. The Cyb3rhq server pre-decodes, decodes, and matches the received logs against predefined rules to generate security alerts. If the logs match the rules, an alert is generated and stored in the ``/var/ossec/logs/alerts/alerts.log`` and ``/var/ossec/logs/alerts/alerts.json`` files on the Cyb3rhq server. The alert is simultaneously displayed on the Cyb3rhq dashboard.

The image below shows the components involved in the command monitoring process.

.. thumbnail:: /images/manual/command-monitoring/command-monitoring.png
  :title: Command monitoring workflow
  :alt: Command monitoring workflow
  :align: center
  :width: 80%
 