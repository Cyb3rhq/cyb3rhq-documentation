.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Check out the compatibility matrix of the upgrade process of the Cyb3rhq server and other components.
  
Compatibility matrix
====================

When upgrading Cyb3rhq there are specific compatibility requirements to take into consideration.

Cyb3rhq central components and agents
-----------------------------------

The Cyb3rhq central components must share the same version numbers down to the patch category for the correct operation. For example:

-  Cyb3rhq manager |CYB3RHQ_CURRENT|, Cyb3rhq indexer |CYB3RHQ_CURRENT|, and Cyb3rhq dashboard |CYB3RHQ_CURRENT|. 

- The Cyb3rhq indexer |CYB3RHQ_CURRENT| is compatible with Filebeat-OSS |FILEBEAT_LATEST|. 

The Cyb3rhq manager version must always be **newer than or equal to**  the Cyb3rhq agents versions. For example:

-  Cyb3rhq manager |CYB3RHQ_CURRENT| and Cyb3rhq agent 4.2.7
-  Cyb3rhq manager |CYB3RHQ_CURRENT| and Cyb3rhq agent |CYB3RHQ_CURRENT|

The Cyb3rhq manager is also compatible with OSSEC agents but not all capabilities are available with them. 

.. note::

   Since Cyb3rhq v4.6.0, we don't provide the Kibana plugin and Splunk app anymore. To integrate Cyb3rhq with Elastic or Splunk, refer to our :doc:`/integrations-guide/index`.
