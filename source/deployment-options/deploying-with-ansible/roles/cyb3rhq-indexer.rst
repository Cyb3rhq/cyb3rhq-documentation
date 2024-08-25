.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Learn how to use a preconfigured role to install the Cyb3rhq indexer and customize the installation with different variables in this section.

Cyb3rhq indexer
-------------

This role is intended to deploy the Cyb3rhq indexer to a specified node. The following variables can be used to customize the installation:

-  ``indexer_network_hosts``: This defines the listening IP address (default: ``127.0.0.1``).
-  ``indexer_http_port``: This defines the listening port (default: ``9200``).
-  ``indexer_jvm_xms``: This specifies the amount of memory to be used for java (default: ``null``).

To use the role in a playbook, a YAML file ``cyb3rhq-indexer.yml`` can be created with the contents below:

.. code-block:: yaml

   - hosts: indexer
     roles:
     - cyb3rhq-indexer

Custom variable definitions for different environments can be set. For example:

-  For a production environment, the variables can be saved in ``vars-production.yml``:

   .. code-block:: yaml

      indexer_network_host: '<CYB3RHQ_INDEXER_PROD_IP_ADDRESS>'

-  For a development environment, the variables can be saved in ``vars-development.yml``:

   .. code-block:: yaml

      indexer_network_host: '<CYB3RHQ_INDEXER_DEV_IP_ADDRESS>'
        
To run the playbook for a specific environment, the command below is run:

.. code-block:: console

   $ ansible-playbook cyb3rhq-indexer.yml -e@vars-production.yml

The example above will install the Cyb3rhq indexer and set the listening address to: ``<CYB3RHQ_INDEXER_PROD_IP_ADDRESS>`` using ``vars-production.yml``.

Please review the :ref:`variables references <cyb3rhq_ansible_reference_indexer>` section to see all variables available for this role.
