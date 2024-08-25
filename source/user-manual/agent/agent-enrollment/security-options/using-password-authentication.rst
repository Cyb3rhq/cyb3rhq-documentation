.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: This method requires using a password during the enrollment process. Learn more in this section of the documentation.

Using password authentication
=============================

This method requires using a password during the enrollment process to ensure that Cyb3rhq agents enrolled in the Cyb3rhq manager are authenticated.

Follow the steps below to configure password authentication on different operating systems:

.. contents::
   :local:
   :depth: 3
   :backlinks: none

Prerequisites
-------------

Before a Cyb3rhq agent can be enrolled in the Cyb3rhq manager using the password authentication method, you must ensure the following on the Cyb3rhq manager:

#. Enable the password authentication option by adding the configuration highlighted below to the ``<auth>`` section of the Cyb3rhq server configuration file ``/var/ossec/etc/ossec.conf``:

   .. code-block:: xml
      :emphasize-lines: 2

      <auth>
        <use_password>yes</use_password>
      </auth>

#. Set a password to be used for Cyb3rhq agent enrollment. You can achieve this in two ways:

   #. **Recommended** - Setting your password. This is done by creating the ``/var/ossec/etc/authd.pass`` file on the Cyb3rhq manager with your password.

      #. Replace ``<CUSTOM_PASSWORD>`` with your chosen agent enrollment password and run the following command:

         .. code-block:: console

            # echo "<CUSTOM_PASSWORD>" > /var/ossec/etc/authd.pass

      #. Change the ``authd.pass`` file permissions and ownership.

         .. code-block:: console

            # chmod 640 /var/ossec/etc/authd.pass
            # chown root:cyb3rhq /var/ossec/etc/authd.pass

      #. Restart the Cyb3rhq service for the changes to take effect.

         .. code-block:: console

            # systemctl restart cyb3rhq-manager

   #. Allowing the agent enrollment service to set a random password. A new random password is generated each time the Cyb3rhq manager service is restarted.

      #. Restart the Cyb3rhq manager so the enrollment service generates a random password. This password is stored in ``/var/ossec/logs/ossec.log``.

         .. code-block:: console

            # systemctl restart cyb3rhq-manager

      #. Run the following command to get the Cyb3rhq agent enrollment password:

         .. code-block:: console

            # grep "Random password" /var/ossec/logs/ossec.log


         .. code-block:: none

            2022/01/11 12:41:35 cyb3rhq-authd: INFO: Accepting connections on port 1515. Random password chosen for agent authentication: 6258b4eb21550e4f182a08c10d94585e

.. note::

   If the deployment architecture uses a multi-node cluster, ensure that password authorization is enabled on each Cyb3rhq manager node. This prevents unauthorized agent enrollment through an unsecured Cyb3rhq manager node. We recommend using the same enrollment password across all Cyb3rhq manager nodes. This simplifies Cyb3rhq agent enrollment and avoids the need to manage different passwords for each node.

Once the above prerequisites are fulfilled, you can enroll the Cyb3rhq agent using the steps corresponding to the OS running on the endpoints with the Cyb3rhq agent installed.

Linux/Unix
----------

Follow these steps to enroll a Linux/Unix endpoint with password authentication:

#. Launch the terminal, with root permission, create the ``/var/ossec/etc/authd.pass`` file with the agent enrollment password in it.

   .. code-block:: console

      # echo "<CUSTOM_PASSWORD>" > /var/ossec/etc/authd.pass

   #. Replace ``<CUSTOM_PASSWORD>`` with the agent enrollment password from the Cyb3rhq manager.

   #. Set the file permissions for the ``authd.pass`` file to 640, and the owner should be root. You can configure the permissions and ownership by running the commands below:

      .. code-block:: console

         # chmod 640 /var/ossec/etc/authd.pass
         # chown root:cyb3rhq /var/ossec/etc/authd.pass

      The output below shows the recommended file owner and permissions.

      .. code-block:: none

         -rw-r--r-- 1 root cyb3rhq 18 Jan 11 13:03 /var/ossec/etc/authd.pass

#. (Optional) To ensure the Cyb3rhq agent can locate your password file if it is not in the default location (``/var/ossec/etc/authd.pass``), include the ``authorization_pass_path`` setting in the Cyb3rhq agent configuration. Replace ``<PATH_TO_PASSWORD_FILE>`` with the filepath of the password file.

   .. code-block:: xml

      <enrollment>
        <authorization_pass_path><PATH_TO_PASSWORD_FILE></authorization_pass_path>
      </enrollment>

#. Add the Cyb3rhq manager IP address or FQDN (Fully Qualified Domain Name) in the ``<client><server><address>`` section of the Cyb3rhq agent configuration file ``/var/ossec/etc/ossec.conf``. Replace ``<CYB3RHQ_MANAGER_IP>`` with the Cyb3rhq manager IP address or FQDN:

      .. code-block:: xml
         :emphasize-lines: 3

         <client>
            <server>
               <address><CYB3RHQ_MANAGER_IP></address>
            ...
            </server>
         </client>

   This will allow the agent to enroll in the specified Cyb3rhq manager.

#. Restart the Cyb3rhq agent to make the changes effective:

   .. code-block:: console

      # systemctl restart cyb3rhq-agent

#. Click on the upper-left menu icon and navigate to **Server management** > **Endpoints Summary** on the Cyb3rhq dashboard to check for the newly enrolled Cyb3rhq agent and its connection status. If the enrollment was successful, you will have an interface similar to the image below.

   .. thumbnail:: /images/manual/agent/linux-check-newly-enrolled.png
      :title: Check newly enrolled Cyb3rhq agent - Linux
      :alt: Check newly enrolled Cyb3rhq agent - Linux
      :align: center
      :width: 80%

Windows
-------

Follow these steps to enroll a Windows endpoint with password authentication:

The Cyb3rhq agent installation directory depends on the host's architecture.

-  ``C:\Program Files (x86)\ossec-agent`` for 64-bit systems.
-  ``C:\Program Files\ossec-agent`` for 32-bit systems.

#. Launch PowerShell as an administrator.

#. Create a file called ``authd.pass`` and save the password. Replace ``<CUSTOM_PASSWORD>`` with the agent enrollment password created on the Cyb3rhq manager.

   For 32-bit systems

   .. code-block:: console

      # echo “<CUSTOM_PASSWORD>” > "C:\Program Files\ossec-agent\authd.pass"

   For 64-bit systems

   .. code-block:: console

      # echo “<CUSTOM_PASSWORD>” > "C:\Program Files (x86)\ossec-agent\authd.pass"

#. (Optional) To ensure the Cyb3rhq agent can locate your password file if it is not in the default location (``C:\Program Files (x86)\ossec-agent\authd.pass``), include the ``authorization_pass_path`` setting in the Cyb3rhq agent configuration. Replace ``<PATH_TO_PASSWORD_FILE>`` with the filepath of the password file.

   .. code-block:: xml

      <enrollment>
        <authorization_pass_path><PATH_TO_PASSWORD_FILE></authorization_pass_path>
      </enrollment>

#. Add the Cyb3rhq manager IP address or FQDN (Fully Qualified Domain Name) in the ``<client><server><address>`` section of the agent configuration file in ``C:\Program Files (x86)\ossec-agent\ossec.conf``. Replace ``<CYB3RHQ_MANAGER_IP>`` with the IP address or FQDN of the Cyb3rhq manager.

   .. code-block:: xml
      :emphasize-lines: 3

      <client>
         <server>
             <address><CYB3RHQ_MANAGER_IP></address>
            ...
         </server>
      </client>

#. Restart the Cyb3rhq agent to make the changes effective.

   .. tabs::

      .. group-tab:: PowerShell (as an administrator):

         .. code-block:: pwsh-session

            # Restart-Service -Name cyb3rhq

      .. group-tab:: CMD (as an administrator):

         .. code-block:: doscon

            # net stop cyb3rhq
            # net start cyb3rhq

#. Click on the upper-left menu icon and navigate to **Server management** > **Endpoints Summary** on the Cyb3rhq dashboard to check for the newly enrolled Cyb3rhq agent and its connection status. If the enrollment was successful, you will have an interface similar to the image below.

   .. thumbnail:: /images/manual/agent/windows-check-newly-enrolled.png
      :title: Check newly enrolled Cyb3rhq agent - Windows
      :alt: Check newly enrolled Cyb3rhq agent - Windows
      :align: center
      :width: 80%

macOS
-----

Follow the steps below  to enroll a macOS endpoint with password authentication:

#. Launch the terminal, with root permission, create a file called ``/Library/Ossec/etc/authd.pass`` and save the password to it:

   .. code-block:: console

      # echo "<CUSTOM_PASSWORD>" > /Library/Ossec/etc/authd.pass

   #. Replace ``<CUSTOM_PASSWORD>`` with the agent enrollment password created on the Cyb3rhq manager.

   #. Set the file permissions for the ``authd.pass`` file to 640 and the owner should be root. Configure the permissions and ownership by running the commands below:

      .. code-block:: console

         # chmod 640 /Library/Ossec/etc/authd.pass
         # chown root:cyb3rhq /Library/Ossec/etc/authd.pass

      The output below shows the recommended file owner and permissions:

      .. code-block:: none

         -rw-r--r-- 1 root cyb3rhq 18 Jan 11 13:03 /Library/Ossec/etc/authd.pass

#. (Optional) To ensure the Cyb3rhq agent can locate your password file if it is not in the default location (``/Library/Ossec/etc/authd.pass``), include the ``authorization_pass_path`` setting in the Cyb3rhq agent configuration. Replace ``<PATH_TO_PASSWORD_FILE>`` with the filepath of the password file.

   .. code-block:: xml

      <enrollment>
        <authorization_pass_path><PATH_TO_PASSWORD_FILE></authorization_pass_path>
      </enrollment>

#. Add the Cyb3rhq manager IP address or FQDN (Fully Qualified Domain Name) to the agent configuration file in ``/Library/Ossec/etc/ossec.conf``. Replace ``<CYB3RHQ_MANAGER_IP>`` with the IP address or FQDN of the Cyb3rhq manager.

   .. code-block:: xml
      :emphasize-lines: 3

      <client>
        <server>
          <address><CYB3RHQ_MANAGER_IP></address>
          ...
        </server>
      </client>

#. Restart the Cyb3rhq agent to make the changes effective:

   .. code-block:: console

      # /Library/Ossec/bin/cyb3rhq-control restart

#. Click on the upper-left menu icon and navigate to **Server management** > **Endpoints Summary** on the Cyb3rhq dashboard to check for the newly enrolled Cyb3rhq agent and its connection status. If the enrollment was successful, you will have an interface similar to the image below.

   .. thumbnail:: /images/manual/agent/macOS-check-newly-enrolled.png
      :title: Check newly enrolled Cyb3rhq agent - macOS
      :alt: Check newly enrolled Cyb3rhq agent - macOS
      :align: center
      :width: 80%
