.. Copyright (C) 2022 Cyb3rhq, Inc.

rbac_control
============

.. versionadded:: 4.6.0

The ``rbac_control`` tool allows managing resources from the Cyb3rhq RBAC database and resetting the DB to its default state. For more information about the Cyb3rhq RBAC resources and database, please visit the
:doc:`How it works </user-manual/api/rbac/how-it-works>` section.

Usage
-----

+-----------------------------------------+----------------------------------------------------------------------------------------------------------+
| Option name                             | Option description                                                                                       |
+=========================================+==========================================================================================================+
| ``-h, --help``                          | Display the help message.                                                                                |
+-----------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``change-password``                     | Change the password for each default user.                                                               |
+-----------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``factory-reset``                       | Reset the RBAC database to its default state. Ask for confirmation unless the -f/--force flag is used.   |
+-----------------------------------------+----------------------------------------------------------------------------------------------------------+

Examples
--------

``-h`` argument:

.. code-block:: console

   # /var/ossec/bin/rbac_control -h

.. code-block:: console
   :class: output

   usage: rbac_control.py [-h] {change-password,factory-reset} ...

   Cyb3rhq RBAC tool: manage resources from the Cyb3rhq RBAC database

   Arguments:
     {change-password,factory-reset}
       change-password     Change the password for each default user. Empty values will leave the password unchanged.
       factory-reset       Reset the RBAC database to its default state. This will completely wipe your custom RBAC information.

   optional arguments:
     -h, --help            show this help message and exit


``factory-reset`` example:

.. code-block:: console

   # /var/ossec/bin/rbac_control factory-reset

.. code-block:: console
   :class: output

   This action will completely wipe your RBAC configuration and restart it to default values. Type RESET to proceed: RESET
       Successfully reset RBAC database

``factory-reset`` example (aborted):

.. code-block:: console

   # /var/ossec/bin/rbac_control factory-reset

.. code-block:: console
   :class: output

   This action will completely wipe your RBAC configuration and restart it to default values. Type RESET to proceed: aa
       RBAC database reset aborted.


``change-password`` example with an insecure password:

.. code-block:: console

   # /var/ossec/bin/rbac_control change-password

.. code-block:: console
   :class: output

   New password for 'cyb3rhq' (skip):
   New password for 'cyb3rhq-wui' (skip):
       cyb3rhq: FAILED | Error 5007 - Insecure user password provided


``change-password`` example where the `cyb3rhq` user password was changed successfully (to skip any of the user, leave the new password blank):

.. code-block:: console

   # /var/ossec/bin/rbac_control change-password

.. code-block:: console
   :class: output

   New password for 'cyb3rhq' (skip):
   New password for 'cyb3rhq-wui' (skip):
       cyb3rhq: UPDATED
