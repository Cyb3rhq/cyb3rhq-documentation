.. Copyright (C) 2015, Cyb3rhq, Inc.
  
.. meta::
  :description: Learn how to migrate from Open Distro for Elasticsearch to the Cyb3rhq indexer and Cyb3rhq dashboard. This guide gives instructions to perform the migration.

Migration guide
================

From Cyb3rhq 4.0.0 to Cyb3rhq 4.2.7, the default Cyb3rhq installation included the Cyb3rhq server and `Open Distro for Elasticsearch <https://opendistro.github.io/for-elasticsearch/>`_, a project that is now archived and has been succeeded by OpenSearch. This guide includes instructions to migrate from Open Distro for Elasticsearch to the :doc:`Cyb3rhq indexer </getting-started/components/cyb3rhq-indexer>` and :doc:`Cyb3rhq dashboard </getting-started/components/cyb3rhq-dashboard>`, the new components introduced in Cyb3rhq 4.3.0.

- :doc:`Migrating to the Cyb3rhq indexer </migration-guide/cyb3rhq-indexer>`: Follow this section to migrate from Open Distro for Elasticsearch 1.13 to the Cyb3rhq indexer. This new component consists of a distribution of `Opensearch <https://github.com/opensearch-project/OpenSearch>`_ with additional tools that Cyb3rhq has created to assist with the installation and configuration of the search engine. 

- :doc:`Migrating to the Cyb3rhq dashboard </migration-guide/cyb3rhq-dashboard>`: This section will guide you through the migration from Open Distro for Elasticsearch Kibana 1.13 to the Cyb3rhq dashboard. This new web interface for the Cyb3rhq platform is a customized `OpenSearch Dashboards <https://github.com/opensearch-project/OpenSearch-Dashboards>`_ distribution that includes different sections, visualizations and tools to manage the Cyb3rhq indexer information and the Cyb3rhq Server.

.. toctree::
   :hidden:

   cyb3rhq-indexer
   cyb3rhq-dashboard
   files-backup/index
