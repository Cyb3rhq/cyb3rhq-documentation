.. Copyright (C) 2015, Cyb3rhq, Inc.

.. tabs::


  .. group-tab:: Systemd


    .. code-block:: console

      # systemctl daemon-reload
      # systemctl enable cyb3rhq-dashboard
      # systemctl start cyb3rhq-dashboard



  .. group-tab:: SysV init

    Choose one option according to your operating system:

    a) RPM-based operating system:

      .. code-block:: console

        # chkconfig --add cyb3rhq-dashboard
        # service cyb3rhq-dashboard start
    
    b) Debian-based operating system:

      .. code-block:: console

        # update-rc.d cyb3rhq-dashboard defaults 95 10
        # service cyb3rhq-dashboard start

.. End of include file
