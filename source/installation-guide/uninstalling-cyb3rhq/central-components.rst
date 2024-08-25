.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Learn how to uninstall each Cyb3rhq central component.
  
Uninstalling the Cyb3rhq central components
=========================================

You can uninstall all the Cyb3rhq central components using the `Cyb3rhq installation assistant <https://packages.cyb3rhq.com/|CYB3RHQ_CURRENT_MINOR|/cyb3rhq-install.sh>`_.

Run the assistant with the option ``-u`` or ``--uninstall`` as follows:

.. code-block:: console

   $ sudo bash cyb3rhq-install.sh --uninstall

This will remove the Cyb3rhq indexer, the Cyb3rhq server, and the Cyb3rhq dashboard.

If you want to uninstall one specific central component, follow the instructions below.

.. note::
   
   You need root user privileges to run all the commands described below.

.. _uninstall_dashboard:

Uninstall the Cyb3rhq dashboard
-----------------------------

#. Remove the Cyb3rhq dashboard installation.

   .. tabs::

      .. group-tab:: Yum

         .. code:: console
        
            # yum remove cyb3rhq-dashboard -y
            # rm -rf /var/lib/cyb3rhq-dashboard/
            # rm -rf /usr/share/cyb3rhq-dashboard/
            # rm -rf /etc/cyb3rhq-dashboard/

      .. group-tab:: APT

         .. code:: console

            # apt-get remove --purge cyb3rhq-dashboard -y

.. _uninstall_server:

Uninstall the Cyb3rhq server
--------------------------

#. Remove the Cyb3rhq manager installation.

   .. tabs::

      .. group-tab:: Yum

         .. code-block:: console
          
            # yum remove cyb3rhq-manager -y
            # rm -rf /var/ossec/

      .. group-tab:: APT

         .. code-block:: console
        
            # apt-get remove --purge cyb3rhq-manager -y

#. Disable the Cyb3rhq manager service.

   .. include:: ../../_templates/installations/cyb3rhq/common/disable_cyb3rhq_manager_service.rst

#. Remove the Filebeat installation.

   .. tabs::

      .. group-tab:: Yum

         .. code:: console
        
            # yum remove filebeat -y
            # rm -rf /var/lib/filebeat/
            # rm -rf /usr/share/filebeat/
            # rm -rf /etc/filebeat/

      .. group-tab:: APT

         .. code:: console
      
            # apt-get remove --purge filebeat -y

.. _uninstall_indexer:

Uninstall the Cyb3rhq indexer
---------------------------

#. Remove the Cyb3rhq indexer installation.

   .. tabs::

      .. group-tab:: Yum

         .. code:: console
        
            # yum remove cyb3rhq-indexer -y
            # rm -rf /var/lib/cyb3rhq-indexer/
            # rm -rf /usr/share/cyb3rhq-indexer/
            # rm -rf /etc/cyb3rhq-indexer/

      .. group-tab:: APT

         .. code:: console

            # apt-get remove --purge cyb3rhq-indexer -y
