.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: The Cyb3rhq server includes a queue mechanism that streamlines the collection of events from monitored endpoints. Learn more in this section of the documentation.

Cyb3rhq server queue
==================

The Cyb3rhq server includes a queue mechanism that streamlines the collection of events from monitored endpoints. It ensures continuous data flow from the Cyb3rhq agents, syslog endpoints, and agentless devices to the Cyb3rhq server thereby preventing event flooding. The Cyb3rhq server queue utilizes the First In, First Out (FIFO) methodology; therefore, the first queued event is the first to be removed from the queue and processed. It is based on distributed processing, allowing for the parallelization of log analysis tasks. This improves the scalability and performance of the log processing pipeline enabling Cyb3rhq to handle large volumes of log data effectively.

The Cyb3rhq server has two native queues for managing event flows:

-  `Cyb3rhq agent communication queue (queue_rd)`_
-  `Cyb3rhq analysis engine queue (queue_and)`_

The Cyb3rhq agent uses the `Cyb3rhq agent queue (queue_ad)`_ to prevent event congestion. This queue ensures the Cyb3rhq agent does not send events faster than the Cyb3rhq server can process.

Cyb3rhq agent communication queue (queue_rd)
------------------------------------------

The ``queue_rd`` queue resides in the server-side :doc:`agent communication service </user-manual/reference/daemons/cyb3rhq-remoted>`. It receives events from Cyb3rhq agents and sends them to the :doc:`Cyb3rhq analysis engine </user-manual/reference/daemons/cyb3rhq-analysisd>` for event decoding and rule matching.

How to configure the Cyb3rhq agent communication queue
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Configure the Cyb3rhq agent communication queue by editing the ``<queue_size>`` in the remote section of the ``/var/ossec/etc/ossec.conf`` file on the Cyb3rhq server:

   .. code-block:: xml
      :emphasize-lines: 5

      <remote>
        <connection>secure</connection>
        <port>1514</port>
        <protocol>tcp,udp</protocol>
        <queue_size>131072</queue_size>
        <rids_closing_time>5m</rids_closing_time>
        <connection_overtake_time>600</connection_overtake_time>
        <agents>
          <allow_higher_versions>no</allow_higher_versions>
        </agents>
      </remote>

   The ``<queue_size>`` variable sets the queue capacity of the Cyb3rhq agent communication queue. The table below shows the configuration for the ``<queue_size>`` variable.

   =============== ================================
   Default value   Allowed values
   =============== ================================
   131072          Any number between 1 and 262144.
   =============== ================================

   .. note::

      The Cyb3rhq agent communication queue (``queue_rd``) is only available for Cyb3rhq agent events, not remote syslog events. This option only works when the connection is set to ``secure``.

#. Restart the Cyb3rhq manager service to apply the changes

   .. code-block:: console

      # systemctl restart cyb3rhq-manager

When event drops are observed you can increase the value of the ``queue_size`` in the ``<remote>`` block of the ``/var/ossec/etc/ossec.conf`` file, and the ``worker_pool`` size in the ``/var/ossec/etc/internal_options.conf``.

The table below shows the configuration of the ``worker_pool`` size on the Cyb3rhq server.

+--------------------------+----------------+--------------------------------------------------------+
| **remoted.worker_pool**  | Description    | Number of threads that process the payload reception   |
|                          +----------------+--------------------------------------------------------+
|                          | Default value  | 4                                                      |
|                          +----------------+--------------------------------------------------------+
|                          | Allowed value  | Any integer between 1 and 16                           |
+--------------------------+----------------+--------------------------------------------------------+

You can monitor for event drops in the ``cyb3rhq-remoted`` by querying the :doc:`Cyb3rhq server API </user-manual/api/reference>` or reading the daemon statistical state file.

Querying the Cyb3rhq server API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can query the statistical information of the ``cyb3rhq-remoted`` by following the steps below:

#. On the Cyb3rhq dashboard, navigate to **Tools**, then **API Console**.
#. Add the following to the API console and click the green arrow to send the request to query the Cyb3rhq server API:

   .. code-block:: none

      GET /manager/daemons/stats

#. The query result is shown on the left hand side in the screenshot below.

   .. thumbnail:: /images/manual/cyb3rhq-server/cyb3rhq-remoted-query-results.png
      :title: Statistical query of the Cyb3rhq daemons showing cyb3rhq-remoted stats.
      :alt: Statistical query of the Cyb3rhq daemons showing cyb3rhq-remoted stats.
      :align: center
      :width: 80%

The query returns the queue size value, the number of events processed by the ``cyb3rhq-remoted``, and the number of events discarded.

Agent communication statistical state file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This statistical file for ``cyb3rhq-remoted`` offers data regarding the remote daemon, such as queue size, discarded messages, the count of remote connections, and other important information.

Run the command below on the Cyb3rhq server to read the file:

.. code-block:: console

   # cat /var/ossec/var/run/cyb3rhq-remoted.state

Below is an example of the content of the ``cyb3rhq-remoted.state`` file:

.. code-block:: ini

   # State file for cyb3rhq-remoted
   # THIS FILE WILL BE DEPRECATED IN FUTURE VERSIONS
   # Updated every 5 seconds.

   # Queue size
   queue_size='0'

   # Total queue size
   total_queue_size='131072'

   # TCP sessions
   tcp_sessions='1'

   # Events sent to Analysisd
   evt_count='126714'

   # Control messages received
   ctrl_msg_count='2637'

   # Discarded messages
   discarded_count='0'

   # Total number of bytes sent
   sent_bytes='4434745'

   # Total number of bytes received
   recv_bytes='93866086'

   # Messages dequeued after the agent closes the connection
   dequeued_after_close='0'

Cyb3rhq analysis engine queue (queue_and)
---------------------------------------

The ``queue_and`` queue resides in the :doc:`Cyb3rhq analysis engine </user-manual/reference/daemons/cyb3rhq-analysisd>` and streamlines the reception of events. The Cyb3rhq analysis engine then matches the received logs against the rules on the Cyb3rhq server.

How to configure the Cyb3rhq analysis engine queue
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Cyb3rhq analysis engine queue receives logs from Cyb3rhq agents for analysis using the ``queue_and`` queue. All incoming log messages are categorized and queued in the following categories:

-  File integrity monitoring event decoder queue.
-  Syscollector event decoder queue.
-  Root check event decoder queue.
-  Host info event decoder queue.
-  Event decoder queue.
-  Windows event decoder queue.

Each queue category has a set of threads responsible for their First In, First Out (FIFO) event management. The number of threads is individually configurable per event type through the ``/var/ossec/etc/internal_options.conf`` file on the Cyb3rhq server.

.. note::

   To ensure that upgrades do not overwrite queue configurations, use the ``/var/ossec/etc/local_internal_options.conf`` file instead of the ``/var/ossec/etc/internal_options.conf`` file.

The table below shows the configuration options available for the Cyb3rhq analysis engine queue (``queue_and``).

+--------------------------------+------------------------------------------+---------+-----+---------+
| Queues (cyb3rhq-analysisd.state) | Setting (local_internal_options.conf)    | Default | Min | Max     |
+================================+==========================================+=========+=====+=========+
| syscheck_queue_usage           | analysisd.decode_syscheck_queue_size     | 16384   | 128 | 2000000 |
+--------------------------------+------------------------------------------+---------+-----+---------+
| syscollector_queue_usage       | analysisd.decode_syscollector_queue_size | 16384   | 128 | 2000000 |
+--------------------------------+------------------------------------------+---------+-----+---------+
| rootcheck_queue_usage          | analysisd.decode_rootcheck_queue_size    | 16384   | 128 | 2000000 |
+--------------------------------+------------------------------------------+---------+-----+---------+
| sca_queue_usage                | analysisd.decode_sca_queue_size          | 16384   | 128 | 2000000 |
+--------------------------------+------------------------------------------+---------+-----+---------+
| hostinfo_queue_usage           | analysisd.decode_hostinfo_queue_size     | 16384   | 128 | 2000000 |
+--------------------------------+------------------------------------------+---------+-----+---------+
| winevt_queue_usage             | analysisd.decode_winevt_queue_size       | 16384   | 128 | 2000000 |
+--------------------------------+------------------------------------------+---------+-----+---------+
| dbsync_queue_usage             | analysisd.dbsync_queue_size              | 16384   | 128 | 2000000 |
+--------------------------------+------------------------------------------+---------+-----+---------+
| upgrade_queue_usage            | analysisd.upgrade_queue_size             | 16384   | 128 | 2000000 |
+--------------------------------+------------------------------------------+---------+-----+---------+
| event_queue_usage              | analysisd.decode_event_queue_size        | 16384   | 128 | 2000000 |
+--------------------------------+------------------------------------------+---------+-----+---------+
| rule_matching_queue_usage      | analysisd.decode_output_queue_size       | 16384   | 128 | 2000000 |
+--------------------------------+------------------------------------------+---------+-----+---------+
| alerts_queue_usage             | analysisd.alerts_queue_size              | 16384   | 128 | 2000000 |
+--------------------------------+------------------------------------------+---------+-----+---------+
| firewall_queue_usage           | analysisd.firewall_queue_size            | 16384   | 128 | 2000000 |
+--------------------------------+------------------------------------------+---------+-----+---------+
| statistical_queue_usage        | analysisd.statistical_queue_size         | 16384   | 128 | 2000000 |
+--------------------------------+------------------------------------------+---------+-----+---------+
| archives_queue_usage           | analysisd.archives_queue_size            | 16384   | 128 | 2000000 |
|                                +------------------------------------------+---------+-----+---------+
|                                | analysisd.fts_queue_size                 | 16384   | 128 | 2000000 |
|                                +------------------------------------------+---------+-----+---------+
|                                | analysisd.fts_list_size                  | 32      | 12  | 512     |
|                                +------------------------------------------+---------+-----+---------+
|                                | analysisd.fts_min_size_for_str           | 14      | 6   | 128     |
|                                +------------------------------------------+---------+-----+---------+
|                                | analysisd.decoder_order_size             | 256     | 32  | 1024    |
+--------------------------------+------------------------------------------+---------+-----+---------+

The queue settings should be adjusted when “event drops” are observed on the Cyb3rhq analysis engine. You can monitor for event drops in the cyb3rhq-analysisd by querying the :doc:`Cyb3rhq server API </user-manual/api/reference>` or reading the daemon statistical state file.

Querying the Cyb3rhq server API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The log category state can be queried using the Cyb3rhq server API to check the statistical information from the Cyb3rhq analysis engine. The new statistics show a breakdown of received or dropped events by event type. This is vital to adjust only the queue sizes that show dropping.

You can query the statistical information of the Cyb3rhq analysis engine by following the steps below:


#. On the Cyb3rhq dashboard, navigate to **Tools**, then **API Console**.
#. Add the following to the Console and click the green arrow to send the request to query the Cyb3rhq server API:

   .. code-block:: none

      GET /manager/daemons/stats

#. Scroll down to the ``cyb3rhq-analysisd`` section of the query result shown on the right-hand side in the screenshot below.

   .. thumbnail:: /images/manual/cyb3rhq-server/cyb3rhq-analysisd-query-results.png
      :title: Statistical query of the Cyb3rhq daemons showing cyb3rhq-analysisd stats
      :alt: Statistical query of the Cyb3rhq daemons showing cyb3rhq-analysisd stats
      :align: center
      :width: 80%

The query returns the queue size value, the number of events processed by the Cyb3rhq analysis engine, and the number of events discarded.

The Cyb3rhq analysis engine queue can be configured per the event type through the ``/var/ossec/etc/internal_options.conf`` file on the Cyb3rhq server.

.. note::

   To ensure that upgrades do not overwrite queue configurations, use the ``/var/ossec/etc/local_internal_options.conf`` file instead of the ``/var/ossec/etc/internal_options.conf`` file.

The Cyb3rhq analysis engine statistical state file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The statistical file for the Cyb3rhq analysis engine is located at ``/var/ossec/var/run/cyb3rhq-analysisd.state``. The file can be useful when investigating event processing problems on the Cyb3rhq server.

Run the command below on the Cyb3rhq server to read the file:

.. code-block:: console

   # cat /var/ossec/var/run/cyb3rhq-analysisd.state

Below is an example of the content of the cyb3rhq-remoted.state file:

.. code-block:: ini

   # State file for cyb3rhq-analysisd
   # THIS FILE WILL BE DEPRECATED IN FUTURE VERSIONS

   # Total events decoded
   total_events_decoded='137726'

   # Syscheck events decoded
   syscheck_events_decoded='3935'

   # Syscollector events decoded
   syscollector_events_decoded='2590'

   # Rootcheck events decoded
   rootcheck_events_decoded='37'

   # Security configuration assessment events decoded
   sca_events_decoded='8991'

   # Winevt events decoded
   winevt_events_decoded='87993'

   # Database synchronization messages dispatched
   dbsync_messages_dispatched='26004'

   # Other events decoded
   other_events_decoded='8176'

   # Events processed (Rule matching)
   events_processed='112252'

   # Events received
   events_received='138283'

   # Events dropped
   events_dropped='0'

   # Alerts written to disk
   alerts_written='6707'

   # Firewall alerts written to disk
   firewall_written='0'

   # FTS alerts written to disk
   fts_written='0'

   # Syscheck queue
   syscheck_queue_usage='0.00'

   # Syscheck queue size
   syscheck_queue_size='16384'

   # Syscollector queue
   syscollector_queue_usage='0.00'

   # Syscollector queue size
   syscollector_queue_size='16384'

   # Rootcheck queue
   rootcheck_queue_usage='0.00'

   # Rootcheck queue size
   rootcheck_queue_size='16384'

   # Security configuration assessment queue
   sca_queue_usage='0.00'

   # Security configuration assessment queue size
   sca_queue_size='16384'

   # Hostinfo queue
   hostinfo_queue_usage='0.00'

   # Hostinfo queue size
   hostinfo_queue_size='16384'

   # Winevt queue
   winevt_queue_usage='0.00'

   # Winevt queue size
   winevt_queue_size='16384'

   # Database synchronization message queue
   dbsync_queue_usage='0.00'

   # Database synchronization message queue size
   dbsync_queue_size='16384'

   # Upgrade module message queue
   upgrade_queue_usage='0.00'

   # Upgrade module message queue size
   upgrade_queue_size='16384'

   # Event queue
   event_queue_usage='0.00'

   # Event queue size
   event_queue_size='16384'

   # Rule matching queue
   rule_matching_queue_usage='0.00'

   # Rule matching queue size
   rule_matching_queue_size='16384'

   # Alerts log queue
   alerts_queue_usage='0.00'

   # Alerts log queue size
   alerts_queue_size='16384'

   # Firewall log queue
   firewall_queue_usage='0.00'

   # Firewall log queue size
   firewall_queue_size='16384'

   # Statistical log queue
   statistical_queue_usage='0.00'

   # Statistical log queue size
   statistical_queue_size='16384'

   # Archives log queue
   archives_queue_usage='0.00'

   # Archives log queue size
   archives_queue_size='16384'

Cyb3rhq agent queue (queue_ad)
----------------------------

The ``queue_ad`` queue resides in the agent-side :doc:`agent connection service </user-manual/reference/daemons/cyb3rhq-agentd>` and manages event forwarding from the Cyb3rhq agent to the Cyb3rhq server. The queue collects logs like system events and security configuration assessment outputs before forwarding them to the Cyb3rhq server. It also includes an anti-flooding mechanism that throttles event forwarding based on configurable parameters, mitigating the risk of overwhelming the processing capacity of the Cyb3rhq server.

Cyb3rhq queue decoder and rules
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cyb3rhq provides an out-of-the-box decoder and rules to analyze the event flooding output and generate alerts on the Cyb3rhq dashboard.

Decoder
~~~~~~~

The decoder is available in the ``/var/ossec/ruleset/decoders/0005-cyb3rhq_decoders.xml`` file on the Cyb3rhq server. The decoder is responsible for analyzing flooding events on the Cyb3rhq server.

.. code-block:: xml

   <decoder name="agent-buffer">
     <parent>cyb3rhq</parent>
     <prematch offset="after_parent">^Agent buffer:</prematch>
     <regex offset="after_prematch">^ '(\S+)'.</regex>
     <order>level</order>
   </decoder>

Rules
~~~~~

As shown below, the rules are defined with IDs from ``201`` to ``205`` and are available in the ``/var/ossec/ruleset/rules/0016-cyb3rhq_rules.xml`` file on the Cyb3rhq server.

.. code-block:: xml

   <!-- Agent buffer rules -->
   <rule id="201" level="0">
     <if_sid>200</if_sid>
     <match>^cyb3rhq: Agent buffer: </match>
     <description>Agent event queue rule</description>
     <group>agent_flooding,</group>
   </rule>

   <rule id="202" level="7">
     <if_sid>201</if_sid>
     <field name="level">%</field>
     <description>Agent event queue is $(level) full.</description>
     <group>agent_flooding,pci_dss_10.6.1,gdpr_IV_35.7.d,</group>
   </rule>

   <rule id="203" level="9">
     <if_sid>201</if_sid>
     <field name="level">full</field>
     <description>Agent event queue is full. Events may be lost.</description>
     <group>agent_flooding,pci_dss_10.6.1,gdpr_IV_35.7.d,</group>
   </rule>

   <rule id="204" level="12">
     <if_sid>201</if_sid>
     <field name="level">flooded</field>
     <description>Agent event queue is flooded. Check the agent configuration.</description>
     <group>agent_flooding,pci_dss_10.6.1,gdpr_IV_35.7.d,</group>
   </rule>

   <rule id="205" level="3">
     <if_sid>201</if_sid>
     <field name="level">normal</field>
     <description>Agent event queue is back to normal load.</description>
     <group>agent_flooding,</group>
   </rule>

Where:

-  Rule ID ``201`` is the base rule for the event queue.
-  Rule ID ``202`` is triggered when the event queue level reaches 90%.
-  Rule ID ``203`` is triggered when the event queue is full.
-  Rule ID ``204`` is triggered when the event queue is flooded.
-  Rule ID ``205`` is triggered when the event queue becomes normal after a flooding event.
