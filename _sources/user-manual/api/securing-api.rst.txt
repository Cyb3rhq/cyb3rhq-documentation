.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: The communication between the Cyb3rhq dashboard and the Cyb3rhq server API is encrypted with HTTPS by default. learn more in this section of the documentation.

Securing the Cyb3rhq server API
=============================

The communication between the Cyb3rhq dashboard and the Cyb3rhq server API is encrypted with HTTPS by default. The Cyb3rhq server API will generate its own private key and certificate during the first run if users do not supply them. Additionally, the Cyb3rhq server API automatically creates the following username-password pair when installed with the OVA installation:

-  ``cyb3rhq:cyb3rhq``
-  ``cyb3rhq-wui:cyb3rhq-wui``

If the Cyb3rhq deployment was performed using the installation assistant script, the Cyb3rhq API username is ``cyb3rhq`` and you can extract the password by running the following command:

.. code-block:: console

   # tar -axf cyb3rhq-install-files.tar cyb3rhq-install-files/cyb3rhq-passwords.txt -O | grep -P "\'cyb3rhq\'" -A 1

Therefore, securing the Cyb3rhq server API is crucial after installing the Cyb3rhq manager.

.. warning::

   We highly recommend changing the default passwords and to use your own certificate since the one created by the Cyb3rhq server API is self-signed.

Recommended changes to secure the Cyb3rhq server API
--------------------------------------------------

1. Modify HTTPS parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^

The Cyb3rhq server API has HTTPS enabled by default. If there is no available certificate in ``/var/ossec/api/configuration/ssl/``, the Cyb3rhq server will generate the private key and a self-signed certificate when it is started. If that is the case and the API log format is set as ``plain``, the following lines will appear in ``/var/ossec/logs/api.log``:

.. code-block:: none

   INFO: HTTPS is enabled but cannot find the private key and/or certificate. Attempting to generate them.
   INFO: Generated private key file in CYB3RHQ_PATH/api/configuration/ssl/server.key.
   INFO: Generated certificate file in CYB3RHQ_PATH/api/configuration/ssl/server.crt.

You can change these HTTPS options, including their status or the path to the certificate, by editing the Cyb3rhq server API configuration file located at ``/var/ossec/api/configuration/api.yaml``:

.. code-block:: yaml

   https:
     enabled: yes
     key: "server.key"
     cert: "server.crt"
     use_ca: False
     ca: "ca.crt"
     ssl_protocol: "auto"
     ssl_ciphers: ""

Restart the Cyb3rhq server API using the Cyb3rhq manager service to apply the changes:

.. include:: /_templates/common/restart_manager.rst

2. Change the default password for the administrative users
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can change the default password for the administrative users  ``cyb3rhq`` and ``cyb3rhq-wui`` using the following Cyb3rhq server API request: :api-ref:`PUT /security/users/{user_id} <operation/api.controllers.security_controller.update_user>`.

.. note::

   The password for users must be between 8 and 64 characters long. It should contain at least one uppercase, lowercase letter, number, and symbol.

**We show an example of changing the password  using curl below**:

#. Get a list of users along with their user IDs:

   .. code-block:: console

      # curl -k -X GET "https://localhost:55000/security/users?pretty=true" -H  "Authorization: Bearer $TOKEN"

#. Change the password of the desired user:

   .. code-block:: console

      # curl -k -X PUT "https://localhost:55000/security/users/<USER_ID>" -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{"password": "<NEW_PASSWORD>"}'

   Replace ``<USER_ID>`` with the user’s ID and ``<NEW_PASSWORD>`` with the new password.

   .. warning::

      Changing the ``cyb3rhq-wui`` user password will affect the Cyb3rhq dashboard. You will have to update the ``/usr/share/cyb3rhq-dashboard/data/cyb3rhq/config/cyb3rhq.yml`` configuration file accordingly with the new credentials. To learn more, see the :doc:`Cyb3rhq dashboard configuration file </user-manual/cyb3rhq-dashboard/config-file>` document.

3. Change the default host and port
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, the ``host`` is set to ``0.0.0.0``, allowing the Cyb3rhq server API to accept incoming connections on all available network interfaces. To restrict access, edit the Cyb3rhq server API configuration in ``/var/ossec/api/configuration/api.yaml``:

.. code-block:: yaml

   host: 0.0.0.0

You can also change the default port:

.. code-block:: yaml

   port: 55000

After configuring these parameters, restart the Cyb3rhq server API using the Cyb3rhq manager service with Systemd or SysV init:

.. include:: /_templates/common/restart_manager.rst

4. Set maximum number of requests per minute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To prevent overloading the Cyb3rhq server API, you can implement rate limiting to establish the maximum number of requests the API can handle per minute. If this limit is exceeded, the API will reject further requests from any user for the rest of the period.

The default limit is 300 requests per minute. Adjust this by changing the ``max_request_per_minute`` setting in ``/var/ossec/api/configuration/api.yaml``.

.. note::

   To disable rate limiting, set its value to 0.

5. Set maximum number of login attempts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To protect against brute force attacks, you can limit login attempts from the same IP address within a specific timeframe. Exceeding this limit blocks the IP address for the duration of that period.

By default, you're allowed 50 login attempts per 300-second period. To adjust these limits, edit the ``max_login_attempts`` and/or ``block_time`` settings in ``/var/ossec/api/configuration/api.yaml``.

You can find a complete Cyb3rhq server API configuration guide :doc:`here <configuration>`.