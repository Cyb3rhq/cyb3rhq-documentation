.. Copyright (C) 2015, Cyb3rhq, Inc.


#. Run the following commands replacing ``<indexer-node-name>`` with the name of the Cyb3rhq indexer node you are configuring as defined in ``config.yml``. For example, ``node-1``. This deploys the SSL certificates to encrypt communications between the Cyb3rhq central components.

   .. code-block:: console

     # NODE_NAME=<indexer-node-name>

   .. code-block:: console 
     
     # mkdir /etc/cyb3rhq-indexer/certs
     # tar -xf ./cyb3rhq-certificates.tar -C /etc/cyb3rhq-indexer/certs/ ./$NODE_NAME.pem ./$NODE_NAME-key.pem ./admin.pem ./admin-key.pem ./root-ca.pem
     # mv -n /etc/cyb3rhq-indexer/certs/$NODE_NAME.pem /etc/cyb3rhq-indexer/certs/indexer.pem
     # mv -n /etc/cyb3rhq-indexer/certs/$NODE_NAME-key.pem /etc/cyb3rhq-indexer/certs/indexer-key.pem
     # chmod 500 /etc/cyb3rhq-indexer/certs
     # chmod 400 /etc/cyb3rhq-indexer/certs/*
     # chown -R cyb3rhq-indexer:cyb3rhq-indexer /etc/cyb3rhq-indexer/certs
    
#. **Recommended action**: If no other Cyb3rhq components are going to be installed on this node, remove the ``cyb3rhq-certificates.tar`` file by running ``rm -f ./cyb3rhq-certificates.tar`` to increase security.

.. End of include file
