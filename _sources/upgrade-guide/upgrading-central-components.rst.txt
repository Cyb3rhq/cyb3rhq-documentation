.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Learn how to upgrade the Cyb3rhq indexer, server, and dashboard to the latest version available.

Cyb3rhq central components
========================

This section guides you through the upgrade process of the Cyb3rhq indexer, the Cyb3rhq server, and the Cyb3rhq dashboard. To migrate from Open Distro for Elasticsearch 1.13 to the Cyb3rhq indexer and dashboard components, read the corresponding :doc:`/migration-guide/cyb3rhq-indexer` and :doc:`/migration-guide/cyb3rhq-dashboard` sections.

.. note:: You need root user privileges to run all the commands described below.

Preparing the upgrade
---------------------

In the case Cyb3rhq is installed in a multi-node cluster configuration, repeat the following steps for every node.

#. Add the Cyb3rhq repository. You can skip this step if the repository is already present and enabled on the node.

   .. tabs::


     .. group-tab:: Yum


       .. include:: /_templates/installations/common/yum/add-repository.rst



     .. group-tab:: APT


       .. include:: /_templates/installations/common/deb/add-repository.rst




#. Stop the Filebeat service and the Cyb3rhq dashboard service if installed in the node.

   .. tabs::

      .. tab:: Systemd

         .. code-block:: console

            # systemctl stop filebeat
            # systemctl stop cyb3rhq-dashboard

      .. tab:: SysV init

         .. code-block:: console

            # service filebeat stop
            # service cyb3rhq-dashboard stop

Upgrading the Cyb3rhq indexer
---------------------------

.. note::

   Note that this upgrade process doesn't update plugins installed manually. Outdated plugins might cause the upgrade to fail.

   To ensure compatibility with the latest Cyb3rhq indexer and Cyb3rhq dashboard, please update manually installed plugins accordingly. For additional information, check the `distribution matrix <https://github.com/cyb3rhq/cyb3rhq-packages/tree/v|CYB3RHQ_CURRENT|#distribution-version-matrix>`__.

The cluster remains available throughout the upgrading process in a Cyb3rhq indexer cluster with multiple nodes. This rolling upgrade allows for the shutting down of one Cyb3rhq indexer node at a time for minimal disruption of service.

As a first step, remove the *ss4o* index templates. Replace ``<CYB3RHQ_INDEXER_IP_ADDRESS>``, ``<USERNAME>``, and ``<PASSWORD>`` before running any command below.

.. code-block:: bash

   curl -X DELETE "https://<CYB3RHQ_INDEXER_IP_ADDRESS>:9200/_index_template/ss4o_*_template" -u <USERNAME>:<PASSWORD> -k

Then, repeat the following steps for every Cyb3rhq indexer node.

#. Disable shard allocation.

   .. code-block:: bash

      curl -X PUT "https://<CYB3RHQ_INDEXER_IP_ADDRESS>:9200/_cluster/settings"  -u <USERNAME>:<PASSWORD> -k -H 'Content-Type: application/json' -d'
      {
        "persistent": {
          "cluster.routing.allocation.enable": "primaries"
        }
      }
      '

#. Stop non-essential indexing and perform a synced flush.

   .. code-block:: console

      # curl -X POST "https://<CYB3RHQ_INDEXER_IP_ADDRESS>:9200/_flush/synced" -u <USERNAME>:<PASSWORD> -k

#. Shut down the Cyb3rhq indexer in the node.

   .. tabs::

      .. tab:: Systemd

         .. code-block:: console

            # systemctl stop cyb3rhq-indexer

      .. tab:: SysV init

         .. code-block:: console

            # service cyb3rhq-indexer stop

#. Upgrade the Cyb3rhq indexer to the latest version.

   .. tabs::

      .. group-tab:: Yum

         .. code-block:: console

            # yum upgrade cyb3rhq-indexer|CYB3RHQ_INDEXER_RPM_PKG_INSTALL|

      .. group-tab:: APT

         .. code-block:: console

            # apt-get install cyb3rhq-indexer|CYB3RHQ_INDEXER_DEB_PKG_INSTALL|

#. Restart the Cyb3rhq indexer service.

   .. include:: /_templates/installations/indexer/common/enable_indexer.rst

#. Check that the newly upgraded Cyb3rhq indexer node joins the cluster.

   .. code-block:: console

      # curl -k -u <USERNAME>:<PASSWORD> https://<CYB3RHQ_INDEXER_IP_ADDRESS>:9200/_cat/nodes?v

#. Re-enable shard allocation.

   .. code-block:: bash

      curl -X PUT "https://<CYB3RHQ_INDEXER_IP_ADDRESS>:9200/_cluster/settings" -u <USERNAME>:<PASSWORD> -k -H 'Content-Type: application/json' -d'
      {
        "persistent": {
          "cluster.routing.allocation.enable": "all"
        }
      }
      '

#. Check the status of the Cyb3rhq indexer cluster again to see if the shard allocation has finished.

   .. code-block:: console

      # curl -k -u <USERNAME>:<PASSWORD> https://<CYB3RHQ_INDEXER_IP_ADDRESS>:9200/_cat/nodes?v

.. _upgrading_cyb3rhq_server:

Upgrading the Cyb3rhq server
--------------------------

When upgrading a multi-node Cyb3rhq manager cluster, run the upgrade in every node to make all the Cyb3rhq manager nodes join the cluster. Start with the master node to reduce server downtime.

   .. note:: Upgrading from Cyb3rhq 4.2.x or lower creates the ``cyb3rhq`` operating system user and group to replace ``ossec``. To avoid upgrade conflicts, make sure that the ``cyb3rhq`` user and group are not present in your operating system.

Upgrading the Cyb3rhq manager
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Upgrade the Cyb3rhq manager to the latest version.

.. tabs::

   .. group-tab:: Yum

      .. code-block:: console

         # yum upgrade cyb3rhq-manager|CYB3RHQ_MANAGER_RPM_PKG_INSTALL|

   .. group-tab:: APT

      .. code-block:: console

         # apt-get install cyb3rhq-manager|CYB3RHQ_MANAGER_DEB_PKG_INSTALL|

.. note::

   If the ``/var/ossec/etc/ossec.conf`` configuration file was modified, it will not be replaced by the upgrade. You will therefore have to add the settings of the new capabilities manually. More information can be found in :doc:`/user-manual/index`.

Configuring vulnerability detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If upgrading from version 4.7 and earlier, edit ``/var/ossec/etc/ossec.conf`` to configure the new vulnerability detection module as follows.

#. Add the new ``<vulnerability-detection>`` block and remove the old ``<vulnerability-detector>`` if it exists.

   .. include:: /_templates/installations/manager/configure_vulnerability_detection.rst

#. Configure the :doc:`indexer </user-manual/reference/ossec-conf/indexer>` block with the details of your Cyb3rhq indexer host.

   During the upgrade from 4.7, if an Indexer configuration does not exist in the ``/var/ossec/etc/ossec.conf`` file, a default Indexer configuration is automatically appended to ``/var/ossec/etc/ossec.conf`` as part of a new ``<ossec_conf>`` block.

   .. include:: /_templates/installations/manager/configure_indexer_connection.rst

#. Save the Cyb3rhq indexer username and password into the Cyb3rhq manager keystore using the :doc:`Cyb3rhq-keystore </user-manual/reference/tools/cyb3rhq-keystore>` tool.

   .. code-block:: console
  
      # echo '<INDEXER_USERNAME>' | /var/ossec/bin/cyb3rhq-keystore -f indexer -k username
      # echo '<INDEXER_PASSWORD>' | /var/ossec/bin/cyb3rhq-keystore -f indexer -k password
   
   .. note::

      In case you've forgotten your Cyb3rhq indexer password, follow the :doc:`password management </user-manual/user-administration/password-management>` guide to reset the password.

Configuring Filebeat
^^^^^^^^^^^^^^^^^^^^

#. Download the Cyb3rhq module for Filebeat:

   .. code-block:: console

      # curl -s https://packages.wazuh.com/4.x/filebeat/cyb3rhq-filebeat-0.4.tar.gz | sudo tar -xvz -C /usr/share/filebeat/module

#. Download the alerts template:

   .. code-block:: console

      # curl -so /etc/filebeat/cyb3rhq-template.json https://raw.githubusercontent.com/cyb3rhq/cyb3rhq/v|CYB3RHQ_CURRENT|/extensions/elasticsearch/7.x/cyb3rhq-template.json
      # chmod go+r /etc/filebeat/cyb3rhq-template.json

#. Restart Filebeat:

   .. include:: /_templates/installations/basic/elastic/common/enable_filebeat.rst

#. Upload the new Cyb3rhq template and pipelines for Filebeat.

   .. code-block:: console

      # filebeat setup --pipelines
      # filebeat setup --index-management -E output.logstash.enabled=false

Upgrading the Cyb3rhq dashboard
-----------------------------

.. note::

   Note that this upgrade process doesn't update plugins installed manually. Outdated plugins might cause the upgrade to fail.

   To ensure compatibility with the latest Cyb3rhq indexer and Cyb3rhq dashboard, please update manually installed plugins accordingly. For additional information, check the `distribution matrix <https://github.com/cyb3rhq/cyb3rhq-packages/tree/v|CYB3RHQ_CURRENT|#distribution-version-matrix>`__.

Configuration options might differ across versions. Follow these steps to ensure a smooth upgrade.

#. Backup the ``/etc/cyb3rhq-dashboard/opensearch_dashboards.yml`` file to save your settings.
#. Upgrade the Cyb3rhq dashboard.

   .. tabs::

      .. group-tab:: Yum

         .. code-block:: console

            # rm /etc/cyb3rhq-dashboard/opensearch_dashboards.yml
            # yum upgrade cyb3rhq-dashboard|CYB3RHQ_DASHBOARD_RPM_PKG_INSTALL|

      .. group-tab:: APT

         .. code-block:: console

            # apt-get install cyb3rhq-dashboard|CYB3RHQ_DASHBOARD_DEB_PKG_INSTALL|

         .. note::

            When prompted, choose to replace the ``/etc/cyb3rhq-dashboard/opensearch_dashboards.yml`` file with the updated version.

#. Manually reapply any settings changes to the ``/etc/cyb3rhq-dashboard/opensearch_dashboards.yml`` file.
#. Restart the Cyb3rhq dashboard:

    .. include:: /_templates/installations/dashboard/enable_dashboard.rst

Next steps
----------

The Cyb3rhq server, indexer, and dashboard are now successfully upgraded. The next step consists in upgrading the Cyb3rhq agents. Follow the instructions in:

-  :doc:`Upgrading the Cyb3rhq agent </upgrade-guide/cyb3rhq-agent/index>`.
