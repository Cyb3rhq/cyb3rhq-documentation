.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Learn how to install the Cyb3rhq indexer using the assisted installation method. The Cyb3rhq indexer is a highly scalable full-text search engine and offers advanced security, alerting, index management, deep performance analysis, and several other features.

Installing the Cyb3rhq indexer using the assisted installation method
===================================================================

Install and configure the Cyb3rhq indexer as a single-node or multi-node cluster using the assisted installation method. The Cyb3rhq indexer is a highly scalable full-text search engine. It offers advanced security, alerting, index management, deep performance analysis, and several other features.

Cyb3rhq indexer cluster installation
----------------------------------

The installation process is divided into three stages.

#. Initial configuration

#. Cyb3rhq indexer nodes installation

#. Cluster initialization

.. note:: You need root user privileges to run all the commands described below.

1. Initial configuration
------------------------

Indicate your deployment configuration, create the SSL certificates to encrypt communications between the Cyb3rhq components, and generate random passwords to secure your installation.

#. Download the Cyb3rhq installation assistant and the configuration file.

      .. code-block:: console

          # curl -sO https://packages.wazuh.com/|CYB3RHQ_CURRENT_MINOR|/cyb3rhq-install.sh
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


#. Run the Cyb3rhq installation assistant with the option ``--generate-config-files`` to generate the  Cyb3rhq cluster key, certificates, and passwords necessary for installation. You can find these files in ``./cyb3rhq-install-files.tar``. The Cyb3rhq installation assistant requires dependencies like ``openssl`` and ``lsof`` to work. To install them automatically, add the ``--install-dependencies`` option to the command.

      .. code-block:: console

        # bash cyb3rhq-install.sh --generate-config-files


#. Copy the ``cyb3rhq-install-files.tar`` file to all the servers of the distributed deployment, including the Cyb3rhq server, the Cyb3rhq indexer, and the Cyb3rhq dashboard nodes. This can be done by using the ``scp`` utility.


2. Cyb3rhq indexer nodes installation
------------------------------------

Install and configure the Cyb3rhq indexer nodes.


#. Download the Cyb3rhq installation assistant.

      .. code-block:: console

        # curl -sO https://packages.wazuh.com/|CYB3RHQ_CURRENT_MINOR|/cyb3rhq-install.sh


#. Run the Cyb3rhq installation assistant with the option ``--cyb3rhq-indexer`` and the node name to install and configure the Cyb3rhq indexer. The node name must be the same one used in ``config.yml`` for the initial configuration, for example, ``node-1``. The Cyb3rhq installation assistant requires dependencies like ``openssl`` and ``lsof`` to work. To install them automatically, add the ``--install-dependencies`` option to the command.

      .. note:: Make sure that a copy of ``cyb3rhq-install-files.tar``, created during the initial configuration step, is placed in your working directory.

      .. code-block:: console

        # bash cyb3rhq-install.sh --cyb3rhq-indexer node-1


Repeat this stage of the installation process for every Cyb3rhq indexer node in your cluster. Then proceed with initializing your single-node or multi-node cluster in the next stage.


3. Cluster initialization
-------------------------

The final stage of installing the Cyb3rhq indexer single-node or multi-node cluster consists of running the security admin script.

#. Run the Cyb3rhq installation assistant with option ``--start-cluster`` on any Cyb3rhq indexer node to load the new certificates information and start the cluster.

   .. code-block:: console

     # bash cyb3rhq-install.sh --start-cluster

   .. note:: You only have to initialize the cluster `once`, there is no need to run this command on every node.

Testing the cluster installation
--------------------------------

#. Run the following command to get the *admin* password:

   .. code-block:: console

      # tar -axf cyb3rhq-install-files.tar cyb3rhq-install-files/cyb3rhq-passwords.txt -O | grep -P "\'admin\'" -A 1

#. Run the following command to confirm that the installation is successful. Replace ``<ADMIN_PASSWORD>`` with the password gotten from the output of the previous command. Replace ``<CYB3RHQ_INDEXER_IP>`` with the configured Cyb3rhq indexer IP address:

   .. code-block:: console

      # curl -k -u admin:<ADMIN_PASSWORD> https://<CYB3RHQ_INDEXER_IP>:9200

   .. code-block:: none
      :class: output

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

#. Replace ``<CYB3RHQ_INDEXER_IP>`` and ``<ADMIN_PASSWORD>``, and run the following command to check if the cluster is working correctly:

   .. code-block:: console

      # curl -k -u admin:<ADMIN_PASSWORD> https://<CYB3RHQ_INDEXER_IP>:9200/_cat/nodes?v

Next steps
----------

The Cyb3rhq indexer is now successfully installed, and you can proceed with installing the Cyb3rhq server. To perform this action, see the :doc:`../cyb3rhq-server/installation-assistant` section.
