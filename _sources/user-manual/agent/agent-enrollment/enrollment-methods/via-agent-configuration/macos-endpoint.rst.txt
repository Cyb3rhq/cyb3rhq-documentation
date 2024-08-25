.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Follow these steps to configure a macOS endpoint for enrollment via the Cyb3rhq agent configuration method.

macOS
=====

Follow these steps to configure a macOS endpoint for enrollment via the Cyb3rhq agent configuration method:

#. Launch the terminal, obtain root access, edit the Cyb3rhq agent configuration file ``/Library/Ossec/etc/ossec.conf``, and make the following changes:

   #. Include the Cyb3rhq manager IP address or FQDN (Fully Qualified Domain Name) in the ``<client><server><address>`` section. Replace ``<CYB3RHQ_MANAGER_IP>`` with the Cyb3rhq manager IP address or FQDN of the Cyb3rhq manager:

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

   #. (Optional) Add enrollment parameters in the ``<client><enrollment>`` section.

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
      -  ``<groups>GROUP1,GROUP2,GROUP3</groups>``: This specifies the group(s) in which the Cyb3rhq agent should be added. An agent group is a collection of agents that would share the same configuration. This allows the Cyb3rhq manager to push configuration settings to a set of Cyb3rhq agents that belong to the same group. The Cyb3rhq agent enrollment will fail if a non-existent group is specified. Therefore, it is necessary to create the desired group on the Cyb3rhq manager before using the group parameter. Additional information on agent groups can be found :doc:`here </user-manual/agent/agent-management/grouping-agents>`.

	   More optional enrollment parameters and their usage are provided :ref:`here <enrollment>`.

#. Restart the Cyb3rhq agent to make the changes effective:

   .. code-block:: console

      # /Library/Ossec/bin/cyb3rhq-control restart

#. Click on the upper-left menu icon and navigate to **Server management** > **Endpoints Summary** on the Cyb3rhq dashboard to check for the newly enrolled Cyb3rhq agent and its connection status. If the enrollment was successful, you will have an interface similar to the image below.

   .. thumbnail:: /images/manual/agent/macOS-check-newly-enrolled.png
      :title: Check newly enrolled Cyb3rhq agent - macOS
      :alt: Check newly enrolled Cyb3rhq agent - macOS
      :align: center
      :width: 80%
