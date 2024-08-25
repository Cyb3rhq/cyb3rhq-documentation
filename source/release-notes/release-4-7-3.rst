.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Cyb3rhq 4.7.3 has been released. Check out our release notes to discover the changes and additions of this release.

4.7.3 Release notes - 4 March 2024
==================================

This section lists the changes in version 4.7.3. Every update of the Cyb3rhq solution is cumulative and includes all enhancements and fixes from previous releases.

Resolved issues
---------------

This release resolves known issues as the following:

Cyb3rhq manager
^^^^^^^^^^^^^

===========================================================  =============
 Reference                                                   Description
===========================================================  =============
`#21997 <https://github.com/cyb3rhq/cyb3rhq/pull/21997>`__       Resolved a transitive mutex locking issue in cyb3rhq-db that was impacting performance.
`#21977 <https://github.com/cyb3rhq/cyb3rhq/pull/21977>`__       Cyb3rhq DB internal SQL queries have been optimized by tuning database indexes to improve performance.
===========================================================  =============

Cyb3rhq dashboard
^^^^^^^^^^^^^^^

=======================================================================    =============
Reference                                                                  Description
=======================================================================    =============
`#6458 <https://github.com/cyb3rhq/cyb3rhq-dashboard-plugins/pull/6458>`__     Fixed an error when uploading CDB lists.
=======================================================================    =============

Changelogs
----------

More details about these changes are provided in the changelog of each component:

- `cyb3rhq/cyb3rhq <https://github.com/cyb3rhq/cyb3rhq/blob/v4.7.3/CHANGELOG.md>`__
- `cyb3rhq/cyb3rhq-dashboard <https://github.com/cyb3rhq/cyb3rhq-dashboard-plugins/blob/v4.7.3-2.8.0/CHANGELOG.md>`__
- `cyb3rhq/cyb3rhq-packages <https://github.com/cyb3rhq/cyb3rhq-packages/releases/tag/v4.7.3>`__
