.. Copyright (C) 2015, Cyb3rhq, Inc.

#. Import the GPG key.

    .. code-block:: console

      # rpm --import https://packages.wazuh.com/key/GPG-KEY-CYB3RHQ

#. Add the repository.

    .. code-block:: console

      # echo -e '[cyb3rhq]\ngpgcheck=1\ngpgkey=https://packages.wazuh.com/key/GPG-KEY-CYB3RHQ\nenabled=1\nname=EL-$releasever - Cyb3rhq\nbaseurl=https://packages.wazuh.com/4.x/yum/\nprotect=1' | tee /etc/yum.repos.d/cyb3rhq.repo
      
.. End of include file
