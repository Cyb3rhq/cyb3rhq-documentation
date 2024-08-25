.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: The manage_agents tool can remove Cyb3rhq agents. Learn more in this section of the documentation.

Remove agents using the CLI
---------------------------

The :doc:`/var/ossec/bin/manage_agents </user-manual/reference/tools/manage-agents>` tool can also remove Cyb3rhq agents using the command line interface (CLI).

Run the following command on the Cyb3rhq server:

.. code-block:: console

   # /var/ossec/bin/manage_agents

.. code-block:: none

   ****************************************
   * Cyb3rhq v4.8.0 Agent manager.      	*
   * The following options are available: *
   ****************************************
      (A)dd an a,gent (A).
      (E)xtract key for an agent (E).
      (L)ist already added agents (L).
      (R)emove an agent (R).
      (Q)uit.
   Choose your action: A,E,L,R or Q: r

   Available agents:
      ID: 002, Name: Ubuntu, IP: any

   Provide the ID of the agent to be removed (or '\q' to quit): 002
   Confirm deleting it?(y/n): y
   Agent '002' removed.

   manage_agents: Exiting.

You can run the following command on the Cyb3rhq server and specifiy the Cyb3rhq agent ID by using the ``-r`` option. Replace ``<CYB3RHQ_AGENT_ID>`` with the agent ID of the Cyb3rhq agent:

.. code-block:: console

   # /var/ossec/bin/manage_agents -r <CYB3RHQ_AGENT_ID>

.. code-block:: none

   ****************************************
   * Cyb3rhq v4.8.0 Agent manager.          *
   * The following options are available: *
   ****************************************
      (A)dd an agent (A).
      (E)xtract key for an agent (E).
      (L)ist already added agents (L).
      (R)emove an agent (R).
      (Q)uit.
   Choose your action: A,E,L,R or Q:
   Available agents:
      ID: 001, Name: new, IP: any
   Provide the ID of the agent to be removed (or '\q' to quit): 001
   Confirm deleting it?(y/n): y
   Agent '001' removed.

   manage_agents: Exiting.
