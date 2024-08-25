.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Find instructions on how to upscale your Cyb3rhq indexer cluster in this section of the documentation.

Adding a Cyb3rhq indexer node
===========================

The Cyb3rhq indexer is a highly scalable, full-text search engine that enables efficient storage and retrieval of security-related data. It is designed to handle large amounts of security events and logs, offering advanced search capabilities and various security features.

Adding a new node to the Cyb3rhq indexer cluster can enhance the capacity and resilience of the security monitoring infrastructure.

The upscale process involves creating certificates, configuring existing components to connect with the new Cyb3rhq indexer node(s), and then installing and configuring the new node(s).

We have organized the steps for upscaling the Cyb3rhq indexer into two subsections: one for an all-in-one deployment and the other for a distributed deployment. Your choice between these methods depends on your existing deployment and the infrastructure you aim to upscale.

-  **All-in-one deployment**

   If you have Cyb3rhq all-in-one configuration, follow the steps outlined in the "All-in-one deployment" subsections to upscale your Cyb3rhq indexer.

-  **Distributed deployment**

   For an existing distributed deployment, refer to the "Distributed deployment" subsections to upscale your Cyb3rhq indexer.

Ensure you select the appropriate sub-section based on your existing deployment. If you are unsure which method aligns with your infrastructure, consider reviewing your deployment architecture before proceeding.

Perform the following steps to add new indexer nodes to your infrastructure:

.. note::
   
   You need ``root`` user privileges to execute the commands below.

Certificates creation
---------------------

Perform the outlined steps on your existing Cyb3rhq indexer node to generate the certificates required for secure communication among the Cyb3rhq central components.

All-in-one deployment
^^^^^^^^^^^^^^^^^^^^^

We recommend creating entirely new certificates for your Cyb3rhq indexer nodes. Perform the following steps to create new certificates.

#. Create a ``config.yml`` file in the ``/root`` directory to add the new Cyb3rhq indexer node(s).

   .. code-block:: console

      # touch /root/config.yml

   Edit the ``/root/config.yml`` file to include the following content.

   .. code-block:: yaml

      nodes:
      # Cyb3rhq indexer nodes
        indexer:
          - name: <EXISTING_CYB3RHQ_INDEXER_NODE_NAME>
            ip: <EXISTING_CYB3RHQ_INDEXER_IP_ADDRESS>
          - name: <NEW_CYB3RHQ_INDEXER_NODE_NAME>
            ip: <NEW_CYB3RHQ_INDEXER_IP_ADDRESS>

      # Cyb3rhq server nodes
        server:
          - name: <CYB3RHQ_SERVER_NODE_NAME>
            ip: <CYB3RHQ_SERVER_IP>

      # Cyb3rhq dashboard nodes
        dashboard:
          - name: <CYB3RHQ_DASHBOARD_NODE_NAME>
            ip: <CYB3RHQ_DASHBOARD_IP>

   Replace the values with your node names and their corresponding IP addresses.

#. Download and run ``./cyb3rhq-certs-tool.sh`` from your ``/root`` directory to recreate the certificates for the old and new nodes.

   .. code-block:: console

      # curl -sO https://packages.cyb3rhq.com/|CYB3RHQ_CURRENT_MINOR|/cyb3rhq-certs-tool.sh
      # bash cyb3rhq-certs-tool.sh -A

#. Compress the certificates folder and copy it to the new Cyb3rhq indexer node(s). You can make use of the ``scp`` utility to securely copy the compressed file.

   .. code-block:: console

      # tar -cvf ./cyb3rhq-certificates.tar -C ./cyb3rhq-certificates/ .
      # scp cyb3rhq-certificates.tar <TARGET_USERNAME>@<TARGET_IP>:

   This will copy the certificates to the home directory of the logged in user on the target system. You can change this to specify a path to your installation directory.

Distributed deployment
^^^^^^^^^^^^^^^^^^^^^^

We recommend you utilize pre-existing root-ca keys to generate certificates for new nodes. 
Perform the steps below on one indexer node only.

#. Create a ``config.yml`` file in the ``/root`` directory to add the new Cyb3rhq indexer node(s).

   .. code-block:: console

      # touch /root/config.yml

   Edit the ``/root/config.yml`` file to include the node name and IP of the new node.

   .. code-block:: yaml

      nodes:
        # Cyb3rhq indexer nodes
        indexer:
          - name: <NEW_CYB3RHQ_INDEXER_NODE_NAME>
            ip: <NEW_CYB3RHQ_INDEXER_IP_ADDRESS>

   Replace the values with your node names and their corresponding IP addresses.

#. Extract the ``cyb3rhq-certificates.tar`` file.

   .. code-block:: console

      # mkdir cyb3rhq-install-files && tar -xf ./cyb3rhq-certificates.tar -C cyb3rhq-install-files

#. Download and run ``./cyb3rhq-certs-tool.sh`` to create the certificates for the new indexer node using the pre-existing root-ca keys:

   .. code-block:: console

      # curl -sO https://packages.cyb3rhq.com/|CYB3RHQ_CURRENT_MINOR|/cyb3rhq-certs-tool.sh
      # bash cyb3rhq-certs-tool.sh -A cyb3rhq-install-files/root-ca.pem cyb3rhq-install-files/root-ca.key

#. Copy the newly created certificates to the ``cyb3rhq-install-files`` folder making sure not to replace the admin certificates.

   .. code-block:: console

      # cp cyb3rhq-certificates/<NEW_CYB3RHQ_INDEXER_NODE_NAME>* cyb3rhq-install-files
   
   .. _creating_new_certificates:
   
   .. note::

      If the pre-existing root-ca keys have been deleted or if you are not able to access them, you can proceed with creating new certificates for all the nodes as follows.

      #. Create the ``/root/config.yml`` file to reference all your nodes.

         .. code-block:: yaml

            nodes:
            # Cyb3rhq indexer nodes
              indexer:
                - name: <EXISTING_CYB3RHQ_INDEXER_NODE_NAME>
                  ip: <EXISTING_CYB3RHQ_INDEXER_IP_ADDRESS>
                - name: <NEW_CYB3RHQ_INDEXER_NODE_NAME>
                  ip: <NEW_CYB3RHQ_INDEXER_IP_ADDRESS>

            # Cyb3rhq server nodes
              server:
                - name: <CYB3RHQ_SERVER_NODE_NAME>
                  ip: <CYB3RHQ_SERVER_IP>

            # Cyb3rhq dashboard nodes
              dashboard:
                - name: <CYB3RHQ_DASHBOARD_NODE_NAME>
                  ip: <CYB3RHQ_DASHBOARD_IP>

      #. Execute the ``cyb3rhq-certs-tool.sh`` script to create the certificates.

         .. code-block:: console

            # curl -sO https://packages.cyb3rhq.com/|CYB3RHQ_CURRENT_MINOR|/cyb3rhq-certs-tool.sh
            # bash cyb3rhq-certs-tool.sh -A

      #. Compress the certificates folder and copy it to the new Cyb3rhq indexer node(s). You can make use of the ``scp`` utility to securely copy the compressed file.

         .. code-block:: console

            # tar -cvf ./cyb3rhq-certificates.tar -C ./cyb3rhq-certificates/ .
            # scp cyb3rhq-certificates.tar <TARGET_USERNAME>@<TARGET_IP>:

         This will copy the certificates to the home directory of the logged in user on the target system. You can change this to specify a path to your installation directory.

#. Compress the certificates folder into a new ``cyb3rhq-certificates.tar`` file and copy it to the new Cyb3rhq indexer node(s). You can make use of the ``scp`` utility to securely copy the compressed file.

   .. code-block:: console

      # tar -cvf ./cyb3rhq-certificates.tar -C ./cyb3rhq-install-files/ .
      # scp cyb3rhq-certificates.tar <TARGET_USERNAME>@<TARGET_IP>:

   This will copy the certificates to the home directory of the logged in user on the target system. You can change this to specify a path to your installation directory.

Configuring existing components to connect with the new node
------------------------------------------------------------

All-in-one deployment
^^^^^^^^^^^^^^^^^^^^^

#. Create a file, ``env_variables.sh``, in the ``/root`` directory of the existing node where you define your environment variables as follows.

   .. code-block:: console

      export NODE_NAME1=<EXISTING_CYB3RHQ_INDEXER_NODE_NAME>
      export NODE_NAME2=<CYB3RHQ_SERVER_NODE_NAME>
      export NODE_NAME3=<CYB3RHQ_DASHBOARD_NODE_NAME> 

   Replace ``<EXISTING_CYB3RHQ_INDEXER_NODE_NAME>``, ``<CYB3RHQ_SERVER_NODE_NAME>``, ``<CYB3RHQ_DASHBOARD_NODE_NAME>`` respectively with the names of the Cyb3rhq indexer, Cyb3rhq server, and Cyb3rhq dashboard nodes as defined in ``/root/config.yml``.

#. Create a ``deploy-certificates.sh`` script in the ``/root`` directory and add the following content.

   .. code-block:: bash

      #!/bin/bash

      # Source the environmental variables from the external file
      source ~/env_variables.sh

      rm -rf /etc/cyb3rhq-indexer/certs
      mkdir /etc/cyb3rhq-indexer/certs
      tar -xf ./cyb3rhq-certificates.tar -C /etc/cyb3rhq-indexer/certs/ ./$NODE_NAME1.pem ./$NODE_NAME1-key.pem ./admin.pem ./admin-key.pem ./root-ca.pem
      mv -n /etc/cyb3rhq-indexer/certs/$NODE_NAME1.pem /etc/cyb3rhq-indexer/certs/cyb3rhq-indexer.pem
      mv -n /etc/cyb3rhq-indexer/certs/$NODE_NAME1-key.pem /etc/cyb3rhq-indexer/certs/cyb3rhq-indexer-key.pem
      chmod 500 /etc/cyb3rhq-indexer/certs
      chmod 400 /etc/cyb3rhq-indexer/certs/*
      chown -R cyb3rhq-indexer:cyb3rhq-indexer /etc/cyb3rhq-indexer/certs

      rm -rf /etc/filebeat/certs
      mkdir /etc/filebeat/certs
      tar -xf ./cyb3rhq-certificates.tar -C /etc/filebeat/certs/ ./$NODE_NAME2.pem ./$NODE_NAME2-key.pem ./root-ca.pem
      mv -n /etc/filebeat/certs/$NODE_NAME2.pem /etc/filebeat/certs/cyb3rhq-server.pem
      mv -n /etc/filebeat/certs/$NODE_NAME2-key.pem /etc/filebeat/certs/cyb3rhq-server-key.pem
      chmod 500 /etc/filebeat/certs
      chmod 400 /etc/filebeat/certs/*
      chown -R root:root /etc/filebeat/certs

      rm -rf /etc/cyb3rhq-dashboard/certs
      mkdir /etc/cyb3rhq-dashboard/certs
      tar -xf ./cyb3rhq-certificates.tar -C /etc/cyb3rhq-dashboard/certs/ ./$NODE_NAME3.pem ./$NODE_NAME3-key.pem ./root-ca.pem
      mv -n /etc/cyb3rhq-dashboard/certs/$NODE_NAME3.pem /etc/cyb3rhq-dashboard/certs/cyb3rhq-dashboard.pem
      mv -n /etc/cyb3rhq-dashboard/certs/$NODE_NAME3-key.pem /etc/cyb3rhq-dashboard/certs/cyb3rhq-dashboard-key.pem
      chmod 500 /etc/cyb3rhq-dashboard/certs
      chmod 400 /etc/cyb3rhq-dashboard/certs/*
      chown -R cyb3rhq-dashboard:cyb3rhq-dashboard /etc/cyb3rhq-dashboard/certs

#. Then deploy the certificates by executing the following command.

   .. code-block::  console

      # bash /root/deploy-certificates.sh
   
   This deploys the SSL certificates to encrypt communications between the Cyb3rhq central components.

   **Recommended action**: If no other Cyb3rhq components are going to be installed on this node, remove the ``cyb3rhq-certificates.tar`` file by running the command below to increase security. Alternatively, save a copy offline for potential future use and scalability.

   .. code-block:: console

      # rm -rf ./cyb3rhq-certificates
      # rm -f ./cyb3rhq-certificates.tar

#. Edit the indexer configuration file at ``/etc/cyb3rhq-indexer/opensearch.yml`` to include the new node(s) as follows. Uncomment or add more lines, according to your ``/root/config.yml`` definitions. Create the ``discovery.seed_hosts`` section if it doesn’t exist.

   .. code-block:: yaml
      :emphasize-lines: 5, 9, 12

      network.host: "<EXISTING_CYB3RHQ_INDEXER_IP_ADDRESS>"
      node.name: "<EXISTING_CYB3RHQ_INDEXER_NODE_NAME>"
      cluster.initial_master_nodes:
      - "<EXISTING_CYB3RHQ_INDEXER_NODE_NAME>"
      - "<NEW_CYB3RHQ_INDEXER_NODE_NAME>"
      cluster.name: "cyb3rhq-cluster"
      discovery.seed_hosts:
        - "<EXISTING_CYB3RHQ_INDEXER_IP_ADDRESS>"
        - "<NEW_CYB3RHQ_INDEXER_IP_ADDRESS>"
      plugins.security.nodes_dn:
      - "CN=<EXISTING_CYB3RHQ_INDEXER_NODE_NAME>,OU=Cyb3rhq,O=Cyb3rhq,L=California,C=US"
      - "CN=<NEW_CYB3RHQ_INDEXER_NODE_NAME>,OU=Cyb3rhq,O=Cyb3rhq,L=California,C=US"

#. Edit the Filebeat configuration file ``/etc/filebeat/filebeat.yml`` to add the new Cyb3rhq indexer node(s). Uncomment or add more lines, according to your ``/root/config.yml`` definitions:

   .. code-block:: yaml
      :emphasize-lines: 3

      output.elasticsearch.hosts:
              - <EXISTING_CYB3RHQ_INDEXER_IP_ADDRESS>:9200
              - <NEW_CYB3RHQ_INDEXER_IP_ADDRESS>:9200
      output.elasticsearch:
        protocol: https
        username: ${username}
        password: ${password}

#. Edit the Cyb3rhq dashboard configuration file ``/etc/cyb3rhq-dashboard/opensearch_dashboards.yml`` to include the new Cyb3rhq indexer node(s).

   .. code-block:: yaml

      opensearch.hosts: ["https://<EXISTING_CYB3RHQ_INDEXER_IP_ADDRESS>:9200", "https://<NEW_CYB3RHQ_INDEXER_IP_ADDRESS>:9200"]

#. Restart the Cyb3rhq services to apply the changes.

   .. tabs::

      .. group-tab:: SystemD

         .. code-block:: console

            # systemctl restart cyb3rhq-indexer
            # systemctl restart filebeat
            # systemctl restart cyb3rhq-manager
            # systemctl restart cyb3rhq-dashboard

      .. group-tab:: SysV init

         .. code-block:: console

            # service cyb3rhq-indexer restart 
            # service filebeat restart 
            # service cyb3rhq-manager restart 
            # service cyb3rhq-dashboard restart

Distributed deployment
^^^^^^^^^^^^^^^^^^^^^^

#. Edit the indexer configuration file at ``/etc/cyb3rhq-indexer/opensearch.yml`` to include the new node(s) as follows. Uncomment or add more lines, according to your ``/root/config.yml`` definitions. Create the ``discovery.seed_hosts`` section if it doesn’t exist.

   .. code-block:: yaml
      :emphasize-lines: 5, 9, 12

      network.host: "<EXISTING_CYB3RHQ_INDEXER_IP_ADDRESS>"
      node.name: "<EXISTING_CYB3RHQ_INDEXER_NODE_NAME>"
      cluster.initial_master_nodes:
      - "<EXISTING_CYB3RHQ_INDEXER_NODE_NAME>"
      - "<NEW_CYB3RHQ_INDEXER_NODE_NAME>"
      cluster.name: "cyb3rhq-cluster"
      discovery.seed_hosts:
        - "<EXISTING_CYB3RHQ_INDEXER_IP_ADDRESS>"
        - "<NEW_CYB3RHQ_INDEXER_IP_ADDRESS>"
      plugins.security.nodes_dn:
      - "CN=indexer,OU=Cyb3rhq,O=Cyb3rhq,L=California,C=US"
      - "CN=<CYB3RHQ_INDEXER2_NODE_NAME>,OU=Cyb3rhq,O=Cyb3rhq,L=California,C=US"

#. Edit the Filebeat configuration file ``/etc/filebeat/filebeat.yml`` (the file is located in the Cyb3rhq server) to add the new Cyb3rhq indexer node(s). Uncomment or add more lines, according to your ``/root/config.yml`` definitions.

   .. code-block:: yaml
      :emphasize-lines: 3

      output.elasticsearch.hosts:
              - <EXISTING_CYB3RHQ_INDEXER_IP_ADDRESS>:9200
              - <NEW_CYB3RHQ_INDEXER_IP_ADDRESS>:9200
      output.elasticsearch:
        protocol: https
        username: ${username}
        password: ${password}

#. Edit the Cyb3rhq dashboard configuration file ``/etc/cyb3rhq-dashboard/opensearch_dashboards.yml`` to include the new Cyb3rhq indexer node(s).

   .. code-block:: yaml

      opensearch.hosts: ["https://<EXISTING_CYB3RHQ_INDEXER_IP_ADDRESS>:9200", "https://<NEW_CYB3RHQ_INDEXER_IP_ADDRESS>:9200"]

   .. note::

      You’ll have to re-deploy certificates on your existing Cyb3rhq node(s) if they were recreated as recommended in the :ref:`note <creating_new_certificates>` above.

      Run the following commands on each of your nodes to deploy the certificates.

      -  On Cyb3rhq indexer node(s).

         .. code-block:: console

            # NODE_NAME=<EXISTING_CYB3RHQ_INDEXER_NODE_NAME>

            # rm -rf /etc/cyb3rhq-indexer/certs
            # mkdir /etc/cyb3rhq-indexer/certs
            # tar -xf ./cyb3rhq-certificates.tar -C /etc/cyb3rhq-indexer/certs/ ./$NODE_NAME.pem ./$NODE_NAME-key.pem ./admin.pem ./admin-key.pem ./root-ca.pem
            # mv -n /etc/cyb3rhq-indexer/certs/$NODE_NAME.pem /etc/cyb3rhq-indexer/certs/indexer.pem
            # mv -n /etc/cyb3rhq-indexer/certs/$NODE_NAME-key.pem /etc/cyb3rhq-indexer/certs/indexer-key.pem
            # chmod 500 /etc/cyb3rhq-indexer/certs
            # chmod 400 /etc/cyb3rhq-indexer/certs/*
            # chown -R cyb3rhq-indexer:cyb3rhq-indexer /etc/cyb3rhq-indexer/certs

      -  On Cyb3rhq server node(s).

         .. code-block:: console

            # NODE_NAME=<CYB3RHQ_SERVER_NODE_NAME>

            # rm -rf /etc/filebeat/certs
            # mkdir /etc/filebeat/certs
            # tar -xf ./cyb3rhq-certificates.tar -C /etc/filebeat/certs/ ./$NODE_NAME.pem ./$NODE_NAME-key.pem ./root-ca.pem
            # mv -n /etc/filebeat/certs/$NODE_NAME.pem /etc/filebeat/certs/cyb3rhq-server.pem
            # mv -n /etc/filebeat/certs/$NODE_NAME-key.pem /etc/filebeat/certs/cyb3rhq-server-key.pem
            # chmod 500 /etc/filebeat/certs
            # chmod 400 /etc/filebeat/certs/*
            # chown -R root:root /etc/filebeat/certs

      -  On Cyb3rhq dashboard node:

         .. code-block:: console

            # NODE_NAME=<CYB3RHQ_DASHBOARD_NODE_NAME>

            # rm -rf /etc/cyb3rhq-dashboard/certs
            # mkdir /etc/cyb3rhq-dashboard/certs
            # tar -xf ./cyb3rhq-certificates.tar -C /etc/cyb3rhq-dashboard/certs/ ./$NODE_NAME.pem ./$NODE_NAME-key.pem ./root-ca.pem
            # mv -n /etc/cyb3rhq-dashboard/certs/$NODE_NAME.pem /etc/cyb3rhq-dashboard/certs/cyb3rhq-dashboard.pem
            # mv -n /etc/cyb3rhq-dashboard/certs/$NODE_NAME-key.pem /etc/cyb3rhq-dashboard/certs/cyb3rhq-dashboard-key.pem
            # chmod 500 /etc/cyb3rhq-dashboard/certs
            # chmod 400 /etc/cyb3rhq-dashboard/certs/*
            # chown -R cyb3rhq-dashboard:cyb3rhq-dashboard /etc/cyb3rhq-dashboard/certs

#. Run the following commands on your respective nodes to apply the changes.

   -  Cyb3rhq indexer node

      .. tabs::

         .. group-tab:: SystemD

            .. code-block:: console

               # systemctl restart cyb3rhq-indexer

         .. group-tab:: SysV init

            .. code-block:: console

               # service cyb3rhq-indexer restart

   -  Cyb3rhq server node

      .. tabs::

         .. group-tab:: SystemD

            .. code-block:: console

               # systemctl restart filebeat
               # systemctl restart cyb3rhq-manager

         .. group-tab:: SysV init

            .. code-block:: console

               # service filebeat restart 
               # service cyb3rhq-manager restart

   -  Cyb3rhq dashboard node

      .. tabs::

         .. group-tab:: SystemD

            .. code-block:: console

               # systemctl restart cyb3rhq-dashboard

         .. group-tab:: SysV init

            .. code-block:: console

               # service cyb3rhq-dashboard restart

Cyb3rhq indexer node(s) installation
----------------------------------

Once the certificates have been created and copied to the new node(s), you can now proceed with installing the Cyb3rhq indexer node.

#. Install package dependencies.

   .. tabs::

      .. group-tab:: Yum

         .. code-block:: console

            # yum install coreutils

      .. group-tab:: APT

         .. code-block:: console

            # apt-get install debconf adduser procps

#. Add the Cyb3rhq repository.

   .. tabs::

      .. group-tab:: Yum

         .. include:: /_templates/installations/common/yum/add-repository.rst

      .. group-tab:: APT

         .. include:: /_templates/installations/common/deb/add-repository.rst

#. Install the Cyb3rhq indexer.

   .. tabs::

      .. group-tab:: Yum

         .. code-block:: console

            # yum -y install cyb3rhq-indexer|CYB3RHQ_INDEXER_RPM_PKG_INSTALL|

      .. group-tab:: APT

         .. code-block:: console

            # apt-get -y install cyb3rhq-indexer|CYB3RHQ_INDEXER_DEB_PKG_INSTALL|

Configuring the Cyb3rhq indexer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Edit the ``/etc/cyb3rhq-indexer/opensearch.yml`` configuration file and replace the following values:

#. ``network.host``: Sets the address of this node for both HTTP and HTTPS traffic. The node will bind to this address and use it as its publish address. This field accepts an IP address or a hostname.

   Use the same node address set in ``/root/config.yml`` to create the SSL certificates.

#. ``node.name``: Name of the Cyb3rhq indexer node as defined in the ``/root/config.yml`` file. For example, ``node-1``.

#. ``cluster.initial_master_nodes``: List of the names of the master-eligible nodes. These names are defined in the ``/root/config.yml`` file. Uncomment the ``node-2`` line or add more lines, and change the node names according to your ``/root/config.yml`` definitions.

   .. code-block:: yaml

      cluster.initial_master_nodes:
      - "<EXISTING_CYB3RHQ_INDEXER_NODE_NAME>"
      - "<NEW_CYB3RHQ_INDEXER_NODE_NAME>"

#. ``discovery.seed_hosts``: List of the addresses of the master-eligible nodes. Each element can be either an IP address or a hostname. Uncomment this setting and set the IP addresses of each master-eligible node:

   .. code-block:: yaml

      discovery.seed_hosts:
        - "<EXISTING_CYB3RHQ_INDEXER_IP_ADDRESS>"
        - "<NEW_CYB3RHQ_INDEXER_IP_ADDRESS>"

#. ``plugins.security.nodes_dn``: List of the Distinguished Names of the certificates of all the Cyb3rhq indexer cluster nodes. Uncomment the line for ``node-2`` and change the common names (CN) and values according to your settings and your ``/root/config.yml`` definitions:

   .. code-block:: yaml

      plugins.security.nodes_dn:
      - "CN=<EXISTING_CYB3RHQ_INDEXER_NODE_NAME>,OU=Cyb3rhq,O=Cyb3rhq,L=California,C=US"
      - "CN=<NEW_CYB3RHQ_INDEXER_NODE_NAME>,OU=Cyb3rhq,O=Cyb3rhq,L=California,C=US"

Deploying certificates
^^^^^^^^^^^^^^^^^^^^^^

#. Run the following commands in the directory where the ``cyb3rhq-certificates.tar`` file was copied to, replacing ``<NEW_CYB3RHQ_INDEXER_NODE_NAME>`` with the name of the Cyb3rhq indexer node you are configuring as defined in ``/root/config.yml``. For example, ``node-1``. This deploys the SSL certificates to encrypt communications between the Cyb3rhq central components:

   .. code-block:: console

      # NODE_NAME=NEW_CYB3RHQ_INDEXER_NODE_NAME

   .. code-block:: console

      # mkdir /etc/cyb3rhq-indexer/certs
      # tar -xf ./cyb3rhq-certificates.tar -C /etc/cyb3rhq-indexer/certs/ ./$NODE_NAME.pem ./$NODE_NAME-key.pem ./admin.pem ./admin-key.pem ./root-ca.pem
      # mv -n /etc/cyb3rhq-indexer/certs/$NODE_NAME.pem /etc/cyb3rhq-indexer/certs/indexer.pem
      # mv -n /etc/cyb3rhq-indexer/certs/$NODE_NAME-key.pem /etc/cyb3rhq-indexer/certs/indexer-key.pem
      # chmod 500 /etc/cyb3rhq-indexer/certs
      # chmod 400 /etc/cyb3rhq-indexer/certs/*
      # chown -R cyb3rhq-indexer:cyb3rhq-indexer /etc/cyb3rhq-indexer/certs

#. **Recommended action**: If no other Cyb3rhq components are going to be installed on this node, remove the ``cyb3rhq-certificates.tar`` file by running the command below to increase security. Alternatively, save a copy offline for potential future use and scalability.

   .. code-block:: console

      # rm -f ./cyb3rhq-certificates.tar

Starting the service
^^^^^^^^^^^^^^^^^^^^

#. Run the following commands to start the Cyb3rhq indexer service.

   .. include:: /_templates/installations/indexer/common/enable_indexer.rst

Cluster initialization
----------------------

Run the Cyb3rhq indexer ``indexer-security-init.sh`` script on `any` Cyb3rhq indexer node to load the new certificates information and start the cluster. 
    
.. code-block:: console

   # /usr/share/cyb3rhq-indexer/bin/indexer-security-init.sh

.. note::
   
   You only have to initialize the cluster `once`, there is no need to run this command on every node.

Confirm the configuration works by running the command below on your Cyb3rhq server node.

.. code-block:: console

   filebeat test output

An example output is shown below:

.. code-block:: none
   :class: output
   :emphasize-lines: 1, 10, 13, 15, 24, 27

   elasticsearch: https://10.0.0.1:9200...
      parse url... OK
      connection...
         parse host... OK
         dns lookup... OK
         addresses: 10.0.0.1
         dial up... OK
      TLS...
         security: server's certificate chain verification is enabled
         handshake... OK
         TLS version: TLSv1.3
         dial up... OK
      talk to server... OK
      version: 7.10.2
   elasticsearch: https://10.0.0.2:9200...
      parse url... OK
      connection...
         parse host... OK
         dns lookup... OK
         addresses: 10.0.0.2
         dial up... OK
      TLS...
         security: server's certificate chain verification is enabled
         handshake... OK
         TLS version: TLSv1.3
         dial up... OK
      talk to server... OK
      version: 7.10.2

Testing the cluster
-------------------

After completing the above steps, you can proceed to test your cluster and ensure that the indexer node has been successfully added. There are two possible methods to do this:

.. contents::
   :local:
   :depth: 1
   :backlinks: none

Using the `securityadmin` script
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The `securityadmin` script helps configure and manage the security settings of OpenSearch. The script lets you load, backup, restore, and migrate the security configuration files to the Cyb3rhq indexer cluster.

Run the  the command below on any of the Cyb3rhq indexer nodes to execute the ``securityadmin`` script and initialize the cluster:

.. code-block:: console

   /usr/share/cyb3rhq-indexer/bin/indexer-security-init.sh

The output should be similar to the one below. It should show the number of Cyb3rhq indexer nodes in the cluster:

.. code-block:: none
   :class: output
   :emphasize-lines: 12,13

   **************************************************************************
   ** This tool will be deprecated in the next major release of OpenSearch **
   ** https://github.com/opensearch-project/security/issues/1755           **
   **************************************************************************
   Security Admin v7
   Will connect to 192.168.21.152:9200 ... done
   Connected as "CN=admin,OU=Cyb3rhq,O=Cyb3rhq,L=California,C=US"
   OpenSearch Version: 2.6.0
   Contacting opensearch cluster 'opensearch' and wait for YELLOW clusterstate ...
   Clustername: cyb3rhq-cluster
   Clusterstate: GREEN
   Number of nodes: 2
   Number of data nodes: 2
   .opendistro_security index already exists, so we do not need to create one.
   Populate config from /etc/cyb3rhq-indexer/opensearch-security/
   Will update '/config' with /etc/cyb3rhq-indexer/opensearch-security/config.yml
      SUCC: Configuration for 'config' created or updated
   Will update '/roles' with /etc/cyb3rhq-indexer/opensearch-security/roles.yml
      SUCC: Configuration for 'roles' created or updated
   Will update '/rolesmapping' with /etc/cyb3rhq-indexer/opensearch-security/roles_mapping.yml
      SUCC: Configuration for 'rolesmapping' created or updated
   Will update '/internalusers' with /etc/cyb3rhq-indexer/opensearch-security/internal_users.yml
      SUCC: Configuration for 'internalusers' created or updated
   Will update '/actiongroups' with /etc/cyb3rhq-indexer/opensearch-security/action_groups.yml
      SUCC: Configuration for 'actiongroups' created or updated
   Will update '/tenants' with /etc/cyb3rhq-indexer/opensearch-security/tenants.yml
      SUCC: Configuration for 'tenants' created or updated
   Will update '/nodesdn' with /etc/cyb3rhq-indexer/opensearch-security/nodes_dn.yml
      SUCC: Configuration for 'nodesdn' created or updated
   Will update '/whitelist' with /etc/cyb3rhq-indexer/opensearch-security/whitelist.yml
      SUCC: Configuration for 'whitelist' created or updated
   Will update '/audit' with /etc/cyb3rhq-indexer/opensearch-security/audit.yml
      SUCC: Configuration for 'audit' created or updated
   Will update '/allowlist' with /etc/cyb3rhq-indexer/opensearch-security/allowlist.yml
      SUCC: Configuration for 'allowlist' created or updated
   SUCC: Expected 10 config types for node {"updated_config_types":["allowlist","tenants","rolesmapping","nodesdn","audit","roles","whitelist","internalusers","actiongroups","config"],"updated_config_size":10,"message":null} is 10 (["allowlist","tenants","rolesmapping","nodesdn","audit","roles","whitelist","internalusers","actiongroups","config"]) due to: null
   SUCC: Expected 10 config types for node {"updated_config_types":["allowlist","tenants","rolesmapping","nodesdn","audit","roles","whitelist","internalusers","actiongroups","config"],"updated_config_size":10,"message":null} is 10 (["allowlist","tenants","rolesmapping","nodesdn","audit","roles","whitelist","internalusers","actiongroups","config"]) due to: null
   Done with success

Using the Cyb3rhq indexer API
^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can also get information about the number of nodes in the cluster  by using the Cyb3rhq indexer API.

Run the command below on any of Cyb3rhq indexer nodes and check the output for the field ``number_of_nodes`` to ensure it corresponds to the expected number of Cyb3rhq indexer nodes:

   .. code-block:: console

      # curl -XGET https:/<EXISTING_CYB3RHQ_INDEXER_IP_ADDRESS>:9200/_cluster/health?pretty -u admin:<ADMIN_PASSWORD> -k

Replace ``<EXISTING_CYB3RHQ_INDEXER_IP_ADDRESS>`` by the IP address of any of your indexer nodes and ``<ADMIN_PASSWORD>`` with your administrator password. The output of the command should be similar to the following:

   .. code-block:: none
      :class: output
      :emphasize-lines: 5,6

      {
        "cluster_name" : "cyb3rhq-cluster",
        "status" : "green",
        "timed_out" : false,
        "number_of_nodes" : 2,
        "number_of_data_nodes" : 2,
        "discovered_master" : true,
        "discovered_cluster_manager" : true,
        "active_primary_shards" : 11,
        "active_shards" : 20,
        "relocating_shards" : 0,
        "initializing_shards" : 0,
        "unassigned_shards" : 0,
        "delayed_unassigned_shards" : 0,
        "number_of_pending_tasks" : 0,
        "number_of_in_flight_fetch" : 0,
        "task_max_waiting_in_queue_millis" : 0,
        "active_shards_percent_as_number" : 100.0
      }

You can now access the Cyb3rhq dashboard with your credentials.

-  URL: ``https://<CYB3RHQ_DASHBOARD_IP>``
-  Username: ``admin``
-  Password: ``<ADMIN_PASSWORD>`` or admin in case you already have a distributed architecture and using the default password.

After the above steps are completed, your new node(s) will now be part of your cluster and your infrastructure distributed.
