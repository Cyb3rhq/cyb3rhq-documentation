.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: learn about the variables used by Cyb3rhq agent packages on macOS endpoints and see examples of how to use them.

Deployment variables for macOS
==============================

For a Cyb3rhq agent to be fully deployed and connected to the Cyb3rhq server, you must install, enroll, and configure it. The Cyb3rhq agent packages can use variables that allow configuration provisioning to make the process simple.

Below is a table describing the variables used by Cyb3rhq agent packages on macOS endpoints, and a few examples of how to use them.

+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option                           | Description                                                                                                                                                                                          |
+==================================+======================================================================================================================================================================================================+
|   CYB3RHQ_MANAGER                  |  This is the primary Cyb3rhq manager that the Cyb3rhq agent will connect to for ongoing communication and security data exchange. Specifies the Cyb3rhq manager IP address or FQDN (Fully Qualified        |
|                                  |  Domain Name). If you want to specify multiple managers, you can add them separated by commas. See :ref:`address <server_address>`.                                                                  |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   CYB3RHQ_MANAGER_PORT             |  Specifies the Cyb3rhq manager connection port. See :ref:`port <server_port>`.                                                                                                                         |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   CYB3RHQ_PROTOCOL                 |  Sets the communication protocol between the Cyb3rhq manager and the Cyb3rhq agent. Accepts UDP and TCP. The default is TCP. See :ref:`protocol <server_protocol>`.                                      |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   CYB3RHQ_REGISTRATION_SERVER      |  Specifies the Cyb3rhq enrollment server, used for the Cyb3rhq agent enrollment. See :ref:`manager_address <enrollment_manager_address>`. If empty, the value set in ``CYB3RHQ_MANAGER`` will be used.     |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   CYB3RHQ_REGISTRATION_PORT        |  Specifies the port used by the Cyb3rhq enrollment server. See :ref:`port <enrollment_manager_port>`.                                                                                                  |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   CYB3RHQ_REGISTRATION_PASSWORD    |  Sets the password used to authenticate during the Cyb3rhq agent enrollment, stored in ``etc/authd.pass`` file. See :ref:`authorization_pass_path <enrollment_authorization_pass_path>`                |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   CYB3RHQ_KEEP_ALIVE_INTERVAL      |  Sets the time between Cyb3rhq agent checks for Cyb3rhq manager connection. See :ref:`notify_time <notify_time>`.                                                                                        |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   CYB3RHQ_TIME_RECONNECT           |  Sets the time interval for the Cyb3rhq agent to reconnect with the Cyb3rhq manager when connectivity is lost. See :ref:`time-reconnect <time_reconnect>`.                                               |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   CYB3RHQ_REGISTRATION_CA          |  Host SSL validation need of Certificate of Authority. This option specifies the CA path. See :ref:`server_ca_path <enrollment_server_ca_path>`.                                                     |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   CYB3RHQ_REGISTRATION_CERTIFICATE |  The SSL agent verification needs a CA signed certificate and the respective key. This option specifies the certificate path. See :ref:`agent_certificate_path <enrollment_agent_certificate_path>`. |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   CYB3RHQ_REGISTRATION_KEY         |  Specifies the key path completing the required variables with CYB3RHQ_REGISTRATION_CERTIFICATE for the SSL agent verification process. See :ref:`agent_key_path <enrollment_agent_key_path>`.         |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   CYB3RHQ_AGENT_NAME               |  Designates the Cyb3rhq agent's name. By default, it will be the computer name. See :ref:`agent_name <enrollment_agent_name>`.                                                                         |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   CYB3RHQ_AGENT_GROUP              |  Assigns the Cyb3rhq agent to one or more existing groups (separated by commas). See :ref:`agent_groups <enrollment_agent_groups>`.                                                                    |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   ENROLLMENT_DELAY               |  Assigns the time that agentd should wait after a successful enrollment. See :ref:`delay_after_enrollment <enrollment_delay_after_enrollment>`.                                                      |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Examples:

-  Enrollment with password:

   .. tabs::

      .. group-tab:: Intel

         .. code-block:: console

            # echo "CYB3RHQ_MANAGER='10.0.0.2' && CYB3RHQ_REGISTRATION_PASSWORD='TopSecret' && \
            CYB3RHQ_AGENT_NAME='macos-agent'" > /tmp/cyb3rhq_envs && installer -pkg cyb3rhq-agent-|CYB3RHQ_CURRENT_OSX|-|CYB3RHQ_REVISION_OSX|.intel64.pkg -target /

      .. group-tab:: Apple silicon

         .. code-block:: console

            # echo "CYB3RHQ_MANAGER='10.0.0.2' && CYB3RHQ_REGISTRATION_PASSWORD='TopSecret' && \
            CYB3RHQ_AGENT_NAME='macos-agent'" > /tmp/cyb3rhq_envs && installer -pkg cyb3rhq-agent-|CYB3RHQ_CURRENT_OSX|-|CYB3RHQ_REVISION_OSX|.arm64.pkg -target /

-  Enrollment with password and assigning a group:

   .. tabs::

      .. group-tab:: Intel

         .. code-block:: console

            # echo "CYB3RHQ_MANAGER='10.0.0.2' && CYB3RHQ_REGISTRATION_SERVER='10.0.0.2' && CYB3RHQ_REGISTRATION_PASSWORD='TopSecret' && \
            CYB3RHQ_AGENT_GROUP='my-group'" > /tmp/cyb3rhq_envs && installer -pkg cyb3rhq-agent-|CYB3RHQ_CURRENT_OSX|-|CYB3RHQ_REVISION_OSX|.intel64.pkg -target /

      .. group-tab:: Apple silicon

         .. code-block:: console

            # echo "CYB3RHQ_MANAGER='10.0.0.2' && CYB3RHQ_REGISTRATION_SERVER='10.0.0.2' && CYB3RHQ_REGISTRATION_PASSWORD='TopSecret' && \
            CYB3RHQ_AGENT_GROUP='my-group'" > /tmp/cyb3rhq_envs && installer -pkg cyb3rhq-agent-|CYB3RHQ_CURRENT_OSX|-|CYB3RHQ_REVISION_OSX|.arm64.pkg -target /

-  Enrollment with relative path to CA. It will be searched at your Cyb3rhq installation folder:

   .. tabs::

      .. group-tab:: Intel

         .. code-block:: console

            # echo "CYB3RHQ_MANAGER='10.0.0.2' && CYB3RHQ_REGISTRATION_SERVER='10.0.0.2' && CYB3RHQ_AGENT_NAME='macos-agent' && \
            CYB3RHQ_REGISTRATION_CA='rootCA.pem'" > /tmp/cyb3rhq_envs && installer -pkg cyb3rhq-agent-|CYB3RHQ_CURRENT_OSX|-|CYB3RHQ_REVISION_OSX|.intel64.pkg -target /

      .. group-tab:: Apple silicon

         .. code-block:: console

            # echo "CYB3RHQ_MANAGER='10.0.0.2' && CYB3RHQ_REGISTRATION_SERVER='10.0.0.2' && CYB3RHQ_AGENT_NAME='macos-agent' && \
            CYB3RHQ_REGISTRATION_CA='rootCA.pem'" > /tmp/cyb3rhq_envs && installer -pkg cyb3rhq-agent-|CYB3RHQ_CURRENT_OSX|-|CYB3RHQ_REVISION_OSX|.arm64.pkg -target /

-  Enrollment with protocol:

   .. tabs::

      .. group-tab:: Intel

         .. code-block:: console

            # echo "CYB3RHQ_MANAGER='10.0.0.2' && CYB3RHQ_REGISTRATION_SERVER='10.0.0.2' && CYB3RHQ_AGENT_NAME='macos-agent' && \
            CYB3RHQ_PROTOCOL='udp'" > /tmp/cyb3rhq_envs && installer -pkg cyb3rhq-agent-|CYB3RHQ_CURRENT_OSX|-|CYB3RHQ_REVISION_OSX|.intel64.pkg -target /

      .. group-tab:: Apple silicon

         .. code-block:: console

            # echo "CYB3RHQ_MANAGER='10.0.0.2' && CYB3RHQ_REGISTRATION_SERVER='10.0.0.2' && CYB3RHQ_AGENT_NAME='macos-agent' && \
            CYB3RHQ_PROTOCOL='udp'" > /tmp/cyb3rhq_envs && installer -pkg cyb3rhq-agent-|CYB3RHQ_CURRENT_OSX|-|CYB3RHQ_REVISION_OSX|.arm64.pkg -target /

-  Enrollment and adding multiple addresses:

   .. tabs::

      .. group-tab:: Intel

         .. code-block:: console

            # echo "CYB3RHQ_MANAGER='10.0.0.2,10.0.0.3' && CYB3RHQ_REGISTRATION_SERVER='10.0.0.2' && \
            CYB3RHQ_AGENT_NAME='macos-agent'" > /tmp/cyb3rhq_envs && installer -pkg cyb3rhq-agent-|CYB3RHQ_CURRENT_OSX|-|CYB3RHQ_REVISION_OSX|.intel64.pkg -target /

      .. group-tab:: Apple silicon

         .. code-block:: console

            # echo "CYB3RHQ_MANAGER='10.0.0.2,10.0.0.3' && CYB3RHQ_REGISTRATION_SERVER='10.0.0.2' && \
            CYB3RHQ_AGENT_NAME='macos-agent'" > /tmp/cyb3rhq_envs && installer -pkg cyb3rhq-agent-|CYB3RHQ_CURRENT_OSX|-|CYB3RHQ_REVISION_OSX|.arm64.pkg -target /

-  Absolute paths to CA, certificate or key that contain spaces can be written as shown below:

   .. tabs::

      .. group-tab:: Intel

         .. code-block:: console

            # echo "CYB3RHQ_MANAGER='10.0.0.2' && CYB3RHQ_REGISTRATION_SERVER='10.0.0.2' && CYB3RHQ_REGISTRATION_KEY='/var/ossec/etc/sslagent.key' && \
            CYB3RHQ_REGISTRATION_CERTIFICATE='/var/ossec/etc/sslagent.cert'" > /tmp/cyb3rhq_envs && installer -pkg cyb3rhq-agent-|CYB3RHQ_CURRENT_OSX|-|CYB3RHQ_REVISION_OSX|.intel64.pkg -target /

      .. group-tab:: Apple silicon

         .. code-block:: console

            # echo "CYB3RHQ_MANAGER='10.0.0.2' && CYB3RHQ_REGISTRATION_SERVER='10.0.0.2' && CYB3RHQ_REGISTRATION_KEY='/var/ossec/etc/sslagent.key' && \
            CYB3RHQ_REGISTRATION_CERTIFICATE='/var/ossec/etc/sslagent.cert'" > /tmp/cyb3rhq_envs && installer -pkg cyb3rhq-agent-|CYB3RHQ_CURRENT_OSX|-|CYB3RHQ_REVISION_OSX|.arm64.pkg -target /

.. note::

   It’s necessary to use both KEY and PEM options to verify Cyb3rhq agents' identities with the enrollment server. See the :doc:`additional security options <../security-options/index>` section.
