.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: The Cyb3rhq dashboard gives you a quick view of your agents, alerts, and cluster. Learn how to configure its features in this section. 
  
Dashboard management
========================

The **Dashboard management** section allows you to do the following:

-  Configure and customize your Cyb3rhq dashboard experience.

   -  `Dashboards Management`_
   -  `Server APIs`_
   -  `App Settings`_

-  View generated reports.

   -  `Reporting`_

Dashboards Management
---------------------

Index patterns
^^^^^^^^^^^^^^

In this section, you can list, configure, and create new index patterns. Index patterns are templates defining data organization for efficient retrieval and analysis.

.. thumbnail:: /images/kibana-app/features/settings/index-patterns.png
   :align: center
   :width: 80%

Saved objects
^^^^^^^^^^^^^

Saved objects of the application include:

-  Index patterns
-  Application settings
-  Custom visualizations and dashboards

.. thumbnail:: /images/kibana-app/features/settings/saved-objects.png
   :align: center
   :width: 80%

Advanced settings
^^^^^^^^^^^^^^^^^

In this section, you can configure advanced settings of the Cyb3rhq Dashboard such as the date format.

.. thumbnail:: /images/kibana-app/features/settings/advanced-settings.png
   :align: center
   :width: 80%

You can also switch the appearance to dark mode within advanced settings.
 
.. thumbnail:: /images/kibana-app/features/settings/dark-mode.png
   :align: center
   :width: 80%

Reporting
---------

Here, you can access the reports generated when clicked **Generate Report** in various modules.

.. thumbnail:: /images/kibana-app/features/settings/reporting.png
   :align: center
   :width: 80%

Server APIs
-----------

In this section, you can see information from all the Cyb3rhq servers configured in ``/usr/share/cyb3rhq-dashboard/data/cyb3rhq/config/cyb3rhq.yml``. This information includes:

-  ID
-  Cluster mode
-  Hostname
-  Version
-  *Run as* mode

It also includes connection information such as

-  Server host
-  API port
-  API connection status.

Additionally, it shows possible updates for each server.

.. thumbnail:: /images/kibana-app/features/settings/api.png
   :align: center
   :width: 80%

App Settings
-------------

Configuration
^^^^^^^^^^^^^

The Cyb3rhq dashboard configuration file is located at ``/usr/share/cyb3rhq-dashboard/data/cyb3rhq/config/cyb3rhq.yml``. You can take a look at the configuration parameters in the Cyb3rhq dashboard under **Configuration**.

.. thumbnail:: /images/kibana-app/features/settings/configuration.png
   :align: center
   :width: 80%


Miscellaneous
^^^^^^^^^^^^^

You can manually run the Cyb3rhq dashboard health check from this section. This health check assesses the operational status and performance of the Cyb3rhq dashboard.

.. thumbnail:: /images/kibana-app/features/settings/miscellaneous.png
   :align: center
   :width: 80%

About
-----

This section provides information about your currently installed Cyb3rhq dashboard package, including:

- Version
- Revision
- Installation date

To discover new features in each release, check the `Cyb3rhq dashboard changelog file <https://github.com/cyb3rhq/cyb3rhq-dashboard-plugins/blob/v|CYB3RHQ_CURRENT|-2.8.0/CHANGELOG.md>`__.

.. thumbnail:: /images/kibana-app/features/settings/about.png
   :align: center
   :width: 80%
