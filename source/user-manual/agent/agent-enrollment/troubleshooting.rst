.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Learn about the logs on the Cyb3rhq manager and Cyb3rhq agent.

Troubleshooting
===============

We recommend checking the logs on the Cyb3rhq manager and Cyb3rhq agent for errors when a Cyb3rhq agent fails to enroll. The location of the Cyb3rhq manager log file is ``/var/ossec/logs/ossec.log``. The location of the Cyb3rhq agent log file is dependent on the operating system:

================ =================================================
Operating system Cyb3rhq agent log file
================ =================================================
Linux/Unix       ``/var/ossec/logs/ossec.log``
macOS            ``/Library/Ossec/logs/ossec.log``
Windows 64-bit   ``C:\Program Files (x86)\ossec-agent\ossec.log``
Windows 32-bit   ``C:\Program Files\ossec-agent\ossec.log``
================ =================================================

In the list below, you can access the different cases included in this troubleshooting section:

.. contents::
   :local:
   :depth: 1
   :backlinks: none

Verifying communication with the Cyb3rhq manager
----------------------------------------------

In some scenarios, the Cyb3rhq agent may be unable to enroll or establish a connection with the Cyb3rhq manager because the necessary ports on the Cyb3rhq manager are unreachable.

The following default ports on the Cyb3rhq manager should be opened:

-  1514/TCP for agent communication.
-  1515/TCP for enrollment via agent configuration.
-  55000/TCP for enrollment via Cyb3rhq server API.

On Linux and macOS systems (with netcat installed), open a terminal and run the following command. Replace ``<CYB3RHQ_MANAGER_IP>`` with your Cyb3rhq manager IP address or FQDN (Fully Qualified Domain Name).

.. code-block:: console

   # nc -zv <CYB3RHQ_MANAGER_IP> 1514 1515 55000

If there is connectivity, the output should be a connection success message:

.. code-block:: none

   Connection to <CYB3RHQ_MANAGER_IP> port 1514 [tcp] succeeded!
   Connection to <CYB3RHQ_MANAGER_IP> port 1515 [tcp] succeeded!
   Connection to <CYB3RHQ_MANAGER_IP> port 55000 [tcp] succeeded!

On Windows, open a PowerShell terminal and run the following command:

.. code-block:: pwsh-session

   # (new-object Net.Sockets.TcpClient).Connect("<CYB3RHQ_MANAGER_IP>", 1514)
   # (new-object Net.Sockets.TcpClient).Connect("<CYB3RHQ_MANAGER_IP>", 1515)
   # (new-object Net.Sockets.TcpClient).Connect("<CYB3RHQ_MANAGER_IP>", 55000)

If there is connectivity, there is no output. Otherwise, an error is shown:

.. code-block:: none

   A connection attempt failed because the connected party did not properly respond after a period of time (...)

Authentication error
--------------------

The ``client.keys`` file stores the data used to authenticate the Cyb3rhq agent and the Cyb3rhq manager. The Cyb3rhq agent may be unable to authenticate with the Cyb3rhq manager if the ``client.keys`` on the Cyb3rhq manager and the Cyb3rhq agent are different.

**Location**: Cyb3rhq manager log file at ``/var/ossec/logs/ossec.log``.

**Error log**:

.. code-block:: none

   2022/02/03 10:07:32 cyb3rhq-remoted: WARNING: (1404): Authentication error. Wrong key or corrupt payload. Message received from agent '001' at 'any'.

**Resolution**: Ensure that the client key on the Cyb3rhq agent matches the key in the Cyb3rhq manager ``client.keys`` file. You can find the ``client.keys`` key file at the following locations:

============= ====================================================
Endpoint      Location
============= ====================================================
Cyb3rhq manager ``/var/ossec/etc/client.keys``
Linux/Unix    ``/var/ossec/etc/client.keys``
macOS         ``/Library/Ossec/etc/client.keys``
Windows       ``"C:\Program Files (x86)\ossec-agent\client.keys"``
============= ====================================================

Also, verify that each agent has a unique agent key stored in the Cyb3rhq manager ``/var/ossec/etc/client.keys`` file. Duplicate keys can arise if you previously deleted agents with the highest IDs or copied the ``client.keys`` file between agents.


Invalid agent name for enrollment
---------------------------------

Each Cyb3rhq agent must have a unique name before successfully enrolling in the Cyb3rhq manager. If you do not specify a Cyb3rhq agent name during the deployment process, Cyb3rhq will use the endpoint's hostname. If two or more endpoints have the same hostname, the Cyb3rhq agent enrollment will not be successful.

**Location**: Cyb3rhq agent log file

Refer to the table in the :doc:`Troubleshooting <troubleshooting>` section for the Cyb3rhq agent log file location.

**Error log**:

.. code-block:: none

   2022/01/26 08:59:10 cyb3rhq-agentd: INFO: Using agent name as: localhost.localdomain
   2022/01/26 08:59:10 cyb3rhq-agentd: INFO: Waiting for server reply
   2022/01/26 08:59:10 cyb3rhq-agentd: ERROR: Invalid agent name: localhost.localdomain (from manager)
   2022/01/26 08:59:10 cyb3rhq-agentd: ERROR: Unable to add agent (from manager)

**Resolution**: Ensure the Cyb3rhq agent hostname is unique and does not match an already enrolled agent. Alternatively, specify a unique agent name in the ``<client><enrollment><agent_name>`` section of the Cyb3rhq agent ``ossec.conf`` file. You can find the ``ossec.conf`` file at the following locations:

-  Linux/Unix endpoints - ``/var/ossec/etc/ossec.conf``
-  macOS endpoint - ``/Library/Ossec/etc/ossec.conf``
-  Windows endpoints - ``C:\Program Files (x86)\ossec-agent\ossec.conf``

.. code-block:: xml
   :emphasize-lines: 4

   <client>
        ...
        <enrollment>
            <agent_name>EXAMPLE_NAME</agent_name>
            ...
        </enrollment>
    </client>

Unable to read CA certificate file
----------------------------------

The Cyb3rhq agent may not be able to authenticate with the Cyb3rhq manager if the root certificate authority is missing on either the Cyb3rhq manager or the Cyb3rhq agent. This applies when additional security options such as :doc:`Cyb3rhq manager identity verification <security-options/manager-identity-verification>` and :doc:`Cyb3rhq agent identity verification <security-options/agent-identity-verification>` are used.

**Location**: Cyb3rhq manager log file at ``/var/ossec/logs/ossec.log``.

**Error log**:

.. code-block:: none

   2022/01/26 08:25:01 cyb3rhq-authd: ERROR: Unable to read CA certificate file "/var/ossec/etc/rootCA.pem"
   2022/01/26 08:25:01 cyb3rhq-authd: ERROR: SSL error. Exiting.

**Resolution**: Ensure the certificate authority file is in the location specified in the ``<ssl_agent_ca>`` section of the Cyb3rhq manager ``/var/ossec/etc/ossec.conf`` file.

**Location**: Cyb3rhq agent log file

Refer to the table in the :doc:`Troubleshooting <troubleshooting>` section for the Cyb3rhq agent log file location.

**Error log**:

.. code-block:: none

   2022/01/26 08:25:01 cyb3rhq-authd: ERROR: Unable to read CA certificate file "/var/ossec/etc/rootCA.pem"
   2022/01/26 08:25:01 cyb3rhq-authd: ERROR: SSL error. Exiting.

**Resolution**: Ensure the certificate authority file is in the location specified in the ``<server_ca_path>`` section of the Cyb3rhq agent configuration file (``ossec.conf``). You can find the ``ossec.conf`` file at the following locations:

-  Linux/Unix endpoints - ``/var/ossec/etc/ossec.conf``
-  macOS endpoint - ``/Library/Ossec/etc/ossec.conf``
-  Windows endpoints - ``C:\Program Files (x86)\ossec-agent\ossec.conf``

Unable to read private key file
-------------------------------

The Cyb3rhq agent may not be able to authenticate with the Cyb3rhq manager if the private key file is missing on the Cyb3rhq agent. This applies when :doc:`Cyb3rhq agent identity verification <security-options/agent-identity-verification>` is used for the Cyb3rhq agent enrollment.

**Location**: Cyb3rhq agent log file

Refer to the table in the :doc:`Troubleshooting <troubleshooting>` section for the Cyb3rhq agent log file location.

**Error log**:

.. code-block:: none

   2022/01/26 08:57:18 cyb3rhq-agentd: ERROR: Unable to read private key file: /var/ossec/etc/sslagent.key
   2022/01/26 08:57:18 cyb3rhq-agentd: ERROR: Could not set up SSL connection! Check certification configuration.

**Resolution**: Ensure the agent private key file is in the location specified in the ``<agent_key_path>`` section of the Cyb3rhq agent ``ossec.conf`` file. You can find the ossec.conf file at the following locations:

-  Linux/Unix endpoints - ``/var/ossec/etc/ossec.conf``
-  macOS endpoint - ``/Library/Ossec/etc/ossec.conf``
-  Windows endpoints - ``C:\Program Files (x86)\ossec-agent\ossec.conf``

Unable to read certificate file
-------------------------------

The Cyb3rhq agent may not be able to authenticate with the Cyb3rhq manager if the signed SSL certificate is missing on the Cyb3rhq agent. This applies when :doc:`Cyb3rhq agent identity verification <security-options/agent-identity-verification>` is used for the Cyb3rhq agent enrollment.

**Location**: Cyb3rhq agent log file

Refer to the table in the :doc:`Troubleshooting <troubleshooting>` section for the Cyb3rhq agent log file location.

**Error log**:

.. code-block:: none

   2022/01/26 08:54:55 cyb3rhq-agentd: ERROR: Unable to read certificate file (not found): /var/ossec/etc/sslagent.cert
   2022/01/26 08:54:55 cyb3rhq-agentd: ERROR: Could not set up SSL connection! Check certification configuration.

**Resolution**: Ensure the agent certificate file is in the location specified in the ``<agent_certificate_path>`` section of the Cyb3rhq agent ``ossec.conf`` file. You can find the ``ossec.conf`` file at the following locations:

-  Linux/Unix endpoints - ``/var/ossec/etc/ossec.conf``
-  macOS endpoint - ``/Library/Ossec/etc/ossec.conf``
-  Windows endpoints - ``C:\Program Files (x86)\ossec-agent\ossec.conf``

Invalid password
----------------

If you enable :doc:`password authentication <security-options/using-password-authentication>` for agent enrollment, the Cyb3rhq agent may not be able to authenticate with the Cyb3rhq manager if there's an invalid or missing password.

**Location**: Cyb3rhq agent log file

Refer to the table in the :doc:`Troubleshooting <troubleshooting>` section for the Cyb3rhq agent log file location.

**Error log**:

.. code-block:: none

   2022/01/26 12:28:10 cyb3rhq-agentd: INFO: Requesting a key from server: X.X.X.X
   2022/01/26 12:28:10 cyb3rhq-agentd: INFO: No authentication password provided
   2022/01/26 12:28:10 cyb3rhq-agentd: INFO: Using agent name as: random
   2022/01/26 12:28:10 cyb3rhq-agentd: INFO: Waiting for server reply
   2022/01/26 12:28:10 cyb3rhq-agentd: ERROR: Invalid password (from manager)
   2022/01/26 12:28:10 cyb3rhq-agentd: ERROR: Unable to add agent (from manager)

**Resolution**:

#. Ensure the same password is used by the Cyb3rhq manager and the Cyb3rhq agent
#. Ensure that the ``authd.pass`` password file is in the ``/var/ossec/etc/`` directory and has the right permission. The file permissions should be set to 640, and the owner should be ``root``.
#. If password authentication is not needed, it should be disabled in the ``<auth>`` section of the Cyb3rhq manager ``/var/ossec/etc/ossec.conf`` file. You can find the ``ossec.conf`` file at the following locations:

   -  Linux/Unix endpoints - ``/var/ossec/etc/ossec.conf``
   -  macOS endpoint - ``/Library/Ossec/etc/ossec.conf``
   -  Windows endpoints - ``C:\Program Files (x86)\ossec-agent\ossec.conf``