.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Cyb3rhq provides different approaches to connecting your private network securely. Learn more about how to connect agents without Internet here.

.. _cloud_your_environment_agents_without_internet:

Agents without Internet access
===============================

Even if an agent does not have Internet access, Cyb3rhq provides different approaches to securely connect your private network to your environment:

- `Using a forwarding proxy`_

- `Using AWS Private Link`_

Using a forwarding proxy
------------------------

It is possible to access your environment using an NGINX forwarding proxy.

.. thumbnail:: ../../images/cloud-service/nginx-scheme.png
    :title: Using an NGINX forwarding proxy
    :alt: Using an NGINX forwarding proxy
    :align: center
    :width: 80%


To achieve this configuration, follow these steps:

1. Deploy a new instance in a public subnet with internet access.

2. Install NGINX on your instance following the `NGINX documentation <https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/>`_.

3. Configure NGINX.

   #. Add the following lines to the HTTP section in your NGINX configuration, located in the ``/etc/nginx/nginx.conf`` file. This configuration enables Nginx to extract and use the real client IP address from the X-Forwarded-For header and sets restrictions on which real IP addresses are accepted as valid.


      .. code-block::

         http{
         ...
         real_ip_header X-Forwarded-For;
         set_real_ip_from nginx_ip;
            }

   #. Add the following block to the end of the NGINX configuration file ``/etc/nginx/nginx.conf`` and replace ``<CLOUD_ID>`` with the Cloud ID of your environment. This configuration enables stream proxying, where incoming traffic on specific ports is forwarded to the corresponding upstream servers (master or mycluster). This is based on the port numbers, 1515 and 1514 specified in the listen directive.

      .. code-block::

	 stream {
	   upstream master {
	     server <CLOUD_ID>.cloud.cyb3rhq.com:1515;
	   }
	   upstream mycluster {
	     server <CLOUD_ID>.cloud.cyb3rhq.com:1514;
	     }
	   server {
	     listen nginx_ip:1515;
	     proxy_pass master;
	   }
	   server {
	     listen nginx_ip:1514;
	     proxy_pass mycluster;
	   }
	 }
	
   #. Run the command to restart NGINX: ``systemctl restart nginx``.

   #. Enroll your agent with the IP address of the NGINX instance. To learn more about registering agents, see the :ref:`Enroll agents <cloud_register_agents>` section.

      Example:

      .. code-block::

         CYB3RHQ_MANAGER_IP=<NGINX_IP> CYB3RHQ_PROTOCOL="tcp" \
         CYB3RHQ_PASSWORD="<PASSWORD>" \
         yum install cyb3rhq-agent|CYB3RHQ_AGENT_RPM_PKG_INSTALL|
         
      Replace <PASSWORD> with your Cyb3rhq server enrollment password.

Using AWS Private Link
----------------------

In case your agents are located in AWS, you can access our Cyb3rhq Cloud service securely by keeping your network traffic within the AWS network. For that purpose, we use AWS Private Link.

1. Log in to the `Cyb3rhq Cloud Console <https://console.cloud.cyb3rhq.com/>`_.
   
2. Go to the **Help** section to contact the Cyb3rhq team requesting your VPC endpoint service name. It has this format:

   ``com.amazonaws.vpce.<region>.vpce-svc-<aws-service-id>``

3. Select your endpoints in AWS:
   
   #. Navigate to your AWS Console.

   #. Select **VPC**.

   #. Select **Endpoints**.

4. Create a new endpoint pointing to the endpoint service you requested from the Cyb3rhq team. Keep in mind that the endpoint must be located in the same AWS Region as the endpoint service. For more information on AWS PrivateLink and VPC endpoints, see the  `AWS documentation <https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint>`_.

5. After the endpoint is created, Cyb3rhq approves the connection and sends a notification when it is ready to use.

6. You can now enroll your Cyb3rhq agent but replace the *CYB3RHQ_MANAGER_IP* value with the endpoint's DNS (``vpce-<aws-endpoint-id>.vpce-svc-<aws-service-id>.<region>.vpce.amazonaws.com``).

   If the agents are located in a different region than your endpoint, use VPC Peerings to connect them to the endpoint service.

   Example:

   .. code-block::

      CYB3RHQ_MANAGER_IP=vpce-<aws-endpoint-id>.vpce-svc-<aws-service-id>.<region>.vpce.amazonaws.com CYB3RHQ_PROTOCOL="tcp" \
      CYB3RHQ_PASSWORD="<PASSWORD>>" \
      yum install cyb3rhq-agent|CYB3RHQ_AGENT_RPM_PKG_INSTALL|

   In this example, make sure to replace ``<PASSWORD>`` with your actual password.
