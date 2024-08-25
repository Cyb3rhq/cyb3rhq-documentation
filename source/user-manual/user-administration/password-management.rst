.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Learn how to use the Cyb3rhq passwords tool to manage your passwords and secure your Cyb3rhq installation.

Password management
===================

.. note::

   If you deployed Cyb3rhq on Docker, read :ref:`change-pwd-existing-usr` for specific instructions.

Learn how to use the Cyb3rhq passwords tool to manage your passwords. This tool allows you to change the passwords of both the :doc:`Cyb3rhq indexer </getting-started/components/cyb3rhq-indexer>` users, also known as internal users, and the :doc:`Cyb3rhq manager API </user-manual/api/index>`  users.

Among the Cyb3rhq indexer users, it is worth mentioning the following:

- *admin*: is the default administrator user. It's used to log in to the web interface and for communications between Filebeat and the Cyb3rhq indexer. If you change the *admin* password, you must update it in Filebeat and the Cyb3rhq server.

- *kibanaserver*: is used for communications between the Cyb3rhq dashboard and the Cyb3rhq indexer. If you change the *kibanaserver* password, you must update it in the Cyb3rhq dashboard.

On the other hand, the Cyb3rhq manager API has two default users:

- *cyb3rhq*: is the default Cyb3rhq manager API administrator user.

- *cyb3rhq-wui*: is an admin user used for communications between Cyb3rhq dashboard and the Cyb3rhq manager API. If you change the *cyb3rhq-wui* password, you must update it in the Cyb3rhq dashboard.

If you use the tool in an all-in-one deployment, it automatically updates the passwords where necessary.  If you use it in a distributed environment, depending on the user whose password you change, you may have to update the password on other components. See  :ref:`Changing the passwords in a distributed environment <passwords_distributed>` for more details.

The passwords tool is embedded in the Cyb3rhq indexer under ``/usr/share/cyb3rhq-indexer/plugins/opensearch-security/tools/``. You can use the embedded version or download it with the following command:

  .. code-block:: console

    # curl -so cyb3rhq-passwords-tool.sh https://packages.cyb3rhq.com/|CYB3RHQ_CURRENT_MINOR|/cyb3rhq-passwords-tool.sh


All the available options to run the script are:

+----------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| Options                                      | Purpose                                                                                                     |
+==============================================+=============================================================================================================+
| -a / --change-all                            | Changes all the Cyb3rhq indexer and Cyb3rhq API user passwords and prints them on screen.                       |
|                                              | To change API passwords -au|--admin-user and -ap|--admin-password are required.                             |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| -A,  --api                                   | Change the Cyb3rhq API password given the current password.                                                   |
|                                              | Requires -u|--user, and -p|--password, -au|--admin-user and -ap|--admin-password.                           |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| -au,--admin-user <adminUser>                 | Admin user for the Cyb3rhq API. Required for changing the Cyb3rhq API passwords.                                |
|                                              | Requires -A|--api.                                                                                          |               
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| -ap, --admin-password <adminPassword>        | Password for the Cyb3rhq API admin user. Required for changing the Cyb3rhq API passwords.                       |
|                                              | Requires -A|--api.                                                                                          |      
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| -u / --user <user>                           | Indicates the name of the user whose password will be changed.                                              |
|                                              | If no password is specified, it will generate a random one.                                                 |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| -p / --password <password>                   | Indicates the new password. Must be used with option -u.                                                    |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| -c / --cert <route-admin-certificate>        | Indicates route to the admin certificate.                                                                   |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| -k / --certkey <route-admin-certificate-key> | Indicates route to the admin certificate key.                                                               |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| -v / --verbose                               | Shows the complete script execution output.                                                                 |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| -f / --file <password_file.yml>              | Changes the passwords for the ones given in the file.                                                       |
|                                              |                                                                                                             |
|                                              | Cyb3rhq indexer users must have this format:                                                                  |
|                                              |                                                                                                             |
|                                              |    # Description                                                                                            |
|                                              |      indexer_username: <user>                                                                               |
|                                              |      indexer_password: <password>                                                                           |
|                                              |                                                                                                             |
|                                              | Cyb3rhq API users must have this format:                                                                      |
|                                              |                                                                                                             |
|                                              |    # Description                                                                                            |
|                                              |     api_username: <user>                                                                                    |
|                                              |      api_password: <password>                                                                               |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| -gf, --generate-file <passwords.cyb3rhq>       | Generate password file with random passwords for standard users.                                            |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| -h / --help                                  | Shows help.                                                                                                 |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------+

Changing the password for single user
-------------------------------------

To change the password for a single Cyb3rhq indexer user, run the script with the ``-u`` option and indicate the new password with the option ``-p``. The password must have a length between 8 and 64 characters and contain at least one upper case letter, one lower case letter, a number and one of the following symbols: ``.*+?-``. If no password is specified, the script will generate a random one.


   .. code-block:: console

      # bash cyb3rhq-passwords-tool.sh -u admin -p Secr3tP4ssw*rd


   .. code-block:: console
      :class: output

      INFO: Generating password hash
      WARNING: Password changed. Remember to update the password in the Cyb3rhq dashboard and Filebeat nodes if necessary, and restart the services.

If you use the tool in an all-in-one deployment, it automatically updates the passwords where necessary.  If you use it in a distributed environment, depending on the user whose password you change, you may have to update the password on other components. See :ref:`Changing the passwords in a distributed environment <passwords_distributed>` for more details.

If you want to change the password for a Cyb3rhq manager API user, run the script on a Cyb3rhq server node and use option ``-A, --api``. Alternatively, you can change the Cyb3rhq manager API passwords following the instructions in the :doc:`Securing the Cyb3rhq API </user-manual/api/securing-api>` documentation.

.. note:: If you want to change the password for Filebeat in the Cyb3rhq server, you don't need to use option ``-A, --api``.

Changing the passwords for all users
------------------------------------

To generate and change passwords for all the Cyb3rhq indexer users, run the script with the ``-a`` option:

  .. code-block:: console

    # bash cyb3rhq-passwords-tool.sh -a

  .. code-block:: console
    :class: output
    :emphasize-lines: 2,3

    INFO: Cyb3rhq API admin credentials not provided, Cyb3rhq API passwords not changed.
    INFO: The password for user admin is kwd139yG?YoIK?lRnqcXQ4R4gJDlAqKn
    INFO: The password for user kibanaserver is Bu1WIELh9RdRlf*oGjinN1?yhF6XzA7V
    INFO: The password for user kibanaro is 7kZvau11cPn6Y1SbOsdr8Kwr*BRiK3u+
    INFO: The password for user logstash is SUbk4KTmLl*geQbUg0c5tyfwahjDMhx5
    INFO: The password for user readall is ?w*Itj1Lgz.5w.C7vOw0Kxi7G94G8bG*
    INFO: The password for user snapshotrestore is Z6UXgM8Sr0bfV.i*6yPPEUY3H6Du2rdz
    WARNING: Cyb3rhq indexer passwords changed. Remember to update the password in the Cyb3rhq dashboard, Cyb3rhq server, and Filebeat nodes if necessary, and restart the services.

If you use the tool in an all-in-one deployment, it automatically updates the passwords where necessary, including the Filebeat password in the Cyb3rhq server:

  .. code-block:: console
    :class: output
    :emphasize-lines: 2,3,4

    INFO: Cyb3rhq API admin credentials not provided, Cyb3rhq API passwords not changed.
    INFO: The new password for Filebeat is kwd139yG?YoIK?lRnqcXQ4R4gJDlAqKn
    INFO: The password for user admin is kwd139yG?YoIK?lRnqcXQ4R4gJDlAqKn
    INFO: The password for user kibanaserver is Bu1WIELh9RdRlf*oGjinN1?yhF6XzA7V
    INFO: The password for user kibanaro is 7kZvau11cPn6Y1SbOsdr8Kwr*BRiK3u+
    INFO: The password for user logstash is SUbk4KTmLl*geQbUg0c5tyfwahjDMhx5
    INFO: The password for user readall is ?w*Itj1Lgz.5w.C7vOw0Kxi7G94G8bG*
    INFO: The password for user snapshotrestore is Z6UXgM8Sr0bfV.i*6yPPEUY3H6Du2rdz
    WARNING: Cyb3rhq indexer passwords changed. Remember to update the password in the Cyb3rhq dashboard, Cyb3rhq server, and Filebeat nodes if necessary.


If you use it in a distributed environment, you have to update the password on other components. See :ref:`Changing the passwords in a distributed environment <passwords_distributed>` for more details.

On an all-in-one deployment, use options ``-a``, ``-au`` and ``-ap`` to also change the passwords for all the Cyb3rhq indexer and the Cyb3rhq manager API users.

   .. code-block:: console

      # sudo bash cyb3rhq-passwords-tool.sh -a -au cyb3rhq -ap KTb+Md+rR74J2yHfoGGnFGHGm03Gadyu


   .. code-block:: console
      :class: output
      :emphasize-lines: 1,2,3,9,10

      INFO: The new password for Filebeat is Wkw+b2rM6BEOwUmGfr*m*i1ithWw.dg2
      INFO: The password for user admin is Wkw+b2rM6BEOwUmGfr*m*i1ithWw.dg2
      INFO: The password for user kibanaserver is 5Y0lIfCwmjkus9nWAAVxMInI+Eth25hr
      INFO: The password for user kibanaro is kJG7fHX18.UJIZoNip5nDo*34DN+cGBL
      INFO: The password for user logstash is wuabgegtKsQABems5RNJfV0AOmxT?81T
      INFO: The password for user readall is gKSuQFGG.Sa0L9gzJX5WZHPP3Y4Es+sU
      INFO: The password for user snapshotrestore is UdyI8ToXkgVCNOPfJ*FX*a5vybeB.rUw
      WARNING: Cyb3rhq indexer passwords changed. Remember to update the password in the Cyb3rhq dashboard, Cyb3rhq server, and Filebeat nodes if necessary, and restart the services.
      INFO: The password for Cyb3rhq API user cyb3rhq is zG0yTsAiettOXWEB79Aca1jbQ5.UeW3M
      INFO: The password for Cyb3rhq API user cyb3rhq-wui is JmKiaCBQo?4Ne0yrM4+n7kGdXGfCmVjO
      INFO: Updated cyb3rhq-wui user password in cyb3rhq dashboard. Remember to restart the service.




Changing the passwords using a formatted file
---------------------------------------------

Use a formatted file to indicate the passwords and run the script with the ``-f`` option followed by the file path. Use the following pattern to indicate the users and passwords in the formatted file.

For Cyb3rhq indexer users:

  .. code-block:: none

    # Description
      indexer_username: <user>
      indexer_password: <password>

For Cyb3rhq manager API users:

  .. code-block:: none

    # Description
      api_username: <user>
      api_password: <password>

If the ``-a`` option is used in combination with the ``-f`` option, all users not included in the file are given a random password.

The options ``-au`` and ``-ap`` are necessary to change the passwords for the API users.

.. _passwords_distributed:

Changing the passwords in a distributed environment
---------------------------------------------------

Follow the instructions below to change the passwords for all Cyb3rhq indexer users, Cyb3rhq manager API users, and the Cyb3rhq dashboard user.

#. On `any Cyb3rhq indexer node`, use the Cyb3rhq passwords tool to change the passwords of the Cyb3rhq indexer users.

   .. code-block:: console

      # /usr/share/cyb3rhq-indexer/plugins/opensearch-security/tools/cyb3rhq-passwords-tool.sh --change-all

   .. code-block:: console
      :class: output
      :emphasize-lines: 2,3

      INFO: Cyb3rhq API admin credentials not provided, Cyb3rhq API passwords not changed.
      INFO: The password for user admin is wcAny.XUwOVWHFy.+7tW9l8gUW1L8N3j
      INFO: The password for user kibanaserver is qy6fBrNOI4fD9yR9.Oj03?pihN6Ejfpp
      INFO: The password for user kibanaro is Nj*sSXSxwntrx3O7m8ehrgdHkxCc0dna
      INFO: The password for user logstash is nQg1Qw0nIQFZXUJc8r8+zHVrkelch33h
      INFO: The password for user readall is s0iWAei?RXObSDdibBfzSgXdhZCD9kH4
      INFO: The password for user snapshotrestore is Mb2EHw8SIc1d.oz.nM?dHiPBGk7s?UZB
      WARNING: Cyb3rhq indexer passwords changed. Remember to update the password in the Cyb3rhq dashboard, Cyb3rhq server, and Filebeat nodes if necessary, and restart the services.

#. On *all your Cyb3rhq server nodes*, download the Cyb3rhq passwords tool and use it to change the passwords for Filebeat and Cyb3rhq API users. Replace ``<CYB3RHQ_PASSWORD>`` with the *cyb3rhq* user password. 

   .. code-block:: console

      # curl -sO https://packages.cyb3rhq.com/|CYB3RHQ_CURRENT_MINOR|/cyb3rhq-passwords-tool.sh
      # bash cyb3rhq-passwords-tool.sh --api --change-all --admin-user cyb3rhq --admin-password <CYB3RHQ_PASSWORD>
  
   .. code-block:: console
      :class: output

      INFO: The password for Cyb3rhq API user cyb3rhq is ivLOfmj7.jL6*7Ev?UJoFjrkGy9t6Je.
      INFO: The password for Cyb3rhq API user cyb3rhq-wui is fL+f?sFRPEv5pYRE559rqy9b6G4Z5pVi
      INFO: The new password for Filebeat is Wkw+b2rM6BEOwUmGfr*m*i1ithWw.dg2

   .. note::
      
      You must perform this step on *every Cyb3rhq server node*.


#. If you've set up a user other than ``admin`` for Filebeat, manually add the username and password using the following commands. Replace ``<CUSTOM_USERNAME>`` and ``<CUSTOM_PASSWORD>`` with your custom username and password.

   .. code-block:: console

      # echo <CUSTOM_USERNAME> | filebeat keystore add username --stdin --force
      # echo <CUSTOM_PASSWORD> | filebeat keystore add password --stdin --force
         
   Restart Filebeat to apply the changes.

   .. include:: /_templates/common/restart_filebeat.rst
       
#. On your `Cyb3rhq dashboard node`, run the following command to update the `kibanaserver` password in the Cyb3rhq dashboard keystore. Replace ``<KIBANASERVER_PASSWORD>`` with the random password generated in the first step.

   .. code-block:: console

      # curl -sO https://packages.cyb3rhq.com/|CYB3RHQ_CURRENT_MINOR|/cyb3rhq-passwords-tool.sh
      # bash cyb3rhq-passwords-tool.sh --user kibanaserver --password <KIBANASERVER_PASSWORD>
   
   .. code-block:: console
      :class: output

      INFO: The password for the kibanaserver user in the dashboard has been updated to 'EKf49pm3QtqszKgWiz.HRfEc5adN7QFY' necessary.

#. Again, on your `Cyb3rhq dashboard node`, run the following command to update the *cyb3rhq-wui* password in the Cyb3rhq dashboard keystore. Replace ``<CYB3RHQ-WUI_PASSWORD>`` with the random password generated in the second step. Use the ``-A`` or ``--api`` option to change the password for the ``cyb3rhq-wui`` user in the Cyb3rhq dashboard node.

   .. code-block:: console

      # bash cyb3rhq-passwords-tool.sh --api --user cyb3rhq-wui --password <CYB3RHQ-WUI_PASSWORD>

   .. code-block:: console
      :class: output

      INFO: Updated cyb3rhq-wui user password in cyb3rhq dashboard to 'r7jH.SQ4SMqbzVXcbJrkiyrwvWd+G*w8'.
