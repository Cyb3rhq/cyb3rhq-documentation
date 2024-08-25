.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Learn how to restore a backup of key files of your Cyb3rhq central components installation.
  
Cyb3rhq central components
========================

Perform the following actions to restore the Cyb3rhq central components data, depending on your deployment type.

.. note::
   
   For a multi-node setup, there should be a backup file for each node within the cluster. You need root user privileges to execute the commands below.

Single-node data restoration
----------------------------

You need to have a new installation of Cyb3rhq. Follow the :doc:`/quickstart` guide to perform a fresh installation of the Cyb3rhq central components on a new server.

The actions below will guide you through the data restoration process for a single-node deployment.

Preparing the data restoration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Compress the files generated after performing Cyb3rhq files backup and transfer them to the new server:

   .. code-block:: console

      # tar -cvzf cyb3rhq_central_components.tar.gz ~/cyb3rhq_files_backup/

#. Move the compressed file to the root ``/`` directory of your node:

   .. code-block:: console

      # mv cyb3rhq_central_components.tar.gz /
      # cd /

#. Decompress the backup files and change the current working directory to the directory based on the date and time of the backup files:

   .. code-block:: console

      # tar -xzvf cyb3rhq_central_components.tar.gz
      # cd ~/cyb3rhq_files_backup/<DATE_TIME>

Restoring Cyb3rhq indexer files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Perform the following steps to restore the Cyb3rhq indexer files on the new server.

#. Stop the Cyb3rhq indexer to prevent any modifications to the Cyb3rhq indexer files during the restoration process:

   .. code-block:: console

      # systemctl stop cyb3rhq-indexer

#. Restore the Cyb3rhq indexer configuration files and change the file permissions and ownerships accordingly:

   .. code-block:: console

      # sudo cp etc/cyb3rhq-indexer/jvm.options /etc/cyb3rhq-indexer/jvm.options
      # chown cyb3rhq-indexer:cyb3rhq-indexer /etc/cyb3rhq-indexer/jvm.options
      # sudo cp -r etc/cyb3rhq-indexer/jvm.options.d/* /etc/cyb3rhq-indexer/jvm.options.d/
      # chown cyb3rhq-indexer:cyb3rhq-indexer /etc/cyb3rhq-indexer/jvm.options.d
      # sudo cp etc/cyb3rhq-indexer/log4j2.properties /etc/cyb3rhq-indexer/log4j2.properties
      # chown cyb3rhq-indexer:cyb3rhq-indexer /etc/cyb3rhq-indexer/log4j2.properties
      # sudo cp etc/cyb3rhq-indexer/opensearch.keystore /etc/cyb3rhq-indexer/opensearch.keystore
      # chown cyb3rhq-indexer:cyb3rhq-indexer /etc/cyb3rhq-indexer/opensearch.keystore
      # sudo cp -r etc/cyb3rhq-indexer/opensearch-observability/* /etc/cyb3rhq-indexer/opensearch-observability/
      # chown -R cyb3rhq-indexer:cyb3rhq-indexer /etc/cyb3rhq-indexer/opensearch-observability/
      # sudo cp -r etc/cyb3rhq-indexer/opensearch-reports-scheduler/* /etc/cyb3rhq-indexer/opensearch-reports-scheduler/
      # chown -R cyb3rhq-indexer:cyb3rhq-indexer /etc/cyb3rhq-indexer/opensearch-reports-scheduler/
      # sudo cp usr/lib/sysctl.d/cyb3rhq-indexer.conf /usr/lib/sysctl.d/cyb3rhq-indexer.conf

#. Start the Cyb3rhq indexer service:

   .. code-block:: console

      # systemctl start cyb3rhq-indexer

.. _restoring-server-single-node:

Restoring Cyb3rhq server files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Perform the following steps to restore the Cyb3rhq server files on the new server.

#. Stop the Cyb3rhq manager and Filebeat to prevent any modification to the Cyb3rhq server files during the restore process:

   .. code-block:: console

      # systemctl stop filebeat
      # systemctl stop cyb3rhq-manager

#. Copy the Cyb3rhq server data and configuration files, and change the file permissions and ownerships accordingly:

   .. code-block:: console

      # sudo cp etc/filebeat/filebeat.reference.yml /etc/filebeat/
      # sudo cp etc/filebeat/fields.yml /etc/filebeat/
      # sudo cp -r etc/filebeat/modules.d/* /etc/filebeat/modules.d/
      # sudo cp -r etc/postfix/* /etc/postfix/
      # sudo cp var/ossec/etc/client.keys /var/ossec/etc/
      # chown root:cyb3rhq /var/ossec/etc/client.keys
      # sudo cp -r var/ossec/etc/sslmanager* /var/ossec/etc/
      # sudo cp var/ossec/etc/ossec.conf /var/ossec/etc/
      # chown root:cyb3rhq /var/ossec/etc/ossec.conf
      # sudo cp var/ossec/etc/internal_options.conf /var/ossec/etc/
      # chown root:cyb3rhq /var/ossec/etc/internal_options.conf
      # sudo cp var/ossec/etc/local_internal_options.conf /var/ossec/etc/
      # chown root:cyb3rhq /var/ossec/etc/local_internal_options.conf
      # sudo cp -r var/ossec/etc/rules/* /var/ossec/etc/rules/
      # chown -R cyb3rhq:cyb3rhq /var/ossec/etc/rules/
      # sudo cp -r var/ossec/etc/decoders/* /var/ossec/etc/decoders
      # chown -R cyb3rhq:cyb3rhq /var/ossec/etc/decoders/
      # sudo cp -r var/ossec/etc/shared/* /var/ossec/etc/shared/
      # chown -R cyb3rhq:cyb3rhq /var/ossec/etc/shared/
      # chown root:cyb3rhq /var/ossec/etc/shared/ar.conf
      # sudo cp -r var/ossec/logs/* /var/ossec/logs/
      # chown -R cyb3rhq:cyb3rhq /var/ossec/logs/
      # sudo cp -r var/ossec/queue/agentless/*  /var/ossec/queue/agentless/
      # chown -R cyb3rhq:cyb3rhq /var/ossec/queue/agentless/
      # sudo cp var/ossec/queue/agents-timestamp /var/ossec/queue/
      # chown root:cyb3rhq /var/ossec/queue/agents-timestamp
      # sudo cp -r var/ossec/queue/fts/* /var/ossec/queue/fts/
      # chown -R cyb3rhq:cyb3rhq /var/ossec/queue/fts/
      # sudo cp -r var/ossec/queue/rids/* /var/ossec/queue/rids/
      # chown -R cyb3rhq:cyb3rhq /var/ossec/queue/rids/
      # sudo cp -r var/ossec/stats/* /var/ossec/stats/ 
      # chown -R cyb3rhq:cyb3rhq /var/ossec/stats/ 
      # sudo cp -r var/ossec/var/multigroups/* /var/ossec/var/multigroups/
      # chown -R cyb3rhq:cyb3rhq /var/ossec/var/multigroups/

#. Restore certificates for Cyb3rhq agent and Cyb3rhq server communication, and additional configuration files if present:

   .. code-block:: console

      # sudo cp -r var/ossec/etc/*.pem /var/ossec/etc/
      # chown -R root:cyb3rhq /var/ossec/etc/*.pem
      # sudo cp var/ossec/etc/authd.pass /var/ossec/etc/
      # chown -R root:cyb3rhq /var/ossec/etc/authd.pass

#. Restore your custom files. If you have custom active response scripts, CDB lists, integrations, or wodles, adapt the following commands accordingly:

   .. code-block:: console

      # sudo cp var/ossec/active-response/bin/<CUSTOM_ACTIVE_RESPONSE_SCRIPT> /var/ossec/active-response/bin/
      # chown root:cyb3rhq /var/ossec/active-response/bin/<CUSTOM_ACTIVE_RESPONSE_SCRIPT> 
      # sudo cp var/ossec/etc/lists/<USER_CDB_LIST>.cdb /var/ossec/etc/lists/
      # chown root:cyb3rhq /var/ossec/etc/lists/<USER_CDB_LIST>.cdb 
      # sudo cp var/ossec/integrations/<CUSTOM_INTEGRATION_SCRIPT> /var/ossec/integrations/
      # chown root:cyb3rhq /var/ossec/integrations/<CUSTOM_INTEGRATION_SCRIPT>
      # sudo cp var/ossec/wodles/<CUSTOM_WODLE_SCRIPT> /var/ossec/wodles/
      # chown root:cyb3rhq /var/ossec/wodles/<CUSTOM_WODLE_SCRIPT>

#. Restore the Cyb3rhq databases that contain collected data from the Cyb3rhq agents:

   .. code-block:: console

      # sudo cp var/ossec/queue/db/* /var/ossec/queue/db/ 
      # chown -R cyb3rhq:cyb3rhq /var/ossec/queue/db/

#. Start the Filebeat service:

   .. code-block:: console

      # systemctl start filebeat

#. Start the Cyb3rhq manager service:

   .. code-block:: console

      # systemctl start cyb3rhq-manager

Restoring Cyb3rhq dashboard files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Perform the following steps to restore Cyb3rhq reports and custom images on the new server if you have any from your backup.

#. Restore your Cyb3rhq reports using the following command:

   .. code-block:: console

      # mkdir -p /usr/share/cyb3rhq-dashboard/data/cyb3rhq/downloads/reports/
      # sudo cp -r usr/share/cyb3rhq-dashboard/data/cyb3rhq/downloads/reports/* /usr/share/cyb3rhq-dashboard/data/cyb3rhq/downloads/reports/ 
      # chown -R cyb3rhq-dashboard:cyb3rhq-dashboard /usr/share/cyb3rhq-dashboard/data/cyb3rhq/downloads/

#. Navigate to **Dashboard management** > **App Settings** > **Custom branding** from the Cyb3rhq dashboard and upload your custom images.

Restoring old logs
^^^^^^^^^^^^^^^^^^

Cyb3rhq, by default, compresses logs that are older than a day. While performing old log restoration in the :ref:`restoring-server-single-node` section, the old logs remain compressed.

Perform the following actions on your Cyb3rhq server to decompress these logs and index them in the new Cyb3rhq indexer:

.. note::
   
   Restoring old logs will have a creation date of the day when the restoration is performed.

#. Create a Python script called ``recovery.py`` on your Cyb3rhq server. This script decompresses all the old logs and stores them in the ``recovery.json`` file in the ``/tmp`` directory:

   .. code-block:: console

      # touch recovery.py

#. Add the following content to the ``recovery.py`` script:


   .. code-block:: python

      #!/usr/bin/env python

      import gzip
      import time
      import json
      import argparse
      import re
      import os
      from datetime import datetime
      from datetime import timedelta

      def log(msg):
          now_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
          final_msg = "{0} cyb3rhq-reinjection: {1}".format(now_date, msg)
          print(final_msg)
          if log_file:
              f_log.write(final_msg + "\n")

      EPS_MAX = 400
      cyb3rhq_path = '/var/ossec/'
      max_size=1
      log_file = None

      parser = argparse.ArgumentParser(description='Reinjection script')
      parser.add_argument('-eps','--eps', metavar='eps', type=int, required = False, help='Events per second.')
      parser.add_argument('-min', '--min_timestamp', metavar='min_timestamp', type=str, required = True, help='Min timestamp. Example: 2017-12-13T23:59:06')
      parser.add_argument('-max', '--max_timestamp', metavar='max_timestamp', type=str, required = True, help='Max timestamp. Example: 2017-12-13T23:59:06')
      parser.add_argument('-o', '--output_file', metavar='output_file', type=str, required = True, help='Output filename.')
      parser.add_argument('-log', '--log_file', metavar='log_file', type=str, required = False, help='Logs output')
      parser.add_argument('-w', '--cyb3rhq_path', metavar='cyb3rhq_path', type=str, required = False, help='Path to Cyb3rhq. By default:/var/ossec/')
      parser.add_argument('-sz', '--max_size', metavar='max_size', type=float, required = False, help='Max output file size in Gb. Default: 1Gb. Example: 2.5')

      args = parser.parse_args()

      if args.log_file:
          log_file = args.log_file
          f_log = open(log_file, 'a+')


      if args.max_size:
          max_size = args.max_size

      if args.cyb3rhq_path:
          cyb3rhq_path = args.cyb3rhq_path

      output_file = args.output_file

      #Gb to bytes
      max_bytes = int(max_size * 1024 * 1024 * 1024)

      if (max_bytes <= 0):
          log("Error: Incorrect max_size")
          exit(1)

      month_dict = ['Null','Jan','Feb','Mar','Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov','Dec']

      if args.eps:
          EPS_MAX = args.eps

      if EPS_MAX < 0:
          log("Error: incorrect EPS")
          exit(1)

      min_date = re.search('(\\d\\d\\d\\d)-(\\d\\d)-(\\d\\d)T\\d\\d:\\d\\d:\\d\\d', args.min_timestamp)
      if min_date:
          min_year = int(min_date.group(1))
          min_month = int(min_date.group(2))
          min_day = int(min_date.group(3))
      else:
          log("Error: Incorrect min timestamp")
          exit(1)

      max_date = re.search('(\\d\\d\\d\\d)-(\\d\\d)-(\\d\\d)T\\d\\d:\\d\\d:\\d\\d', args.max_timestamp)
      if max_date:
          max_year = int(max_date.group(1))
          max_month = int(max_date.group(2))
          max_day = int(max_date.group(3))
      else:
          log("Error: Incorrect max timestamp")
          exit(1)

      # Converting timestamp args to datetime
      min_timestamp = datetime.strptime(args.min_timestamp, '%Y-%m-%dT%H:%M:%S')
      max_timestamp = datetime.strptime(args.max_timestamp, '%Y-%m-%dT%H:%M:%S')

      chunk = 0
      written_alerts = 0
      trimmed_alerts = open(output_file, 'w')

      max_time=datetime(max_year, max_month, max_day)
      current_time=datetime(min_year, min_month, min_day)

      while current_time <= max_time: 
          alert_file = "{0}logs/alerts/{1}/{2}/ossec-alerts-{3:02}.json.gz".format(cyb3rhq_path,current_time.year,month_dict[current_time.month],current_time.day)

          if os.path.exists(alert_file):
              daily_alerts = 0
              compressed_alerts = gzip.open(alert_file, 'r')
              log("Reading file: "+ alert_file)
              for line in compressed_alerts:
                  # Transform line to json object
                  try:
                      line_json = json.loads(line.decode("utf-8", "replace"))

                      # Remove unnecessary part of the timestamp
                      string_timestamp = line_json['timestamp'][:19]

                      # Ensure timestamp integrity
                      while len(line_json['timestamp'].split("+")[0]) < 23:
                          line_json['timestamp'] = line_json['timestamp'][:20] + "0" + line_json['timestamp'][20:]

                      # Get the timestamp readable
                      event_date = datetime.strptime(string_timestamp, '%Y-%m-%dT%H:%M:%S')

                      # Check the timestamp belongs to the selected range
                      if (event_date <= max_timestamp and event_date >= min_timestamp):
                          chunk+=1
                          trimmed_alerts.write(json.dumps(line_json))
                          trimmed_alerts.write("\n")
                          trimmed_alerts.flush()
                          daily_alerts += 1
                          if chunk >= EPS_MAX:
                              chunk = 0
                              time.sleep(2)
                          if os.path.getsize(output_file) >= max_bytes:
                              trimmed_alerts.close()
                              log("Output file reached max size, setting it to zero and restarting")
                              time.sleep(EPS_MAX/100)
                              trimmed_alerts = open(output_file, 'w')

                  except ValueError as e:
                      print("Oops! Something went wrong reading: {}".format(line))
                      print("This is the error: {}".format(str(e)))

              compressed_alerts.close()
              log("Extracted {0} alerts from day {1}-{2}-{3}".format(daily_alerts,current_time.day,month_dict[current_time.month],current_time.year))
          else:
              log("Couldn't find file {}".format(alert_file))

          #Move to next file
          current_time += timedelta(days=1)

      trimmed_alerts.close()

   While you run the ``recovery.py`` script, you need to consider the following parameters:

   .. code-block:: none

      usage: recovery.py [-h] [-eps eps] -min min_timestamp -max max_timestamp -o
                            output_file [-log log_file] [-w cyb3rhq_path]
                            [-sz max_size]

        -eps eps, --eps eps   Events per second. Default: 400
        -min min_timestamp, --min_timestamp min_timestamp
                              Min timestamp. Example: 2019-11-13T08:42:17
        -max max_timestamp, --max_timestamp max_timestamp
                              Max timestamp. Example: 2019-11-13T23:59:06
        -o output_file, --output_file output_file
                              Alerts output file.
        -log log_file, --log_file log_file
                              Logs output.
        -w cyb3rhq_path, --cyb3rhq_path cyb3rhq_path
                              Path to Cyb3rhq. By default:/var/ossec/
        -sz max_size, --max_size max_size
                              Max output file size in Gb. Default: 1Gb. Example: 2.5

#. Run the command below to make the ``recovery.py`` script executable:

   .. code-block:: console

      # chmod +x recovery.py

#. Execute the script using ``nohup`` command in the background to keep it running after the session is closed. It may take time depending on the size of the old logs.

   Usage example:

   .. code-block:: console

      # nohup ./recovery.py -eps 500 -min 2023-06-10T00:00:00 -max 2023-06-18T23:59:59 -o /tmp/recovery.json -log ./recovery.log -sz 2.5 &

#. Add the ``/tmp/recovery.json`` path to the Cyb3rhq Filebeat module ``/usr/share/filebeat/module/cyb3rhq/alerts/manifest.yml`` so that Filebeat sends the old alerts to the Cyb3rhq indexer for indexing: 


   .. code-block:: yaml
      :emphasize-lines: 7

      module_version: 0.1

      var:
        - name: paths
          default:
            - /var/ossec/logs/alerts/alerts.json
            - /tmp/recovery.json
        - name: index_prefix
          default: cyb3rhq-alerts-4.x-

      input: config/alerts.yml

      ingest_pipeline: ingest/pipeline.json

#. Restart Filebeat for the changes to take effect:

   .. code-block:: console

      # systemctl restart filebeat

Verifying data restoration
^^^^^^^^^^^^^^^^^^^^^^^^^^

Using the Cyb3rhq dashboard, navigate to the **Threat Hunting**, **File Integrity Monitoring**, **Vulnerability Detection**, and any other modules to see if the data is restored successfully.

Multi-node data restoration
---------------------------

Perform the actions below to restore the Cyb3rhq central components on their respective Cyb3rhq nodes.

Preparing the data restoration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Compress the files generated after performing :doc:`Cyb3rhq files backup <../creating/cyb3rhq-central-components>` and transfer them to the respective new servers:

   .. code-block:: console

      # tar -cvzf <SERVER_HOSTNAME>.tar.gz ~/cyb3rhq_files_backup/ 

   Where:

   -  ``<SERVER_HOSTNAME>`` represents the current server name. Consider adding the naming convention, ``_indexer``, ``_server``, ``_dashboard`` if the current hostnames don’t specify them.

   .. note::
      
      Make sure that Cyb3rhq indexer compressed files are transferred to the new Cyb3rhq indexer nodes, Cyb3rhq server compressed files are transferred to the new Cyb3rhq server nodes, and Cyb3rhq dashboard compressed files are transferred to the new Cyb3rhq dashboard nodes.

#. Move the compressed file to the root ``/`` directory of each node:

   .. code-block:: console

      # mv <SERVER_HOSTNAME>.tar.gz /
      # cd /

#. Decompress the backup files and change the current working directory to the directory based on the date and time of the backup files:

   .. code-block:: console

      # tar -xzvf <SERVER_HOSTNAME>.tar.gz
      # cd ~/cyb3rhq_files_backup/<DATE_TIME>

Restoring Cyb3rhq indexer files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You need to have a new installation of Cyb3rhq indexer. Follow the :doc:`Cyb3rhq indexer - Installation guide </installation-guide/cyb3rhq-indexer/index>` to perform a fresh Cyb3rhq indexer installation.

Perform the following steps on each Cyb3rhq indexer node.

#. Stop the Cyb3rhq indexer to prevent any modification to the Cyb3rhq indexer files during the restore process:

   .. code-block:: console

      # systemctl stop cyb3rhq-indexer

#. Restore the Cyb3rhq indexer configuration files, and change the file permissions and ownerships accordingly:

   .. code-block:: console

      # sudo cp etc/cyb3rhq-indexer/jvm.options /etc/cyb3rhq-indexer/jvm.options
      # chown cyb3rhq-indexer:cyb3rhq-indexer /etc/cyb3rhq-indexer/jvm.options
      # sudo cp etc/cyb3rhq-indexer/jvm.options.d /etc/cyb3rhq-indexer/jvm.options.d
      # chown cyb3rhq-indexer:cyb3rhq-indexer /etc/cyb3rhq-indexer/jvm.options.d
      # sudo cp etc/cyb3rhq-indexer/log4j2.properties /etc/cyb3rhq-indexer/log4j2.properties
      # chown cyb3rhq-indexer:cyb3rhq-indexer /etc/cyb3rhq-indexer/log4j2.properties
      # sudo cp etc/cyb3rhq-indexer/opensearch.keystore /etc/cyb3rhq-indexer/opensearch.keystore
      # chown cyb3rhq-indexer:cyb3rhq-indexer /etc/cyb3rhq-indexer/opensearch.keystore
      # sudo cp -r etc/cyb3rhq-indexer/opensearch-observability/* /etc/cyb3rhq-indexer/opensearch-observability/
      # chown -R cyb3rhq-indexer:cyb3rhq-indexer /etc/cyb3rhq-indexer/opensearch-observability/
      # sudo cp -r etc/cyb3rhq-indexer/opensearch-reports-scheduler/* /etc/cyb3rhq-indexer/opensearch-reports-scheduler/
      # chown -R cyb3rhq-indexer:cyb3rhq-indexer /etc/cyb3rhq-indexer/opensearch-reports-scheduler/
      # sudo cp usr/lib/sysctl.d/cyb3rhq-indexer.conf /usr/lib/sysctl.d/cyb3rhq-indexer.conf

#. Start the Cyb3rhq indexer service:

   .. code-block:: console

      # systemctl start cyb3rhq-indexer

.. _restoring-server-multi-node:

Restoring Cyb3rhq server files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You need to have a new installation of a Cyb3rhq server. Follow the :doc:`Cyb3rhq server - Installation guide </installation-guide/cyb3rhq-server/index>` to perform a multi-node Cyb3rhq server installation. There will be at least one master node and one worker node as node types. Perform the steps below, considering your node type.

#. Stop the Cyb3rhq manager and Filebeat to prevent any modification to the Cyb3rhq server files during the restore process:

   .. code-block:: console

      # systemctl stop filebeat
      # systemctl stop cyb3rhq-manager

#. Copy Cyb3rhq server data and configuration files, and change the file permissions and ownerships accordingly:

   .. code-block:: console

      # sudo cp etc/filebeat/filebeat.reference.yml /etc/filebeat/
      # sudo cp etc/filebeat/fields.yml /etc/filebeat/
      # sudo cp -r etc/filebeat/modules.d/* /etc/filebeat/modules.d/
      # sudo cp -r etc/postfix/* /etc/postfix/
      # sudo cp var/ossec/etc/client.keys /var/ossec/etc/
      # chown root:cyb3rhq /var/ossec/etc/client.keys
      # sudo cp -r var/ossec/etc/sslmanager* /var/ossec/etc/
      # sudo cp var/ossec/etc/ossec.conf /var/ossec/etc/
      # chown root:cyb3rhq /var/ossec/etc/ossec.conf
      # sudo cp var/ossec/etc/internal_options.conf /var/ossec/etc/
      # chown root:cyb3rhq /var/ossec/etc/internal_options.conf
      # sudo cp var/ossec/etc/local_internal_options.conf /var/ossec/etc/
      # chown root:cyb3rhq /var/ossec/etc/local_internal_options.conf
      # sudo cp -r var/ossec/etc/rules/* /var/ossec/etc/rules/
      # chown -R cyb3rhq:cyb3rhq /var/ossec/etc/rules/
      # sudo cp -r var/ossec/etc/decoders/* /var/ossec/etc/decoders
      # chown -R cyb3rhq:cyb3rhq /var/ossec/etc/decoders/
      # sudo cp -r var/ossec/etc/shared/*  /var/ossec/etc/shared/
      # chown -R cyb3rhq:cyb3rhq /var/ossec/etc/shared/
      # chown root:cyb3rhq /var/ossec/etc/shared/ar.conf
      # sudo cp -r var/ossec/logs/* /var/ossec/logs/
      # chown -R cyb3rhq:cyb3rhq /var/ossec/logs/
      # sudo cp -r var/ossec/queue/agentless/*  /var/ossec/queue/agentless/
      # chown -R cyb3rhq:cyb3rhq /var/ossec/queue/agentless/
      # sudo cp var/ossec/queue/agents-timestamp /var/ossec/queue/
      # chown root:cyb3rhq /var/ossec/queue/agents-timestamp
      # sudo cp -r var/ossec/queue/fts/* /var/ossec/queue/fts/
      # chown -R cyb3rhq:cyb3rhq /var/ossec/queue/fts/
      # sudo cp -r var/ossec/queue/rids/* /var/ossec/queue/rids/
      # chown -R cyb3rhq:cyb3rhq /var/ossec/queue/rids/
      # sudo cp -r var/ossec/stats/* /var/ossec/stats/ 
      # chown -R cyb3rhq:cyb3rhq /var/ossec/stats/ 
      # sudo cp -r var/ossec/var/multigroups/* /var/ossec/var/multigroups/
      # chown -R cyb3rhq:cyb3rhq /var/ossec/var/multigroups/

#. Restore certificates for Cyb3rhq agent and Cyb3rhq server communication, and additional configuration files if present:

   .. code-block:: console

      # sudo cp -r var/ossec/etc/*.pem /var/ossec/etc/
      # chown -R root:cyb3rhq /var/ossec/etc/*.pem
      # sudo cp var/ossec/etc/authd.pass /var/ossec/etc/
      # chown -R root:cyb3rhq /var/ossec/etc/authd.pass

#. Restore your custom files. If you have custom active response scripts, CDB lists, integrations, or wodle commands, adapt the following commands accordingly:

   .. code-block:: console

      # sudo cp var/ossec/active-response/bin/<CUSTOM_AR_SCRIPT> /var/ossec/active-response/bin/
      # chown root:cyb3rhq /var/ossec/active-response/bin/<CUSTOM_AR_SCRIPT> 
      # sudo cp var/ossec/etc/lists/<USER_CDB_LIST>.cdb /var/ossec/etc/lists/
      # chown root:cyb3rhq /var/ossec/etc/lists/<USER_CDB_LIST>.cdb 
      # sudo cp var/ossec/integrations/<CUSTOM_INTEGRATION_SCRIPT> /var/ossec/integrations/
      # chown root:cyb3rhq /var/ossec/integrations/<CUSTOM_INTEGRATION_SCRIPT>
      # sudo cp var/ossec/wodles/<CUSTOM_WODLE_SCRIPT> /var/ossec/wodles/
      # chown root:cyb3rhq /var/ossec/wodles/<CUSTOM_WODLE_SCRIPT>

#. Restore the Cyb3rhq databases that contain collected data from Cyb3rhq agents:

   .. code-block:: console

      # sudo cp var/ossec/queue/db/* /var/ossec/queue/db/ 
      # chown -R root:cyb3rhq /var/ossec/queue/db/

#. Start the Filebeat service:

   .. code-block:: console

      # systemctl start filebeat

#. Start the Cyb3rhq manager service:

   .. code-block:: console

      # systemctl start cyb3rhq-manager

Restoring Cyb3rhq dashboard files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You need to have a new installation of the Cyb3rhq dashboard. Follow :doc:`Cyb3rhq dashboard - Installation guide </installation-guide/cyb3rhq-dashboard/index>` to perform Cyb3rhq dashboard installation.

Perform the following steps to restore Cyb3rhq reports and custom images on the new server if you have any from your backup.

#. Restore your Cyb3rhq reports using the following command:

   .. code-block:: console

      # mkdir -p /usr/share/cyb3rhq-dashboard/data/cyb3rhq/downloads/reports/
      # sudo cp -r usr/share/cyb3rhq-dashboard/data/cyb3rhq/downloads/reports/* /usr/share/cyb3rhq-dashboard/data/cyb3rhq/downloads/reports/ 
      # chown -R cyb3rhq-dashboard:cyb3rhq-dashboard /usr/share/cyb3rhq-dashboard/data/cyb3rhq/downloads/

#. Navigate to **Dashboard management** > **App Settings** > **Custom branding** from the Cyb3rhq dashboard and upload your custom images.

Restoring old logs
^^^^^^^^^^^^^^^^^^

Cyb3rhq, by default, compresses logs that are older than a day. While performing log restoration in the :ref:`restoring-server-multi-node` section, the old logs remain compressed.

Perform the following actions on both master and worker nodes of your Cyb3rhq server to decompress the old logs and re-inject them for indexing to the Cyb3rhq indexer.

.. note::
   
   Restoring old logs will have a creation date of the day when the restoration is performed.

#. Create a Python script called ``recovery.py`` on your Cyb3rhq server. This script decompresses all the old logs and stores them in the ``recovery.json`` file in ``/tmp`` directory.

   .. code-block:: console

      # touch recovery.py

#. Add the following content to the ``recovery.py`` script:

   .. code-block:: python

      #!/usr/bin/env python

      import gzip
      import time
      import json
      import argparse
      import re
      import os
      from datetime import datetime
      from datetime import timedelta

      def log(msg):
          now_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
          final_msg = "{0} cyb3rhq-reinjection: {1}".format(now_date, msg)
          print(final_msg)
          if log_file:
              f_log.write(final_msg + "\n")

      EPS_MAX = 400
      cyb3rhq_path = '/var/ossec/'
      max_size=1
      log_file = None

      parser = argparse.ArgumentParser(description='Reinjection script')
      parser.add_argument('-eps','--eps', metavar='eps', type=int, required = False, help='Events per second.')
      parser.add_argument('-min', '--min_timestamp', metavar='min_timestamp', type=str, required = True, help='Min timestamp. Example: 2017-12-13T23:59:06')
      parser.add_argument('-max', '--max_timestamp', metavar='max_timestamp', type=str, required = True, help='Max timestamp. Example: 2017-12-13T23:59:06')
      parser.add_argument('-o', '--output_file', metavar='output_file', type=str, required = True, help='Output filename.')
      parser.add_argument('-log', '--log_file', metavar='log_file', type=str, required = False, help='Logs output')
      parser.add_argument('-w', '--cyb3rhq_path', metavar='cyb3rhq_path', type=str, required = False, help='Path to Cyb3rhq. By default:/var/ossec/')
      parser.add_argument('-sz', '--max_size', metavar='max_size', type=float, required = False, help='Max output file size in Gb. Default: 1Gb. Example: 2.5')

      args = parser.parse_args()

      if args.log_file:
          log_file = args.log_file
          f_log = open(log_file, 'a+')


      if args.max_size:
          max_size = args.max_size

      if args.cyb3rhq_path:
          cyb3rhq_path = args.cyb3rhq_path

      output_file = args.output_file

      #Gb to bytes
      max_bytes = int(max_size * 1024 * 1024 * 1024)

      if (max_bytes <= 0):
          log("Error: Incorrect max_size")
          exit(1)

      month_dict = ['Null','Jan','Feb','Mar','Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov','Dec']

      if args.eps:
          EPS_MAX = args.eps

      if EPS_MAX < 0:
          log("Error: incorrect EPS")
          exit(1)

      min_date = re.search('(\\d\\d\\d\\d)-(\\d\\d)-(\\d\\d)T\\d\\d:\\d\\d:\\d\\d', args.min_timestamp)
      if min_date:
          min_year = int(min_date.group(1))
          min_month = int(min_date.group(2))
          min_day = int(min_date.group(3))
      else:
          log("Error: Incorrect min timestamp")
          exit(1)

      max_date = re.search('(\\d\\d\\d\\d)-(\\d\\d)-(\\d\\d)T\\d\\d:\\d\\d:\\d\\d', args.max_timestamp)
      if max_date:
          max_year = int(max_date.group(1))
          max_month = int(max_date.group(2))
          max_day = int(max_date.group(3))
      else:
          log("Error: Incorrect max timestamp")
          exit(1)

      # Converting timestamp args to datetime
      min_timestamp = datetime.strptime(args.min_timestamp, '%Y-%m-%dT%H:%M:%S')
      max_timestamp = datetime.strptime(args.max_timestamp, '%Y-%m-%dT%H:%M:%S')

      chunk = 0
      written_alerts = 0
      trimmed_alerts = open(output_file, 'w')

      max_time=datetime(max_year, max_month, max_day)
      current_time=datetime(min_year, min_month, min_day)

      while current_time <= max_time: 
          alert_file = "{0}logs/alerts/{1}/{2}/ossec-alerts-{3:02}.json.gz".format(cyb3rhq_path,current_time.year,month_dict[current_time.month],current_time.day)

          if os.path.exists(alert_file):
              daily_alerts = 0
              compressed_alerts = gzip.open(alert_file, 'r')
              log("Reading file: "+ alert_file)
              for line in compressed_alerts:
                  # Transform line to json object
                  try:
                      line_json = json.loads(line.decode("utf-8", "replace"))

                      # Remove unnecessary part of the timestamp
                      string_timestamp = line_json['timestamp'][:19]

                      # Ensure timestamp integrity
                      while len(line_json['timestamp'].split("+")[0]) < 23:
                          line_json['timestamp'] = line_json['timestamp'][:20] + "0" + line_json['timestamp'][20:]

                      # Get the timestamp readable
                      event_date = datetime.strptime(string_timestamp, '%Y-%m-%dT%H:%M:%S')

                      # Check the timestamp belongs to the selected range
                      if (event_date <= max_timestamp and event_date >= min_timestamp):
                          chunk+=1
                          trimmed_alerts.write(json.dumps(line_json))
                          trimmed_alerts.write("\n")
                          trimmed_alerts.flush()
                          daily_alerts += 1
                          if chunk >= EPS_MAX:
                              chunk = 0
                              time.sleep(2)
                          if os.path.getsize(output_file) >= max_bytes:
                              trimmed_alerts.close()
                              log("Output file reached max size, setting it to zero and restarting")
                              time.sleep(EPS_MAX/100)
                              trimmed_alerts = open(output_file, 'w')

                  except ValueError as e:
                      print("Oops! Something went wrong reading: {}".format(line))
                      print("This is the error: {}".format(str(e)))

              compressed_alerts.close()
              log("Extracted {0} alerts from day {1}-{2}-{3}".format(daily_alerts,current_time.day,month_dict[current_time.month],current_time.year))
          else:
              log("Couldn't find file {}".format(alert_file))

          #Move to next file
          current_time += timedelta(days=1)

      trimmed_alerts.close()

   While you run the ``recovery.py`` script, you need to consider the following parameters:

   .. code-block:: none

      usage: recovery.py [-h] [-eps eps] -min min_timestamp -max max_timestamp -o
                            output_file [-log log_file] [-w cyb3rhq_path]
                            [-sz max_size]

        -eps eps, --eps eps   Events per second. Default: 400
        -min min_timestamp, --min_timestamp min_timestamp
                              Min timestamp. Example: 2019-11-13T08:42:17
        -max max_timestamp, --max_timestamp max_timestamp
                              Max timestamp. Example: 2019-11-13T23:59:06
        -o output_file, --output_file output_file
                              Alerts output file.
        -log log_file, --log_file log_file
                              Logs output.
        -w cyb3rhq_path, --cyb3rhq_path cyb3rhq_path
                              Path to Cyb3rhq. By default:/var/ossec/
        -sz max_size, --max_size max_size
                              Max output file size in Gb. Default: 1Gb. Example: 2.5

#. Run the command below to make the ``recovery.py`` script executable:

   .. code-block:: console

      # chmod +x recovery.py

#. Execute the script using ``nohup`` command in the background to keep it running after the session is closed. It may take time depending on the size of the old logs.

   Usage example:

   .. code-block:: console

      # nohup ./recovery.py -eps 500 -min 2023-06-10T00:00:00 -max 2023-06-18T23:59:59 -o /tmp/recovery.json -log ./recovery.log -sz 2.5 &

#. Add the ``/tmp/recovery.json`` path to the Cyb3rhq Filebeat module ``/usr/share/filebeat/module/cyb3rhq/alerts/manifest.yml`` so that Filebeat sends the old alerts to the Cyb3rhq indexer for indexing:

   .. code-block:: yaml
      :emphasize-lines: 7

      module_version: 0.1

      var:
        - name: paths
          default:
            - /var/ossec/logs/alerts/alerts.json
            - /tmp/recovery.json
        - name: index_prefix
          default: cyb3rhq-alerts-4.x-

      input: config/alerts.yml

      ingest_pipeline: ingest/pipeline.json

#. Restart Filebeat for the changes to take effect.

   .. code-block:: console

      # systemctl restart filebeat

Verifying data restoration
^^^^^^^^^^^^^^^^^^^^^^^^^^

Using the Cyb3rhq dashboard, navigate to the **Threat Hunting**, **File Integrity Monitoring**, **Vulnerability Detection**, and any other modules to see if the data is restored successfully.
