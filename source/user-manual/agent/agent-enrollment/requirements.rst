.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Learn about the requirements to ensure the Cyb3rhq agent enrollment is successful.

Requirements
============

The following requirements have to be in place to ensure the Cyb3rhq agent enrollment is successful:

-  An installed and running Cyb3rhq manager.
-  An installed and running Cyb3rhq agent on the endpoint that the user needs to enroll.
-  Outbound connectivity from the Cyb3rhq agent to the Cyb3rhq manager services. The following ports are configurable:

   -  1514/TCP for agent communication.
   -  1515/TCP for enrollment via automatic agent request.
   -  55000/TCP for enrollment via Cyb3rhq server API.

.. note::

   Instructions for installing and enrolling agents can be found in the Cyb3rhq dashboard. Go to **Server Management** > **Endpoints Summary**, and click on **Deploy new agent**.
