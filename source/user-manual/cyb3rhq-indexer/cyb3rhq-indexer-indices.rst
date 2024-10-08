.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: The Cyb3rhq indexer uses indices to store and organize security data for fast retrieval. Find more information in this section of the documentation.

Cyb3rhq indexer indices
=====================

An index is a collection of documents that relate to each other. The Cyb3rhq indexer uses indices to store and organize security data for fast retrieval. Cyb3rhq uses the following index patterns to store this data:

-  :ref:`cyb3rhq‑alerts-* <cyb3rhq_alerts_indices>`: This is the index pattern for alerts generated by the Cyb3rhq server.
-  :ref:`cyb3rhq‑archives-* <cyb3rhq_archives_indices>`: This is the index pattern for all events sent to the Cyb3rhq server.
-  :ref:`cyb3rhq‑monitoring-* <cyb3rhq_monitoring_indices>`: This is the index pattern for the status of the Cyb3rhq agents.
-  :ref:`cyb3rhq‑statistics-* <cyb3rhq_statistics_indices>`: This is the index pattern for statistical information of the Cyb3rhq server.

You can create a custom index pattern or modify the default index pattern.

Creating custom index pattern
-----------------------------

This section describes creating a custom index pattern, ``my-custom-alerts-*``, alongside the default pattern, ``cyb3rhq-alerts-*``. Switch to the root user and perform the steps below.

#. Stop the Filebeat service:

   .. code-block:: console

      # systemctl stop filebeat

#. Download the Cyb3rhq template and save it into a file (for example, ``template.json``):

   .. code-block:: console

      # curl -so template.json https://raw.githubusercontent.com/cyb3rhq/cyb3rhq/v|CYB3RHQ_CURRENT|/extensions/elasticsearch/7.x/cyb3rhq-template.json

#. Open the template file and locate this line at the beginning of the file:

   .. code-block:: json

      "index_patterns": [
        "cyb3rhq-alerts-4.x-*",
        "cyb3rhq-archives-4.x-*"
      ],

   Add your custom pattern to look like this:

   .. code-block:: json
      :emphasize-lines: 4

      "index_patterns": [
        "cyb3rhq-alerts-4.x-*",
        "cyb3rhq-archives-4.x-*",
        "my-custom-alerts-*"
      ],

   The asterisk character (``*``) on the index patterns is important because Filebeat will create indices using a name that follows this pattern, which is necessary to apply the proper format to visualize the alerts on the Cyb3rhq dashboard.

#. Save the modifications and insert the new template into the Cyb3rhq indexer. This will replace the existing template:

   .. code-block:: console

      # curl -XPUT -k -u <INDEXER_USERNAME>:<INDEXER_PASSWORD> 'https://<INDEXER_IP_ADDRESS>:9200/_template/cyb3rhq' -H 'Content-Type: application/json' -d @template.json

   Replace ``<INDEXER_USERNAME>`` and ``<INDEXER_PASSWORD>`` with the Cyb3rhq indexer username and password. You can obtain the Cyb3rhq indexer credentials for fresh deployments using the command:

   .. note::
      
      If using the Cyb3rhq OVA, use the default credentials ``admin:admin`` or refer to the :doc:`password management </user-manual/user-administration/password-management>` section.

   .. code-block:: console

      # tar -axf cyb3rhq-install-files.tar cyb3rhq-install-files/cyb3rhq-passwords.txt -O | grep -P "\'admin\'" -A 1

   .. code-block:: output
      :class: output

      {"acknowledged":true}


   .. note::
      
      ``{"acknowledged":true}`` indicates that the template was inserted correctly.


   .. warning::
      
      Perform step 5 only if you want to replace the default alert index pattern ``cyb3rhq-alerts-*`` and/or the default archive index pattern ``cyb3rhq‑archives-*`` with ``my-custom-alerts-*``.

#. Open the Cyb3rhq alerts configuration file ``/usr/share/filebeat/module/cyb3rhq/alerts/manifest.yml`` and optionally the archives file ``/usr/share/filebeat/module/cyb3rhq/archives/manifest.yml`` and replace the index name.

   For example, from:

   .. code-block:: yaml

      - name: index_prefix
        default: cyb3rhq-alerts-

   To this:

   .. code-block:: yaml

      - name: index_prefix
        default: my-custom-alerts-

   .. note::

      The index name must not contain the characters ``#``, ``\``, ``/``, ``*``, ``?``, ``"``, ``<``, ``>``, ``|``, ``,``, and must not start with ``_``, ``-``, or ``+``. Also, all the letters must be lowercase.

#. (Optional) If you want to use the new index pattern by default, open the ``/usr/share/cyb3rhq-dashboard/data/cyb3rhq/config/cyb3rhq.yml`` file and add the below configuration:

   .. code-block:: yaml

      pattern: my-custom-alerts-*

   This will make the Cyb3rhq server automatically create and/or select the new index pattern.

#. Restart Filebeat and the Cyb3rhq server components:

   .. code-block:: console

      # systemctl restart filebeat
      # systemctl restart cyb3rhq-manager
      # systemctl restart cyb3rhq-indexer
      # systemctl restart cyb3rhq-dashboard

.. warning::
   
   If you already have indices created with the previous name, they won't be changed. You can still change to the previous index pattern to see them, or you can perform :doc:`reindexing <re-indexing>` to rename the existing indices.

.. thumbnail:: /images/manual/cyb3rhq-indexer/create-custom-alerts-index-pattern.gif
   :title: Creating custom alerts index pattern
   :alt: Creating custom alerts index pattern
   :align: center
   :width: 80%

Checking indices information
----------------------------

You can check for information about Cyb3rhq indices in two ways.

-  Using the web user interface.
-  Making a request to the Cyb3rhq indexer API.

Using the web user interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. In the Cyb3rhq dashboard upper left menu **☰**, go to **Indexer management** > **Index Management**.

   .. thumbnail:: /images/manual/cyb3rhq-indexer/opensearch-plugins-index-management-option.png
      :title: Index management menu option
      :alt: Index management menu option
      :align: center
      :width: 80%

#. Click on **Indices**.

   .. thumbnail:: /images/manual/cyb3rhq-indexer/opensearch-plugins-index-management-indices.png
      :title: Index-management indices option
      :alt: Index-management indices option
      :align: center
      :width: 80%

   If the pattern is not present in the Cyb3rhq dashboard, create a new one using the index pattern used in the template ``my-custom-alerts-*``, and make sure to use ``timestamp`` as the **Time Filter** field name.

Using the Cyb3rhq indexer API
^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can query the indices information using the Cyb3rhq indexer API from the Cyb3rhq dashboard or the Cyb3rhq server.

Cyb3rhq dashboard
~~~~~~~~~~~~~~~

#. Navigate to **☰** > **Indexer management** > **Dev Tools**:

   .. code-block:: none

      GET /_cat/indices/cyb3rhq-*?v

   .. thumbnail:: /images/manual/cyb3rhq-indexer/dev-tools-indices-list.png
      :title: Dev Tools indices list
      :alt: Dev Tools indices list
      :align: center
      :width: 80%

Command line interface
~~~~~~~~~~~~~~~~~~~~~~

#. Obtain the Cyb3rhq indexer username and password for fresh deployments using the below command:

   .. code-block:: console

      # tar -axf cyb3rhq-install-files.tar cyb3rhq-install-files/cyb3rhq-passwords.txt -O | grep -P "\'admin\'" -A 1

   .. note::
      
      If using the Cyb3rhq OVA, use the default credentials admin:admin or refer to the :doc:`password management </user-manual/user-administration/password-management>` section.

#. Run the following command to query your index status. Replace ``<INDEXER_USERNAME>`` and ``<INDEXER_PASSWORD>`` with the username and password obtained. Replace ``<INDEXER_IP_ADDRESS>`` with your Cyb3rhq indexer IP address or FQDN. You can replace ``cyb3rhq-*`` with a more specific pattern for your query, such as ``cyb3rhq-alerts-*``.

   .. code-block:: console

      # curl -k -u <INDEXER_USERNAME>:<INDEXER_PASSWORD> https://<INDEXER_IP_ADDRESS>:9200/_cat/indices/cyb3rhq-*?v

   .. code-block:: output
      :class: output

      health status index                       uuid                   pri rep docs.count docs.deleted store.size pri.store.size
      green  open   cyb3rhq-statistics-2023.30w   xtHZtGqBR0WNJWbs5sjrnQ   1   0       2394            0      1.2mb          1.2mb
      green  open   cyb3rhq-alerts-4.x-2023.07.28 VbBfAasJTsiqw3lwRhY5sg   3   0        513            0      1.9mb          1.9mb
      green  open   cyb3rhq-alerts-4.x-2023.07.27 7s2x8INqRVmtz5uqMDuA7Q   3   0        515            0        2mb            2mb
      green  open   cyb3rhq-alerts-4.x-2023.07.05 0h4cyLJoQYiMvMnqyLDnag   3   0         49            0    370.4kb        370.4kb
      green  open   cyb3rhq-alerts-4.x-2023.07.07 kp_N4c7RRuOE91KkuqPuAw   3   0         98            0    397.7kb        397.7kb
      green  open   cyb3rhq-alerts-4.x-2023.07.29 rbAC4befS7epxOjiSzFRQQ   3   0       1717            0      3.9mb          3.9mb
      green  open   cyb3rhq-monitoring-2023.31w   1WwxsGQHRfG1_DOIZD-Lag   1   0        954            0    771.9kb        771.9kb
      green  open   cyb3rhq-alerts-4.x-2023.07.20 SQbaQC24SgO9eWO_AsBI_w   3   0       1181            0      2.8mb          2.8mb
      green  open   cyb3rhq-statistics-2023.28w   jO52bS6eRamtB2YNmfGzIA   1   0        676            0    501.1kb        501.1kb

.. _cyb3rhq_alerts_indices:

The cyb3rhq‑alerts-* indices
--------------------------

The Cyb3rhq server analyzes events received from monitored endpoints and generates alerts when the events match a detection rule. These alerts are saved using the ``cyb3rhq-alerts-*`` indices.

The Cyb3rhq server logs the alert data into the ``/var/ossec/logs/alerts/alerts.json`` and ``/var/ossec/logs/alerts/alerts.log`` files by default. Once saved in the ``/var/ossec/logs/alerts/alerts.json`` file, it forwards the JSON alert document to the ``/var/lib/cyb3rhq-indexer/`` directory of the Cyb3rhq indexer for indexing.

When forwarding alerts to the Cyb3rhq indexer, the Cyb3rhq server formats the current date into an index name. For example, the Cyb3rhq server will define the index names ``cyb3rhq-alerts-4.x-2023.03.17`` and ``cyb3rhq-alerts-4.x-2023.03.18`` for March 17th and 18th alerts, respectively. The Cyb3rhq indexer then creates alert indices using the defined ``cyb3rhq‑alerts-*`` index names.

You can modify the default index name in the ``/usr/share/filebeat/module/cyb3rhq/alerts/ingest/pipeline.json`` file of the Cyb3rhq server. To do this, navigate to the ``date_index_name`` field and ``date_rounding`` key to change the default index name formatting in the ``/usr/share/filebeat/module/cyb3rhq/alerts/ingest/pipeline.json`` file:

.. code-block:: json
   :emphasize-lines: 61

   {
     "description": "Cyb3rhq alerts pipeline",
     "processors": [
   	{ "json" : { "field" : "message", "add_to_root": true } },
   	{
     	"geoip": {
       	"field": "data.srcip",
       	"target_field": "GeoLocation",
       	"properties": ["city_name", "country_name", "region_name", "location"],
       	"ignore_missing": true,
       	"ignore_failure": true
     	}
   	},
   	{
     	"geoip": {
       	"field": "data.win.eventdata.ipAddress",
       	"target_field": "GeoLocation",
       	"properties": ["city_name", "country_name", "region_name", "location"],
       	"ignore_missing": true,
       	"ignore_failure": true
     	}
   	},
   	{
     	"geoip": {
       	"field": "data.aws.sourceIPAddress",
       	"target_field": "GeoLocation",
       	"properties": ["city_name", "country_name", "region_name", "location"],
       	"ignore_missing": true,
       	"ignore_failure": true
     	}
   	},
   	{
     	"geoip": {
       	"field": "data.gcp.jsonPayload.sourceIP",
       	"target_field": "GeoLocation",
       	"properties": ["city_name", "country_name", "region_name", "location"],
       	"ignore_missing": true,
       	"ignore_failure": true
     	}
   	},
   	{
     	"geoip": {
       	"field": "data.office365.ClientIP",
       	"target_field": "GeoLocation",
       	"properties": ["city_name", "country_name", "region_name", "location"],
       	"ignore_missing": true,
       	"ignore_failure": true
     	}
   	},
   	{
     	"date": {
       	"field": "timestamp",
       	"target_field": "@timestamp",
       	"formats": ["ISO8601"],
       	"ignore_failure": false
     	}
   	},
   	{
     	"date_index_name": {
       	"field": "timestamp",
       	"date_rounding": "d",
       	"index_name_prefix": "{{fields.index_prefix}}",
       	"index_name_format": "yyyy.MM.dd",
       	"ignore_failure": false
     	}
   	},
   	{ "remove": { "field": "message", "ignore_missing": true, "ignore_failure": true } },
   	{ "remove": { "field": "ecs", "ignore_missing": true, "ignore_failure": true } },
   	{ "remove": { "field": "beat", "ignore_missing": true, "ignore_failure": true } },
   	{ "remove": { "field": "input_type", "ignore_missing": true, "ignore_failure": true } },
   	{ "remove": { "field": "tags", "ignore_missing": true, "ignore_failure": true } },
   	{ "remove": { "field": "count", "ignore_missing": true, "ignore_failure": true } },
   	{ "remove": { "field": "@version", "ignore_missing": true, "ignore_failure": true } },
   	{ "remove": { "field": "log", "ignore_missing": true, "ignore_failure": true } },
   	{ "remove": { "field": "offset", "ignore_missing": true, "ignore_failure": true } },
   	{ "remove": { "field": "type", "ignore_missing": true, "ignore_failure": true } },
   	{ "remove": { "field": "host", "ignore_missing": true, "ignore_failure": true } },
   	{ "remove": { "field": "fields", "ignore_missing": true, "ignore_failure": true } },
   	{ "remove": { "field": "event", "ignore_missing": true, "ignore_failure": true } },
   	{ "remove": { "field": "fileset", "ignore_missing": true, "ignore_failure": true } },
   	{ "remove": { "field": "service", "ignore_missing": true, "ignore_failure": true } }
     ],
     "on_failure" : [{
   	"drop" : { }
     }]
   }

Where the values:

|  ``M`` - stands for month
|  ``w`` - stands for week
|  ``d`` - stands for day

.. _cyb3rhq_archives_indices:

The cyb3rhq‑archives-* indices
----------------------------

In addition to logging alerts to the ``/var/ossec/logs/alerts/alerts.json`` and ``/var/ossec/logs/alerts/alerts.log`` files, you can enable the Cyb3rhq archives to log and index all the events the Cyb3rhq server receives. This includes events that are analyzed by Cyb3rhq and events that do not trigger alerts.

Storing and indexing all events might be useful for later analysis and compliance requirements. However, you must consider that enabling logging and indexing of all events will increase the storage requirement on the Cyb3rhq server.

By default, the Cyb3rhq indexer creates event indices for each unique day. You can modify the default index name in the ``/usr/share/filebeat/module/cyb3rhq/archives/ingest/pipeline.json`` file of the Cyb3rhq server. To do this, navigate to the ``date_index_name`` field and ``date_rounding`` key to change the default index name formatting in the ``/usr/share/filebeat/module/cyb3rhq/archives/ingest/pipeline.json`` file.

The sections below provide details on how to enable the cyb3rhq archives and set up the ``cyb3rhq-archives-*`` indices.

Enabling Cyb3rhq archives
^^^^^^^^^^^^^^^^^^^^^^^

#. Edit ``/var/ossec/etc/ossec.conf`` on the Cyb3rhq server and set the ``<logall_json>`` line to ``yes``. This enables logging to :ref:`archives.json <reference_ossec_global_logall_json>` of all events. Forwarding to the Cyb3rhq indexer requires the logging of all events in JSON format.

   .. code-block:: xml

      <logall_json>yes</logall_json>

#. Restart the Cyb3rhq manager to make the change effective.

   .. code-block:: console

      # systemctl restart cyb3rhq-manager

   or

   .. code-block:: console

      # service cyb3rhq-manager restart

#. Edit ``/etc/filebeat/filebeat.yml`` and change ``enabled`` to ``true`` in the archives mapping. This enables events to be forwarded to the Cyb3rhq indexer.

   .. code-block:: yaml
      :emphasize-lines: 6

      filebeat.modules:
       - module: cyb3rhq
        alerts:
         enabled: true
        archives:
         enabled: true

#. Restart the Filebeat service to apply the change:

   .. code-block:: console

      # systemctl restart filebeat

#. Test that the Filebeat service works properly:

   .. code-block:: console

      # filebeat test output
    
   .. code-block:: output
      :class: output

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
          TLS version: TLSv1.2
          dial up... OK
        talk to server... OK
        version: 7.10.2

Defining the index pattern
^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Go to **Dashboard management** > **Dashboards Management** and click **Index Patterns** from the Cyb3rhq dashboard upper left menu **☰**.

#. Click on **Create index pattern**.

#. Set ``cyb3rhq-archives-*`` as the **Index pattern name**. This defines the index pattern to match the events being forwarded and indexed. Click on **Next step**.

#. Select **timestamp** for the **Time** field.

   .. note::
      
      Be careful to choose *timestamp* instead of *@timestamp*.

#. Click on **Create index pattern**.

Viewing the index pattern
^^^^^^^^^^^^^^^^^^^^^^^^^

#. Click **Discover** on the upper left menu **☰**.

#. Select **cyb3rhq-archives-*** to view the events.

   .. thumbnail:: /images/manual/cyb3rhq-indexer/cyb3rhq-archives-events.png
      :title: Cyb3rhq archives events
      :alt: Cyb3rhq archives events
      :align: center
      :width: 80%

.. _cyb3rhq_monitoring_indices:

The cyb3rhq-monitoring-* indices
------------------------------

At any moment, the connection status of an enrolled Cyb3rhq agent is one of the following:

-  **Active**
-  **Disconnected**
-  **Pending**
-  **Never connected**

Cyb3rhq stores a history of the connection status of all its agents. By default, it indexes the agent connection status using the ``cyb3rhq‑monitoring-*`` indices. The Cyb3rhq indexer creates one of these indices per week by default. Check the documentation on :ref:`custom creation intervals <cyb3rhq_monitoring_creation>`. These indices store the connection status of all the agents every 15 minutes by default. Check the documentation on the :ref:`frequency of API requests <cyb3rhq_monitoring_frequency>`.

The Cyb3rhq dashboard requires these indices to display information about agent status. For example, by clicking **Server management** > **Endpoints Summary**, you can see information such as the Cyb3rhq agent's connection status and historical evolution within set timeframes.

.. thumbnail:: /images/manual/cyb3rhq-indexer/status-evolution-agents-dashboard.png
   :title: Status and evolution in Agents dashboard
   :alt: Status and evolution in Agents dashboard
   :align: center
   :width: 80%

In the :doc:`Cyb3rhq dashboard configuration file </user-manual/cyb3rhq-dashboard/config-file>`, you can change the settings to do the following:

-  Disable inserting and showing connection status data for the agents. Change :ref:`cyb3rhq.monitoring.enabled <cyb3rhq_monitoring_enabled>` to accomplish this.

- Change the insertion frequency of connection status data for the agents. Change :ref:`cyb3rhq.monitoring.frequency <cyb3rhq_monitoring_frequency>` to accomplish this.

.. _cyb3rhq_statistics_indices:

The cyb3rhq‑statistics-* indices
------------------------------

The Cyb3rhq dashboard uses the ``cyb3rhq‑statistics-*`` indices to display statistics about the Cyb3rhq server usage and performance. The information displayed includes the number of events decoded, bytes received, and TCP sessions.

The Cyb3rhq dashboard runs requests to the Cyb3rhq manager API to query usage-related information. It inserts data into the ``cyb3rhq‑statistics-*`` indices from the information collected. The Cyb3rhq indexer creates a ``cyb3rhq‑statistics-*`` index per week by default. Check the documentation on the :ref:`Statistics creation interval <cron_statistics_index_creation>`. These indices store Cyb3rhq server statistics every 5 minutes by default. Check the documentation on the :ref:`Frequency of task execution <cron_statistics_interval>`.

To visualize this information in the Cyb3rhq dashboard, go to **Server management** > **Statistics**.

.. thumbnail:: /images/manual/cyb3rhq-indexer/statistics-analysis-engine-dashboard.png
   :title: Statistics analysis engine dashboard
   :alt: Statistics analysis engine dashboard
   :align: center
   :width: 80%
