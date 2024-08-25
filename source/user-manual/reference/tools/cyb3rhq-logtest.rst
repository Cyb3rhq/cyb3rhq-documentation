.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Test and verify rules providing log examples in a sandbox using the cyb3rhq-logtest tool. Learn more about it in this section.
  
.. _cyb3rhq-logtest:

cyb3rhq-logtest
=============

`cyb3rhq-logtest` tool allows the testing and verification of rules against provided log examples inside a sandbox in `cyb3rhq-analysisd`. Helpful when writing and debugging custom rules and decoders, troubleshooting false positives and negatives.

+-------------------------------------------+--------------------------------------------------------------------------------+
| **-d**                                    | Run as a Print debug output to the terminal.                                   |
+-------------------------------------------+--------------------------------------------------------------------------------+
| **-h**                                    | Display the help message.                                                      |
+-------------------------------------------+--------------------------------------------------------------------------------+
| **-U <rule-id:alert-level:decoder-name>** | This option will cause cyb3rhq-logtest to return a zero exit status if the test  |
|                                           |                                                                                |
|                                           | results for the provided log line match the criteria in the arguments.         |
|                                           |                                                                                |
|                                           | Only one log line should be supplied for this to be useful.                    |
+-------------------------------------------+--------------------------------------------------------------------------------+
| **-l <location>**                         | Set custom location.                                                           |
+-------------------------------------------+--------------------------------------------------------------------------------+
| **-V**                                    | Display the version and license information for Cyb3rhq and cyb3rhq-logtest.       |
+-------------------------------------------+--------------------------------------------------------------------------------+
| **-q**                                    | Quiet execution.                                                               |
+-------------------------------------------+--------------------------------------------------------------------------------+
| **-v**                                    | Display the verbose results.                                                   |
+-------------------------------------------+--------------------------------------------------------------------------------+

.. note::

    -v is the key option to troubleshoot a rule or decoder problem.
