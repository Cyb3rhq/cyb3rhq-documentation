.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Cyb3rhq 4.5.4 has been released. Check out our release notes to discover the changes and additions of this release.

4.5.4 Release notes - 23 October 2023
=====================================

This section lists the changes in version 4.5.4. Every update of the Cyb3rhq solution is cumulative and includes all enhancements and fixes from previous releases.


What's new
----------

This version includes new features or improvements, such as the following:

Manager
^^^^^^^

- `#19729 <https://github.com/cyb3rhq/cyb3rhq/pull/19729>`__ Added a timeout on requests between components through the cluster.


Resolved issues
---------------

This release resolves known issues as the following: 

Manager
^^^^^^^

========================================================    ========================================================================================================
Reference                                                   Description
========================================================    ========================================================================================================
`#19702 <https://github.com/cyb3rhq/cyb3rhq/pull/19702>`__      Fixed a bug that might leave some worker's services hanging if the connection to the master was broken.
`#19706 <https://github.com/cyb3rhq/cyb3rhq/pull/19706>`__      Fixed vulnerability scan on Windows agent when the OS version has no release data. 
========================================================    ========================================================================================================


Changelogs
----------

More details about these changes are provided in the changelog of each component:

-  `cyb3rhq/cyb3rhq <https://github.com/cyb3rhq/cyb3rhq/blob/v4.5.4/CHANGELOG.md>`_
-  `cyb3rhq/cyb3rhq-dashboard <https://github.com/cyb3rhq/cyb3rhq-dashboard-plugins/blob/v4.5.4-2.6.0/CHANGELOG.md>`_
-  `cyb3rhq/cyb3rhq-dashboard-plugins 7.10.2 <https://github.com/cyb3rhq/cyb3rhq-dashboard-plugins/blob/v4.5.4-7.10.2/CHANGELOG.md>`_
-  `cyb3rhq/cyb3rhq-dashboard-plugins 7.16.x <https://github.com/cyb3rhq/cyb3rhq-dashboard-plugins/blob/v4.5.4-7.16.3/CHANGELOG.md>`_
-  `cyb3rhq/cyb3rhq-dashboard-plugins 7.17.x <https://github.com/cyb3rhq/cyb3rhq-dashboard-plugins/blob/v4.5.4-7.17.13/CHANGELOG.md>`_
-  `cyb3rhq/cyb3rhq-splunk <https://github.com/cyb3rhq/cyb3rhq-splunk/blob/v4.5.4-8.2/CHANGELOG.md>`_
-  `cyb3rhq/cyb3rhq-packages <https://github.com/cyb3rhq/cyb3rhq-packages/releases/tag/v4.5.4>`_