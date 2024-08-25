.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: This section collects common issues that might occur when upgrading central components and provides steps to resolve them.

Troubleshooting
===============

This section collects common issues that might occur when upgrading the Cyb3rhq central components and provides steps to resolve them.

The 'vulnerability-detector' configuration is deprecated
--------------------------------------------------------

This warning appears because when upgrading the Cyb3rhq manager, the ``/var/ossec/etc/ossec.conf`` file remains unchanged, retaining the previous configuration of the Cyb3rhq Vulnerability Detection module. In addition, invalid configuration warnings might appear for the ``interval``, ``min_full_scan_interval``, ``run_on_start`` and ``provider`` elements. To resolve this issue, update the configuration as specified in :doc:`/user-manual/capabilities/vulnerability-detection/configuring-scans`.

No username and password found in the keystore
----------------------------------------------

To ensure that alerts and vulnerabilities detected by the Cyb3rhq Vulnerability Detection module are indexed and displayed on the Cyb3rhq dashboard, you need to add the credentials of the Cyb3rhq indexer to the Cyb3rhq manager keystore. In case you've forgotten your Cyb3rhq indexer password, follow the :doc:`password management </user-manual/user-administration/password-management>` guide to reset the password.

.. code-block:: console

   # echo '<INDEXER_USERNAME>' | /var/ossec/bin/cyb3rhq-keystore -f indexer -k username
   # echo '<INDEXER_PASSWORD>' | /var/ossec/bin/cyb3rhq-keystore -f indexer -k password

IndexerConnector initialization failed
--------------------------------------

This warning might be due to incorrect keystore credentials or indicate a configuration or certificate error. To resolve this, ensure that the IP address, port, and certificate paths are configured correctly in the :doc:`indexer section</user-manual/reference/ossec-conf/indexer>` in ``/var/ossec/etc/ossec.conf``.

After fixing the error and successfully connecting the Cyb3rhq manager to the Cyb3rhq indexer, you can see a log similar to the following:

.. code-block:: none

   INFO: IndexerConnector initialized successfully for index: ...

To get more information if the error persists, temporarily enable ``cyb3rhq_modules.debug=2`` in ``/var/ossec/etc/local_internal_options.conf``.

Vulnerability detection seems to be disabled or has a problem
-------------------------------------------------------------

This warning indicates that the Vulnerability Detection module might be disabled or there could be a configuration error. To troubleshoot:

#. Ensure that ``vulnerability-detection`` is enabled in ``/var/ossec/etc/ossec.conf``.
#. Search for ``<indexer>`` block in ``/var/ossec/etc/ossec.conf`` and ensure there are no misconfigurations or multiple blocks of the :doc:`indexer </user-manual/reference/ossec-conf/indexer>` section.
#. Verify that the vulnerability index ``cyb3rhq-states-vulnerabilities-*`` has been correctly created. You can check this under **Indexer Management** > **Index Management** > **Indices** configuration.
#. If the index wasn't created, check the Cyb3rhq manager logs for any errors or warnings, as the issue might be related to errors mentioned in previous sections:

   .. code-block:: console

      # cat /var/ossec/logs/ossec.log | grep -i -E "error|warn"

Application Not Found
---------------------

If you encounter the message *Application Not Found* when accessing the Cyb3rhq dashboard after upgrading, it might be that the configuration file ``/etc/cyb3rhq-dashboard/opensearch_dashboards.yml`` wasn't overwritten with new changes. To resolve this issue, update the ``uiSettings.overrides.defaultRoute`` setting with the ``/app/wz-home`` value in the configuration file:

.. code-block:: none

   uiSettings.overrides.defaultRoute: /app/wz-home

None of the above solutions are fixing my problem
-------------------------------------------------

We have a welcoming community that can help you with most of the problems you might have regarding Cyb3rhq deployment and usage `<https://cyb3rhq.com/community>`_.

Also, you can contact us for opening issues in our GitHub repositories under the `organization <https://github.com/cyb3rhq>`_.

When reporting a problem, add as much information as possible, such as version, operating system or relevant logs.
