.. Copyright (C) 2022 Cyb3rhq, Inc.
.. meta::
  :description: Learn more about how to manually restore a Cyb3rhq-DB backup in the Cyb3rhq server administration section of our documentation.

.. _manual_backup_restore:

Cyb3rhq-DB backup restoration
===========================

Cyb3rhq by default performs automatic backups of the **global.db** database. These snapshots may be useful to recover critical information.
Cyb3rhq-DB will restore the last backup available in case of failure during the upgrade. If this process also fails, the restoration must be done manually.

Manual restore process
----------------------

The first step is to turn off Cyb3rhq manager:

  a. For Systemd:

  .. code-block:: console

    # systemctl stop cyb3rhq-manager

  b. For SysV Init:

  .. code-block:: console

    # service cyb3rhq-manager stop

Then, locate the backup to restore. It is stored in ``CYB3RHQ_HOME/backup/db`` with a name format similar to ``global.db-backup-TIMESTAMP-pre_upgrade.gz``.

.. note::
  This process is valid for all the backups in the folder. Snapshots names containing the special tag `pre_upgrade` were created right before upgrading the Cyb3rhq server. Any other snapshot is a periodical backup created according to the :ref:`backup <cyb3rhq-db-config>` setting.

Decompress it. Always use the **-k** flag to preserve the original file:

  .. code-block:: console

    # gzip -dk CYB3RHQ_HOME/backup/db/global.db-backup-TIMESTAMP-pre_upgrade.gz

Remove the current **global.db** database and move the backup to the right location:

  .. code-block:: console

     # rm  CYB3RHQ_HOME/queue/db/global.db
     # mv  CYB3RHQ_HOME/backup/db/global.db-backup-TIMESTAMP-pre_upgrade CYB3RHQ_HOME/queue/db/global.db

And finally, start Cyb3rhq:

  a. For Systemd:

  .. code-block:: console

    # systemctl start cyb3rhq-manager

  b. For SysV Init:

  .. code-block:: console

    # service cyb3rhq-manager start
