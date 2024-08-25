.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: The update-ruleset script updates decoders, rules, and rootchecks. Find out the arguments of this script in this section of the Cyb3rhq documentation. 

.. _update_ruleset:

update_ruleset
=================

.. deprecated:: 4.2

The ``update-ruleset`` script updates decoders, rules, and rootchecks.

+--------+-------------------------------------------------------------------------+
| **-r** | Restart Cyb3rhq when needed.                                              |
+--------+-------------------------------------------------------------------------+
| **-R** | Do not restart Cyb3rhq.                                                   |
+--------+-------------------------------------------------------------------------+
| **-b** | Restore the last backup.                                                |
+--------+-------------------------------------------------------------------------+
| **-h** | Display the help message.                                               |
+--------+-------------------------------------------------------------------------+
| **-f** | Force Cyb3rhq to update the ruleset.                                      |
+--------+-------------------------------------------------------------------------+
| **-o** | Set Cyb3rhq path.                                                         |
+        +-----------------------------------+-------------------------------------+
|        | Default                           | /var/ossec                          |
+--------+-----------------------------------+-------------------------------------+
| **-s** | Select ruleset source path (instead of downloading it).                 |
+--------+-------------------------------------------------------------------------+
| **-j** | JSON output. Must be used in conjunction with the '-s' option.          |
+--------+-------------------------------------------------------------------------+
| **-d** | Run in debug mode.                                                      |
+--------+-------------------------------------------------------------------------+
| **-n** | Branch name (default: stable).                                          |
+--------+-------------------------------------------------------------------------+
