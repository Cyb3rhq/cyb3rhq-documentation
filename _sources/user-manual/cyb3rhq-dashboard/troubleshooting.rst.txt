.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: This section of the Cyb3rhq documentation lists the common installation or usage issues with the Cyb3rhq dashboard and how to resolve them.

.. _cyb3rhq_dashboard_troubleshooting:

Troubleshooting
===============

This section collects common installation or usage issues on the Cyb3rhq dashboard, and some basic steps to solve them.

Cyb3rhq API seems to be down
--------------------------

This issue means that your Cyb3rhq API might be unavailable. Check the status of the Cyb3rhq manager to check if the service is active:

.. include:: /_templates/installations/cyb3rhq/common/check_cyb3rhq_manager.rst

If the Cyb3rhq API is running, try to fetch data using the CLI from the Cyb3rhq dashboard server:

.. code-block:: console

  # curl -k -X GET "https://<api_url>:55000/" -H "Authorization: Bearer $(curl -u <api_user>:<api_password> -k -X POST 'https://<api_url>:55000/security/user/authenticate?raw=true')"

.. code-block:: console
  :class: output

    % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
    100   271  100   271    0     0    879      0 --:--:-- --:--:-- --:--:--   882
    {"data": {"title": "Cyb3rhq API REST", "api_version": "4.1.1", "revision": 40110, "license_name": "GPL 2.0", "license_url": "https://github.com/cyb3rhq/cyb3rhq/blob/4.1/LICENSE", "hostname": "localhost.localdomain", "timestamp": "2021-03-03T10:01:18+0000"}, "error": 0}



I do not see alerts in the Cyb3rhq dashboard
------------------------------------------

The first step is to check if there are alerts in Cyb3rhq indexer.

.. code-block:: console

  # curl https://<CYB3RHQ_INDEXER_IP>:9200/_cat/indices/cyb3rhq-alerts-* -u <cyb3rhq_indexer_user>:<cyb3rhq_indexer_password> -k

.. code-block:: none
    :class: output

     green open cyb3rhq-alerts-4.x-2021.03.03 xwFPX7nFQxGy-O5aBA3LFQ 3 0 340 0 672.6kb 672.6kb

If you do not see any Cyb3rhq related index, it means you have no alerts stored in Cyb3rhq indexer.

To ensure that Filebeat is correctly configured, run the following command:

.. code-block:: console

  # filebeat test output

.. code-block:: none
          :class: output

          elasticsearch: https://127.0.0.1:9200...
            parse url... OK
            connection...
              parse host... OK
              dns lookup... OK
              addresses: 127.0.0.1
              dial up... OK
            TLS...
              security: server's certificate chain verification is enabled
              handshake... OK
              TLS version: TLSv1.3
              dial up... OK
            talk to server... OK
            version: 7.10.2



Could not connect to API with id: default: 3003 - Missing param: API USERNAME
-----------------------------------------------------------------------------

Starting Cyb3rhq 4.0 the Cyb3rhq API username variable changed from ``user`` to ``username``. It's necessary to change the credentials (foo:bar are no longer accepted) as well as the name of the variable in the ``/usr/share/cyb3rhq-dashboard/data/cyb3rhq/config/cyb3rhq.yml`` configuration file. For example, the configuration can be:

.. code-block:: console

   hosts:
    - production:
        url: https://127.0.0.1
        port: 55000
        username: cyb3rhq-wui
        password: cyb3rhq-wui
        run_as: false


"Cyb3rhq API and Cyb3rhq dashboard version mismatch" error is displayed
-------------------------------------------------------------------

This error shows a mismatch between the Cyb3rhq server and the Cyb3rhq dashboard versions.

The Cyb3rhq server and the Cyb3rhq dashboard must run the same major and minor versions. For example:

-  `Cyb3rhq server |CYB3RHQ_CURRENT_MINOR|.x`
-  `Cyb3rhq dashboard |CYB3RHQ_CURRENT_MINOR|.y`

Moreover, we recommend both server and dashboard run the same full version, for example |CYB3RHQ_CURRENT|. Running the same full version ensures the correct operation and communication between these components.

Check out how to upgrade Cyb3rhq in our :doc:`upgrade guide</upgrade-guide/index>`.

Saved object for index pattern not found
----------------------------------------

Saved objects store data for later use, including dashboards, visualizations, maps, index patterns, and more.

This message indicates that there is a problem loading the information of an index pattern which should be stored in a saved object, but the dashboard is unable to find it.

This situation can happen if the indexer is reinstalled and the previously saved objects are lost, while the dashboard is running and is not restarted in the process.

Remediation
^^^^^^^^^^^

The dashboard initializes the saved objects with the index definitions when it starts, so the suggested solution is to restart the service to initialize the saved objects again.

#. Restart the Cyb3rhq dashboard service.

   .. include:: /_templates/common/restart_dashboard.rst

   This will initialize the index with the required mappings.

   .. note:: If the index contains data but has missing objects, the dashboard will migrate the data to a new index with the missing objects added.

If the restart does not solve the problem, we can execute this process manually:

#. Stop the Cyb3rhq dashboard service.

   .. tabs::

      .. group-tab:: Systemd

         .. code-block:: console

            # systemctl stop cyb3rhq-dashboard

      .. group-tab:: SysV

         .. code-block:: console

            # service cyb3rhq-dashboard stop

#. Identify the index or indices that have the wrong field mappings, this depends on the logged user that experiences the problem or the selected tenant. By default, the index name should start with ``.kibana``.

#. Get the field mapping for the ``type`` field for the indices that store the saved objects.

   .. code-block:: console

      # curl https://<CYB3RHQ_INDEXER_IP>:9200/.kibana*/_mapping/field/type?pretty -u <cyb3rhq_indexer_user>:<cyb3rhq_indexer_password> -k

   .. code-block:: none
     :class: output
     :emphasize-lines: 8,10,11,26,28,29

     {
       ".kibana" : {
         "mappings" : {
           "type" : {
             "full_name" : "type",
             "mapping" : {
               "type" : {
                 "type" : "text",
                 "fields" : {
                   "keyword" : {
                     "type" : "keyword",
                     "ignore_above" : 256
                   }
                 }
               }
             }
           }
         }
       },
       ".kibana_92668751_admin_1" : {
         "mappings" : {
           "type" : {
             "full_name" : "type",
             "mapping" : {
               "type" : {
                 "type" : "text",
                 "fields" : {
                   "keyword" : {
                     "type" : "keyword",
                     "ignore_above" : 256
                   }
                 }
               }
             }
           }
         }
       }
     }


   In the output, we can see `type` field mapping for the ``.kibana`` and ``.kibana_92668751_admin_1`` indices.  Note that the field mapping type for the `type` field is ``text`` and that it contains a subfield called `keyword`. This is not the expected result, the `type` field should be ``keyword``, not ``text``, and it should not include the `keyword` subfield.

   These errors happened because there was no template that specified the appropriate field mappings at the time the saved object data was indexed. To solve the errors, we need to remove the index and rebuild it.

#. Delete the index or indices that store the saved objects with the wrong field mapping.

   .. code-block:: console

      # curl https://<CYB3RHQ_INDEXER_IP>:9200/<INDEX/INDICES_SEPARATED_BY_COMMAS> -u <cyb3rhq_indexer_user>:<cyb3rhq_indexer_password> -k -XDELETE

   .. code-block:: none
      :class: output

      {“acknowledged”:true}


#. Restart the Cyb3rhq dashboard service.

   .. include:: /_templates/common/restart_dashboard.rst

.. note:: These actions take into account that the index that stores the saved objects must have valid field mappings. The field mappings are defined through a template, so they should exist before the index is created. This template is added when Cyb3rhq dashboard starts if it doesn’t exist.

Application Not Found
---------------------

If you encounter the message *Application Not Found* when accessing the Cyb3rhq dashboard after upgrading, it might be that the configuration file ``/etc/cyb3rhq-dashboard/opensearch_dashboards.yml`` wasn't overwritten with new changes. To resolve this issue, update the ``uiSettings.overrides.defaultRoute`` setting with the ``/app/wz-home`` value in the configuration file:

.. code-block:: none

   uiSettings.overrides.defaultRoute: /app/wz-home

None of the above solutions are fixing my problem
-------------------------------------------------

We have a welcoming community which can help you with most of the problems you might have regarding Cyb3rhq deployment and usage `<https://cyb3rhq.github.io/community>`_.

Also, you can contact us opening issues in our GitHub repositories under the `organization <https://github.com/cyb3rhq>`_.

We will  be interested in the log files of your deployment. You can check them out on each component:

Check the following log files:

      - Cyb3rhq indexer:

      .. code-block:: console

          # cat /var/log/cyb3rhq-indexer/cyb3rhq-cluster.log | grep -i -E "error|warn"

      - Cyb3rhq manager:

      .. code-block:: console

          # cat /var/log/filebeat/filebeat | grep -i -E "error|warn"

          # cat /var/ossec/logs/ossec.log | grep -i -E "error|warn"

      - Cyb3rhq dashboard:

      .. code-block:: console

          # journalctl -u cyb3rhq-dashboard

          # journalctl -u cyb3rhq-dashboard | grep -i E "error|warn"

    .. note::
      The Cyb3rhq indexer uses the ``/var/log`` folder to store logs by default.

    .. warning::
      By default, the Cyb3rhq dashboard doesn't store logs on a file. You can change this by configuring ``logging.dest`` setting in the ``opensearch_dashboard.yml`` configuration file.
