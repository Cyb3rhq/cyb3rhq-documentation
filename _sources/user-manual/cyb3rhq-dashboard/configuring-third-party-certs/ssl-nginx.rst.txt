.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: You can use third-party certificates, instead of self-signed, in the Cyb3rhq dashboard. Learn more about it in this section of the Cyb3rhq documentation. 

.. _ssl-nginx:

Configuring SSL certificates on the Cyb3rhq dashboard using NGINX
===============================================================

NGINX is an open source software for web serving, reverse proxying, caching, load balancing, and media streaming. It provides improved performance optimization during SSL decryption, better utilization, and complete end-to-end encryption of the Cyb3rhq dashboard server. NGINX can be installed directly on the endpoint hosting the Cyb3rhq dashboard or on a separate endpoint outside of the Cyb3rhq cluster. However, for this use case, NGINX is installed on the Cyb3rhq dashboard node.

Install and configure the Let’s Encrypt SSL certificate using NGINX on a Cyb3rhq dashboard by following the step-by-step instructions below.

Setting up NGINX as Reverse proxy 
---------------------------------

Installing the NGINX software on the Cyb3rhq dashboard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Install NGINX:

   .. tabs::

      .. group-tab:: Yum

         .. code-block:: console

            # yum install epel-release
            # yum install nginx

      .. group-tab:: APT

         .. code-block:: console

            # apt-get update
            # apt-get install nginx

#. Start NGINX and verify the status is active:

   .. code-block:: console

      # systemctl start nginx
      # systemctl status nginx

#. Open ports 80 (HTTP) and 443 (HTTPS):

   .. tabs::

      .. group-tab:: Yum

         .. code-block:: console

            # systemctl start firewalld
            # firewall-cmd --permanent --add-port=443/tcp
            # firewall-cmd --permanent --add-port=80/tcp

      .. group-tab:: APT

         .. code-block:: console

            # ufw allow 443
            # ufw allow 80 

Configure the proxy and the certificates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Install snap: 

   .. tabs::

      .. group-tab:: Yum

         .. code-block:: console

            # yum install epel-release
            # yum upgrade
            # yum install snapd
            # systemctl enable --now snapd.socket
            # ln -s /var/lib/snapd/snap /snap

      .. group-tab:: APT

         .. code-block:: console

            # apt-get update
            # apt-get install snap
            # snap install core; snap refresh core

#. Install certbot:

   .. tabs::

      .. group-tab:: Yum

         .. code-block:: console

            # yum remove certbot
            # snap install --classic certbot

      .. group-tab:: APT

         .. code-block:: console

            # apt remove certbot 
            # snap install --classic certbot

#. Configure a symbolic link to the certbot directory:

   .. code-block:: console

      # ln -s /snap/bin/certbot /usr/bin/certbot

#. Edit the ``/etc/cyb3rhq-dashboard/opensearch_dashboards.yml`` file and change the default dashboard port from ``443`` to another available port number:
      
   .. code-block:: yaml
      :emphasize-lines: 3

      server.host: 0.0.0.0
      opensearch.hosts: https://127.0.0.1:9200
      server.port: <PORT_NUMBER>
      opensearch.ssl.verificationMode: certificate
      # opensearch.username: kibanaserver
      # opensearch.password: kibanaserver
      opensearch.requestHeadersWhitelist: ["securitytenant","Authorization"]
      opensearch_security.multitenancy.enabled: false
      opensearch_security.readonly_mode.roles: ["kibana_read_only"]
      server.ssl.enabled: true
      server.ssl.key: "/etc/cyb3rhq-dashboard/certs/cyb3rhq-dashboard-key.pem"
      server.ssl.certificate: "/etc/cyb3rhq-dashboard/certs/cyb3rhq-dashboard.pem"
      opensearch.ssl.certificateAuthorities: ["/etc/cyb3rhq-dashboard/certs/root-ca.pem"]
      uiSettings.overrides.defaultRoute: /app/wz-home
      opensearch_security.cookie.secure: true

#. Navigate to the ``/etc/nginx/conf.d`` directory and create a ``cyb3rhq.conf`` file for the certificate installation:

   .. code-block:: console

      # unlink /etc/nginx/sites-enabled/default
      # cd /etc/nginx/conf.d
      # touch cyb3rhq.conf

#. Edit ``cyb3rhq.conf`` and add the following configuration.

   .. code-block:: console

      server {
         listen 80 default_server;

         server_name <YOUR_DOMAIN_NAME>;

         location / {
            proxy_pass https://<CYB3RHQ_DASHBOARD_IP_ADDRESS>:<PORT_NUMBER>;
            proxy_set_header Host $host;
         }
      }

   Replace the following:

   - ``<YOUR_DOMAIN_NAME>`` with your domain name.
   - ``<CYB3RHQ_DASHBOARD_IP_ADDRESS>`` with your Cyb3rhq dashboard IP address.
   - ``<PORT_NUMBER>`` with your new port number.

#. Restart the Cyb3rhq dashboard and the Cyb3rhq server
 
   .. code-block:: console

      # systemctl restart cyb3rhq-dashboard
      # systemctl restart cyb3rhq-manager

#. Use certbot to generate an SSL certificate:

   .. code-block:: console

      # certbot --nginx -d <YOUR_DOMAIN_NAME>


#. Check that NGINX is properly configured and verify that you have the same configuration in the ``/etc/nginx/conf.d/cyb3rhq.conf`` file with the sample below: 

   .. code-block:: console

      server {

         server_name <YOUR_DOMAIN_NAME>;

         location / {
            proxy_pass https://<CYB3RHQ_DASHBOARD_IP_ADDRESS>:<PORT_NUMBER>;
            proxy_set_header Host $host;
         }

         listen 443 ssl; # managed by Certbot
         ssl_certificate /etc/letsencrypt/live/<YOUR_DOMAIN_NAME>/fullchain.pem; # managed by Certbot
         ssl_certificate_key /etc/letsencrypt/live/<YOUR_DOMAIN_NAME>/privkey.pem; # managed by Certbot
         include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
         ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

      }
      server {
         if ($host = <YOUR_DOMAIN_NAME>) {
            return 301 https://$host$request_uri;
         } # managed by Certbot


         listen 80 default_server;

         server_name <YOUR_DOMAIN_NAME>;
         return 404; # managed by Certbot


      }


#. Restart the NGINX service:

   .. include:: /_templates/common/restart_nginx.rst

#. Access the Cyb3rhq dashboard via the configured domain name.

      .. thumbnail:: /images/configuring-third-party-certs/cyb3rhq-dashboard.png
         :title: Cyb3rhq dashboard
         :align: center
         :width: 80%

The NGINX server has been configured and the Let’s Encrypt certificate installation is active on the Cyb3rhq dashboard. You can proceed to access it by using the configured domain name.
