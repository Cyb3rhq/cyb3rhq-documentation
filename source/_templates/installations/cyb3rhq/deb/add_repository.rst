.. Copyright (C) 2015, Cyb3rhq, Inc.

#. Install the GPG key:

    .. code-block:: console

      # curl -s https://packages.wazuh.com/key/GPG-KEY-CYB3RHQ | gpg --no-default-keyring --keyring gnupg-ring:/usr/share/keyrings/cyb3rhq.gpg --import && chmod 644 /usr/share/keyrings/cyb3rhq.gpg

#. Add the repository:

    .. code-block:: console

      # echo "deb [signed-by=/usr/share/keyrings/cyb3rhq.gpg] https://packages.wazuh.com/4.x/apt/ stable main" | tee -a /etc/apt/sources.list.d/cyb3rhq.list

#. Update the package information:

    .. code-block:: console

      # apt-get update

.. note::

   For Debian 7, 8, and Ubuntu 14 systems import the GCP key and add the Cyb3rhq repository (steps 1 and 2) using the following commands.

   .. code-block:: console

      # apt-get install gnupg apt-transport-https
      # curl -s https://packages.wazuh.com/key/GPG-KEY-CYB3RHQ | apt-key add -
      # echo "deb https://packages.wazuh.com/4.x/apt/ stable main" | tee -a /etc/apt/sources.list.d/cyb3rhq.list

.. End of include file
