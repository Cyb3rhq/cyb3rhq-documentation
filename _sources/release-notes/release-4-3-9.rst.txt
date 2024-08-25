.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Cyb3rhq 4.3.9 has been released. Check out our release notes to discover the changes and additions of this release.

4.3.9 Release notes - 13 October 2022
=====================================

This section lists the changes in version 4.3.9. Every update of the Cyb3rhq solution is cumulative and includes all enhancements and fixes from previous releases.

What's new
----------

This release includes new features or enhancements as the following:

Cyb3rhq agent
^^^^^^^^^^^

- `#14497 <https://github.com/cyb3rhq/cyb3rhq/issues/14497>`_ An obsolete Windows Audit SCA policy file is removed. 


Cyb3rhq Kibana plugin
^^^^^^^^^^^^^^^^^^^

- Support for Kibana 7.17.6. 

Cyb3rhq Splunk app
^^^^^^^^^^^^^^^^

- Support for Splunk 8.2.7.1 and 8.2.8.

Other
^^^^^

- `#15067 <https://github.com/cyb3rhq/cyb3rhq/pull/15067>`_ The external `protobuf` Python dependency is updated to 3.19.6.

 
Resolved issues
---------------

This release resolves known issues as the following: 


Cyb3rhq agent
^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#15007 <https://github.com/cyb3rhq/cyb3rhq/pull/15007>`_             The remote policy detection in SCA is fixed. 
`#15023 <https://github.com/cyb3rhq/cyb3rhq/pull/15023>`_             Fixed the agent upgrade module settings parser. Now a default CA file is set. 
==============================================================    =============



Changelogs
----------

More details about these changes are provided in the changelog of each component:

- `cyb3rhq/cyb3rhq <https://github.com/cyb3rhq/cyb3rhq/blob/v4.3.9/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-dashboard <https://github.com/cyb3rhq/cyb3rhq-kibana-app/blob/v4.3.9-1.2.0/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-kibana-app 7.10.2 <https://github.com/cyb3rhq/cyb3rhq-kibana-app/blob/v4.3.9-7.10.2/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-kibana-app 7.17.x <https://github.com/cyb3rhq/cyb3rhq-kibana-app/blob/v4.3.9-7.17.6/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-splunk <https://github.com/cyb3rhq/cyb3rhq-splunk/blob/v4.3.9-8.2.8/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-packages <https://github.com/cyb3rhq/cyb3rhq-packages/releases/tag/v4.3.9>`_
