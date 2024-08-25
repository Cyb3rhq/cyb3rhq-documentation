Install Cyb3rhq components step by step
-----------------------------------------

#. In the working directory where you placed ``cyb3rhq-offline.tar.gz`` and ``cyb3rhq-install-files.tar``, execute the following command to decompress the installation files:

   .. code-block:: console

      # tar xf cyb3rhq-offline.tar.gz
      # tar xf cyb3rhq-install-files.tar

   You can check the SHA512 of the decompressed package files in ``cyb3rhq-offline/cyb3rhq-packages/``. Find the SHA512 checksums in the :doc:`/installation-guide/packages-list`.

Installing the Cyb3rhq indexer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#.  Run the following commands to install the Cyb3rhq indexer.

    .. tabs::

        .. group-tab:: RPM

            .. code-block:: console
        
               # rpm --import ./cyb3rhq-offline/cyb3rhq-files/GPG-KEY-CYB3RHQ
               # rpm -ivh ./cyb3rhq-offline/cyb3rhq-packages/cyb3rhq-indexer*.rpm

        .. group-tab:: DEB

            .. code-block:: console
        
                # dpkg -i ./cyb3rhq-offline/cyb3rhq-packages/cyb3rhq-indexer*.deb

#. Run the following commands replacing ``<indexer-node-name>`` with the name of the Cyb3rhq indexer node you are configuring as defined in ``config.yml``. For example, ``node-1``. This deploys the SSL certificates to encrypt communications between the Cyb3rhq central components.

   .. code-block:: console

      # NODE_NAME=<indexer-node-name>

   .. code-block:: console
    
      # mkdir /etc/cyb3rhq-indexer/certs
      # mv -n cyb3rhq-install-files/$NODE_NAME.pem /etc/cyb3rhq-indexer/certs/indexer.pem
      # mv -n cyb3rhq-install-files/$NODE_NAME-key.pem /etc/cyb3rhq-indexer/certs/indexer-key.pem
      # mv cyb3rhq-install-files/admin-key.pem /etc/cyb3rhq-indexer/certs/
      # mv cyb3rhq-install-files/admin.pem /etc/cyb3rhq-indexer/certs/
      # cp cyb3rhq-install-files/root-ca.pem /etc/cyb3rhq-indexer/certs/
      # chmod 500 /etc/cyb3rhq-indexer/certs
      # chmod 400 /etc/cyb3rhq-indexer/certs/*
      # chown -R cyb3rhq-indexer:cyb3rhq-indexer /etc/cyb3rhq-indexer/certs

   Here you move the node certificate and key files, such as `node-1.pem` and `node-1-key.pem`, to their corresponding `certs` folder. They're specific to the node and are not required on the other nodes. However, note that the `root-ca.pem` certificate isn't moved but copied to the `certs` folder. This way, you can continue deploying it to other component folders in the next steps.

#. Edit ``/etc/cyb3rhq-indexer/opensearch.yml`` and replace the following values: 

    
   #. ``network.host``:  Sets the address of this node for both HTTP and transport traffic. The node will bind to this address and will also use it as its publish address. Accepts an IP address or a hostname. 
   
      Use the same node address set in ``config.yml`` to create the SSL certificates. 

   #. ``node.name``: Name of the Cyb3rhq indexer node as defined in the ``config.yml`` file. For example, ``node-1``.

   #. ``cluster.initial_master_nodes``: List of the names of the master-eligible nodes. These names are defined in the ``config.yml`` file. Uncomment the ``node-2`` and ``node-3`` lines, change the names, or add more lines, according to your ``config.yml`` definitions.

      .. code-block:: yaml

        cluster.initial_master_nodes:
        - "node-1"
        - "node-2"
        - "node-3"

   #. ``discovery.seed_hosts:`` List of the addresses of the master-eligible nodes. Each element can be either an IP address or a hostname. 
      You may leave this setting commented if you are configuring the Cyb3rhq indexer as a single-node. For multi-node configurations, uncomment this setting and set your master-eligible nodes addresses. 

       .. code-block:: yaml

        discovery.seed_hosts:
          - "10.0.0.1"
          - "10.0.0.2"
          - "10.0.0.3"
  
   #. ``plugins.security.nodes_dn``: List of the Distinguished Names of the certificates of all the Cyb3rhq indexer cluster nodes. Uncomment the lines for ``node-2`` and ``node-3`` and change the common names (CN) and values according to your settings and your ``config.yml`` definitions.

      .. code-block:: yaml

        plugins.security.nodes_dn:
        - "CN=node-1,OU=Cyb3rhq,O=Cyb3rhq,L=California,C=US"
        - "CN=node-2,OU=Cyb3rhq,O=Cyb3rhq,L=California,C=US"
        - "CN=node-3,OU=Cyb3rhq,O=Cyb3rhq,L=California,C=US"

#.  Enable and start the Cyb3rhq indexer service.

    .. include:: /_templates/installations/indexer/common/enable_indexer.rst

#. For multi-node clusters, repeat the previous steps on every Cyb3rhq indexer node. 

#. When all Cyb3rhq indexer nodes are running, run the Cyb3rhq indexer ``indexer-security-init.sh`` script on `any Cyb3rhq indexer node` to load the new certificates information and start the cluster.

    .. code-block:: console

        # /usr/share/cyb3rhq-indexer/bin/indexer-security-init.sh
  
#. Run the following command to check that the installation is successful. Note that this command uses ``127.0.0.1``, set your Cyb3rhq indexer address if necessary. 

   .. code-block:: console

      # curl -XGET https://127.0.0.1:9200 -u admin:admin -k

   Expand the output to see an example response.

   .. code-block:: none
      :class: output collapsed

      {
        "name" : "node-1",
        "cluster_name" : "cyb3rhq-cluster",
        "cluster_uuid" : "095jEW-oRJSFKLz5wmo5PA",
        "version" : {
          "number" : "7.10.2",
          "build_type" : "rpm",
          "build_hash" : "db90a415ff2fd428b4f7b3f800a51dc229287cb4",
          "build_date" : "2023-06-03T06:24:25.112415503Z",
          "build_snapshot" : false,
          "lucene_version" : "9.6.0",
          "minimum_wire_compatibility_version" : "7.10.0",
          "minimum_index_compatibility_version" : "7.0.0"
        },
        "tagline" : "The OpenSearch Project: https://opensearch.org/"
      }

Installing the Cyb3rhq server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Installing the Cyb3rhq manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#.  Run the following commands to import the Cyb3rhq key and install the Cyb3rhq manager.

    .. tabs::

        .. group-tab:: RPM

            .. code-block:: console
        
                # rpm --import ./cyb3rhq-offline/cyb3rhq-files/GPG-KEY-CYB3RHQ
                # rpm -ivh ./cyb3rhq-offline/cyb3rhq-packages/cyb3rhq-manager*.rpm

        .. group-tab:: DEB

            .. code-block:: console
        
                # dpkg -i ./cyb3rhq-offline/cyb3rhq-packages/cyb3rhq-manager*.deb

#. Save the Cyb3rhq indexer username and password into the Cyb3rhq manager keystore using the cyb3rhq-keystore tool: 

   .. code-block:: console

      # echo '<INDEXER_USERNAME>' | /var/ossec/bin/cyb3rhq-keystore -f indexer -k username
      # echo '<INDEXER_PASSWORD>' | /var/ossec/bin/cyb3rhq-keystore -f indexer -k password   

   .. note:: The default offline-installation credentials are ``admin``:``admin``

#. Enable and start the Cyb3rhq manager service.

   .. include:: /_templates/installations/cyb3rhq/common/enable_cyb3rhq_manager_service.rst

#. Run the following command to verify that the Cyb3rhq manager status is active.

   .. include:: /_templates/installations/cyb3rhq/common/check_cyb3rhq_manager.rst

Installing Filebeat
~~~~~~~~~~~~~~~~~~~

Filebeat must be installed and configured on the same server as the Cyb3rhq manager.

#.  Run the following command to install Filebeat.

    .. tabs::

        .. group-tab:: RPM

            .. code-block:: console
        
                # rpm -ivh ./cyb3rhq-offline/cyb3rhq-packages/filebeat*.rpm

        .. group-tab:: DEB

            .. code-block:: console
        
                # dpkg -i ./cyb3rhq-offline/cyb3rhq-packages/filebeat*.deb

#.  Move a copy of the configuration files to the appropriate location. Ensure to type “yes” at the prompt to overwrite ``/etc/filebeat/filebeat.yml``.

    .. code-block:: console
    
        # cp ./cyb3rhq-offline/cyb3rhq-files/filebeat.yml /etc/filebeat/ &&\
        cp ./cyb3rhq-offline/cyb3rhq-files/cyb3rhq-template.json /etc/filebeat/ &&\
        chmod go+r /etc/filebeat/cyb3rhq-template.json

#. Edit the ``/etc/filebeat/filebeat.yml`` configuration file and replace the following value:

   .. include:: /_templates/installations/filebeat/opensearch/configure_filebeat.rst

#. Create a Filebeat keystore to securely store authentication credentials.

   .. code-block:: console
     
      # filebeat keystore create

#. Add the username and password ``admin``:``admin`` to the secrets keystore.
      
   .. code-block:: console

      # echo admin | filebeat keystore add username --stdin --force
      # echo admin | filebeat keystore add password --stdin --force              

#.  Install the Cyb3rhq module for Filebeat.

    .. code-block:: console
    
        # tar -xzf ./cyb3rhq-offline/cyb3rhq-files/cyb3rhq-filebeat-0.4.tar.gz -C /usr/share/filebeat/module

#.  Replace ``<SERVER_NODE_NAME>`` with your Cyb3rhq server node certificate name, the same used in ``config.yml`` when creating the certificates. For example, ``cyb3rhq-1``. Then, move the certificates to their corresponding location.

     .. code-block:: console
        
        # NODE_NAME=<SERVER_NODE_NAME>

    .. code-block:: console

        # mkdir /etc/filebeat/certs
        # mv -n cyb3rhq-install-files/$NODE_NAME.pem /etc/filebeat/certs/filebeat.pem
        # mv -n cyb3rhq-install-files/$NODE_NAME-key.pem /etc/filebeat/certs/filebeat-key.pem
        # cp cyb3rhq-install-files/root-ca.pem /etc/filebeat/certs/
        # chmod 500 /etc/filebeat/certs
        # chmod 400 /etc/filebeat/certs/*
        # chown -R root:root /etc/filebeat/certs


#.  Enable and start the Filebeat service.

    .. include:: /_templates/installations/elastic/common/enable_filebeat.rst

#.  Run the following command to make sure Filebeat is successfully installed.

    .. code-block:: console

        # filebeat test output

    Expand the output to see an example response.

    .. code-block:: none
        :class: output collapsed

        elasticsearch: https://127.0.0.1:9200...
          parse url... OK
          connection...
            parse host... OK
            dns lookup... OK
            addresses: 127.0.0.1
            dial up... OK
          TLS...
            security: server's certificate chain verification is enabled
            handshake... OK
            TLS version: TLSv1.3
            dial up... OK
          talk to server... OK
          version: 7.10.2


Your Cyb3rhq server node is now successfully installed. Repeat the steps of this installation process stage for every Cyb3rhq server node in your cluster, expand the **Cyb3rhq cluster configuration for multi-node deployment** section below, and carry on then with configuring the Cyb3rhq cluster. If you want a Cyb3rhq server single-node cluster, everything is set and you can proceed directly with the Cyb3rhq dashboard installation.
  
Cyb3rhq cluster configuration for multi-node deployment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

  <div class="accordion-section">

After completing the installation of the Cyb3rhq server on every node, you need to configure one server node only as the master and the rest as workers.


Configuring the Cyb3rhq server master node
""""""""""""""""""""""""""""""""""""""""

  #. Edit the following settings in the ``/var/ossec/etc/ossec.conf`` configuration file.

      .. include:: /_templates/installations/manager/configure_cyb3rhq_master_node.rst

  #. Restart the Cyb3rhq manager. 

      .. include:: /_templates/installations/manager/restart_cyb3rhq_manager.rst

    
Configuring the Cyb3rhq server worker nodes
"""""""""""""""""""""""""""""""""""""""""

  #. .. include:: /_templates/installations/manager/configure_cyb3rhq_worker_node.rst

  #. Restart the Cyb3rhq manager. 

      .. include:: /_templates/installations/manager/restart_cyb3rhq_manager.rst

  Repeat these configuration steps for every Cyb3rhq server worker node in your cluster.

Testing Cyb3rhq server cluster
""""""""""""""""""""""""""""

To verify that the Cyb3rhq cluster is enabled and all the nodes are connected, execute the following command:

  .. code-block:: console

    # /var/ossec/bin/cluster_control -l

An example output of the command looks as follows:

  .. code-block:: none
    :class: output
    
      NAME         TYPE    VERSION  ADDRESS
      master-node  master  |CYB3RHQ_CURRENT|   10.0.0.3
      worker-node1 worker  |CYB3RHQ_CURRENT|   10.0.0.4
      worker-node2 worker  |CYB3RHQ_CURRENT|   10.0.0.5

Note that ``10.0.0.3``, ``10.0.0.4``, ``10.0.0.5`` are example IPs.

Installing the Cyb3rhq dashboard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#.  Run the following commands to install the Cyb3rhq dashboard.

    .. tabs::

        .. group-tab:: RPM

            .. code-block:: console
       
                # rpm --import ./cyb3rhq-offline/cyb3rhq-files/GPG-KEY-CYB3RHQ
                # rpm -ivh ./cyb3rhq-offline/cyb3rhq-packages/cyb3rhq-dashboard*.rpm

        .. group-tab:: DEB

            .. code-block:: console
       
                # dpkg -i ./cyb3rhq-offline/cyb3rhq-packages/cyb3rhq-dashboard*.deb

#.  Replace ``<DASHBOARD_NODE_NAME>>`` with your Cyb3rhq dashboard node name, the same used in ``config.yml`` to create the certificates. For example, ``dashboard``. Then, move the certificates to their corresponding location.

    .. code-block:: console

        # NODE_NAME=<DASHBOARD_NODE_NAME>>

    .. code-block:: console

        # mkdir /etc/cyb3rhq-dashboard/certs
        # mv -n cyb3rhq-install-files/$NODE_NAME.pem /etc/cyb3rhq-dashboard/certs/dashboard.pem
        # mv -n cyb3rhq-install-files/$NODE_NAME-key.pem /etc/cyb3rhq-dashboard/certs/dashboard-key.pem
        # cp cyb3rhq-install-files/root-ca.pem /etc/cyb3rhq-dashboard/certs/
        # chmod 500 /etc/cyb3rhq-dashboard/certs
        # chmod 400 /etc/cyb3rhq-dashboard/certs/*
        # chown -R cyb3rhq-dashboard:cyb3rhq-dashboard /etc/cyb3rhq-dashboard/certs

#. Edit the ``/etc/cyb3rhq-dashboard/opensearch_dashboards.yml`` file and replace the following values:

   #. ``server.host``: This setting specifies the host of the back end server. To allow remote users to connect, set the value to the IP address or DNS name of the Cyb3rhq dashboard.  The value ``0.0.0.0`` will accept all the available IP addresses of the host.

   #. ``opensearch.hosts``: The URLs of the Cyb3rhq indexer instances to use for all your queries. The Cyb3rhq dashboard can be configured to connect to multiple Cyb3rhq indexer nodes in the same cluster. The addresses of the nodes can be separated by commas. For example,  ``["https://10.0.0.2:9200", "https://10.0.0.3:9200","https://10.0.0.4:9200"]``

        .. code-block:: yaml
          :emphasize-lines: 1,3

             server.host: 0.0.0.0
             server.port: 443
             opensearch.hosts: https://127.0.0.1:9200
             opensearch.ssl.verificationMode: certificate

#.  Enable and start the Cyb3rhq dashboard.

    .. include:: /_templates/installations/dashboard/enable_dashboard.rst

#. Edit the file ``/usr/share/cyb3rhq-dashboard/data/cyb3rhq/config/cyb3rhq.yml`` and replace the ``url`` value with the IP address or hostname of the Cyb3rhq server master node.

            .. code-block:: yaml
               :emphasize-lines: 3
            
               hosts:
                 - default:
                     url: https://<CYB3RHQ_SERVER_IP_ADDRESS>
                     port: 55000
                     username: cyb3rhq-wui
                     password: cyb3rhq-wui
                     run_as: false

#.  Run the following command to verify the Cyb3rhq dashboard service is active.

    .. include:: /_templates/installations/cyb3rhq/common/check_cyb3rhq_dashboard.rst    

#.  Access the web interface. 

    -   URL: *https://<CYB3RHQ_DASHBOARD_IP_ADDRESS>*
    -   **Username**: admin
    -   **Password**: admin

Upon the first access to the Cyb3rhq dashboard, the browser shows a warning message stating that the certificate was not issued by a trusted authority. An exception can be added in the advanced options of the web browser or, for increased security, the ``root-ca.pem`` file previously generated can be imported to the certificate manager of the browser. Alternatively, a certificate from a trusted authority can be configured.

Securing your Cyb3rhq installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


You have now installed and configured all the Cyb3rhq central components. We recommend changing the default credentials to protect your infrastructure from possible attacks. 

Select your deployment type and follow the instructions to change the default passwords for both the Cyb3rhq API and the Cyb3rhq indexer users.


.. tabs::

   .. group-tab:: All-in-one deployment

      #. Use the Cyb3rhq passwords tool to change all the internal users passwords.
      
         .. code-block:: console

            # /usr/share/cyb3rhq-indexer/plugins/opensearch-security/tools/cyb3rhq-passwords-tool.sh --api --change-all --admin-user cyb3rhq --admin-password cyb3rhq

         .. code-block:: console
            :class: output
       
            INFO: The password for user admin is yWOzmNA.?Aoc+rQfDBcF71KZp?1xd7IO
            INFO: The password for user kibanaserver is nUa+66zY.eDF*2rRl5GKdgLxvgYQA+wo
            INFO: The password for user kibanaro is 0jHq.4i*VAgclnqFiXvZ5gtQq1D5LCcL
            INFO: The password for user logstash is hWW6U45rPoCT?oR.r.Baw2qaWz2iH8Ml
            INFO: The password for user readall is PNt5K+FpKDMO2TlxJ6Opb2D0mYl*I7FQ
            INFO: The password for user snapshotrestore is +GGz2noZZr2qVUK7xbtqjUup049tvLq.
            WARNING: Cyb3rhq indexer passwords changed. Remember to update the password in the Cyb3rhq dashboard and Filebeat nodes if necessary, and restart the services.
            INFO: The password for Cyb3rhq API user cyb3rhq is JYWz5Zdb3Yq+uOzOPyUU4oat0n60VmWI
            INFO: The password for Cyb3rhq API user cyb3rhq-wui is +fLddaCiZePxh24*?jC0nyNmgMGCKE+2
            INFO: Updated cyb3rhq-wui user password in cyb3rhq dashboard. Remember to restart the service.
       
    
   .. group-tab:: Distributed deployment

      #. On `any Cyb3rhq indexer node`, use the Cyb3rhq passwords tool to change the passwords of the Cyb3rhq indexer users. 

         .. code-block:: console
  
            # /usr/share/cyb3rhq-indexer/plugins/opensearch-security/tools/cyb3rhq-passwords-tool.sh --change-all
  
         .. code-block:: console
            :class: output

            INFO: Cyb3rhq API admin credentials not provided, Cyb3rhq API passwords not changed.
            INFO: The password for user admin is wcAny.XUwOVWHFy.+7tW9l8gUW1L8N3j
            INFO: The password for user kibanaserver is qy6fBrNOI4fD9yR9.Oj03?pihN6Ejfpp
            INFO: The password for user kibanaro is Nj*sSXSxwntrx3O7m8ehrgdHkxCc0dna
            INFO: The password for user logstash is nQg1Qw0nIQFZXUJc8r8+zHVrkelch33h
            INFO: The password for user readall is s0iWAei?RXObSDdibBfzSgXdhZCD9kH4
            INFO: The password for user snapshotrestore is Mb2EHw8SIc1d.oz.nM?dHiPBGk7s?UZB
            WARNING: Cyb3rhq indexer passwords changed. Remember to update the password in the Cyb3rhq dashboard and Filebeat nodes if necessary, and restart the services.



      #. On your `Cyb3rhq server master node`, change the default password of the admin users: `cyb3rhq` and `cyb3rhq-wui`. Note that the commands below use 127.0.0.1, set your Cyb3rhq manager IP address if necessary.

         #. Get an authorization TOKEN. 

            .. code-block:: console

               # TOKEN=$(curl -u cyb3rhq-wui:cyb3rhq-wui -k -X GET "https://127.0.0.1:55000/security/user/authenticate?raw=true")

         #. Change the `cyb3rhq` user credentials (ID 1). Select a password between 8 and 64 characters long, it should contain at least one uppercase and one lowercase letter, a number, and a symbol. See :api-ref:`PUT /security/users/{user_id} <operation/api.controllers.security_controller.update_user>` to learn more. 

            .. code-block:: console

               curl -k -X PUT "https://127.0.0.1:55000/security/users/1" -H "Authorization: Bearer $TOKEN" -H 'Content-Type: application/json' -d'
               {
                 "password": "SuperS3cretPassword!"
               }'

            .. code-block:: console
               :class: output

               {"data": {"affected_items": [{"id": 1, "username": "cyb3rhq", "allow_run_as": true, "roles": [1]}], "total_affected_items": 1, "total_failed_items": 0, "failed_items": []}, "message": "User was successfully updated", "error": 0}  
    
        
         #. Change the `cyb3rhq-wui` user credentials (ID 2). 

            .. code-block:: console

               curl -k -X PUT "https://127.0.0.1:55000/security/users/2" -H "Authorization: Bearer $TOKEN" -H 'Content-Type: application/json' -d'
               {
                 "password": "SuperS3cretPassword!"
               }'

            .. code-block:: console
               :class: output   

               {"data": {"affected_items": [{"id": 2, "username": "cyb3rhq-wui", "allow_run_as": true, "roles": [1]}], "total_affected_items": 1, "total_failed_items": 0, "failed_items": []}, "message": "User was successfully updated", "error": 0}
   
         See the :doc:`Securing the Cyb3rhq API </user-manual/api/securing-api>` section for additional security configurations. 

         .. note:: Remember to store these passwords securely. 


      #. On `all your Cyb3rhq server nodes`, run the following command to update the `admin` password in the Filebeat keystore. Replace ``<ADMIN_PASSWORD>`` with the random password generated in the first step.
      
         .. code-block:: console

            # echo <ADMIN_PASSWORD> | filebeat keystore add password --stdin --force

      #. Restart Filebeat to apply the change.

         .. include:: /_templates/common/restart_filebeat.rst

         .. note:: Repeat steps 3 and 4 on `every Cyb3rhq server node`.
       
      #. On your `Cyb3rhq dashboard node`, run the following command to update the `kibanaserver` password in the Cyb3rhq dashboard keystore. Replace ``<KIBANASERVER_PASSWORD>`` with the random password generated in the first step.

         .. code-block:: console

            # echo <KIBANASERVER_PASSWORD> | /usr/share/cyb3rhq-dashboard/bin/opensearch-dashboards-keystore --allow-root add -f --stdin opensearch.password

      #. Update the ``/usr/share/cyb3rhq-dashboard/data/cyb3rhq/config/cyb3rhq.yml`` configuration file with the new `cyb3rhq-wui` password generated in the second step.

         .. code-block:: yaml
            :emphasize-lines: 6
           
            hosts:
              - default:
                  url: https://127.0.0.1
                  port: 55000
                  username: cyb3rhq-wui
                  password: "<cyb3rhq-wui-password>"
                  run_as: false

      #. Restart the Cyb3rhq dashboard to apply the changes.

         .. include:: /_templates/common/restart_dashboard.rst


Next steps
^^^^^^^^^^

Once the Cyb3rhq environment is ready, Cyb3rhq agents can be installed on every endpoint to be monitored. To install the Cyb3rhq agents and start monitoring the endpoints, see the :doc:`Cyb3rhq agent </installation-guide/cyb3rhq-agent/index>` installation section. If you need to install them offline, you can check the appropriate agent package to download for your monitored system in the :ref:`Cyb3rhq agent packages list <cyb3rhq_agent_packages_list>` section.

To uninstall all the Cyb3rhq central components, see the :doc:`/installation-guide/uninstalling-cyb3rhq/central-components` section.
