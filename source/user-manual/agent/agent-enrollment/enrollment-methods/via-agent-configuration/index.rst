.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: With this option, the Cyb3rhq agent is automatically enrolled. Learn more in this section of the documentation.

Enrollment via agent configuration
==================================

With this option, the Cyb3rhq agent is automatically enrolled after you have configured the Cyb3rhq manager IP address or FQDN (Fully Qualified Domain Name). When using :doc:`additional security options <../../security-options/index>`, you might need to configure other settings.

You can configure the Cyb3rhq manager IP address or FQDN (Fully Qualified Domain Name) in one of two ways on the Cyb3rhq agent:

-  Using environment variables during the Cyb3rhq agent installation process. The guide to this process can be found :doc:`here </installation-guide/cyb3rhq-agent/index>`.
-  Manually configuring the Cyb3rhq manager IP address or FQDN (Fully Qualified Domain Name) in the Cyb3rhq agent configuration file.

Enrollment with additional security options involves the use of passwords for enrollment authorization or certificates for identity validation of the Cyb3rhq agent and Cyb3rhq manager. See the :doc:`additional security options <../../security-options/index>` section for guidance on enrolling a Cyb3rhq agent to a Cyb3rhq manager with additional security options enabled.

The steps below show how to enroll the Cyb3rhq agent for different operating systems:

.. toctree::
   :maxdepth: 1

   linux-endpoint
   windows-endpoint
   macos-endpoint
