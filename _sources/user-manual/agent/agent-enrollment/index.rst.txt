.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Cyb3rhq agent enrollment is the process of registering a Cyb3rhq agent to a Cyb3rhq manager. Learn more in this section of the documentation.

Cyb3rhq agent enrollment
======================

Cyb3rhq agent enrollment is the process of registering a Cyb3rhq agent to a Cyb3rhq manager. This enrollment allows the Cyb3rhq agents to communicate securely with the Cyb3rhq manager and become authorized members of the Cyb3rhq security platform.

The Cyb3rhq agent enrollment process allows:

-  The Cyb3rhq manager to enroll Cyb3rhq agents and generate unique client keys for them.
-  The use of the client key to encrypt communication between the Cyb3rhq agent and the Cyb3rhq manager.
-  The validation of the identity of the Cyb3rhq agents communicating with the Cyb3rhq manager.
-  The Cyb3rhq agent to collect security information from the monitored endpoint and send it to the Cyb3rhq manager for analysis.

.. note::

   When following our :ref:`installation guide <installing_the_cyb3rhq_agent>`, we recommend you use environment variables to configure the Cyb3rhq agent automatically. This allows the Cyb3rhq agent to enroll and connect to the Cyb3rhq manager.

Learn about the different enrollment options and additional information needed for Cyb3rhq agent enrollment in the sections below.

.. toctree::
   :maxdepth: 1

   requirements
   agent-life-cycle
   enrollment-methods/index
   security-options/index
   deployment-variables/index
   troubleshooting
