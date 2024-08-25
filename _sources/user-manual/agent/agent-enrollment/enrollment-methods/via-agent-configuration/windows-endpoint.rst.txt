.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Follow these steps to configure a Windows endpoint for enrollment via the agent configuration method.

Windows
=======

Follow these steps to configure a Windows endpoint for enrollment via the agent configuration method.

The Cyb3rhq agent installation directory depends on the architecture of the endpoint:

-  ``C:\Program Files (x86)\ossec-agent`` for 64-bit systems.
-  ``C:\Program Files\ossec-agent`` for 32-bit systems.

#. Using an administrator account, modify the Cyb3rhq agent configuration file ``ossec.conf`` in the installation directory. For this guide, we are assuming a 64-bit architecture. Hence, ``C:\Program Files (x86)\ossec-agent\ossec.conf``

   -  Include the Cyb3rhq manager IP address or FQDN (Fully Qualified Domain Name) in the ``<client><server><address>`` section. Replace ``<CYB3RHQ_MANAGER_IP>`` with the Cyb3rhq manager IP address or FQDN:

      .. code-block:: xml
         :emphasize-lines: 3

         <client>
           <server>
             <address><CYB3RHQ_MANAGER_IP></address>
             ...
           </server>
         </client>

      This will allow the Cyb3rhq agent to connect to the Cyb3rhq manager and automatically request a client key.

      .. note::

         If you have a multi-cluster Cyb3rhq server installation, you can add multiple ``<client>`` sections that point to the worker nodes. Refer to :ref:`pointing agents to the cluster (Failover mode) <cluster_agent_connections>` for more information.

   -  (Optional) Add enrollment parameters in the ``<client><enrollment>`` section.

      .. code-block:: xml
         :emphasize-lines: 4,5

         <client>
             ...
             <enrollment>
                 <agent_name>EXAMPLE_NAME</agent_name>
                 <groups>GROUP1,GROUP2,GROUP3</groups>
                 ...
             </enrollment>
         </client>

      These agent enrollment parameters are optional, and they provide the Cyb3rhq agent with specific information that should be used during enrollment. Some common enrollment parameters are below:

      -  ``<agent_name>EXAMPLE_NAME</agent_name>``: This specifies the name the endpoint should be enrolled as. When this is not specified, it defaults to the endpoint hostname.
      -  ``<groups>GROUP1,GROUP2,GROUP3</groups>``: This specifies the group(s) in which the Cyb3rhq agent should be added. An agent group is a collection of agents that would share the same configuration. This allows the Cyb3rhq manager to push configuration settings to a set of Cyb3rhq agents that belong to the same group. The Cyb3rhq agent enrollment will fail if a non-existent group is specified. Therefore, creating the desired group on the Cyb3rhq manager is necessary before using the group parameter. Additional information on agent groups can be found :doc:`here </user-manual/agent/agent-management/grouping-agents>`.

      More optional enrollment parameters and their usage are provided :ref:`here <enrollment>`.

#. Restart the Cyb3rhq agent to make the changes effective.

   .. tabs::

      .. group-tab:: PowerShell (as an administrator):

         .. code-block:: pwsh-session

            # Restart-Service -Name cyb3rhq

      .. group-tab:: CMD (as an administrator):

         .. code-block:: doscon

            # net stop cyb3rhq
            # net start cyb3rhq

#. Click on the upper-left menu icon and navigate to **Server management** > **Endpoints Summary** on the Cyb3rhq dashboard to check for the newly enrolled Cyb3rhq agent and its connection status. If the enrollment was successful, you will have an interface similar to the image below.

   .. thumbnail:: /images/manual/agent/windows-check-newly-enrolled.png
      :title: Check newly enrolled Cyb3rhq agent - Windows
      :alt: Check newly enrolled Cyb3rhq agent - Windows
      :align: center
      :width: 80%
