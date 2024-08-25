.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: The Cyb3rhq server is the Cyb3rhq central component that analyzes data it receives from agents, external APIs, and network devices. Learn more in this section of the documentation.

Cyb3rhq server
============

The Cyb3rhq server is the Cyb3rhq central component that analyzes data it receives from agents, external APIs, and network devices. It analyzes the received data by correlating and matching it against a predefined ruleset to generate alerts for security monitoring and management.

The Cyb3rhq server comprises two main components; the :doc:`Cyb3rhq manager <cyb3rhq-manager>` and :ref:`Filebeat <indexer_integration_filebeat>`. The Cyb3rhq manager is responsible for data analysis and alerting, while the indexer integration forwards the analyzed data to the Cyb3rhq indexer. Refer to the :doc:`Cyb3rhq server installation </installation-guide/cyb3rhq-server/index>` documentation for information on how to install and set it up.

.. topic:: Contents

   .. toctree::
      :maxdepth: 2

      cyb3rhq-manager
      indexer-integration
      alert-management
      event-logging
      integration-with-external-apis
      cyb3rhq-server-cluster
      cyb3rhq-server-queue
