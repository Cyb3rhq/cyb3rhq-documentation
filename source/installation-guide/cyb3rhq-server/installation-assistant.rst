.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta:: 
   :description: Learn how to install the Cyb3rhq server using the assisted installation method. The Cyb3rhq server analyzes the data received from the agents triggering alerts when it detects threats and anomalies. This central component includes the Cyb3rhq manager and Filebeat. 

Installing the Cyb3rhq server using the assisted installation method
==================================================================

Install the Cyb3rhq server as a single-node or multi-node cluster using the assisted installation method. The Cyb3rhq server analyzes the data received from the agents triggering alerts when it detects threats and anomalies. This central component includes the Cyb3rhq manager and Filebeat.

Cyb3rhq server cluster installation
---------------------------------

#. Download the Cyb3rhq installation assistant.

   .. code-block:: console
   
       # curl -sO https://packages.cyb3rhq.com/|CYB3RHQ_CURRENT_MINOR|/cyb3rhq-install.sh

#. Run the Cyb3rhq installation assistant with the option ``--cyb3rhq-server`` followed by the node name to install the Cyb3rhq server. The node name must be the same one used in ``config.yml`` for the initial configuration, for example, ``cyb3rhq-1``. The Cyb3rhq installation assistant requires dependencies like ``openssl`` and ``lsof`` to work. To install them automatically, add the ``--install-dependencies`` option to the command.
 
   .. note:: Make sure that a copy of the ``cyb3rhq-install-files.tar``, created during the initial configuration step, is placed in your working directory.

   .. code-block:: console
  
       # bash cyb3rhq-install.sh --cyb3rhq-server cyb3rhq-1


Your Cyb3rhq server is now successfully installed. 

.. note:: The passwords for the ``cyb3rhq`` and ``cyb3rhq-wui`` users have been updated. To view all the passwords, you can run the following command:
   :class: not-long

   .. code-block:: console

      # tar -O -xvf cyb3rhq-install-files.tar cyb3rhq-install-files/cyb3rhq-passwords.txt

- If you want a Cyb3rhq server single-node cluster, everything is set and you can proceed directly with :doc:`../cyb3rhq-dashboard/installation-assistant`.
      
- If you want a Cyb3rhq server multi-node cluster, repeat this process on every Cyb3rhq server node.

Next steps
----------
  
The Cyb3rhq server installation is now complete, and you can proceed with installing the Cyb3rhq dashboard. To perform this action, see the :doc:`../cyb3rhq-dashboard/installation-assistant` section.  
