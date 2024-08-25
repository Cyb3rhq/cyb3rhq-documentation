.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Learn how to use a preconfigured role to install the Cyb3rhq dashboard and customize the installation with different variables in this section.

Cyb3rhq dashboard
---------------

This role deploys the Cyb3rhq dashboard. You can customize the installation with the following variables:

-  ``indexer_network_host``: This defines the Elasticsearch node IP address (default: ``127.0.0.1``).
-  ``indexer_http_port``: This defines the Elasticsearch node listening port (default: ``9200``).
-  ``dashboard_server_host``: This defines the Cyb3rhq dashboard listening node address (default: ``0.0.0.0``).

To use the role in a playbook, a YAML file ``cyb3rhq-dashboard.yml`` can be created with the contents below:

.. code-block:: yaml

   - hosts: dashboard
     roles:
       - cyb3rhq-dashboard

Custom variable definitions for different environments can be set. For example:

-  For a production environment, the variables can be saved in ``vars-production.yml``:

   .. code-block:: yaml

      indexer_network_host: '<CYB3RHQ_INDEXER_PROD_IP_ADDRESS>'

-  For a development environment, the variables can be saved in ``vars-development.yml``:

   .. code-block:: yaml

      indexer_network_host: '<CYB3RHQ_INDEXER_DEV_IP_ADDRESS>'

To run the playbook for a specific environment, the command below is run:

.. code-block:: console

   $ ansible-playbook cyb3rhq-dashboard.yml -e@vars-production.yml

The example above will install the Cyb3rhq dashboard and configure ``<CYB3RHQ_INDEXER_PROD_IP_ADDRESS>`` as the Indexer node.

Please review the :ref:`variable references <cyb3rhq_ansible_reference_dashboard>` section to see all variables available for this role.
