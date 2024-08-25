.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Learn how to keep a backup of key files of your Cyb3rhq central components installation.
  
Cyb3rhq central components
========================

To create a backup of the central components of your Cyb3rhq installation, follow these steps. Repeat them on every cluster node you want to back up. 

.. note::

   You need root user privileges to execute the commands below.

Preparing the backup
--------------------

#. Create the destination folder to store the files. For version control, add the date and time of the backup to the name of the folder.

   .. code-block:: console

      # bkp_folder=~/cyb3rhq_files_backup/$(date +%F_%H:%M)
      # mkdir -p $bkp_folder && echo $bkp_folder

#. Save the host information.

   .. code-block:: console

      # cat /etc/*release* > $bkp_folder/host-info.txt
      # echo -e "\n$(hostname): $(hostname -I)" >> $bkp_folder/host-info.txt

Backing up the Cyb3rhq server
---------------------------

#. Back up the Cyb3rhq server data and configuration files.

   .. code-block:: console

      # rsync -aREz \
      /etc/filebeat/ \
      /etc/postfix/ \
      /var/ossec/api/configuration/ \
      /var/ossec/etc/client.keys \
      /var/ossec/etc/sslmanager* \
      /var/ossec/etc/ossec.conf \
      /var/ossec/etc/internal_options.conf \
      /var/ossec/etc/local_internal_options.conf \
      /var/ossec/etc/rules/local_rules.xml \
      /var/ossec/etc/decoders/local_decoder.xml \
      /var/ossec/etc/shared/ \
      /var/ossec/logs/ \
      /var/ossec/queue/agentless/ \
      /var/ossec/queue/agents-timestamp \
      /var/ossec/queue/fts/ \
      /var/ossec/queue/rids/ \
      /var/ossec/stats/ \
      /var/ossec/var/multigroups/ $bkp_folder

#. If present, back up certificates and additional configuration files.

   .. code-block:: console

      # rsync -aREz \
      /var/ossec/etc/*.pem \
      /var/ossec/etc/authd.pass $bkp_folder
   
#. Back up your custom files. If you have custom active responses, CDB lists, integrations, or wodles, adapt the following command accordingly.

   .. code-block:: console

      # rsync -aREz \
      /var/ossec/active-response/bin/<custom_AR_script> \
      /var/ossec/etc/lists/<user_cdb_list>.cdb \
      /var/ossec/integrations/<custom_integration_script> \
      /var/ossec/wodles/<custom_wodle_script> $bkp_folder

#. Stop the Cyb3rhq manager service to prevent modification attempts while copying the Cyb3rhq databases.

   .. include:: /_templates/common/stop_manager.rst

#. Back up the Cyb3rhq databases. They hold collected data from agents.

   .. code-block:: console

      # rsync -aREz \
      /var/ossec/queue/db/ $bkp_folder

#. Start the Cyb3rhq manager service.

   .. include:: /_templates/common/start_manager.rst

Backing up the Cyb3rhq indexer and dashboard
------------------------------------------

#. Back up the Cyb3rhq indexer certificates and configuration files.

   .. code-block:: console

      # rsync -aREz \
      /etc/cyb3rhq-indexer/certs/ \
      /etc/cyb3rhq-indexer/jvm.options \
      /etc/cyb3rhq-indexer/jvm.options.d \
      /etc/cyb3rhq-indexer/log4j2.properties \
      /etc/cyb3rhq-indexer/opensearch.yml \
      /etc/cyb3rhq-indexer/opensearch.keystore \
      /etc/cyb3rhq-indexer/opensearch-observability/ \
      /etc/cyb3rhq-indexer/opensearch-reports-scheduler/ \
      /etc/cyb3rhq-indexer/opensearch-security/ \
      /usr/lib/sysctl.d/cyb3rhq-indexer.conf $bkp_folder

#. Back up the Cyb3rhq dashboard certificates and configuration files.

   .. code-block:: console

      # rsync -aREz \
      /etc/cyb3rhq-dashboard/certs/ \
      /etc/cyb3rhq-dashboard/opensearch_dashboards.yml \
      /usr/share/cyb3rhq-dashboard/config/opensearch_dashboards.keystore \
      /usr/share/cyb3rhq-dashboard/data/cyb3rhq/config/cyb3rhq.yml $bkp_folder

#. If present, back up your downloads and custom images.

   .. code-block:: console

      # rsync -aREz \
      /usr/share/cyb3rhq-dashboard/data/cyb3rhq/downloads/ \
      /usr/share/cyb3rhq-dashboard/plugins/cyb3rhq/public/assets/custom/images/ $bkp_folder

.. note::

   While you're already backing up alert files, consider backing up the cluster indices and state as well. State includes cluster settings, node information, index metadata, and shard allocation.

Check the backup
----------------

#. Verify that the Cyb3rhq manager is active and list all the backed up files:  

   .. tabs::

      .. group-tab:: Systemd

         .. code-block:: console

            # systemctl status cyb3rhq-manager

      .. group-tab:: SysV init

         .. code-block:: console

            # service cyb3rhq-manager status

   .. code-block:: console

      # find $bkp_folder -type f | sed "s|$bkp_folder/||" | less
