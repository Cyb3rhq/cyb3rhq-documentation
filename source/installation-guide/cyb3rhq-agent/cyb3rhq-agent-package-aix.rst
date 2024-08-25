.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Learn how to deploy the Cyb3rhq agent on AIX using deployment variables that facilitate the task of installing, registering, and configuring the agent.

Deploying Cyb3rhq agents on AIX endpoints
=======================================

The agent runs on the endpoint you want to monitor and communicates with the Cyb3rhq server, sending data in near real-time through an encrypted and authenticated channel.

The deployment of a Cyb3rhq agent on an AIX system uses deployment variables that facilitate the task of installing, registering, and configuring the agent.

.. note::

   You need root user privileges to run all the commands described below.

   Required dependencies:
      * bash

#. To start the deployment process, download the `AIX installer <https://packages.cyb3rhq.com/|CYB3RHQ_CURRENT_MAJOR_AIX|/aix/cyb3rhq-agent-|CYB3RHQ_CURRENT_AIX|-|CYB3RHQ_REVISION_AIX|.aix.ppc.rpm>`_.

#. To deploy the Cyb3rhq agent to your endpoint, edit the ``CYB3RHQ_MANAGER`` variable so that it contains the Cyb3rhq manager IP address or hostname.

   .. code-block:: console

      # CYB3RHQ_MANAGER="10.0.0.2" rpm -ivh cyb3rhq-agent-|CYB3RHQ_CURRENT_AIX|-|CYB3RHQ_REVISION_AIX|.aix.ppc.rpm

   For additional deployment options such as agent name, agent group, and registration password, see :doc:`Deployment variables for AIX </user-manual/agent/agent-enrollment/deployment-variables/deployment-variables-aix>` section.
   
   .. note:: Alternatively, if you want to install an agent without registering it, omit the deployment variables.  To learn more about the different registration methods, see the :doc:`Cyb3rhq agent enrollment </user-manual/agent/agent-enrollment/index>` section.

#. To complete the installation process, start the Cyb3rhq agent.

    .. code-block:: console

      # /var/ossec/bin/cyb3rhq-control start


The deployment process is now complete, and the Cyb3rhq agent is successfully running on your AIX endpoint.
