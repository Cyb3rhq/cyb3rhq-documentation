.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Learn how to deploy the Cyb3rhq agent on Linux with deployment variables that facilitate the task of installing, registering, and configuring the agent. 

Deploying Cyb3rhq agents on Linux endpoints
=========================================

The agent runs on the host you want to monitor and communicates with the Cyb3rhq server, sending data in near real-time through an encrypted and authenticated channel. 

The deployment of a Cyb3rhq agent on a Linux system uses deployment variables that facilitate the task of installing, registering, and configuring the agent. Alternatively, if you want to download the Cyb3rhq agent package directly, see the :doc:`packages list </installation-guide/packages-list>` section. 

.. note:: You need root user privileges to run all the commands described below.

Add the Cyb3rhq repository
-------------------------

Add the Cyb3rhq repository to download the official packages. 

.. tabs::


  .. group-tab:: Yum


    .. include:: ../../_templates/installations/cyb3rhq/yum/add_repository.rst



  .. group-tab:: APT


    .. include:: ../../_templates/installations/cyb3rhq/deb/add_repository.rst



  .. group-tab:: ZYpp


    .. include:: ../../_templates/installations/cyb3rhq/zypp/add_repository.rst



  .. group-tab:: APK


    .. include:: ../../_templates/installations/cyb3rhq/apk/add_repository.rst



Deploy a Cyb3rhq agent
--------------------

#. To deploy the Cyb3rhq agent on your endpoint, select your package manager and edit the ``CYB3RHQ_MANAGER`` variable to contain your Cyb3rhq manager IP address or hostname.   

   .. tabs::
   
      .. group-tab:: Yum
   
         .. code-block:: console
          
            # CYB3RHQ_MANAGER="10.0.0.2" yum install cyb3rhq-agent|CYB3RHQ_AGENT_RPM_PKG_INSTALL|

         For additional deployment options such as agent name, agent group, and registration password, see the :doc:`Deployment variables for Linux </user-manual/agent/agent-enrollment/deployment-variables/deployment-variables-linux>` section.

          .. note:: Alternatively, if you want to install an agent without registering it, omit the deployment variables. To learn more about the different registration methods, see the :doc:`Cyb3rhq agent enrollment </user-manual/agent/agent-enrollment/index>` section. 
   
      .. group-tab:: APT
   
         .. code-block:: console
          
            # CYB3RHQ_MANAGER="10.0.0.2" apt-get install cyb3rhq-agent|CYB3RHQ_AGENT_DEB_PKG_INSTALL|

         For additional deployment options such as agent name, agent group, and registration password, see the :doc:`Deployment variables for Linux </user-manual/agent/agent-enrollment/deployment-variables/deployment-variables-linux>` section.

         .. note:: Alternatively, if you want to install an agent without registering it, omit the deployment variables. To learn more about the different registration methods, see the :doc:`Cyb3rhq agent enrollment </user-manual/agent/agent-enrollment/index>` section. 
   
      .. group-tab:: ZYpp
   
         .. code-block:: console
          
            # CYB3RHQ_MANAGER="10.0.0.2" zypper install cyb3rhq-agent|CYB3RHQ_AGENT_ZYPP_PKG_INSTALL|

         For additional deployment options such as agent name, agent group, and registration password, see the :doc:`Deployment variables for Linux </user-manual/agent/agent-enrollment/deployment-variables/deployment-variables-linux>` section.

         .. note:: Alternatively, if you want to install an agent without registering it, omit the deployment variables. To learn more about the different registration methods, see the :doc:`Cyb3rhq agent enrollment </user-manual/agent/agent-enrollment/index>` section. 

      .. group-tab:: APK
   
         #. Install the Cyb3rhq agent:

            .. code-block:: console
            
               # apk add cyb3rhq-agent|CYB3RHQ_AGENT_APK_PKG_INSTALL|

         #. Edit the agent configuration to add the address of your Cyb3rhq manager:

            .. code-block:: console
            
               # export CYB3RHQ_MANAGER="10.0.0.2" && sed -i "s|MANAGER_IP|$CYB3RHQ_MANAGER|g" /var/ossec/etc/ossec.conf

            For more customization options, like agent name or group, see the :doc:`Linux/Unix endpoint configuration </user-manual/agent/agent-enrollment/enrollment-methods/via-agent-configuration/linux-endpoint>` page. For more security options, check the :doc:`Additional security options </user-manual/agent/agent-enrollment/security-options/index>` section. 

#. Enable and start the Cyb3rhq agent service.

   .. include:: ../../_templates/installations/cyb3rhq/common/enable_cyb3rhq_agent_service.rst

The deployment process is now complete, and the Cyb3rhq agent is successfully running on your Linux system. 

- **Recommended action** -  Disable Cyb3rhq updates

  Compatibility between the Cyb3rhq agent and the Cyb3rhq manager is guaranteed when the Cyb3rhq manager version is later than or equal to that of the Cyb3rhq agent. Therefore, we recommend disabling the Cyb3rhq repository to prevent accidental upgrades. To do so, use the following command:

    .. tabs::


      .. group-tab:: Yum


        .. include:: ../../_templates/installations/cyb3rhq/yum/disabling_repository.rst



      .. group-tab:: APT


        .. include:: ../../_templates/installations/cyb3rhq/deb/disabling_repository.rst



      .. group-tab:: ZYpp

        .. include:: ../../_templates/installations/cyb3rhq/zypp/disabling_repository.rst



      .. group-tab:: APK

        .. include:: ../../_templates/installations/cyb3rhq/apk/disabling_repository.rst
