.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: The cyb3rhq-syscheckd program checks files for changes to the checksums, permissions and ownership. Learn more in this section. 

.. _cyb3rhq-syscheckd:

cyb3rhq-syscheckd
===============

The cyb3rhq-syscheckd program checks configured files for changes to the checksums, permissions and ownership.  It is run using cyb3rhq-control.

+-----------------+-------------------------------------------------------------------------------------------------+
| **-c <config>** | Run using <config> as the configuration file.                                                   |
+                 +-------------------------------------------+-----------------------------------------------------+
|                 | Default value                             | /var/ossec/etc/ossec.conf                           |
+-----------------+-------------------------------------------+-----------------------------------------------------+
| **-d**          | Run in debug mode. This option may be repeated to increase the verbosity of the debug messages. |
+-----------------+-------------------------------------------------------------------------------------------------+
| **-f**          | Run in the foreground.                                                                          |
+-----------------+-------------------------------------------------------------------------------------------------+
| **-h**          | Display the help message.                                                                       |
+-----------------+-------------------------------------------------------------------------------------------------+
| **-t**          | Test configuration.                                                                             |
+-----------------+-------------------------------------------------------------------------------------------------+
| **-V**          | Display the version and license information                                                     |
+-----------------+-------------------------------------------------------------------------------------------------+
