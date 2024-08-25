.. Copyright (C) 2015, Cyb3rhq, Inc.

#. Import the RSA key:

   .. code-block:: console

      # wget -O /etc/apk/keys/alpine-devel@cyb3rhq.github.io-633d7457.rsa.pub https://packages.wazuh.com/key/alpine-devel%40cyb3rhq.github.io-633d7457.rsa.pub

#. Add the repository:

   .. code-block:: console

      # echo "https://packages.wazuh.com/4.x/alpine/v3.12/main" >> /etc/apk/repositories

#. Update the metadata information:

   .. code-block:: console

      # apk update
      
.. End of include file
