.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: The Cyb3rhq agent lifecycle includes the Installation and enrollment, Agent connection states, and Removal stages. Learn more in this section of the documentation.

Cyb3rhq agent life cycle
======================

The Cyb3rhq agent lifecycle refers to the various stages a Cyb3rhq agent goes through from its initial installation on an endpoint to its removal from the Cyb3rhq platform. It includes the following stages:

.. contents::
   :local:
   :depth: 1
   :backlinks: none

Installation and enrollment
---------------------------

The first step involves installing the Cyb3rhq agent on the endpoint to be monitored. Once the Cyb3rhq agent is installed, it must be enrolled in the Cyb3rhq manager to establish communication. Refer to :doc:`Cyb3rhq agent enrollment <index>`.

.. _agent-status-cycle:

Agent connection states
-----------------------

After successful enrollment, the Cyb3rhq manager stores information about the Cyb3rhq agent and its connection status until it is deleted by a user.

In this phase, there are four different connection states that a Cyb3rhq agent may be in at any given time, as shown in the image below:

.. thumbnail:: /images/manual/agent/agent-connection-states.png
  :title: Agent connections states
  :alt: Agent connections states
  :align: center
  :width: 80%

-  **Never connected**: The Cyb3rhq agent has been enrolled but has not yet connected to the Cyb3rhq manager.
-  **Pending**: The authentication process has not been completed because the Cyb3rhq manager received a request for connection from the Cyb3rhq agent but has not received anything else. The Cyb3rhq agent will be in this state one time in its life cycle after each startup. If the Cyb3rhq agent persists in this state, it may indicate a connectivity issue.
-  **Active**: The Cyb3rhq agent has successfully connected and can now communicate with the Cyb3rhq manager.
-  **Disconnected**: The Cyb3rhq manager will consider the agent disconnected if it does not receive any ``keep alive`` messages within :ref:`agents_disconnection_time <reference_agents_disconnection_time>` (the default time is ``10m``).

Removal
-------

The life cycle of the Cyb3rhq agent comes to an end when it is removed from the Cyb3rhq manager. This can be done through the :doc:`Cyb3rhq server API <../agent-management/remove-agents/restful-api-remove>` or :doc:`command line <../agent-management/remove-agents/remove>`. 