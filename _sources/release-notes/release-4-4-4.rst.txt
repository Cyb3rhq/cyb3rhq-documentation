.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Cyb3rhq 4.4.4 has been released. Check out our release notes to discover the changes and additions of this release.

4.4.4 Release notes - 13 June 2023
==================================

This section lists the changes in version 4.4.4. Every update of the Cyb3rhq solution is cumulative and includes all enhancements and fixes from previous releases.

What's new
----------

This release includes new features or enhancements as the following:

Agent
^^^^^
- `#17506 <https://github.com/cyb3rhq/cyb3rhq/pull/17506>`_ The Windows agent package signing certificate has been updated.

Ruleset
^^^^^^^

- `#17211 <https://github.com/cyb3rhq/cyb3rhq/pull/17211>`_ Updated all current rule descriptions from "Ossec" to "Cyb3rhq".

Cyb3rhq dashboard
^^^^^^^^^^^^^^^

- `#5416 <https://github.com/cyb3rhq/cyb3rhq-kibana-app/pull/5416>`_ Changed the title and added a warning in step 3 of the **Deploy new agent** section.

Cyb3rhq Kibana plugin for Kibana 7.10.2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- `#5416 <https://github.com/cyb3rhq/cyb3rhq-kibana-app/pull/5416>`_ Changed the title and added a warning in step 3 of the **Deploy new agent** section.

Cyb3rhq Kibana plugin for Kibana 7.16.x and 7.17.x
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- `#5416 <https://github.com/cyb3rhq/cyb3rhq-kibana-app/pull/5416>`_ Changed the title and added a warning in step 3 of the **Deploy new agent** section.

Resolved issues
---------------

This release resolves known issues as the following: 

Cyb3rhq manager
^^^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#17178 <https://github.com/cyb3rhq/cyb3rhq/pull/17178>`_             The vulnerability scanner stops producing false positives for some Windows 11 vulnerabilities due to a change in the feed's CPE.
`#16908 <https://github.com/cyb3rhq/cyb3rhq/pull/16908>`_             Prevented the VirusTotal integration from querying the API when the source alert misses the MD5.
==============================================================    =============

Changelogs
----------

More details about these changes are provided in the changelog of each component:

- `cyb3rhq/cyb3rhq <https://github.com/cyb3rhq/cyb3rhq/blob/v4.4.4/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-dashboard <https://github.com/cyb3rhq/cyb3rhq-kibana-app/blob/v4.4.4-2.6.0/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-kibana-app 7.10.2 <https://github.com/cyb3rhq/cyb3rhq-kibana-app/blob/v4.4.4-7.10.2/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-kibana-app 7.17.x <https://github.com/cyb3rhq/cyb3rhq-kibana-app/blob/v4.4.4-7.17.9/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-splunk <https://github.com/cyb3rhq/cyb3rhq-splunk/blob/v4.4.4-8.2/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-packages <https://github.com/cyb3rhq/cyb3rhq-packages/releases/tag/v4.4.4>`_