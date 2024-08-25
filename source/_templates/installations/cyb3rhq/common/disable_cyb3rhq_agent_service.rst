.. Copyright (C) 2015, Cyb3rhq, Inc.

.. tabs::


  .. group-tab:: Systemd


    .. code-block:: console

      # systemctl disable cyb3rhq-agent
      # systemctl daemon-reload


  .. group-tab:: SysV init

    Choose one option according to your operating system.

    a) RPM-based operating systems:

      .. code-block:: console

        # chkconfig cyb3rhq-agent off
        # chkconfig --del cyb3rhq-agent

    b) Debian-based operating systems:

      .. code-block:: console

        # update-rc.d -f cyb3rhq-agent remove



  .. group-tab:: No service manager

     No action required.

.. End of include file