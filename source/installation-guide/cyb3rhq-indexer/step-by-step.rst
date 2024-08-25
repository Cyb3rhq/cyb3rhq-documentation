.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Cyb3rhq indexer is a highly scalable full-text search engine. Install the Cyb3rhq indexer in a single-node or multi-node configuration according to your environment needs.

Installing the Cyb3rhq indexer step by step
=========================================

Install and configure the Cyb3rhq indexer as a single-node or multi-node cluster following step-by-step instructions. Cyb3rhq indexer is a highly scalable full-text search engine and offers advanced security, alerting, index management, deep performance analysis, and several other features.

The installation process is divided into three stages.

#. Certificates creation

#. Nodes installation

#. Cluster initialization


.. note:: You need root user privileges to run all the commands described below.

.. _certificates_creation:

1. Certificates creation
------------------------
.. raw:: html

    <div class="accordion-section open">

Generating the SSL certificates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Download the ``cyb3rhq-certs-tool.sh`` script and the ``config.yml`` configuration file. This creates the certificates that encrypt communications between the Cyb3rhq central components.

   .. code-block:: console

    # curl -sO https://packages.wazuh.com/|CYB3RHQ_CURRENT_MINOR|/cyb3rhq-certs-tool.sh
    # curl -sO https://packages.wazuh.com/|CYB3RHQ_CURRENT_MINOR|/config.yml

#. Edit ``./config.yml`` and replace the node names and IP values with the corresponding names and IP addresses. You need to do this for all Cyb3rhq server, Cyb3rhq indexer, and Cyb3rhq dashboard nodes. Add as many node fields as needed.

      .. code-block:: yaml

        nodes:
          # Cyb3rhq indexer nodes
          indexer:
            - name: indexer-1
              ip: "<indexer-node-ip>"
            #- name: indexer-2
            #  ip: "<indexer-node-ip>"
            #- name: indexer-3
            #  ip: "<indexer-node-ip>"

          # Cyb3rhq server nodes
          # If there is more than one Cyb3rhq server
          # node, each one must have a node_type
          server:
            - name: server-1
              ip: "<server-node-ip>"
            #  node_type: master
            #- name: server-2
            #  ip: "<server-node-ip>"
            #  node_type: worker
            #- name: server-3
            #  ip: "<server-node-ip>"
            #  node_type: worker

          # Cyb3rhq dashboard nodes
          dashboard:
            - name: dashboard
              ip: "<dashboard-node-ip>"


      To learn more about how to create and configure the certificates, see the :doc:`/user-manual/cyb3rhq-indexer/certificates` section.

#. Run ``./cyb3rhq-certs-tool.sh`` to create the certificates. For a multi-node cluster, these certificates need to be later deployed to all Cyb3rhq instances in your cluster.

   .. code-block:: console

     #  bash ./cyb3rhq-certs-tool.sh -A

   .. note::

      To use the Cyb3rhq certificates tool in macOS and Windows, ensure Docker is installed. For more information, see :ref:`cyb3rhq_cert_tool_docker`.

#. Compress all the necessary files.

   .. code-block:: console

     # tar -cvf ./cyb3rhq-certificates.tar -C ./cyb3rhq-certificates/ .
     # rm -rf ./cyb3rhq-certificates


#. Copy the ``cyb3rhq-certificates.tar`` file to all the nodes, including the Cyb3rhq indexer, Cyb3rhq server, and Cyb3rhq dashboard nodes. This can be done by using the ``scp`` utility.


2. Nodes installation
---------------------
.. raw:: html

    <div class="accordion-section open">


Installing package dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: /_templates/installations/indexer/common/install-dependencies.rst

Adding the Cyb3rhq repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. tabs::


      .. group-tab:: Yum


        .. include:: /_templates/installations/common/yum/add-repository.rst



      .. group-tab:: APT


        .. include:: /_templates/installations/common/deb/add-repository.rst



Installing the Cyb3rhq indexer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Install the Cyb3rhq indexer package.

   .. tabs::

      .. group-tab:: Yum

         .. code-block:: console

            # yum -y install cyb3rhq-indexer|CYB3RHQ_INDEXER_RPM_PKG_INSTALL|

      .. group-tab:: APT

         .. code-block:: console

            # apt-get -y install cyb3rhq-indexer|CYB3RHQ_INDEXER_DEB_PKG_INSTALL|

Configuring the Cyb3rhq indexer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  .. include:: /_templates/installations/indexer/common/configure_indexer_nodes.rst


Deploying certificates
^^^^^^^^^^^^^^^^^^^^^^

  .. note::
    Make sure that a copy of the ``cyb3rhq-certificates.tar`` file, created during the initial configuration step, is placed in your working directory.

  .. include:: /_templates/installations/indexer/common/deploy_certificates.rst

Starting the service
^^^^^^^^^^^^^^^^^^^^

  #. Enable and start the Cyb3rhq indexer service.

      .. include:: /_templates/installations/indexer/common/enable_indexer.rst

Repeat this stage of the installation process for every Cyb3rhq indexer node in your cluster. Then proceed with initializing your single-node or multi-node cluster in the next stage.


3. Cluster initialization
-------------------------
.. raw:: html

    <div class="accordion-section open">

#. Run the Cyb3rhq indexer ``indexer-security-init.sh`` script on `any` Cyb3rhq indexer node to load the new certificates information and start the single-node or multi-node cluster.

   .. code-block:: console

      # /usr/share/cyb3rhq-indexer/bin/indexer-security-init.sh

   .. note::

      You only have to initialize the cluster *once*, there is no need to run this command on every node.

Testing the cluster installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Replace ``<CYB3RHQ_INDEXER_IP_ADDRESS>`` and run the following commands to confirm that the installation is successful.

   .. code-block:: console

      # curl -k -u admin:admin https://<CYB3RHQ_INDEXER_IP_ADRESS>:9200

   .. code-block:: none
      :class: output accordion-output

      {
        "name" : "node-1",
        "cluster_name" : "cyb3rhq-cluster",
        "cluster_uuid" : "095jEW-oRJSFKLz5wmo5PA",
        "version" : {
          "number" : "7.10.2",
          "build_type" : "rpm",
          "build_hash" : "db90a415ff2fd428b4f7b3f800a51dc229287cb4",
          "build_date" : "2023-06-03T06:24:25.112415503Z",
          "build_snapshot" : false,
          "lucene_version" : "9.6.0",
          "minimum_wire_compatibility_version" : "7.10.0",
          "minimum_index_compatibility_version" : "7.0.0"
        },
        "tagline" : "The OpenSearch Project: https://opensearch.org/"
      }

#. Replace ``<CYB3RHQ_INDEXER_IP_ADDRESS>`` and run the following command to check if the single-node or multi-node cluster is working correctly.

   .. code-block:: console

      # curl -k -u admin:admin https://<CYB3RHQ_INDEXER_IP_ADDRESS>:9200/_cat/nodes?v

Next steps
----------

The Cyb3rhq indexer is now successfully installed on your single-node or multi-node cluster, and you can proceed with installing the Cyb3rhq server. To perform this action, see the :doc:`../cyb3rhq-server/step-by-step` section.

If you want to uninstall the Cyb3rhq indexer, see :ref:`uninstall_indexer`.
