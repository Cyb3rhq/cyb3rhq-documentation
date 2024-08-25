.. Copyright (C) 2015, Cyb3rhq, Inc.

.. tabs::


  .. group-tab:: Systemd


    .. code-block:: console

      # systemctl daemon-reload
      # systemctl enable cyb3rhq-manager
      # systemctl start cyb3rhq-manager


  .. group-tab:: SysV init

    Choose one option according to your operating system:

    a) RPM-based operating system:

      .. code-block:: console

        # chkconfig --add cyb3rhq-manager
        # service cyb3rhq-manager start

    b) Debian-based operating system:

      .. code-block:: console

        # update-rc.d cyb3rhq-manager defaults 95 10
        # service cyb3rhq-manager start

.. End of include file
