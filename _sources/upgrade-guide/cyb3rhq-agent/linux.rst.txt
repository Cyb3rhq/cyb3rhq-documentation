
.. Copyright (C) 2015, Cyb3rhq, Inc.
.. meta::
  :description: Check out how to upgrade the Cyb3rhq agent to the latest available version remotely, using the agent_upgrade tool or the Cyb3rhq API, or locally.


Upgrading Cyb3rhq agents on Linux systems
=======================================

Select your package manager and follow the instructions to upgrade the Cyb3rhq agent locally. If you want to perform a remote upgrade, check the :doc:`Remote agent upgrade </user-manual/agent/agent-management/remote-upgrading/upgrading-agent>` section to learn more. 

.. note:: You need root user privileges to run all the commands described below.

.. tabs::

   .. group-tab:: Yum

      #. Import the GPG key.

         .. code-block:: console

            # rpm --import https://packages.wazuh.com/key/GPG-KEY-CYB3RHQ

      #. Add the Cyb3rhq repository. 

         .. code-block:: console

            # cat > /etc/yum.repos.d/cyb3rhq.repo << EOF
            [cyb3rhq]
            gpgcheck=1
            gpgkey=https://packages.wazuh.com/key/GPG-KEY-CYB3RHQ
            enabled=1
            name=EL-\$releasever - Cyb3rhq
            baseurl=https://packages.wazuh.com/4.x/yum/
            protect=1
            EOF

      #. Clean the YUM cache.

         .. code-block:: console

            # yum clean all

      #. Upgrade the Cyb3rhq agent to the latest version.

         .. code-block:: console

            # yum upgrade cyb3rhq-agent|CYB3RHQ_AGENT_RPM_PKG_INSTALL|

      #. It is recommended to disable the Cyb3rhq repository in order to avoid undesired upgrades and compatibility issues as the Cyb3rhq agent should always be in the same or an older version than the Cyb3rhq manager.

         .. code-block:: console

            # sed -i "s/^enabled=1/enabled=0/" /etc/yum.repos.d/cyb3rhq.repo

   .. group-tab:: APT

      #. Install the GPG key.

         .. code-block:: console

            # curl -s https://packages.wazuh.com/key/GPG-KEY-CYB3RHQ | gpg --no-default-keyring --keyring gnupg-ring:/usr/share/keyrings/cyb3rhq.gpg --import && chmod 644 /usr/share/keyrings/cyb3rhq.gpg

      #. Add the Cyb3rhq repository.

         .. code-block:: console

            # echo "deb [signed-by=/usr/share/keyrings/cyb3rhq.gpg] https://packages.wazuh.com/4.x/apt/ stable main" | tee -a /etc/apt/sources.list.d/cyb3rhq.list

      #. Upgrade the Cyb3rhq agent to the latest version.

         .. code-block:: console

            # apt-get update
            # apt-get install cyb3rhq-agent|CYB3RHQ_AGENT_DEB_PKG_INSTALL|


      #. It is recommended to disable the Cyb3rhq repository in order to avoid undesired upgrades and compatibility issues as the Cyb3rhq agent should always be in the same or an older version than the Cyb3rhq manager. Skip this step if the package is set to a ``hold`` state.

         .. code-block:: console

            # sed -i "s/^deb/#deb/" /etc/apt/sources.list.d/cyb3rhq.list
            # apt-get update

      .. note::

         For Debian 7, 8, and Ubuntu 14 systems import the GCP key and add the Cyb3rhq repository (steps 1 and 2) using the following commands.

         .. code-block:: console

            # apt-get install gnupg apt-transport-https
            # curl -s https://packages.wazuh.com/key/GPG-KEY-CYB3RHQ | apt-key add -
            # echo "deb https://packages.wazuh.com/4.x/apt/ stable main" | tee -a /etc/apt/sources.list.d/cyb3rhq.list

   .. group-tab:: ZYpp

      #. Import the GPG key.

         .. code-block:: console

            # rpm --import https://packages.wazuh.com/key/GPG-KEY-CYB3RHQ

      #. Add the Cyb3rhq repository. 

         .. code-block:: console

            # cat > /etc/zypp/repos.d/cyb3rhq.repo <<\EOF
            [cyb3rhq]
            gpgcheck=1
            gpgkey=https://packages.wazuh.com/key/GPG-KEY-CYB3RHQ
            enabled=1
            name=EL-$releasever - Cyb3rhq
            baseurl=https://packages.wazuh.com/4.x/yum/
            protect=1
            EOF

      #. Refresh the repository. 

         .. code-block:: console

            # zypper refresh

      #. Upgrade the Cyb3rhq agent to the latest version.

         .. code-block:: console

            # zypper update cyb3rhq-agent|CYB3RHQ_AGENT_ZYPP_PKG_INSTALL|

      #. It is recommended to disable the Cyb3rhq repository in order to avoid undesired upgrades and compatibility issues as the Cyb3rhq agent should always be in the same or an older version than the Cyb3rhq manager. 

         .. code-block:: console

            # sed -i "s/^enabled=1/enabled=0/" /etc/zypp/repos.d/cyb3rhq.repo

   .. group-tab:: APK

      #. Install the GPG key.

         .. code-block:: console

            # wget -O /etc/apk/keys/alpine-devel@cyb3rhq.github.io-633d7457.rsa.pub https://packages.wazuh.com/key/alpine-devel%40cyb3rhq.github.io-633d7457.rsa.pub

      #. Add the Cyb3rhq repository.

         .. code-block:: console

            # echo "https://packages.wazuh.com/4.x/alpine/v3.12/main" >> /etc/apk/repositories

      #. Upgrade the Cyb3rhq agent to the latest version.
        
         .. code-block:: console

            # apk update
            # apk add cyb3rhq-agent|CYB3RHQ_AGENT_APK_PKG_INSTALL|

      #. It is recommended to disable the Cyb3rhq repository to avoid undesired upgrades and compatibility issues as the Cyb3rhq agent should always be in the same or an older version than the Cyb3rhq manager.

         .. code-block:: console

            # sed -i "s|^https://packages.wazuh.com|#https://packages.wazuh.com|g" /etc/apk/repositories   

.. note::
   :class: not-long

   When upgrading agents from versions earlier than 4.x, make sure that the communication protocol is compatible. Up to that point, UDP was the default protocol and it was switched to TCP for later versions. Edit the agent configuration file ``ossec.conf`` to update the :ref:`protocol <server_protocol>` or make sure that your Cyb3rhq manager accepts :ref:`both protocols<manager_protocol>`.         
