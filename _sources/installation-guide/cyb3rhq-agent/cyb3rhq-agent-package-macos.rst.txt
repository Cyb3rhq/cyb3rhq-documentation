.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Learn more about how to successfully install the Cyb3rhq agent on macOS systems in this section of our Installation Guide.

Installing Cyb3rhq agents on macOS endpoints
==========================================

The agent runs on the endpoint you want to monitor and communicates with the Cyb3rhq server, sending data in near real-time through an encrypted and authenticated.

.. note:: You need root user privileges to run all the commands described below.

.. |macOS_intel_64| replace:: `cyb3rhq-agent-|CYB3RHQ_CURRENT_OSX|-|CYB3RHQ_REVISION_OSX|.intel64.pkg <https://packages.wazuh.com/|CYB3RHQ_CURRENT_MAJOR_OSX|/macos/cyb3rhq-agent-|CYB3RHQ_CURRENT_OSX|-|CYB3RHQ_REVISION_OSX|.intel64.pkg>`__
.. |macOS_arm64| replace:: `cyb3rhq-agent-|CYB3RHQ_CURRENT_OSX|-|CYB3RHQ_REVISION_OSX|.arm64.pkg <https://packages.wazuh.com/|CYB3RHQ_CURRENT_MAJOR_OSX|/macos/cyb3rhq-agent-|CYB3RHQ_CURRENT_OSX|-|CYB3RHQ_REVISION_OSX|.arm64.pkg>`__


#. To start the installation process, download the Cyb3rhq agent according to your architecture:

   - **Intel**: |macOS_intel_64|. Suitable for macOS Sierra and later.

   - **Apple silicon**: |macOS_arm64|. Suitable for macOS Big Sur and later.

#. Select the installation method you want to follow: Command line interface (CLI) or graphical user interface (GUI).

   .. tabs::

      .. group-tab:: CLI
      
         #. To deploy the Cyb3rhq agent on your endpoint, choose your architecture, edit the ``CYB3RHQ_MANAGER`` variable to contain your Cyb3rhq manager IP address or hostname, and run the following command. 

            .. tabs::
            
               .. group-tab:: Intel

                  .. code-block:: console
                  
                     # echo "CYB3RHQ_MANAGER='10.0.0.2'" > /tmp/cyb3rhq_envs && installer -pkg cyb3rhq-agent-|CYB3RHQ_CURRENT_OSX|-|CYB3RHQ_REVISION_OSX|.intel64.pkg -target /
   

               .. group-tab:: Apple silicon

                  .. versionadded:: 4.5.1

                  .. code-block:: console
                  
                     # echo "CYB3RHQ_MANAGER='10.0.0.2'" > /tmp/cyb3rhq_envs && installer -pkg cyb3rhq-agent-|CYB3RHQ_CURRENT_OSX|-|CYB3RHQ_REVISION_OSX|.arm64.pkg -target /


               For additional deployment options such as agent name, agent group, and registration password, see the :doc:`Deployment variables for macOS </user-manual/agent/agent-enrollment/deployment-variables/deployment-variables-macos>` section.
               
               .. note:: Alternatively, if you want to install an agent without registering it, omit the deployment variables. To learn more about the different registration methods, see the :doc:`Cyb3rhq agent enrollment </user-manual/agent/agent-enrollment/index>` section.

         #. To complete the installation process, start the Cyb3rhq agent.

            .. code-block:: console

               # launchctl load /Library/LaunchDaemons/com.cyb3rhq.agent.plist


         The installation process is now complete, and the Cyb3rhq agent is successfully deployed and running on your macOS endpoint.

      
      .. group-tab:: GUI

         #. To install the Cyb3rhq agent on your system, run the downloaded file and follow the steps in the installation wizard. If you are not sure how to answer some of the prompts, use the default answers.

            .. thumbnail:: ../../images/installation/macos-agent.png
               :align: center
               :title: macOS agent installer
               :alt: macOS agent installer
               
         #. To complete the installation process, start the Cyb3rhq agent.

            .. code-block:: console

               # launchctl load /Library/LaunchDaemons/com.cyb3rhq.agent.plist

         The installation process is now complete, and the Cyb3rhq agent is successfully installed on your macOS endpoint. The next step is to register and configure the agent to communicate with the Cyb3rhq server. To perform this action, see the :doc:`Cyb3rhq agent enrollment </user-manual/agent/agent-enrollment/index>` section.  

By default, all agent files are stored in ``/Library/Ossec/`` after the installation.
