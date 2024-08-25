.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: This PoC shows how Cyb3rhq detects if Netcat is running on a monitored host. Learn more about this in this section of the documentation.

Detecting unauthorized processes
================================

The Cyb3rhq :doc:`command monitoring </user-manual/capabilities/command-monitoring/index>` capability runs commands on an endpoint and monitors the output of the commands.

In this use case, you use the Cyb3rhq command monitoring capability to detect when Netcat is running on an Ubuntu endpoint. Netcat is a computer networking utility used for port scanning and port listening.

Infrastructure
--------------

+---------------+-------------------------------------------------------------------------------------------------------------+
| Endpoint      | Description                                                                                                 |
+===============+=============================================================================================================+
| Ubuntu 22.04  | You configure the Cyb3rhq command monitoring module on this endpoint to detect a running Netcat process.      |
+---------------+-------------------------------------------------------------------------------------------------------------+

Configuration
-------------

Ubuntu endpoint
^^^^^^^^^^^^^^^

Take the following steps to configure command monitoring and query a list of all running processes on the Ubuntu endpoint.

#. Add the following configuration block to the Cyb3rhq agent ``/var/ossec/etc/ossec.conf`` file. This allows to periodically get a list of running processes:

   .. code-block:: xml

      <ossec_config>
        <localfile>
          <log_format>full_command</log_format>
          <alias>process list</alias>
          <command>ps -e -o pid,uname,command</command>
          <frequency>30</frequency>
        </localfile>
      </ossec_config>

#. Restart the Cyb3rhq agent to apply the changes:

   .. code-block:: console

      $ sudo systemctl restart cyb3rhq-agent

#. Install Netcat and the required dependencies:

   .. code-block:: console

      $ sudo apt install ncat nmap -y

Cyb3rhq server
^^^^^^^^^^^^

You have to configure the following steps on the Cyb3rhq server to create a rule that triggers every time the Netcat program launches.

#. Add the following rules to the ``/var/ossec/etc/rules/local_rules.xml`` file on the Cyb3rhq server:

   .. code-block:: xml

      <group name="ossec,">
        <rule id="100050" level="0">
          <if_sid>530</if_sid>
          <match>^ossec: output: 'process list'</match>
          <description>List of running processes.</description>
          <group>process_monitor,</group>
        </rule>

        <rule id="100051" level="7" ignore="900">
          <if_sid>100050</if_sid>
          <match>nc -l</match>
          <description>netcat listening for incoming connections.</description>
          <group>process_monitor,</group>
        </rule>
      </group>

#. Restart the Cyb3rhq manager to apply the changes:

   .. code-block:: console

      $ sudo systemctl restart cyb3rhq-manager

Attack emulation
----------------

On the monitored Ubuntu endpoint, run ``nc -l 8000`` for 30 seconds.

Visualize the alerts
--------------------

You can visualize the alert data in the Cyb3rhq dashboard. To do this, go to the **Threat Hunting** module and add the filters in the search bar to query the alerts.

-  ``rule.id:(100051)``

.. thumbnail:: /images/poc/unauthorized-processes-alerts.png
   :title: Unauthorized processes alerts
   :align: center
   :width: 80%
