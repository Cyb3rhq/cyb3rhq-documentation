Install Cyb3rhq components using the assistant
--------------------------------------------

Install and configure the different Cyb3rhq components with the aid of the Cyb3rhq installation assistant. 

.. note:: You need root user privileges to run all the commands described below.

Please, make sure that a copy of the ``cyb3rhq-install-files.tar`` and ``cyb3rhq-offline.tar.gz`` files, created during the initial configuration step, is placed in your working directory.

Installing the Cyb3rhq indexer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Install and configure the Cyb3rhq indexer nodes. 


#. Run the assistant with the ``--offline-installation`` to perform an offline installation. Use the option ``--cyb3rhq-indexer`` and the node name to install and configure the Cyb3rhq indexer. The node name must be the same one used in ``config.yml`` for the initial configuration, for example, ``node-1``.
      
   .. code-block:: console

      # bash cyb3rhq-install.sh --offline-installation --cyb3rhq-indexer node-1 

   Repeat this step for every Cyb3rhq indexer node in your cluster. Then proceed with initializing your single-node or multi-node cluster in the next step.

#. Run the Cyb3rhq installation assistant with option ``--start-cluster`` on any Cyb3rhq indexer node to load the new certificates information and start the cluster. 

   .. code-block:: console
 
      # bash cyb3rhq-install.sh --offline-installation --start-cluster
 
   .. note:: You only have to initialize the cluster `once`, there is no need to run this command on every node. 

Testing the cluster installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Run the following command to get the *admin* password:

   .. code-block:: console

      # tar -axf cyb3rhq-install-files.tar cyb3rhq-install-files/cyb3rhq-passwords.txt -O | grep -P "\'admin\'" -A 1

#. Run the following command to confirm that the installation is successful. Replace ``<ADMIN_PASSWORD>`` with the password gotten from the output of the previous command. Replace ``<CYB3RHQ_INDEXER_IP>`` with the configured Cyb3rhq indexer IP address:

   .. code-block:: console

      # curl -k -u admin:<ADMIN_PASSWORD> https://<CYB3RHQ_INDEXER_IP>:9200

   .. code-block:: none
      :class: output

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

#. Replace ``<CYB3RHQ_INDEXER_IP>`` and ``<ADMIN_PASSWORD>``, and run the following command to check if the cluster is working correctly:

   .. code-block:: console

      # curl -k -u admin:<ADMIN_PASSWORD> https://<CYB3RHQ_INDEXER_IP>:9200/_cat/nodes?v

Installing the Cyb3rhq server
^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Run the assistant with the ``--offline-installation`` to perform an offline installation. Use the option ``--cyb3rhq-server`` followed by the node name to install the Cyb3rhq server. The node name must be the same one used in ``config.yml`` for the initial configuration, for example, ``cyb3rhq-1``.
 
   .. code-block:: console
  
      # bash cyb3rhq-install.sh --offline-installation --cyb3rhq-server cyb3rhq-1

Your Cyb3rhq server is now successfully installed. 

-  If you want a Cyb3rhq server multi-node cluster, repeat this step on every Cyb3rhq server node.
-  If you want a Cyb3rhq server single-node cluster, everything is set and you can proceed directly with the next stage.

Installing the Cyb3rhq dashboard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Run the assistant with the ``--offline-installation`` to perform an offline installation. Use the option ``--cyb3rhq-dashboard`` and the node name to install and configure the Cyb3rhq dashboard. The node name must be the same one used in ``config.yml`` for the initial configuration, for example, ``dashboard``.
   
   .. code-block:: console

      # bash cyb3rhq-install.sh --offline-installation --cyb3rhq-dashboard dashboard

   The default Cyb3rhq web user interface port is 443, used by the Cyb3rhq dashboard. You can change this port using the optional parameter ``-p|--port <port_number>``. Some recommended ports are 8443, 8444, 8080, 8888, and 9000.

   Once the assistant finishes the installation, the output shows the access credentials and a message that confirms that the installation was successful.

   .. code-block:: none
      :emphasize-lines: 3,4          
    
      INFO: --- Summary ---
      INFO: You can access the web interface https://<cyb3rhq-dashboard-ip>
         User: admin
         Password: <ADMIN_PASSWORD>

      INFO: Installation finished.

   You now have installed and configured Cyb3rhq. All passwords generated by the Cyb3rhq installation assistant can be found in the ``cyb3rhq-passwords.txt`` file inside the ``cyb3rhq-install-files.tar`` archive. To print them, run the following command:
   
   .. code-block:: console
   
      # tar -O -xvf cyb3rhq-install-files.tar cyb3rhq-install-files/cyb3rhq-passwords.txt

#. Access the Cyb3rhq web interface with your credentials. 

   -  URL: *https://<cyb3rhq-dashboard-ip>*
   -  **Username**: *admin*
   -  **Password**: *<ADMIN_PASSWORD>*

   When you access the Cyb3rhq dashboard for the first time, the browser shows a warning message stating that the certificate was not issued by a trusted authority. An exception can be added in the advanced options of the web browser. For increased security, the ``root-ca.pem`` file previously generated can be imported to the certificate manager of the browser instead. Alternatively, a certificate from a trusted authority can be configured. 
