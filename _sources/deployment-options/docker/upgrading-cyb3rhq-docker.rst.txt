.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Learn more about upgrading the Cyb3rhq deployment on Docker in this section of our documentation. 

Upgrading Cyb3rhq Docker
======================

This section describes how to upgrade your Cyb3rhq Docker deployment, starting from version 4.3. To upgrade Cyb3rhq deployments of versions earlier than 4.3, refer to the :doc:`/deployment-options/docker/data-migration` documentation.

To upgrade to version |CYB3RHQ_CURRENT_MINOR|, you can follow one of two strategies.

- `Using default docker-compose files`_ : This strategy uses the default docker-compose files for Cyb3rhq |CYB3RHQ_CURRENT_MINOR|. It replaces the docker-compose files of your outdated Cyb3rhq version. 
- `Keeping custom docker-compose files`_ : This strategy preserves the docker-compose files of your outdated Cyb3rhq deployment. It ignores the docker-compose files of the latest Cyb3rhq version. 

Using default docker-compose files
----------------------------------

#. Run the following command from your cyb3rhq-docker directory, such as ``cyb3rhq-docker/single-node/`` or ``cyb3rhq-docker/multi-node/``, to stop the outdated environment:

   .. code-block::

      # docker-compose down

#. Checkout the tag for the current version of cyb3rhq-docker:

      .. code-block::

         # git checkout v|CYB3RHQ_CURRENT_DOCKER|

#. Start the new version of Cyb3rhq using ``docker-compose``:

   .. code-block::

      # docker-compose up -d

Keeping custom docker-compose files
-----------------------------------

In Cyb3rhq 4.4, some paths are different to those in earlier versions. You have to update the old paths with the new ones.

``old-path`` -> ``new-path``

-  ``/usr/share/cyb3rhq-dashboard/config/certs/`` -> ``/usr/share/cyb3rhq-dashboard/certs/``
-  ``/usr/share/cyb3rhq-indexer/config/certs/`` -> ``/usr/share/cyb3rhq-indexer/certs/``
-  ``/usr/share/cyb3rhq-indexer/plugins/opensearch-security/securityconfig/`` -> ``/usr/share/cyb3rhq-indexer/opensearch-security/``

To upgrade your deployment keeping your custom docker-compose files, do the following.

#. Run the following command from your cyb3rhq-docker directory, such as ``cyb3rhq-docker/single-node/`` or ``cyb3rhq-docker/multi-node/``, to stop the outdated environment:

   .. code-block::

      # docker-compose down

#. If you are updating from 4.3, edit ``docker-compose.yml`` and update it with the new paths in 4.4. You can see the new paths for single node docker compose files, such as  ``single-node/docker-compose.yml`` below. For multi node docker compose files, such as  ``multi-node/docker-compose.yml``, you need to do similar changes in the corresponding files.

   .. code-block:: yaml
      :emphasize-lines: 8-12, 14, 19-21

      cyb3rhq.manager:
         image: cyb3rhq/cyb3rhq-manager:|CYB3RHQ_CURRENT_KUBERNETES|
      ...
      cyb3rhq.indexer:
         image: cyb3rhq/cyb3rhq-indexer:|CYB3RHQ_CURRENT_KUBERNETES|
         volumes:
            - cyb3rhq-indexer-data:/var/lib/cyb3rhq-indexer
            - ./config/cyb3rhq_indexer_ssl_certs/root-ca.pem:/usr/share/cyb3rhq-indexer/certs/root-ca.pem
            - ./config/cyb3rhq_indexer_ssl_certs/cyb3rhq.indexer-key.pem:/usr/share/cyb3rhq-indexer/certs/cyb3rhq.indexer.key
            - ./config/cyb3rhq_indexer_ssl_certs/cyb3rhq.indexer.pem:/usr/share/cyb3rhq-indexer/certs/cyb3rhq.indexer.pem
            - ./config/cyb3rhq_indexer_ssl_certs/admin.pem:/usr/share/cyb3rhq-indexer/certs/admin.pem
            - ./config/cyb3rhq_indexer_ssl_certs/admin-key.pem:/usr/share/cyb3rhq-indexer/certs/admin-key.pem
            - ./config/cyb3rhq_indexer/cyb3rhq.indexer.yml:/usr/share/cyb3rhq-indexer/opensearch.yml
            - ./config/cyb3rhq_indexer/internal_users.yml:/usr/share/cyb3rhq-indexer/opensearch-security/internal_users.yml
      ...
      cyb3rhq.dashboard:
         image: cyb3rhq/cyb3rhq-dashboard:|CYB3RHQ_CURRENT_KUBERNETES|
         volumes:
            - ./config/cyb3rhq_indexer_ssl_certs/cyb3rhq.dashboard.pem:/usr/share/cyb3rhq-dashboard/certs/cyb3rhq-dashboard.pem
            - ./config/cyb3rhq_indexer_ssl_certs/cyb3rhq.dashboard-key.pem:/usr/share/cyb3rhq-dashboard/certs/cyb3rhq-dashboard-key.pem
            - ./config/cyb3rhq_indexer_ssl_certs/root-ca.pem:/usr/share/cyb3rhq-dashboard/certs/root-ca.pem
            - ./config/cyb3rhq_dashboard/opensearch_dashboards.yml:/usr/share/cyb3rhq-dashboard/config/opensearch_dashboards.yml
            - ./config/cyb3rhq_dashboard/cyb3rhq.yml:/usr/share/cyb3rhq-dashboard/data/cyb3rhq/config/cyb3rhq.yml

#. Start the new version of Cyb3rhq using ``docker-compose``:

   .. code-block::

      # docker-compose up -d            

