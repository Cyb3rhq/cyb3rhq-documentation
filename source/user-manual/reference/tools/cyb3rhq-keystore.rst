.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Tool where sensitive configuration data can be securely stored, including any information that the Cyb3rhq manager daemons/tools need for their work.

cyb3rhq-keystore
==============

The cyb3rhq-keystore increases the security of sensitive information, storing in it any information that the Cyb3rhq manager requires for its correct operation.

cyb3rhq-keystore options
----------------------

+------------------------+---------------------------------------------------------+
| **-h**                 | Display the help message.                               |
+------------------------+---------------------------------------------------------+
| **-f <FAMILY>**        | Specifies the target column family for the insertion.   |
+------------------------+---------------------------------------------------------+
| **-k <KEY>**           | Specifies the key for the key-value pair.               |
+------------------------+---------------------------------------------------------+
| **-v <VALUE>**         | Specifies the value associated with the key.            |
+------------------------+---------------------------------------------------------+
| **-vp <VALUE>**        | Specifies the path to a single-line file with the value.|
+------------------------+---------------------------------------------------------+

You can use only one of the options ``-v`` or ``-vp`` at a time. If neither is specified, the tool reads the value from standard input.

When using ``-vp``, the file must contain a single line with the value.

Example
-------

-  Set the indexer username and password:

   .. code-block:: console

      # echo 'admin' | /var/ossec/bin/cyb3rhq-keystore -f indexer -k username
      # echo 'admin' | /var/ossec/bin/cyb3rhq-keystore -f indexer -k password

-  Alternate methods to set values:

   .. code-block:: console

      # /var/ossec/bin/cyb3rhq-keystore -f indexer -k username -v admin
      # /var/ossec/bin/cyb3rhq-keystore -f indexer -k password -vp /file/with/password
