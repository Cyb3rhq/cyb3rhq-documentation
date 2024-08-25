.. Copyright (C) 2015, Cyb3rhq, Inc.

#. Install the following packages if missing.

    .. code-block:: console

      # apt-get install gnupg apt-transport-https

#. Install the GPG key.

    .. code-block:: console

      # curl -s https://packages.wazuh.com/key/GPG-KEY-CYB3RHQ | gpg --no-default-keyring --keyring gnupg-ring:/usr/share/keyrings/cyb3rhq.gpg --import && chmod 644 /usr/share/keyrings/cyb3rhq.gpg

#. Add the repository.

    .. code-block:: console

       # echo "deb [signed-by=/usr/share/keyrings/cyb3rhq.gpg] https://packages.wazuh.com/4.x/apt/ stable main" | tee -a /etc/apt/sources.list.d/cyb3rhq.list

#. Update the packages information.

    .. code-block:: console

      # apt-get update

.. End of include file
