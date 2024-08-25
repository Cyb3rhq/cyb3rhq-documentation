.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
      :description: Cyb3rhq 4.2.4 has been released. Check out our release notes to discover the changes and additions of this release.

.. _release_4_2_4:

4.2.4 Release notes - 20 October 2021
=====================================

This section lists the changes in version 4.2.4. Every update of the Cyb3rhq solution is cumulative and includes all enhancements and fixes from previous releases.

What's new
----------

This release includes new features or enhancements.

Cyb3rhq Kibana plugin
^^^^^^^^^^^^^^^^^^^

- Cyb3rhq Kibana plugin is now compatible with Cyb3rhq 4.2.4.

Cyb3rhq Splunk app
^^^^^^^^^^^^^^^^

- Cyb3rhq Splunk app is now compatible with Cyb3rhq 4.2.4.

Resolved issues
---------------

This release resolves known issues. 

Manager
^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#9158 <https://github.com/cyb3rhq/cyb3rhq/pull/9158>`_               This fix prevents files belonging to deleted agents from remaining in the manager.
`#10432 <https://github.com/cyb3rhq/cyb3rhq/pull/10432>`_             Fixed inaccurate agent group file cleanup in the database sync module. Now, the module syncs up the agent database from ``client.keys`` before cleaning up the groups folder.
`#10479 <https://github.com/cyb3rhq/cyb3rhq/pull/10479>`_             This fix prevents the manager from corrupting the agent data integrity when the disk gets full.
`#10559 <https://github.com/cyb3rhq/cyb3rhq/pull/10559>`_             A resource leak in Vulnerability Detector when scanning Windows agents is now fixed.
==============================================================    =============

Cyb3rhq Kibana plugin
^^^^^^^^^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#3638 <https://github.com/cyb3rhq/cyb3rhq-kibana-app/pull/3638>`_    An issue that caused the user's auth token not to be deprecated correctly after logging out of the API is now fixed. 
==============================================================    =============

Changelogs
----------

More details about these changes are provided in the changelog of each component:

- `cyb3rhq/cyb3rhq <https://github.com/cyb3rhq/cyb3rhq/blob/v4.2.4/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-kibana-app <https://github.com/cyb3rhq/cyb3rhq-kibana-app/blob/v4.2.4-7.10.2/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-splunk <https://github.com/cyb3rhq/cyb3rhq-splunk/blob/v4.2.4-8.1.4/CHANGELOG.md>`_