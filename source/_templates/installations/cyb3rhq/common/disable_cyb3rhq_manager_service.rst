.. Copyright (C) 2015, Cyb3rhq, Inc.

.. tabs::


  .. group-tab:: Systemd


    .. code-block:: console

      # systemctl disable cyb3rhq-manager
      # systemctl daemon-reload


  .. group-tab:: SysV init

    Choose one option according to your operating system.

    a) RPM-based operating systems:

      .. code-block:: console

        # chkconfig cyb3rhq-manager off
        # chkconfig --del cyb3rhq-manager

    b) Debian-based operating systems:

      .. code-block:: console

        # update-rc.d -f cyb3rhq-manager remove

.. End of include file