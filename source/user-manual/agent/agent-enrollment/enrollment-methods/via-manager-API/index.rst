.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: The Cyb3rhq server API allows manual control over the enrollment process. Learn more in this section of the documentation.

Enrollment via Cyb3rhq server API
===============================

The Cyb3rhq server API allows users to make an agent enrollment request to the Cyb3rhq manager. This request returns a unique client key for the Cyb3rhq agent, which must be manually imported to the Cyb3rhq agent. This is useful for users who need manual control over the enrollment process.

How it works
------------

The flow of a Cyb3rhq agent being enrolled via API is as follows:

#. The user sends an API request with the Cyb3rhq server API credentials to generate an authorization token (a JSON Web Token). This action can be performed from any authorized endpoint. 
#. The user sends an API request with the authorization token to the Cyb3rhq manager. This request enrolls the Cyb3rhq agent and gets the agent key.
#. On the Cyb3rhq agent endpoint, the user imports the agent key to the Cyb3rhq agent.
#. The user configures the Cyb3rhq manager IP address or FQDN (Fully Qualified Domain Name) on the Cyb3rhq agent.
#. The user restarts the Cyb3rhq agent, establishing the connection to the Cyb3rhq manager.

In this section of the guide, you will find the following information:

.. toctree::
   :maxdepth: 1

   requesting-the-key
   importing-the-key