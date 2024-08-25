.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: The Cyb3rhq server is in charge of analyzing the data received from the Cyb3rhq agents. Install the Cyb3rhq server in a single-node or multi-node configuration according to your environment needs.

Installing the Cyb3rhq server step by step
========================================

Install and configure the Cyb3rhq server as a single-node or multi-node cluster following step-by-step instructions. The Cyb3rhq server is a central component that includes the Cyb3rhq manager and Filebeat. The Cyb3rhq manager collects and analyzes data from the deployed Cyb3rhq agents. It triggers alerts when threats or anomalies are detected. Filebeat securely forwards alerts and archived events to the Cyb3rhq indexer.

The installation process is divided into two stages.

#. Cyb3rhq server node installation

#. Cluster configuration for multi-node deployment

.. note:: You need root user privileges to run all the commands described below.

1. Cyb3rhq server node installation
----------------------------------
.. raw:: html

  <div class="accordion-section open">

Adding the Cyb3rhq repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^

  .. note::
    If you are installing the Cyb3rhq server on the same host as the Cyb3rhq indexer, you may skip these steps as you may have added the Cyb3rhq repository already.

  ..
    Add the Cyb3rhq repository to download the official Cyb3rhq packages. As an alternative, you can download the Cyb3rhq packages directly from :doc:`../packages-list`.

  .. tabs::


    .. group-tab:: Yum


      .. include:: /_templates/installations/common/yum/add-repository.rst



    .. group-tab:: APT


      .. include:: /_templates/installations/common/deb/add-repository.rst




Installing the Cyb3rhq manager
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Install the Cyb3rhq manager package.

   .. tabs::

      .. group-tab:: Yum

         .. code-block:: console

            # yum -y install cyb3rhq-manager|CYB3RHQ_MANAGER_RPM_PKG_INSTALL|

      .. group-tab:: APT

         .. code-block:: console

            # apt-get -y install cyb3rhq-manager|CYB3RHQ_MANAGER_DEB_PKG_INSTALL|

.. _cyb3rhq_server_multi_node_filebeat:

Installing Filebeat
^^^^^^^^^^^^^^^^^^^

  #. Install the Filebeat package.

      .. tabs::


        .. group-tab:: Yum


          .. include:: /_templates/installations/filebeat/common/yum/install_filebeat.rst



        .. group-tab:: APT


          .. include:: /_templates/installations/filebeat/common/apt/install_filebeat.rst


.. _installation_configuring_filebeat:

Configuring Filebeat
^^^^^^^^^^^^^^^^^^^^

  #. Download the preconfigured Filebeat configuration file.

      .. code-block:: console

        # curl -so /etc/filebeat/filebeat.yml https://packages.wazuh.com/|CYB3RHQ_CURRENT_MINOR|/tpl/cyb3rhq/filebeat/filebeat.yml


  #. Edit the ``/etc/filebeat/filebeat.yml`` configuration file and replace the following value:

     .. include:: /_templates/installations/filebeat/opensearch/configure_filebeat.rst

  #. Create a Filebeat keystore to securely store authentication credentials.

      .. code-block:: console

        # filebeat keystore create

  #. Add the default username and password ``admin``:``admin`` to the secrets keystore.

      .. code-block:: console

        # echo admin | filebeat keystore add username --stdin --force
        # echo admin | filebeat keystore add password --stdin --force

  #. Download the alerts template for the Cyb3rhq indexer.

     .. code-block:: console

        # curl -so /etc/filebeat/cyb3rhq-template.json https://raw.githubusercontent.com/cyb3rhq/cyb3rhq/v|CYB3RHQ_CURRENT|/extensions/elasticsearch/7.x/cyb3rhq-template.json
        # chmod go+r /etc/filebeat/cyb3rhq-template.json

  #. Install the Cyb3rhq module for Filebeat.

      .. code-block:: console

        # curl -s https://packages.wazuh.com/4.x/filebeat/cyb3rhq-filebeat-0.4.tar.gz | tar -xvz -C /usr/share/filebeat/module

Deploying certificates
^^^^^^^^^^^^^^^^^^^^^^

  .. note::
    Make sure that a copy of the ``cyb3rhq-certificates.tar`` file, created during the initial configuration step, is placed in your working directory.

  #. Replace ``<SERVER_NODE_NAME>`` with your Cyb3rhq server node certificate name, the same one used in ``config.yml`` when creating the certificates. Then, move the certificates to their corresponding location.

      .. include:: /_templates/installations/filebeat/opensearch/copy_certificates_filebeat_cyb3rhq_cluster.rst

Configuring the Cyb3rhq indexer connection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   You can skip this step if you are not going to use the vulnerability detection capability.

#. Save the Cyb3rhq indexer username and password into the Cyb3rhq manager keystore using the cyb3rhq-keystore tool:

   .. code-block:: console

      # echo '<INDEXER_USERNAME>' | /var/ossec/bin/cyb3rhq-keystore -f indexer -k username
      # echo '<INDEXER_PASSWORD>' | /var/ossec/bin/cyb3rhq-keystore -f indexer -k password

   .. note::

      The default step-by-step installation credentials are ``admin``:``admin``

#. Edit ``/var/ossec/etc/ossec.conf`` to configure the indexer connection.

   .. include:: /_templates/installations/manager/configure_indexer_connection.rst

Starting the Cyb3rhq manager
^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Enable and start the Cyb3rhq manager service.

   .. include:: /_templates/installations/cyb3rhq/common/enable_cyb3rhq_manager_service.rst

#. Run the following command to verify the Cyb3rhq manager status.

   .. include:: /_templates/installations/cyb3rhq/common/check_cyb3rhq_manager.rst

Starting the Filebeat service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  #. Enable and start the Filebeat service.

      .. include:: /_templates/installations/filebeat/common/enable_filebeat.rst

  #. Run the following command to verify that Filebeat is successfully installed.

     .. code-block:: console

        # filebeat test output

     Expand the output to see an example response.

     .. code-block:: none
          :class: output accordion-output

          elasticsearch: https://127.0.0.1:9200...
            parse url... OK
            connection...
              parse host... OK
              dns lookup... OK
              addresses: 127.0.0.1
              dial up... OK
            TLS...
              security: server's certificate chain verification is enabled
              handshake... OK
              TLS version: TLSv1.3
              dial up... OK
            talk to server... OK
            version: 7.10.2


Your Cyb3rhq server node is now successfully installed. Repeat this stage of the installation process for every Cyb3rhq server node in your Cyb3rhq cluster, then proceed with configuring the Cyb3rhq cluster. If you want a Cyb3rhq server single-node cluster, everything is set and you can proceed directly with :doc:`../cyb3rhq-dashboard/step-by-step`.

2. Cluster configuration for multi-node deployment
--------------------------------------------------
.. raw:: html

  <div class="accordion-section">

After completing the installation of the Cyb3rhq server on every node, you need to configure one server node only as the master and the rest as workers.

.. _cyb3rhq_server_master_node:

Configuring the Cyb3rhq server master node
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  #. Edit the following settings in the ``/var/ossec/etc/ossec.conf`` configuration file.

      .. include:: /_templates/installations/manager/configure_cyb3rhq_master_node.rst

  #. Restart the Cyb3rhq manager.

      .. include:: /_templates/installations/manager/restart_cyb3rhq_manager.rst

.. _cyb3rhq_server_worker_nodes:

Configuring the Cyb3rhq server worker nodes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  #. .. include:: /_templates/installations/manager/configure_cyb3rhq_worker_node.rst

  #. Restart the Cyb3rhq manager.

      .. include:: /_templates/installations/manager/restart_cyb3rhq_manager.rst

  Repeat these configuration steps for every Cyb3rhq server worker node in your cluster.

Testing Cyb3rhq server cluster
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To verify that the Cyb3rhq cluster is enabled and all the nodes are connected, execute the following command:

  .. code-block:: console

    # /var/ossec/bin/cluster_control -l

An example output of the command looks as follows:

  .. code-block:: none
    :class: output

      NAME         TYPE    VERSION  ADDRESS
      master-node  master  |CYB3RHQ_CURRENT|   10.0.0.3
      worker-node1 worker  |CYB3RHQ_CURRENT|   10.0.0.4
      worker-node2 worker  |CYB3RHQ_CURRENT|   10.0.0.5

Note that ``10.0.0.3``, ``10.0.0.4``, ``10.0.0.5`` are example IPs.

Next steps
----------

The Cyb3rhq server installation is now complete, and you can proceed with :doc:`../cyb3rhq-dashboard/step-by-step`.

If you want to uninstall the Cyb3rhq server, see :ref:`uninstall_server`.
