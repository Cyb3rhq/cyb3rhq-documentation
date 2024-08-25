.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: The FIM module runs periodic scans on specific paths and monitors specific directories for changes in real time. Learn more about how FIM works in this section. 
  
How it works
============

The FIM module runs periodic scans on specific paths and monitors specific directories for changes in real time. You can set which paths to monitor in the configuration of the Cyb3rhq agents and manager.

FIM stores the files checksums and other attributes in a local FIM database. Upon a scan, the Cyb3rhq agent reports any changes the FIM module finds in the monitored paths to the Cyb3rhq server. The FIM module looks for file modifications by comparing the checksums of a file to its stored checksums and attribute values. It generates an alert if it finds discrepancies.

The Cyb3rhq FIM module uses two databases to collect FIM event data, such as file creation, modification, and deletion data. One is a local SQLite-based database on the monitored endpoint that stores the data in: 

- ``C:\Program Files (x86)\ossec-agent\queue\fim\db`` on Windows.
- ``/var/ossec/queue/fim/db`` on Linux.
- ``/Library/Ossec/queue/fim/db`` on macOS. 

The other is an agent database on the Cyb3rhq server. The :doc:`cyb3rhq-db </user-manual/reference/daemons/cyb3rhq-db>`. daemon creates and manages a database for each agent on the Cyb3rhq server. It uses the ID of the agent to identify the database. This service stores the databases at ``/var/ossec/queue/db``.

.. thumbnail:: ../../../images/manual/fim/fim-flow.png
  :title: File Integrity Monitoring
  :alt: File Integrity Monitoring
  :align: center
  :width: 80%

The FIM module keeps the Cyb3rhq agent and the Cyb3rhq server databases synchronized with each other. It always updates the file inventory in the Cyb3rhq server with the data available to  the Cyb3rhq agent. An up-to-date Cyb3rhq server database allows for servicing FIM-related API queries. The synchronization mechanism only updates the Cyb3rhq server with information from the Cyb3rhq agents such as checksums and file attributes that have changed. 

The Cyb3rhq agent and manager have the FIM module enabled and :ref:`pre-configured <reference_ossec_syscheck_default_configuration>` by default. However, we recommend that you review the configuration of your endpoints to ensure that you tailor the FIM settings, such as monitored paths, to your environment.

