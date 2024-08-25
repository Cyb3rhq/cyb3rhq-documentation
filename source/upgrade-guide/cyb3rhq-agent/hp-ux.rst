.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Check out how to upgrade the Cyb3rhq agent to the latest available version remotely, using the agent_upgrade tool or the Cyb3rhq API, or locally.


Upgrading Cyb3rhq agents on HP-UX systems
=======================================

Follow the steps to upgrade the Cyb3rhq agent on HP-UX systems.

#. Download the latest `HP-UX installer <https://packages.cyb3rhq.com/|CYB3RHQ_CURRENT_MAJOR_HPUX|/hp-ux/cyb3rhq-agent-|CYB3RHQ_CURRENT_HPUX|-|CYB3RHQ_REVISION_HPUX|-hpux-11v3-ia64.tar.gz>`_.

#. Stop the Cyb3rhq agent.

   .. code-block:: console

      # /var/ossec/bin/cyb3rhq-control stop


#. Backup the ``ossec.conf`` configuration file.

   .. code-block:: console

      # cp /var/ossec/etc/ossec.conf ~/ossec.conf.bk
      # cp /var/ossec/etc/client.keys ~/client.keys.bk


#. **Only for upgrades from version 4.2.7 or lower**:

   #. Delete the ossec user and group.

      .. code-block:: console

         # groupdel ossec
         # userdel ossec

   #. Create the cyb3rhq user and group.

      .. code-block:: console

         # groupadd cyb3rhq
         # useradd -G cyb3rhq cyb3rhq

#. Deploy the Cyb3rhq agent files.

   .. code-block:: console

      # gzip -d cyb3rhq-agent-|CYB3RHQ_CURRENT_HPUX|-|CYB3RHQ_REVISION_HPUX|-hpux-11v3-ia64.tar.gz
      # tar -xvf cyb3rhq-agent-|CYB3RHQ_CURRENT_HPUX|-|CYB3RHQ_REVISION_HPUX|-hpux-11v3-ia64.tar


#. Restore the ``ossec.conf`` configuration file.

   .. code-block:: console

      # mv ~/ossec.conf.bk /var/ossec/etc/ossec.conf
      # chown root:cyb3rhq /var/ossec/etc/ossec.conf
      # mv ~/client.keys.bk /var/ossec/etc/client.keys
      # chown root:cyb3rhq /var/ossec/etc/client.keys


#. Start the cyb3rhq-agent.

   .. code-block:: console

      # /var/ossec/bin/cyb3rhq-control start

.. note::
   :class: not-long

   When upgrading agents from versions earlier than 4.x, make sure that the communication protocol is compatible. Up to that point, UDP was the default protocol and it was switched to TCP for later versions. Edit the agent configuration file ``ossec.conf`` to update the :ref:`protocol <server_protocol>` or make sure that your Cyb3rhq manager accepts :ref:`both protocols<manager_protocol>`.
