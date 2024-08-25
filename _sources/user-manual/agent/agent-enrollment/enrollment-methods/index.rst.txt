.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: This section describes the two methods available for enrolling Cyb3rhq agents. Learn more in this section of the documentation.

Enrollment methods
==================

This section describes the two methods available for enrolling Cyb3rhq agents. It guides in configuring the necessary settings to ensure a successful connection of the Cyb3rhq agent to the Cyb3rhq server.

-  :doc:`Enrollment via agent configuration <via-agent-configuration/index>`: Once the IP address or FQDN (Fully Qualified Domain Name) of the Cyb3rhq server has been set, the Cyb3rhq agent can request the client key and import it automatically. This is the recommended enrollment method.
-  :doc:`Enrollment via Cyb3rhq server API <via-manager-API/index>`: The user requests the client key from the Cyb3rhq server API and then manually imports it to the Cyb3rhq agent.

.. toctree::
   :hidden:
   :maxdepth: 1

   via-agent-configuration/index
   via-manager-API/index
