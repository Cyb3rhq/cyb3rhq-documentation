.. Copyright (C) 2015, Cyb3rhq, Inc.

.. tabs::


  .. group-tab:: Systemd


    .. code-block:: console

      # systemctl daemon-reload
      # systemctl enable cyb3rhq-agent
      # systemctl start cyb3rhq-agent


  .. group-tab:: SysV init

    Choose one option according to your operating system.

    a) RPM-based operating systems:

      .. code-block:: console

        # chkconfig --add cyb3rhq-agent
        # service cyb3rhq-agent start

    b) Debian-based operating systems:

      .. code-block:: console

        # update-rc.d cyb3rhq-agent defaults 95 10
        # service cyb3rhq-agent start



  .. group-tab:: No service manager

     On some systems, like Alpine Linux, you need to start the agent manually: 

     .. code-block:: console

       # /var/ossec/bin/cyb3rhq-control start

.. End of include file