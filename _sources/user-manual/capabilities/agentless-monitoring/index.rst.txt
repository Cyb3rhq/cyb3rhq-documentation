.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: The Cyb3rhq agentless monitoring capability uses the SSH protocol to collect and transfer events to the Cyb3rhq server. Learn more about it in this section.

.. _manual_agentless:

Agentless monitoring
====================

The Cyb3rhq server analyzes the data it receives from the Cyb3rhq agents to monitor, detect, and trigger alerts for security events and incidents on endpoints. However, some endpoints may have limitations that prevent the installation of the Cyb3rhq agent. Cyb3rhq solves this problem by using the agentless monitoring capability.

Agentless monitoring refers to a type of endpoint monitoring that does not require the installation of an agent or software. This approach uses existing protocols to access and gather information from the monitored endpoint. 

The Cyb3rhq agentless monitoring capability uses the SSH (Secure Shell) protocol to collect and transfer events from endpoints to the Cyb3rhq server. The supported platforms include routers, firewalls, switches, and Linux/BSD systems. It allows endpoints with software installation restrictions to meet security and compliance requirements.

.. topic:: Contents

    .. toctree::
        :maxdepth: 2

        how-it-works
        connection
        agentless-configuration
        visualization
        use-cases
