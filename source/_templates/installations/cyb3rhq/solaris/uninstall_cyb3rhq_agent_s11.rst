.. Copyright (C) 2015, Cyb3rhq, Inc.

Run the following command to uninstall the Cyb3rhq agent in Solaris 11.

.. code-block:: console

   # /var/ossec/bin/cyb3rhq-control stop
   # pkg uninstall cyb3rhq-agent

.. note:: 
  
   If you uninstall the Cyb3rhq agent in Solaris 11.4 or later, the Solaris 11 package manager does not remove the group ``cyb3rhq`` from the system. Run the ``groupdel cyb3rhq`` command to manually remove it.

.. End of include file
