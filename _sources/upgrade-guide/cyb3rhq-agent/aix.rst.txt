.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Check out how to upgrade the Cyb3rhq agent to the latest available version remotely, using the agent_upgrade tool or the Cyb3rhq API, or locally.


Upgrading Cyb3rhq agents on AIX systems
=====================================

Follow the steps to upgrade the Cyb3rhq agent on AIX systems.  
  
#. Download the latest `AIX installer <https://packages.wazuh.com/|CYB3RHQ_CURRENT_MAJOR_AIX|/aix/cyb3rhq-agent-|CYB3RHQ_CURRENT_AIX|-|CYB3RHQ_REVISION_AIX|.aix.ppc.rpm>`_. 

#. Run the following command:

   .. code-block:: console

      # rpm -U cyb3rhq-agent-|CYB3RHQ_CURRENT_AIX|-|CYB3RHQ_REVISION_AIX|.aix.ppc.rpm



.. note::
   :class: not-long

   When upgrading agents from versions earlier than 4.x, make sure that the communication protocol is compatible. Up to that point, UDP was the default protocol and it was switched to TCP for later versions. Edit the agent configuration file ``ossec.conf`` to update the :ref:`protocol <server_protocol>` or make sure that your Cyb3rhq manager accepts :ref:`both protocols<manager_protocol>`. 