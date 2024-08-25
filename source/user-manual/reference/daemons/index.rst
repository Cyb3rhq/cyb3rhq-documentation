.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Know the Cyb3rhq Daemons that perform different actions between the different components of the Cyb3rhq platform. Learn more about it in this section.

.. _daemons:

Daemons
=======

+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| Daemons                                           | Descriptions                                                    | Supported installations     |
+===================================================+=================================================================+=============================+
| :doc:`cyb3rhq-agentd <cyb3rhq-agentd>`                | Client side daemon that communicates with the server.           | agent                       |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`cyb3rhq-agentlessd <cyb3rhq-agentlessd>`        | Runs integrity checking on systems where no agent is installed  | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`cyb3rhq-analysisd <cyb3rhq-analysisd>`          | Receives log messages and compares them to the rules            | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`cyb3rhq-authd <cyb3rhq-authd>`                  | Adds agents to the Cyb3rhq manager                                | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`cyb3rhq-csyslogd <cyb3rhq-csyslogd>`            | Forwards Cyb3rhq alerts via syslog                                | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`cyb3rhq-dbd <cyb3rhq-dbd>`                      | Inserts alert logs into a database                              | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`cyb3rhq-execd <cyb3rhq-execd>`                  | Executes active responses                                       | manager, agent              |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`cyb3rhq-logcollector <cyb3rhq-logcollector>`    | Monitors configured files and commands for new log messages     | manager, agent              |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`cyb3rhq-maild <cyb3rhq-maild>`                  | Sends Cyb3rhq alerts via email                                    | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`cyb3rhq-monitord <cyb3rhq-monitord>`            | Monitors agent connectivity and compresses log files            | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`cyb3rhq-remoted <cyb3rhq-remoted>`              | Communicates with agents                                        | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`cyb3rhq-reportd <cyb3rhq-reportd>`              | Creates reports from Cyb3rhq alerts                               | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`cyb3rhq-syscheckd <cyb3rhq-syscheckd>`          | Checks configured files for security changes                    | manager, agent              |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`cyb3rhq-clusterd <clusterd>`                  | Manages the Cyb3rhq cluster manager                               | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`cyb3rhq-modulesd <cyb3rhq-modulesd>`            | Manages the Cyb3rhq modules                                       | manager, agent              |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`cyb3rhq-db <cyb3rhq-db>`                        | Manages the Cyb3rhq database                                      | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| :doc:`cyb3rhq-integratord <cyb3rhq-integratord>`      | Allows Cyb3rhq to connect to external APIs and alerting tools     | manager                     |
+---------------------------------------------------+-----------------------------------------------------------------+-----------------------------+


.. toctree::
    :hidden:
    :maxdepth: 1

    cyb3rhq-agentd
    cyb3rhq-agentlessd
    cyb3rhq-analysisd
    cyb3rhq-authd
    cyb3rhq-csyslogd
    cyb3rhq-dbd
    cyb3rhq-execd
    cyb3rhq-logcollector
    cyb3rhq-maild
    cyb3rhq-monitord
    cyb3rhq-remoted
    cyb3rhq-reportd
    cyb3rhq-syscheckd
    clusterd
    cyb3rhq-modulesd
    cyb3rhq-db
    cyb3rhq-integratord
