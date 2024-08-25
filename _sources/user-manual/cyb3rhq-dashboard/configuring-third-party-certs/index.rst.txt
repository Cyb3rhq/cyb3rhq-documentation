.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: You can use third-party certificates, instead of self-signed, in the Cyb3rhq dashboard. Learn more about it in this section of the Cyb3rhq documentation.

.. _configuring-third-party-certs:

Configuring third-party SSL certificates
========================================

In the Cyb3rhq dashboard installation guide, self-signed SSL certificates generated during the Cyb3rhq indexer installation were configured for the Cyb3rhq dashboard.

You can use third-party certificates instead of self-signed ones in the Cyb3rhq dashboard. This guide includes instructions for creating and configuring Let's Encrypt certificates. Let's Encrypt is a nonprofit Certificate Authority providing free SSL/TLS certificates to millions of websites.

To generate this type of certificate, you need a fully qualified domain name (FQDN). Let's Encrypt verifies if you have control over the domain.

You can install the SSL certificate directly on the Cyb3rhq dashboard. Alternatively, you can install it using NGINX, a third-party open source proxy software, to offload the SSL decryption processing from the Cyb3rhq dashboard.

Choose a preferred method to start configuring the SSL/TLS certificate for the Cyb3rhq dashboard:

- :doc:`Configuring SSL certificates directly on the Cyb3rhq dashboard <ssl>`
- :doc:`Configuring SSL certificates on the Cyb3rhq dashboard using NGINX <ssl-nginx>`

    .. toctree::
        :hidden:
        :maxdepth: 1

        ssl
        ssl-nginx
        
