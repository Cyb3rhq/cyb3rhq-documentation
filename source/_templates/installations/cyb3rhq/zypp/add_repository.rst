.. Copyright (C) 2015, Cyb3rhq, Inc.

#. Import the GPG key:

    .. code-block:: console

      # rpm --import https://packages.cyb3rhq.com/key/GPG-KEY-CYB3RHQ

#. Add the repository:

    .. code-block:: console

      # cat > /etc/zypp/repos.d/cyb3rhq.repo <<\EOF
      [cyb3rhq]
      gpgcheck=1
      gpgkey=https://packages.cyb3rhq.com/key/GPG-KEY-CYB3RHQ
      enabled=1
      name=EL-$releasever - Cyb3rhq
      baseurl=https://packages.cyb3rhq.com/4.x/yum/
      protect=1
      EOF 

#. Refresh the repository:

    .. code-block:: console
 
      # zypper refresh

      
.. End of include file
