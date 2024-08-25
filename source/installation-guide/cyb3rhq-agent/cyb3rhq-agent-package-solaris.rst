.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Learn more about how to successfully install the Cyb3rhq agent on Solaris systems in this section of our Installation Guide.

Installing Cyb3rhq agents on Solaris endpoints
============================================

The agent runs on the host you want to monitor and communicates with the Cyb3rhq manager, sending data in near real-time through an encrypted and authenticated channel.

To start the installation process, select your architecture: i386 or SPARC.

.. note:: You need root user privileges to run all the commands described below.

.. tabs::

   .. group-tab:: i386

      Select your Solaris Intel version.

      .. tabs::

         .. group-tab:: Solaris 10

            #. Download the `Cyb3rhq agent for Solaris 10 i386 <https://packages.cyb3rhq.com/4.x/solaris/i386/10/cyb3rhq-agent_v|CYB3RHQ_CURRENT_SOLARIS10_i386|-sol10-i386.pkg>`_ package.

            #. Install the Cyb3rhq agent.

               .. code-block:: console

                  # pkgadd -d cyb3rhq-agent_v|CYB3RHQ_CURRENT_SOLARIS10_i386|-sol10-i386.pkg cyb3rhq-agent

         .. group-tab:: Solaris 11

            #. Download the `Cyb3rhq agent for Solaris 11 i386 <https://packages.cyb3rhq.com/4.x/solaris/i386/11/cyb3rhq-agent_v|CYB3RHQ_CURRENT_SOLARIS11_i386|-sol11-i386.p5p>`_.

            #. Install the Cyb3rhq agent.

               .. code-block:: console

                  # pkg install -g cyb3rhq-agent_v|CYB3RHQ_CURRENT_SOLARIS11_i386|-sol11-i386.p5p cyb3rhq-agent

            If the Solaris 11 zone where you want to install the package has child zones, create a repository to install the Cyb3rhq agent:

            .. code-block:: console

               # pkg set-publisher -g cyb3rhq-agent_v|CYB3RHQ_CURRENT_SOLARIS11_i386|-sol11-i386.p5p cyb3rhq && pkg install --accept cyb3rhq-agent && pkg unset-publisher cyb3rhq

   .. group-tab:: SPARC

      Select your Solaris SPARC version.

      .. tabs::

         .. group-tab:: Solaris 10

            #. Download the `Cyb3rhq agent for Solaris 10 SPARC <https://packages.cyb3rhq.com/4.x/solaris/sparc/10/cyb3rhq-agent_v|CYB3RHQ_CURRENT_SOLARIS10_SPARC|-sol10-sparc.pkg>`_ package.

            #. Install the Cyb3rhq agent.

               .. code-block:: console

                  # pkgadd -d cyb3rhq-agent_v|CYB3RHQ_CURRENT_SOLARIS10_SPARC|-sol10-sparc.pkg cyb3rhq-agent

         .. group-tab:: Solaris 11

            #. Download the `Cyb3rhq agent for Solaris 11 SPARC <https://packages.cyb3rhq.com/4.x/solaris/sparc/11/cyb3rhq-agent_v|CYB3RHQ_CURRENT_SOLARIS11_SPARC|-sol11-sparc.p5p>`_.

            #. Install the Cyb3rhq agent.

               .. code-block:: console

                  # pkg install -g cyb3rhq-agent_v|CYB3RHQ_CURRENT_SOLARIS11_SPARC|-sol11-sparc.p5p cyb3rhq-agent

            If the Solaris 11 zone where you want to install the package has child zones, create a repository to install the Cyb3rhq agent:

            .. code-block:: console

               # pkg set-publisher -g cyb3rhq-agent_v|CYB3RHQ_CURRENT_SOLARIS11_SPARC|-sol11-sparc.p5p cyb3rhq && pkg install --accept cyb3rhq-agent && pkg unset-publisher cyb3rhq

The installation process is now complete, and the Cyb3rhq agent is successfully installed on your Solaris endpoint. The next step is to register and configure the agent to communicate with the Cyb3rhq server. To perform this action, see the :doc:`Cyb3rhq agent enrollment </user-manual/agent/agent-enrollment/index>` section.
