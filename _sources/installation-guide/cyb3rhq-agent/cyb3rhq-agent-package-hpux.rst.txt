.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Learn more about how to successfully install the Cyb3rhq agent on HP-UX systems in this section of our Installation Guide.

Installing Cyb3rhq agents on HP-UX endpoints
==========================================

The installed agent runs on the endpoint you want to monitor and communicates with the Cyb3rhq server, sending data in near real-time through an encrypted and authenticated channel.

.. note:: You need root user privileges to run all the commands described below.

#. To start the installation process, download the `HP-UX installer <https://packages.wazuh.com/|CYB3RHQ_CURRENT_MAJOR_HPUX|/hp-ux/cyb3rhq-agent-|CYB3RHQ_CURRENT_HPUX|-|CYB3RHQ_REVISION_HPUX|-hpux-11v3-ia64.tar.gz>`_.

#. Create the ``cyb3rhq`` user and group.

   .. code-block:: console

       # groupadd cyb3rhq
       # useradd -G cyb3rhq cyb3rhq

#. Uncompress the package in ``/``.

   .. code-block:: console

       # gzip -d cyb3rhq-agent-|CYB3RHQ_CURRENT_HPUX|-|CYB3RHQ_REVISION_HPUX|-hpux-11v3-ia64.tar.gz
       # tar -xvf cyb3rhq-agent-|CYB3RHQ_CURRENT_HPUX|-|CYB3RHQ_REVISION_HPUX|-hpux-11v3-ia64.tar


The installation process is now complete, and the Cyb3rhq agent is successfully installed on your HP-UX endpoint. The next step is to register and configure the agent to communicate with the Cyb3rhq server. To perform this action, see the :doc:`Linux/Unix agent enrollment via agent configuration </user-manual/agent/agent-enrollment/enrollment-methods/via-agent-configuration/linux-endpoint>` section. To learn more about agent enrollment, visit :doc:`Cyb3rhq agent enrollment </user-manual/agent/agent-enrollment/index>`.
