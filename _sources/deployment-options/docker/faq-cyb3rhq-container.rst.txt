.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Get answers to the most frequently asked questions about the Cyb3rhq deployment on Docker in this FAQ. 
    
FAQ
===

How can I tune the Cyb3rhq dashboard configuration?
-------------------------------------------------

The Cyb3rhq dashboard reads its configuration from ``config/cyb3rhq_dashboard/opensearch_dashboards.yml``:

.. code-block:: yaml

    cyb3rhq-dashboard:
    ...
    volumes:
      - ./custom_opensearch_dashboards.yml:/usr/share/cyb3rhq-dashboard/opensearch_dashboards.yml

Read the `YAML files Opensearch documentation <https://opensearch.org/docs/latest/security-plugin/configuration/yaml/#opensearchyml>`__ to know more about the variables you can use on this image.

How can I tune the Cyb3rhq indexer configuration?
-----------------------------------------------

The Cyb3rhq indexer container uses the default configuration, and it’s not exposed by default.

If you want to override the default configuration, create a file ``config/cyb3rhq_indexer/<new_cyb3rhq_indexer>.yml`` and add your custom version of the configuration to it. Then map your configuration file inside the container in the ``docker-compose.yml``. Update the Cyb3rhq indexer container declaration to:

.. code-block:: yaml

    <new_cyb3rhq_indexer>:
      image: cyb3rhq/cyb3rhq-indexer:latest
      ports:
        - "9200:9200"
        - "9300:9300"
      environment:
        ES_JAVA_OPTS: "-Xms6g -Xmx6g"
      networks:
        - docker_cyb3rhq

How can I store the Cyb3rhq indexer data?
---------------------------------------

The data stored in the Cyb3rhq indexer persists after container reboots but not after container removal.

By default, the single-node and multi-node deployments already have volumes configured. For example, see  ``cyb3rhq1.indexer`` volume in the multi-node ``docker-compose.yml`` file:

.. code-block:: yaml

   cyb3rhq1.indexer:
    ...
    volumes:
      - cyb3rhq-indexer-data-1:/var/lib/cyb3rhq-indexer

This stores Cyb3rhq indexer data inside ``cyb3rhq-indexer-data-1`` volume in the Docker host local file system.
