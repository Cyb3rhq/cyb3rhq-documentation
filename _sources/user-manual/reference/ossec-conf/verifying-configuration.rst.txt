.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Find out how to verify sections of the Cyb3rhq configuration in this section of the Cyb3rhq documentation.

.. _verifying_configuration:

Verifying configuration
========================

+--------------------------------------+----------------------------------------+
| Configuration section                | command                                |
+======================================+========================================+
| Syscheck/Rootcheck                   | /var/ossec/bin/cyb3rhq-syscheckd -t      |
+--------------------------------------+----------------------------------------+
| local files                          | /var/ossec/bin/cyb3rhq-logcollector -t   |
+--------------------------------------+----------------------------------------+
| Wodles                               | /var/ossec/bin/cyb3rhq-modulesd -t       |
+--------------------------------------+----------------------------------------+
| global/rules/decoders (manager only) | /var/ossec/bin/cyb3rhq-analysisd -t      |
+--------------------------------------+----------------------------------------+
| Client (agent only)                  | /var/ossec/bin/cyb3rhq-agentd -t         |
+--------------------------------------+----------------------------------------+
