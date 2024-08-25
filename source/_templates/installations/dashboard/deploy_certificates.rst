.. Copyright (C) 2015, Cyb3rhq, Inc.

#. Replace ``<DASHBOARD_NODE_NAME>`` with your Cyb3rhq dashboard node name, the same one used in ``config.yml`` to create the certificates, and move the certificates to their corresponding location. 

    .. code-block:: console

      # NODE_NAME=<DASHBOARD_NODE_NAME>
      
    .. code-block:: console  
    
      # mkdir /etc/cyb3rhq-dashboard/certs
      # tar -xf ./cyb3rhq-certificates.tar -C /etc/cyb3rhq-dashboard/certs/ ./$NODE_NAME.pem ./$NODE_NAME-key.pem ./root-ca.pem
      # mv -n /etc/cyb3rhq-dashboard/certs/$NODE_NAME.pem /etc/cyb3rhq-dashboard/certs/dashboard.pem
      # mv -n /etc/cyb3rhq-dashboard/certs/$NODE_NAME-key.pem /etc/cyb3rhq-dashboard/certs/dashboard-key.pem
      # chmod 500 /etc/cyb3rhq-dashboard/certs
      # chmod 400 /etc/cyb3rhq-dashboard/certs/*
      # chown -R cyb3rhq-dashboard:cyb3rhq-dashboard /etc/cyb3rhq-dashboard/certs

.. End of include file
