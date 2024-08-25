.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Learn more about the active response scripts included with the default Cyb3rhq installation

Default active response scripts
================================

This section lists out-of-the-box active response scripts for the following operating systems:

.. contents::
   :local:
   :depth: 1
   :backlinks: none

Linux, macOS, and Unix-based endpoints
--------------------------------------

The table below lists out-of-the-box active response scripts for:

-  Linux/Unix endpoints located in the Cyb3rhq agent ``/var/ossec/active-response/bin`` directory. 
-  macOS endpoints located in the Cyb3rhq agent ``/Library/Ossec/active-response/bin`` directory.

Click on the name of each active response to open its source code. 

.. |disable-account| replace:: `disable-account <https://github.com/cyb3rhq/cyb3rhq/blob/v|CYB3RHQ_CURRENT|/src/active-response/disable-account.c>`__
.. |firewall-drop| replace:: `firewall-drop <https://github.com/cyb3rhq/cyb3rhq/blob/v|CYB3RHQ_CURRENT|/src/active-response/firewalls/default-firewall-drop.c>`__
.. |firewalld-drop| replace:: `firewalld-drop <https://github.com/cyb3rhq/cyb3rhq/blob/v|CYB3RHQ_CURRENT|/src/active-response/firewalld-drop.c>`__
.. |host-deny| replace:: `host-deny <https://github.com/cyb3rhq/cyb3rhq/blob/v|CYB3RHQ_CURRENT|/src/active-response/host-deny.c>`__
.. |ip-customblock| replace:: `ip-customblock <https://github.com/cyb3rhq/cyb3rhq/blob/v|CYB3RHQ_CURRENT|/src/active-response/ip-customblock.c>`__
.. |ipfw| replace:: `ipfw <https://github.com/cyb3rhq/cyb3rhq/blob/v|CYB3RHQ_CURRENT|/src/active-response/firewalls/ipfw.c>`__
.. |npf| replace:: `npf <https://github.com/cyb3rhq/cyb3rhq/blob/v|CYB3RHQ_CURRENT|/src/active-response/firewalls/npf.c>`__
.. |cyb3rhq-slack| replace:: `cyb3rhq-slack <https://github.com/cyb3rhq/cyb3rhq/blob/v|CYB3RHQ_CURRENT|/src/active-response/cyb3rhq-slack.c>`__
.. |pf| replace:: `pf <https://github.com/cyb3rhq/cyb3rhq/blob/v|CYB3RHQ_CURRENT|/src/active-response/firewalls/pf.c>`__
.. |restart.sh| replace:: `restart.sh <https://github.com/cyb3rhq/cyb3rhq/blob/master/src/active-response/restart.sh>`__
.. |restart-cyb3rhq| replace:: `restart-cyb3rhq <https://github.com/cyb3rhq/cyb3rhq/blob/v|CYB3RHQ_CURRENT|/src/active-response/restart-cyb3rhq.c>`__
.. |route-null| replace:: `route-null <https://github.com/cyb3rhq/cyb3rhq/blob/v|CYB3RHQ_CURRENT|/src/active-response/route-null.c>`__
.. |kaspersky| replace:: `kaspersky <https://github.com/cyb3rhq/cyb3rhq/blob/master/src/active-response/kaspersky.c>`__

+---------------------------+-------------------------------------------------------------------------------------------------------------+
| Name of script            | Description                                                                                                 |
+===========================+=============================================================================================================+
| |disable-account|         | Disables a user account                                                                                     |
+---------------------------+-------------------------------------------------------------------------------------------------------------+
| |firewall-drop|           | Adds an IP address to the iptables deny list.                                                               |
+---------------------------+-------------------------------------------------------------------------------------------------------------+
| |firewalld-drop|          | Adds an IP address to the firewalld drop list. Requires firewalld installed on the endpoint.                |
+---------------------------+-------------------------------------------------------------------------------------------------------------+
| |host-deny|               | Adds an IP address to the ``/etc/hosts.deny`` file.                                                         |
+---------------------------+-------------------------------------------------------------------------------------------------------------+
| |ip-customblock|          | Custom Cyb3rhq block, easily modifiable for a custom response.                                                |
+---------------------------+-------------------------------------------------------------------------------------------------------------+
| |ipfw|                    | Firewall-drop response script created for IPFW. Requires IPFW installed on the endpoint.                    |
+---------------------------+-------------------------------------------------------------------------------------------------------------+
| |npf|                     | Firewall-drop response script created for NPF. Requires NPF installed on the endpoint.                      |
+---------------------------+-------------------------------------------------------------------------------------------------------------+
| |cyb3rhq-slack|             | Posts notifications on Slack. Requires a slack hook URL passed as an ``extra_args``.                        |
+---------------------------+-------------------------------------------------------------------------------------------------------------+
| |pf|                      | Firewall-drop response script created for PF. Requires PF installed on the endpoint.                        |
+---------------------------+-------------------------------------------------------------------------------------------------------------+
| |restart.sh|              | Restarts the Cyb3rhq agent or manager.                                                                        |
+---------------------------+-------------------------------------------------------------------------------------------------------------+
| |restart-cyb3rhq|           | Restarts the Cyb3rhq agent or manager.                                                                        |
+---------------------------+-------------------------------------------------------------------------------------------------------------+
| |route-null|              | Adds an IP address to a null route.                                                                         |
+---------------------------+-------------------------------------------------------------------------------------------------------------+
| |kaspersky|               | Integration of Cyb3rhq agents with Kaspersky endpoint security. This uses Kaspersky Endpoint Security for     |
|                           | Linux CLI to execute relevant commands based on a trigger.                                                  |
+---------------------------+-------------------------------------------------------------------------------------------------------------+

Windows endpoints
-----------------

The table below lists out-of-the-box scripts for Windows endpoints, located in the Cyb3rhq agent ``C:\Program Files (x86)\ossec-agent\active-response\bin`` directory. Click on the name of each script to see its source code.

.. |netsh.exe| replace:: `netsh.exe <https://github.com/cyb3rhq/cyb3rhq/blob/v|CYB3RHQ_CURRENT|/src/active-response/netsh.c>`__
.. |restart-cyb3rhq.exe| replace:: `restart-cyb3rhq.exe <https://github.com/cyb3rhq/cyb3rhq/blob/v|CYB3RHQ_CURRENT|/src/active-response/restart-cyb3rhq.c>`__
.. |route-null.exe| replace:: `route-null.exe <https://github.com/cyb3rhq/cyb3rhq/blob/v|CYB3RHQ_CURRENT|/src/active-response/route-null.c>`__

+-------------------------+---------------------------------------------------------------+
| Name of script          |                          Description                          |
+=========================+===============================================================+
| |netsh.exe|             | Blocks an IP address using ``netsh``.                         |
+-------------------------+---------------------------------------------------------------+
| |restart-cyb3rhq.exe|     | Restarts the Cyb3rhq agent.                                     |
+-------------------------+---------------------------------------------------------------+
| |route-null.exe|        | Adds an IP address to null route.                             |
+-------------------------+---------------------------------------------------------------+

