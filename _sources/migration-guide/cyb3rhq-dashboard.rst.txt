.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Follow this guide to migrate from Open Distro for Elasticsearch Kibana to the Cyb3rhq dashboard.
  
.. _migration_guide_dashboard:

Migrating to the Cyb3rhq dashboard
================================

Follow this guide to migrate from Open Distro for Elasticsearch Kibana 1.13 to the Cyb3rhq dashboard. These instructions are intended for a standard Cyb3rhq installation, you may need to make some changes to adapt them to your environment.

To guarantee a correct operation of Cyb3rhq, make sure to also migrate from Open Distro for Elasticsearch to the Cyb3rhq indexer. To learn more, see the :doc:`Migrating to the Cyb3rhq indexer </migration-guide/cyb3rhq-indexer>` documentation. 

.. note:: You need root user privileges to run all the commands described below.

#. Stop the Kibana service. 

   .. tabs::
   
    .. group-tab:: Systemd
   
     .. code-block:: console
   
      # systemctl stop kibana
   
    .. group-tab:: SysV init
   
     .. code-block:: console
   
      # service kibana stop  

#. Add the Cyb3rhq repository. You can skip this step if the repository is already present and enabled on your server.

    .. tabs::


      .. group-tab:: Yum


        .. include:: /_templates/installations/common/yum/add-repository.rst



      .. group-tab:: APT


        .. include:: /_templates/installations/common/deb/add-repository.rst



#. Install the Cyb3rhq dashboard package.

   .. tabs::

      .. group-tab:: Yum

         .. code-block:: console

            # yum -y install cyb3rhq-dashboard|CYB3RHQ_DASHBOARD_RPM_PKG_INSTALL|

      .. group-tab:: APT

         .. code-block:: console
              
            # apt-get -y install cyb3rhq-dashboard|CYB3RHQ_DASHBOARD_DEB_PKG_INSTALL|

   .. note::

      Make sure that your Cyb3rhq manager is updated to the latest version. To learn more, see :ref:`upgrading_cyb3rhq_server`. 

#. Create the ``/etc/cyb3rhq-dashboard/certs`` directory, copy your old certificates to the new location and change ownership and permissions.    

   .. code-block:: console

     # mkdir /etc/cyb3rhq-dashboard/certs
     # cp /etc/kibana/certs/kibana.pem /etc/cyb3rhq-dashboard/certs/dashboard.pem
     # cp /etc/kibana/certs/kibana-key.pem /etc/cyb3rhq-dashboard/certs/dashboard-key.pem
     # cp /etc/kibana/certs/root-ca.pem /etc/cyb3rhq-dashboard/certs/root-ca.pem
     # chmod 500 /etc/cyb3rhq-dashboard/certs
     # chmod 400 /etc/cyb3rhq-dashboard/certs/*
     # chown -R cyb3rhq-dashboard:cyb3rhq-dashboard /etc/cyb3rhq-dashboard/certs

#. Port your settings from ``/etc/kibana/kibana.yml`` to the ``/etc/cyb3rhq-dashboard/opensearch_dashboards.yml`` file. You can omit the ``opensearch.username`` and the ``opensearch.password`` settings as they are now stored in the Cyb3rhq dashboard keystore. 

    .. code-block:: yaml
      :emphasize-lines: 1,3

      server.host: 0.0.0.0
      server.port: 443
      opensearch.hosts: https://localhost:9200
      opensearch.ssl.verificationMode: certificate
      #opensearch.username:
      #opensearch.password:
      opensearch.requestHeadersAllowlist: ["securitytenant","Authorization"]
      opensearch_security.multitenancy.enabled: false
      opensearch_security.readonly_mode.roles: ["kibana_read_only"]
      server.ssl.enabled: true
      server.ssl.key: "/etc/cyb3rhq-dashboard/certs/dashboard-key.pem"
      server.ssl.certificate: "/etc/cyb3rhq-dashboard/certs/dashboard.pem"
      opensearch.ssl.certificateAuthorities: ["/etc/cyb3rhq-dashboard/certs/root-ca.pem"]
      uiSettings.overrides.defaultRoute: /app/wz-home

#. Add the password of the ``kibanaserver`` user to the Cyb3rhq dashboard keystore.  Execute the command below and follow the instructions. You may find your old password in the ``/etc/kibana/kibana.yml`` configuration file. 

    .. code-block:: console

      /usr/share/cyb3rhq-dashboard/bin/opensearch-dashboards-keystore --allow-root add opensearch.password    
   
    **Optional action** -  To change the default user, run the following command. You will need to change the password accordingly. 

    .. code-block:: console

      /usr/share/cyb3rhq-dashboard/bin/opensearch-dashboards-keystore --allow-root add opensearch.username 


#. Enable and start the Cyb3rhq dashboard service.

      .. include:: /_templates/installations/dashboard/enable_dashboard.rst            


#.  Port your settings from ``/usr/share/kibana/data/cyb3rhq/config/cyb3rhq.yml`` to ``/usr/share/cyb3rhq-dashboard/data/cyb3rhq/config/cyb3rhq.yml``. It is recommended to copy the content from ``/usr/share/kibana/data/cyb3rhq/downloads/`` as well.

#. Access the Cyb3rhq web interface at ``https://<dashboard_ip>`` with your credentials and make sure that everything is working as expected. 

#. Uninstall Kibana.

    .. tabs::
    
    
      .. group-tab:: Yum
    
    
        .. include:: /_templates/installations/elastic/yum/uninstall_kibana.rst
    
    
    
      .. group-tab:: APT
    
    
        .. include:: /_templates/installations/elastic/deb/uninstall_kibana.rst
