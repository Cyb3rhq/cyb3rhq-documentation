.. Copyright (C) 2015, Cyb3rhq, Inc.

.. tabs::


  .. group-tab:: Systemd


    .. code-block:: console

      # systemctl daemon-reload
      # systemctl enable cyb3rhq-indexer
      # systemctl start cyb3rhq-indexer



  .. group-tab:: SysV init

    Choose one option according to the operating system used.

    a) RPM-based operating system:

      .. code-block:: console

        # chkconfig --add cyb3rhq-indexer
        # service cyb3rhq-indexer start
    
    b) Debian-based operating system:

      .. code-block:: console

        # update-rc.d cyb3rhq-indexer defaults 95 10
        # service cyb3rhq-indexer start

.. End of include file
