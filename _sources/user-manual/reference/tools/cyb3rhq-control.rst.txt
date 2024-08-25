.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: The cyb3rhq-control script is used to start, stop, configure, and check the status of Cyb3rhq processes. Learn more about it in this section.
  
.. _cyb3rhq-control:

cyb3rhq-control
=============

The cyb3rhq-control script is used to start, stop, configure, check on the status of Cyb3rhq processes and enable the debug mode.

.. note::
    We recommend using the ``systemctl`` or ``service`` commands (depending on your OS) to **start**, **stop** or **restart** the Cyb3rhq service. This will avoid inconsistencies between the *service* status and the *processes* status.

The ``-j`` option is used for enabling JSON output format, but only in Cyb3rhq server installations.

+-------------+---------------------------------------------------------------------------------------------------------+
| **start**   | Start the Cyb3rhq processes.                                                                              |
+-------------+---------------------------------------------------------------------------------------------------------+
| **stop**    | Stop the Cyb3rhq processes.                                                                               |
+-------------+---------------------------------------------------------------------------------------------------------+
| **restart** | Restart the Cyb3rhq processes.                                                                            |
+-------------+---------------------------------------------------------------------------------------------------------+
| **reload**  | Restart all Cyb3rhq processes except cyb3rhq-execd.                                                         |
|             |                                                                                                         |
|             | This allows an agent to reload without losing active response status.                                   |
|             |                                                                                                         |
|             | This option is not available on a local Cyb3rhq installation.                                             |
+-------------+---------------------------------------------------------------------------------------------------------+
| **status**  | Determine which Cyb3rhq processes are running.                                                            |
+-------------+---------------------------------------------------------------------------------------------------------+
| **info**    | Prints the Cyb3rhq installation type, version, and revision in environment variables format.              |
+-------------+-----------------+---------------+-----------------------------------------------------------------------+
| **info**    |    [-v -r -t]   | Only one option at the time, prints the value of: version, revision or type.          |
+-------------+-----------------+---------------+-----------------------------------------------------------------------+
| **enable**  |  debug          | Run all Cyb3rhq daemons in debug mode.                                                  |
+-------------+-----------------+---------------+-----------------------------------------------------------------------+
| **disable** | debug           | Turn off debug mode.                                                                  |
+-------------+-----------------+---------------+-----------------------------------------------------------------------+

.. note::
    To use the database option, Database support must be compiled in during initial installation.
