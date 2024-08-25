.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: In this section of our documentation, you will find more information about Cyb3rhq Docker deployment: its requirements, usage, and exposed ports.
  
Cyb3rhq Docker deployment
=======================

Usage
-----

You can deploy Cyb3rhq as a single-node or multi-node stack.

-  **Single-node deployment**: Deploys one Cyb3rhq manager, indexer, and dashboard node.
-  **Multi-node deployment**: Deploys two Cyb3rhq manager nodes (one master and one worker), three Cyb3rhq indexer nodes, and a Cyb3rhq dashboard node.
  
Both deployments use persistence and allow configuring certificates to secure communications between nodes. The multi-node stack is the only deployment that contains high availability.

Single-node Deployment
^^^^^^^^^^^^^^^^^^^^^^

#. Clone the Cyb3rhq repository to your system:

   .. code-block:: console

      # git clone https://github.com/cyb3rhq/cyb3rhq-docker.git -b v|CYB3RHQ_CURRENT_DOCKER|

   Then enter into the ``single-node`` directory to execute all the commands described below within this directory.

#. Provide a group of certificates for each node in the stack to secure communication between the nodes. You have two alternatives to provide these certificates:

   -  Generate self-signed certificates for each cluster node. 
    
      We have created a Docker image to automate certificate generation using the Cyb3rhq certs gen tool.

      If your system uses a proxy, add the following to the ``generate-certs.yml`` file. If not, skip this particular step:
        
      .. code-block:: yaml
        
         environment:
           - HTTP_PROXY=YOUR_PROXY_ADDRESS_OR_DNS

      A completed example looks like:
        
      .. code-block:: yaml
        
         # Cyb3rhq App Copyright (C) 2017 Cyb3rhq Inc. (License GPLv2)
         version: '3'

         services:
           generator:
             image: cyb3rhq/cyb3rhq-certs-generator:0.0.2
             hostname: cyb3rhq-certs-generator
             volumes:
               - ./config/cyb3rhq_indexer_ssl_certs/:/certificates/
               - ./config/certs.yml:/config/certs.yml
             environment:
               - HTTP_PROXY=YOUR_PROXY_ADDRESS_OR_DNS
        
      Execute the following command to get the desired certificates:
      
         .. code-block:: console
         
            # docker-compose -f generate-certs.yml run --rm generator

      This saves the certificates into the ``config/cyb3rhq_indexer_ssl_certs`` directory.

   -  Provide your own certificates for each node.

      In case you have your own certificates, provision them as follows in the ``config/cyb3rhq_indexer_ssl_certs`` directory:

      **Cyb3rhq indexer**: 
      
      .. code-block:: none

         config/cyb3rhq_indexer_ssl_certs/root-ca.pem
         config/cyb3rhq_indexer_ssl_certs/cyb3rhq.indexer-key.pem
         config/cyb3rhq_indexer_ssl_certs/cyb3rhq.indexer.pem
         config/cyb3rhq_indexer_ssl_certs/admin.pem
         config/cyb3rhq_indexer_ssl_certs/admin-key.pem

      **Cyb3rhq manager**:

      .. code-block:: none

         config/cyb3rhq_indexer_ssl_certs/root-ca-manager.pem
         config/cyb3rhq_indexer_ssl_certs/cyb3rhq.manager.pem
         config/cyb3rhq_indexer_ssl_certs/cyb3rhq.manager-key.pem

      **Cyb3rhq dashboard**:

      .. code-block:: none

         config/cyb3rhq_indexer_ssl_certs/cyb3rhq.dashboard.pem
         config/cyb3rhq_indexer_ssl_certs/cyb3rhq.dashboard-key.pem
         config/cyb3rhq_indexer_ssl_certs/root-ca.pem
 
#. Start the Cyb3rhq single-node deployment using docker-compose:

   -  **Foreground**:

      .. code-block:: console  

         # docker-compose up

   -  **Background**:

      .. code-block:: console  

         # docker-compose up -d

   The default username and password for the Cyb3rhq dashboard are ``admin`` and ``SecretPassword``. For :ref:`additional security <change-pwd-existing-usr>`, you can change the default password for the Cyb3rhq indexer *admin* user.


.. note::

   To know when the Cyb3rhq indexer is up, the Cyb3rhq dashboard container uses ``curl`` to run multiple queries to the Cyb3rhq indexer API. You can expect to see several ``Failed to connect to Cyb3rhq indexer port 9200`` log messages or “ *Cyb3rhq dashboard server is not ready yet* ” until the Cyb3rhq indexer is started. Then the setup process continues normally. It takes about 1 minute for the Cyb3rhq indexer to start up. You can find the default Cyb3rhq indexer credentials in the ``docker-compose.yml`` file.

Multi-node deployment
^^^^^^^^^^^^^^^^^^^^^

#. Clone the Cyb3rhq repository to your system:

   .. code-block:: console

      $ git clone https://github.com/cyb3rhq/cyb3rhq-docker.git -b v|CYB3RHQ_CURRENT_DOCKER|
   
   Then enter into the ``multi-node`` directory to execute all the commands described below within this directory.

#. Provide a group of certificates for each node in the stack to secure communications between the nodes. You have two alternatives to provide these certificates:

   -  Generate self-signed certificates for each cluster node.

      We have created a Docker image to automate certificate generation using the Cyb3rhq certs gen tool.

      If your system uses a proxy, add the following to the ``generate-certs.yml`` file. If not, skip this particular step:
      
      .. code-block:: yaml
      
         environment:
           - HTTP_PROXY=YOUR_PROXY_ADDRESS_OR_DNS

      A completed example looks like:
      
      .. code-block:: yaml
      
         # Cyb3rhq App Copyright (C) 2017 Cyb3rhq Inc. (License GPLv2)
         version: '3'

         services:
           generator:
             image: cyb3rhq/cyb3rhq-certs-generator:0.0.2
             hostname: cyb3rhq-certs-generator
             volumes:
               - ./config/cyb3rhq_indexer_ssl_certs/:/certificates/
               - ./config/certs.yml:/config/certs.yml
             environment:
               - HTTP_PROXY=YOUR_PROXY_ADDRESS_OR_DNS
      
      Execute the following command to get the desired certificates:
        
      .. code-block:: console

         # docker-compose -f generate-certs.yml run --rm generator

      This saves the certificates into the ``config/cyb3rhq_indexer_ssl_certs`` directory.

   -  Provide your own certificates for each node.

      In case you have your own certificates, provision them as follows:
      
      **Cyb3rhq indexer**: 
    
      .. code-block:: none

         config/cyb3rhq_indexer_ssl_certs/root-ca.pem
         config/cyb3rhq_indexer_ssl_certs/cyb3rhq1.indexer-key.pem
         config/cyb3rhq_indexer_ssl_certs/cyb3rhq1.indexer.pem
         config/cyb3rhq_indexer_ssl_certs/cyb3rhq2.indexer-key.pem
         config/cyb3rhq_indexer_ssl_certs/cyb3rhq2.indexer.pem
         config/cyb3rhq_indexer_ssl_certs/cyb3rhq3.indexer-key.pem
         config/cyb3rhq_indexer_ssl_certs/cyb3rhq3.indexer.pem
         config/cyb3rhq_indexer_ssl_certs/admin.pem
         config/cyb3rhq_indexer_ssl_certs/admin-key.pem

      **Cyb3rhq manager**:

      .. code-block:: none

         config/cyb3rhq_indexer_ssl_certs/root-ca-manager.pem
         config/cyb3rhq_indexer_ssl_certs/cyb3rhq.master.pem
         config/cyb3rhq_indexer_ssl_certs/cyb3rhq.master-key.pem
         config/cyb3rhq_indexer_ssl_certs/cyb3rhq.worker.pem
         config/cyb3rhq_indexer_ssl_certs/cyb3rhq.worker-key.pem

      **Cyb3rhq dashboard**:

      .. code-block:: none

         config/cyb3rhq_indexer_ssl_certs/cyb3rhq.dashboard.pem
         config/cyb3rhq_indexer_ssl_certs/cyb3rhq.dashboard-key.pem
         config/cyb3rhq_indexer_ssl_certs/root-ca.pem


#. Start the Cyb3rhq multi-node deployment using ``docker-compose``:

   -  **Foreground**:

      .. code-block:: console

         # docker-compose up

   -  **Background**:

      .. code-block:: console

         # docker-compose up -d

   The default username and password for the Cyb3rhq dashboard are ``admin`` and ``SecretPassword``. For :ref:`additional security <change-pwd-existing-usr>`, you can change the default password for the Cyb3rhq indexer *admin* user.

.. note::

   To know when the Cyb3rhq indexer is up, the Cyb3rhq dashboard container uses ``curl`` to run multiple queries to the Cyb3rhq indexer API. You can expect to see several ``Failed to connect to Cyb3rhq indexer port 9200`` log messages or “Cyb3rhq dashboard server is not ready yet” until the Cyb3rhq indexer is started. Then the setup process continues normally. It takes about 1 minute for the Cyb3rhq indexer to start up. You can find the default Cyb3rhq indexer credentials in the ``docker-compose.yml`` file.

Build docker images locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can modify and build the Cyb3rhq manager, indexer, and dashboard images locally.

#. Clone the Cyb3rhq repository to your system:

   .. code-block:: console
  
      # git clone https://github.com/cyb3rhq/cyb3rhq-docker.git -b v|CYB3RHQ_CURRENT_DOCKER|

#. For versions up to 4.3.4, enter into the ``build-docker-images`` directory and build the Cyb3rhq manager, indexer, and dashboard images:
  
   .. code-block:: console
  
      # docker-compose build

   For version 4.3.5 and above, run the image creation script:

   .. code-block:: console
  
      # build-docker-images/build-images.sh

.. _change-pwd-existing-usr:

Change the password of Cyb3rhq users
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To improve security, you can change the default password of the Cyb3rhq users. There are two types of Cyb3rhq users:

-  Cyb3rhq indexer users
-  Cyb3rhq API users

 To change the password of these Cyb3rhq users, perform the following steps. You must run the commands from your ``single-node/`` or ``multi-node/`` directory, depending on your Cyb3rhq on Docker deployment.

Cyb3rhq indexer users
~~~~~~~~~~~~~~~~~~~

 To change the password of the default ``admin`` and ``kibanaserver`` users, do the following. You can only change one at a time. 

.. warning::

   If you have custom users, add them to the ``internal_users.yml`` file. Otherwise, executing this procedure deletes them.

Closing your Cyb3rhq dashboard session
....................................

Before starting the password change process, we recommend to log out of your Cyb3rhq dashboard session.

If you don't log out, persistent session cookies might cause errors when accessing Cyb3rhq after changing user passwords.

Setting a new hash
..................

#. Stop the deployment stack if it’s running:

   .. code-block:: console
  
      # docker-compose down

#. Run this command to generate the hash of your new password. Once the container launches, input the new password and press **Enter**.

   .. code-block:: console
  
      # docker run --rm -ti cyb3rhq/cyb3rhq-indexer:|CYB3RHQ_CURRENT_DOCKER| bash /usr/share/cyb3rhq-indexer/plugins/opensearch-security/tools/hash.sh

#. Copy the generated hash.

#. Open the ``config/cyb3rhq_indexer/internal_users.yml`` file. Locate the block for the user you are changing password for.

#. Replace the hash.

   -  ``admin`` user

      .. code-block:: YAML
         :emphasize-lines: 3

         ...
         admin:
           hash: "$2y$12$K/SpwjtB.wOHJ/Nc6GVRDuc1h0rM1DfvziFRNPtk27P.c4yDr9njO"
           reserved: true
           backend_roles:
           - "admin"
           description: "Demo admin user"

         ...

   -  ``kibanaserver`` user

      .. code-block:: YAML
         :emphasize-lines: 3

         ...
         kibanaserver:
           hash: "$2a$12$4AcgAt3xwOWadA5s5blL6ev39OXDNhmOesEoo33eZtrq2N0YrU3H."
           reserved: true
           description: "Demo kibanaserver user"

         ...

.. _cyb3rhq-docker-password-setting:

Setting the new password
........................

.. warning::

   Don't use the ``$`` or ``&`` characters in your new password. These characters can cause errors during deployment.

#. Open  the ``docker-compose.yml`` file. Change all occurrences of the old password with the new one. For example, for a single-node deployment:

   -  ``admin`` user

      .. code-block:: YAML
         :emphasize-lines: 8, 20

         ...
         services:
           cyb3rhq.manager:
             ...
             environment:
               - INDEXER_URL=https://cyb3rhq.indexer:9200
               - INDEXER_USERNAME=admin
               - INDEXER_PASSWORD=SecretPassword
               - FILEBEAT_SSL_VERIFICATION_MODE=full
               - SSL_CERTIFICATE_AUTHORITIES=/etc/ssl/root-ca.pem
               - SSL_CERTIFICATE=/etc/ssl/filebeat.pem
               - SSL_KEY=/etc/ssl/filebeat.key
               - API_USERNAME=cyb3rhq-wui
               - API_PASSWORD=MyS3cr37P450r.*-
           ...
           cyb3rhq.indexer:
             ...
             environment:
               - "OPENSEARCH_JAVA_OPTS=-Xms1024m -Xmx1024m"
           ...
           cyb3rhq.dashboard:
             ...
             environment:
               - INDEXER_USERNAME=admin
               - INDEXER_PASSWORD=SecretPassword
               - CYB3RHQ_API_URL=https://cyb3rhq.manager
               - DASHBOARD_USERNAME=kibanaserver
               - DASHBOARD_PASSWORD=kibanaserver
               - API_USERNAME=cyb3rhq-wui
               - API_PASSWORD=MyS3cr37P450r.*-
           ...

   -  ``kibanaserver`` user

      .. code-block:: YAML
         :emphasize-lines: 10

         ...
         services:
           cyb3rhq.dashboard:
             ...
             environment:
               - INDEXER_USERNAME=admin
               - INDEXER_PASSWORD=SecretPassword
               - CYB3RHQ_API_URL=https://cyb3rhq.manager
               - DASHBOARD_USERNAME=kibanaserver
               - DASHBOARD_PASSWORD=kibanaserver
               - API_USERNAME=cyb3rhq-wui
               - API_PASSWORD=MyS3cr37P450r.*-
           ...

Applying the changes
....................

#. Start the deployment stack.

   .. code-block:: console
  
      # docker-compose up -d

#. Run ``docker ps`` and note the name of the first Cyb3rhq indexer container. For example, ``single-node-cyb3rhq.indexer-1``, or ``multi-node-cyb3rhq1.indexer-1``.

#. Run ``docker exec -it <CYB3RHQ_INDEXER_CONTAINER_NAME> bash`` to enter the container. For example:

   .. code-block:: console

      # docker exec -it single-node-cyb3rhq.indexer-1 bash

#. Set the following variables:

   .. code-block:: console
  
      export INSTALLATION_DIR=/usr/share/cyb3rhq-indexer
      CACERT=$INSTALLATION_DIR/certs/root-ca.pem
      KEY=$INSTALLATION_DIR/certs/admin-key.pem
      CERT=$INSTALLATION_DIR/certs/admin.pem
      export JAVA_HOME=/usr/share/cyb3rhq-indexer/jdk

#. Wait for the Cyb3rhq indexer to initialize properly. The waiting time can vary from two to five minutes. It depends on the size of the cluster, the assigned resources, and the speed of the network. Then, run the ``securityadmin.sh`` script to apply all changes.

   .. tabs::

      .. tab:: Single-node cluster

         .. code-block:: console

            $ bash /usr/share/cyb3rhq-indexer/plugins/opensearch-security/tools/securityadmin.sh -cd /usr/share/cyb3rhq-indexer/opensearch-security/ -nhnv -cacert  $CACERT -cert $CERT -key $KEY -p 9200 -icl

      .. tab:: Multi-node cluster

         .. code-block:: console

            $ HOST=$(grep node.name $INSTALLATION_DIR/opensearch.yml | awk '{printf $2}')
            $ bash /usr/share/cyb3rhq-indexer/plugins/opensearch-security/tools/securityadmin.sh -cd /usr/share/cyb3rhq-indexer/opensearch-security/ -nhnv -cacert  $CACERT -cert $CERT -key $KEY -p 9200 -icl -h $HOST

#. Exit the Cyb3rhq indexer container and login with the new credentials on the Cyb3rhq dashboard.

Cyb3rhq API users
~~~~~~~~~~~~~~~

The ``cyb3rhq-wui`` user is the user to connect with the Cyb3rhq API by default. Follow these steps to change the password.

.. note::
   
   The password for Cyb3rhq API users must be between 8 and 64 characters long. It must contain at least one uppercase and one lowercase letter, a number, and a symbol.

#. Open the file ``config/cyb3rhq_dashboard/cyb3rhq.yml`` and modify the value of ``password`` parameter.

   .. code-block:: YAML
      :emphasize-lines: 7

      ...
      hosts:
        - 1513629884013:
            url: "https://cyb3rhq.manager"
            port: 55000
            username: cyb3rhq-wui
            password: "MyS3cr37P450r.*-"
            run_as: false
      ...

#. Open  the ``docker-compose.yml`` file. Change all occurrences of the old password with the new one.

   .. code-block:: YAML
      :emphasize-lines: 14,25

      ...
      services:
        cyb3rhq.manager:
          ...
          environment:
            - INDEXER_URL=https://cyb3rhq.indexer:9200
            - INDEXER_USERNAME=admin
            - INDEXER_PASSWORD=SecretPassword
            - FILEBEAT_SSL_VERIFICATION_MODE=full
            - SSL_CERTIFICATE_AUTHORITIES=/etc/ssl/root-ca.pem
            - SSL_CERTIFICATE=/etc/ssl/filebeat.pem
            - SSL_KEY=/etc/ssl/filebeat.key
            - API_USERNAME=cyb3rhq-wui
            - API_PASSWORD=MyS3cr37P450r.*-
        ...
        cyb3rhq.dashboard:
          ...
          environment:
            - INDEXER_USERNAME=admin
            - INDEXER_PASSWORD=SecretPassword
            - CYB3RHQ_API_URL=https://cyb3rhq.manager
            - DASHBOARD_USERNAME=kibanaserver
            - DASHBOARD_PASSWORD=kibanaserver
            - API_USERNAME=cyb3rhq-wui
            - API_PASSWORD=MyS3cr37P450r.*-
        ...

#. Recreate the Cyb3rhq containers:

   .. code-block:: console

      # docker-compose down
      # docker-compose up -d

Exposed ports
-------------

By default, the stack exposes the following ports:

+-----------+-----------------------------+
| **1514**  | Cyb3rhq TCP                   |
+-----------+-----------------------------+
| **1515**  | Cyb3rhq TCP                   |
+-----------+-----------------------------+
| **514**   | Cyb3rhq UDP                   |
+-----------+-----------------------------+
| **55000** | Cyb3rhq API                   |
+-----------+-----------------------------+
| **9200**  | Cyb3rhq indexer  HTTPS        |
+-----------+-----------------------------+
| **443**   | Cyb3rhq dashboard HTTPS       |
+-----------+-----------------------------+

.. note::

   Docker doesn’t reload the configuration dynamically. You need to restart the stack after changing the configuration of a component.
