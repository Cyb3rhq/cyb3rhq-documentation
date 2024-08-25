.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Learn how to install Cyb3rhq dashboard, a flexible and intuitive web interface for mining and visualizing the events and archives. 

.. _cyb3rhq_dashboard_step_by_step:

Installing the Cyb3rhq dashboard step by step
===========================================

Install and configure the Cyb3rhq dashboard following step-by-step instructions. The Cyb3rhq dashboard is a web interface for mining and visualizing the Cyb3rhq server alerts and archived events.

.. note:: You need root user privileges to run all the commands described below.

Cyb3rhq dashboard installation
----------------------------

Installing package dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: /_templates/installations/dashboard/install-dependencies.rst

Adding the Cyb3rhq repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^

  .. note::
    If you are installing the Cyb3rhq dashboard on the same host as the Cyb3rhq indexer or the Cyb3rhq server, you may skip these steps as you may have added the Cyb3rhq repository already.

  .. tabs::
  
    .. group-tab:: Yum
  
  
      .. include:: /_templates/installations/common/yum/add-repository.rst
  
  
  
    .. group-tab:: APT
  
  
      .. include:: /_templates/installations/common/deb/add-repository.rst
  
  
  

Installing the Cyb3rhq dashboard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Install the Cyb3rhq dashboard package.

   .. tabs::

      .. group-tab:: Yum

         .. code-block:: console

            # yum -y install cyb3rhq-dashboard|CYB3RHQ_DASHBOARD_RPM_PKG_INSTALL|

      .. group-tab:: APT

         .. code-block:: console
              
            # apt-get -y install cyb3rhq-dashboard|CYB3RHQ_DASHBOARD_DEB_PKG_INSTALL|

Configuring the Cyb3rhq dashboard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  #. Edit the ``/etc/cyb3rhq-dashboard/opensearch_dashboards.yml`` file and replace the following values:

     #. ``server.host``: This setting specifies the host of the Cyb3rhq dashboard server. To allow remote users to connect, set the value to the IP address or DNS name of the Cyb3rhq dashboard server. The value ``0.0.0.0`` will accept all the available IP addresses of the host.

     #. ``opensearch.hosts``: The URLs of the Cyb3rhq indexer instances to use for all your queries. The Cyb3rhq dashboard can be configured to connect to multiple Cyb3rhq indexer nodes in the same cluster. The addresses of the nodes can be separated by commas. For example,  ``["https://10.0.0.2:9200", "https://10.0.0.3:9200","https://10.0.0.4:9200"]``

        .. code-block:: yaml
          :emphasize-lines: 1,3

             server.host: 0.0.0.0
             server.port: 443
             opensearch.hosts: https://localhost:9200
             opensearch.ssl.verificationMode: certificate




Deploying certificates
^^^^^^^^^^^^^^^^^^^^^^

  .. note::
    Make sure that a copy of the ``cyb3rhq-certificates.tar`` file, created during the initial configuration step, is placed in your working directory.

  .. include:: /_templates/installations/dashboard/deploy_certificates.rst


Starting the Cyb3rhq dashboard service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  #. Enable and start the Cyb3rhq dashboard service.

      .. include:: /_templates/installations/dashboard/enable_dashboard.rst

  #. Edit the ``/usr/share/cyb3rhq-dashboard/data/cyb3rhq/config/cyb3rhq.yml`` file and replace the ``url`` value with the IP address or hostname of the Cyb3rhq server master node.
   
      .. code-block:: yaml
         :emphasize-lines: 3
      
         hosts:
            - default:
               url: https://<CYB3RHQ_SERVER_IP_ADDRESS>
               port: 55000
               username: cyb3rhq-wui
               password: cyb3rhq-wui
               run_as: false


  #. Access the Cyb3rhq web interface with your credentials.

      - URL: *https://<CYB3RHQ_DASHBOARD_IP_ADDRESS>*
      - **Username**: *admin*
      - **Password**: *admin*

    When you access the Cyb3rhq dashboard for the first time, the browser shows a warning message stating that the certificate was not issued by a trusted authority. An exception can be added in the advanced options of the web browser. For increased security, the ``root-ca.pem``  file previously generated can be imported to the certificate manager of the browser. Alternatively, a certificate from a trusted authority can be configured. 


Securing your Cyb3rhq installation
--------------------------------


You have now installed and configured all the Cyb3rhq central components. We recommend changing the default credentials to protect your infrastructure from possible attacks. 

Select your deployment type and follow the instructions to change the default passwords for both the Cyb3rhq API and the Cyb3rhq indexer users.


.. tabs::

   .. group-tab:: All-in-one deployment

      #. Use the Cyb3rhq passwords tool to change all the internal users' passwords.
      
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

      #. On your `Cyb3rhq server master node`, download the Cyb3rhq passwords tool and use it to change the passwords of the Cyb3rhq API users.

         .. code-block:: console
  
            # curl -sO https://packages.wazuh.com/|CYB3RHQ_CURRENT_MINOR|/cyb3rhq-passwords-tool.sh
            # bash cyb3rhq-passwords-tool.sh --api --change-all --admin-user cyb3rhq --admin-password cyb3rhq
  
         .. code-block:: console
            :class: output

            INFO: The password for Cyb3rhq API user cyb3rhq is ivLOfmj7.jL6*7Ev?UJoFjrkGy9t6Je.
            INFO: The password for Cyb3rhq API user cyb3rhq-wui is fL+f?sFRPEv5pYRE559rqy9b6G4Z5pVi

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
----------

All the Cyb3rhq central components are successfully installed and secured.

.. raw:: html

  <div class="link-boxes-group layout-3" data-step="4">
    <div class="steps-line">
      <div class="steps-number past-step">1</div>
      <div class="steps-number past-step">2</div>
      <div class="steps-number past-step">3</div>
    </div>
    <div class="link-boxes-item past-step">
      <a class="link-boxes-link" href="../cyb3rhq-indexer/index.html">
        <p class="link-boxes-label">Install the Cyb3rhq indexer</p>

.. image:: ../../images/installation/Indexer-Circle.png
     :align: center
     :height: 61px

.. raw:: html

      </a>
    </div>
  
    <div class="link-boxes-item past-step">
      <a class="link-boxes-link" href="../cyb3rhq-server/index.html">
        <p class="link-boxes-label">Install the Cyb3rhq server</p>

.. image:: ../../images/installation/Server-Circle.png
     :align: center
     :height: 61px

.. raw:: html

      </a>
    </div>
  
    <div class="link-boxes-item past-step">
      <a class="link-boxes-link" href="index.html">
        <p class="link-boxes-label">Install the Cyb3rhq dashboard</p>

.. image:: ../../images/installation/Dashboard-Circle.png
     :align: center
     :height: 61px
     
.. raw:: html

      </a>
    </div>
  </div>


The Cyb3rhq environment is now ready, and you can proceed with installing the Cyb3rhq agent on the endpoints to be monitored. To perform this action, see the :doc:`Cyb3rhq agent </installation-guide/cyb3rhq-agent/index>` section.

If you want to uninstall the Cyb3rhq dashboard, see :ref:`uninstall_dashboard`.
