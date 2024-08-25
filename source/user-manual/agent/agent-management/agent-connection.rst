.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: This section highlights different methods to verify the connection status between a Cyb3rhq agent and the Cyb3rhq manager.

Cyb3rhq agent connection
======================

This section highlights different methods to verify the connection status between a Cyb3rhq agent and the Cyb3rhq manager. It also discusses how to check the Cyb3rhq agent connnection to the Cyb3rhq manager and verify the synchronization status of the Cyb3rhq agent. These sections are outlined below:

.. contents::
   :local:
   :depth: 1
   :backlinks: none

Checking connection with the Cyb3rhq manager
------------------------------------------

There are different ways to check the connection status between a Cyb3rhq agent and the Cyb3rhq manager. They include navigating the Cyb3rhq dashboard, using the Cyb3rhq agent control utility, querying the Cyb3rhq server API, and reading the Cyb3rhq agent state file. This guide highlights the different methods and contains steps to verify the network communication between a Cyb3rhq agent and the Cyb3rhq manager.

Using the Cyb3rhq dashboard
^^^^^^^^^^^^^^^^^^^^^^^^^

You can check the connection status of a Cyb3rhq agent by selecting **Endpoints Summary** under **Server management** on the Cyb3rhq dashboard.

.. thumbnail:: /images/manual/managing-agents/endpoints-summary-menu.png
   :title: Cyb3rhq dashboard Endpoints Summary menu option
   :alt: Cyb3rhq dashboard Endpoints Summary menu option
   :align: center
   :width: 80%

This option displays the **Endpoints** dashboard with a list of all enrolled Cyb3rhq agents. The list includes the connection status of each Cyb3rhq agent. The Cyb3rhq dashboard also displays a summary with the number of Cyb3rhq agents found for each possible agent connection :ref:`status <agent-status-cycle>`: *Active*, *Disconnected*, *Pending*, or *Never connected*.

.. thumbnail:: /images/manual/managing-agents/endpoints-summary-dashboard.png
   :title: Cyb3rhq Endpoints Summary dashboard
   :alt: Cyb3rhq Endpoints Summary dashboard
   :align: center
   :width: 80%

Using the agent_control utility from the server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can check the :ref:`status <agent-status-cycle>` of a Cyb3rhq agent remotely by using the :doc:`agent_control </user-manual/reference/tools/agent-control>` utility present on the Cyb3rhq server. To get the Cyb3rhq agent status, run the following command and replace the ``<CYB3RHQ_AGENT_ID>`` parameter with your Cyb3rhq agent ID, for example, ``001``. 

.. code-block:: console

   # /var/ossec/bin/agent_control -i <CYB3RHQ_AGENT_ID> | grep Status

.. code-block:: none
   :class: output

   Status:     Active

To list all the available Cyb3rhq agents and their status, use the command ``/var/ossec/bin/agent_control -l``.
Output

.. code-block:: none
   :class: output

   Cyb3rhq agent_control. List of available agents:
      ID: 000, Name: vpc-ossec-manager (server), IP: 127.0.0.1, Active/Local
      ID: 1040, Name: ip-10-0-0-76, IP: 10.0.0.76, Active
      ID: 003, Name: vpc-agent-debian, IP: 10.0.0.121, Active
      ID: 005, Name: vpc-agent-ubuntu-public, IP: 10.0.0.126, Active
      ID: 006, Name: vpc-agent-windows, IP: 10.0.0.124, Active
      ID: 1024, Name: ip-10-0-0-252, IP: 10.0.0.252, Never connected
      ID: 1028, Name: vpc-debian-it, IP: any, Never connected
      ID: 1030, Name: diamorphine-POC, IP: 10.0.0.59, Active
      ID: 015, Name: vpc-agent-centos, IP: 10.0.0.123, Active
      ID: 1031, Name: WIN-UENN0U6R5SF, IP: 10.0.0.124, Never connected
      ID: 1032, Name: vpc-agent-ubuntu, IP: 10.0.0.122, Active
      ID: 1033, Name: vpc-agent-debian8, IP: 10.0.0.128, Active
      ID: 1034, Name: vpc-agent-redhat, IP: 10.0.0.127, Active
      ID: 1035, Name: vpc-agent-centos7, IP: 10.0.0.101, Never connected
      ID: 1041, Name: vpc-agent-centos-public, IP: 10.0.0.125, Active

   List of agentless devices:
      ID: 010, Name: agentless-ubuntu, IP: 10.0.0.135, Active

Using the Cyb3rhq server API
^^^^^^^^^^^^^^^^^^^^^^^^^^

You can check the :ref:`status <agent-status-cycle>` of a Cyb3rhq agent by sending a request to the Cyb3rhq server API to retrieve :api-ref:`statistical information from an agent <operation/api.controllers.agent_controller.get_component_stats>`. This action is performed on the Cyb3rhq server.

.. code-block:: none

   GET /agents/<CYB3RHQ_AGENT_ID>/stats/agent

.. code-block:: none
   :class: output

   {
     "data": {
   	"affected_items": [
     	{
       	"status": "connected",
       	"last_keepalive": "2024-02-14T10:08:36Z",
       	"last_ack": "2024-02-14T10:08:39Z",
       	"msg_count": 3984,
       	"msg_sent": 4191,
       	"msg_buffer": 0,
       	"buffer_enabled": true
     	}
   	],
   	"total_affected_items": 1,
   	"total_failed_items": 0,
   	"failed_items": []
     },
     "message": "Statistical information for each agent was successfully read",
     "error": 0
   }

Reading the local cyb3rhq-agentd.state file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can read the :doc:`/var/ossec/var/run/cyb3rhq-agentd.state </user-manual/reference/statistics-files/cyb3rhq-agentd-state>` file found in the endpoint to check the status of the connection. The Cyb3rhq agent keeps reporting its connection status in this file as follows:

-  ``pending``: Waiting for acknowledgment from the Cyb3rhq manager about the connection established.
-  ``disconnected``: No acknowledgment signal received in the last 60 seconds or lost connection.
-  ``connected``: Acknowledgment about the connection established received from the Cyb3rhq manager.

To check the current status and verify the connection of the Cyb3rhq agent to the Cyb3rhq manager, run the following command on the endpoint:

.. tabs::

   .. group-tab:: Linux/Unix

      .. code-block:: console

         $ sudo grep ^status /var/ossec/var/run/cyb3rhq-agentd.state

      .. code-block:: console
         :class: output

         status='connected'

   .. group-tab:: Windows

      .. code-block:: pwsh-session

         > Select-String -Path 'C:\Program Files (x86)\ossec-agent\cyb3rhq-agent.state' -Pattern "^status"

      .. code-block:: console
         :class: output

         C:\Program Files (x86)\ossec-agent\cyb3rhq-agent.state:7:status='connected'


   .. group-tab:: macOS

      .. code-block:: console

         # sudo grep ^status /Library/Ossec/var/run/cyb3rhq-agentd.state

      .. code-block:: console
         :class: output

         status='connected'

.. _check_network_communication:

Checking network communication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Agent communication with the Cyb3rhq manager requires outbound connectivity from the Cyb3rhq agent to the Cyb3rhq manager. It uses the port ``1514/TCP`` by default.

Run the following commands on the Cyb3rhq agent to verify if a connection to the Cyb3rhq manager is established. The result should match the Cyb3rhq agent and Cyb3rhq manager IP addresses.

.. tabs::

   .. group-tab:: Linux/Unix

      .. code-block:: console

         # netstat -vatunp|grep cyb3rhq-agentd

      .. code-block:: console
         :class: output

         tcp    	0  	0 192.168.33.27:60174 	192.168.33.25:1514  	ESTABLISHED 4415/cyb3rhq-agentd

   .. group-tab:: Windows

      .. code-block:: Powershell

         > Get-NetTCPConnection -RemotePort 1514


      .. code-block:: console
         :class: output

         LocalAddress                    	LocalPort RemoteAddress                   	RemotePort State   	AppliedSetting OwningProcess
         ------------                    	--------- -------------                   	---------- -----   	-------------- -------------
         192.168.33.1                    	62657 	192.168.33.25                   	1514   	Established Internet   	33232

   .. group-tab:: macOS

      .. code-block:: console

         # lsof -i -P | grep ESTABLISHED | grep 1514

      .. code-block:: console
         :class: output

         cyb3rhq-age  1763          cyb3rhq    7u  IPv4 0xca59cd921b0f1ccb      0t0    TCP 10.0.2.15:49326->10.0.2.1:1514 (ESTABLISHED)

Search for errors or warnings in the corresponding agent log files for troubleshooting purposes.

-  Linux/Unix: ``/var/ossec/logs/ossec.log``
-  Windows: ``C:\Program Files (x86)\ossec-agent\ossec.log``
-  macOS: ``/Library/Ossec/logs/ossec.log``

To learn more, see the :doc:`troubleshooting <../agent-enrollment/troubleshooting>` section.

Checking the synchronization status of Cyb3rhq agents group configuration
-----------------------------------------------------------------------

Synchronization ensures the Cyb3rhq agent has the latest security configurations and data for consistent monitoring. To check the synchronization status of the group configuration for agents, you can use the ``/var/ossec/bin/agent_groups`` tool or the :api-ref:`GET /agents <operation/api.controllers.agent_controller.get_agents>` Cyb3rhq server API endpoint.

Using the agent_groups tool
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run the command below on the Cyb3rhq server:

.. code-block:: console

   # /var/ossec/bin/agent_groups -S -i 001

.. code-block:: none
   :class: output

   Agent '001' is synchronized.

For the other capabilities of the ``/var/ossec/bin/agent_groups`` tool, refer to the :doc:`reference </user-manual/reference/tools/agent-groups>` section.

Using the :api-ref:`GET /agents <operation/api.controllers.agent_controller.get_agents>` Cyb3rhq server API endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run the command below on the Cyb3rhq server or any endpoint that has connectivity with the Cyb3rhq server. Replace ``<CYB3RHQ_MANAGER_IP>`` with the IP address or FQDN of the Cyb3rhq server.

.. code-block:: console

   # curl -k -X GET "https://<CYB3RHQ_MANAGER_IP>:55000/agents?agents_list=001&select=group_config_status&pretty=true" -H  "Authorization: Bearer $TOKEN"

.. code-block:: none
   :class: output

   {
      "data": {
         "affected_items": [
            {
               "group_config_status": "synced",
               "id": "001"
            }
         ],
         "total_affected_items": 1,
         "total_failed_items": 0,
         "failed_items": []
      },
      "message": "All selected agents information was returned",
      "error": 0
   }

Refer to the following documentation for other information on the :doc:`Cyb3rhq server API </user-manual/api/reference>`.