.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Filebeat is used in conjunction with the Cyb3rhq manager to send events and alerts to Elasticsearch. Learn how to customize the installation here.
  
Filebeat
--------

Filebeat can be used in conjunction with Cyb3rhq Manager to send events and alerts to the Cyb3rhq indexer. This role will install Filebeat, you can customize the installation with these variables:

-  ``filebeat_output_indexer_hosts``: This defines the indexer node(s) to be used (default: ``127.0.0.1:9200``).

Please review the :ref:`variables references <cyb3rhq_ansible_reference_filebeat>` section to see all variables available for this role.
