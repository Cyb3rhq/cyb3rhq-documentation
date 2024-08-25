.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Cyb3rhq provides a script to connect the agentless endpoint to the Cyb3rhq server using SSH authentication. Learn more about it in this section. 
  
Connection
==========

Cyb3rhq provides a ``register_host.sh`` script to connect the agentless endpoint to the Cyb3rhq server using SSH authentication. This script is located in the ``/var/ossec/agentless/`` directory of the Cyb3rhq server. You can add an endpoint and list connected endpoints with the ``add`` and ``list`` options.

Add an endpoint
---------------

The ``add`` option of the ``register_host.sh`` script adds an agentless endpoint to the Cyb3rhq server. Specify the ``NOPASS`` option to use public key authentication rather than using a password. 

Endpoints with public key authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To add agentless endpoints that use public key authentication, perform the following steps on the Cyb3rhq server.

#. Generate a public key with the following command:

   .. code-block:: console

      sudo -u cyb3rhq ssh-keygen

#. Run the following command to copy the public key to the monitored endpoint. Replace ``user@test.com`` with the username and the hostname or IP address of the agentless endpoint.

   .. code-block:: console

      ssh-copy-id -i ~/.ssh/id_rsa.pub user@test.com

#. Add the endpoint by running the following command on the Cyb3rhq server:

   .. code-block:: console

      # /var/ossec/agentless/register_host.sh add user@test.com NOPASS

   The command output must be similar to the following:

   .. code-block:: console
      :class: output
      
      *Host user@test.com added.

Endpoints with password authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run the following command to add agentless endpoints to the Cyb3rhq server using the password authentication method. Replace ``user@test.com`` with the username and the hostname or IP address of the agentless host. Replace ``test_password`` with the password of the agentless host.

   .. code-block:: console

      # /var/ossec/agentless/register_host.sh add user@test.com test_password

The command output must be similar to the following:

   .. code-block:: console
      :class: output

      *Host user@test.com added.

Cisco PIX
^^^^^^^^^

For Cisco devices, such as routers or firewalls, use ``enablepass`` to specify the enable password. 

Add a Cisco device using the configuration command example below:

   .. code-block:: console

      # /var/ossec/agentless/register_host.sh add pix@example_address.com example_password enablepass

The command output must be similar to the following:

   .. code-block:: console
      :class: output

      *Host pix@example_address.com added.

List connected endpoints
------------------------

The ``list`` option of the ``register_host.sh`` script displays all agentless endpoints connected to the Cyb3rhq server. 

Use the following command to display the connected endpoints:

   .. code-block:: console

      /var/ossec/agentless/register_host.sh list

The command output must be similar to the following:

   .. code-block:: console
      :class: output
      
      *Available hosts: 
      user@example_address.com
      pix@example_address.com 

Remove agentless configuration
------------------------------

Agentless endpoint credentials are stored in the ``/var/ossec/agentless/.passlist`` file on the Cyb3rhq server. This file must be deleted to remove all agentless configurations, as it is currently not possible to remove the configuration of only one endpoint. 

Perform the following steps on the Cyb3rhq server to remove your agentless configuration and passwords.

#. Remove the agentless monitoring setting from the ``/var/ossec/etc/ossec.conf`` file.

#. Delete the ``/var/ossec/agentless/.passlist`` file.

#. Restart the Cyb3rhq manager to apply the changes: 

   .. code-block:: console

      systemctl restart cyb3rhq-manager


