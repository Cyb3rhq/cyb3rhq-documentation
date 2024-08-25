.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Cyb3rhq 4.4.2 has been released. Check out our release notes to discover the changes and additions of this release.

4.4.2 Release notes - 18 May 2023
=================================

This section lists the changes in version 4.4.2. Every update of the Cyb3rhq solution is cumulative and includes all enhancements and fixes from previous releases.

What's new
----------

This release includes new features or enhancements as the following:


Cyb3rhq manager
^^^^^^^^^^^^^
- `#15957 <https://github.com/cyb3rhq/cyb3rhq/pull/15957>`_ Remove an unused variable in ``cyb3rhq-authd`` to fix a *String not null terminated* Coverity finding.


Agent
^^^^^
- `#16515 <https://github.com/cyb3rhq/cyb3rhq/pull/16515>`_ Added a new module to integrate with Amazon Security Lake as a subscriber.
- `#16847 <https://github.com/cyb3rhq/cyb3rhq/pull/16847>`_ Added support for ``localfile`` blocks deployment.
- `#16743 <https://github.com/cyb3rhq/cyb3rhq/pull/16743>`_ Changed ``netstat`` command on macOS agents.

Ruleset
^^^^^^^
- `#15566 <https://github.com/cyb3rhq/cyb3rhq/pull/15566>`_ Added macOS 13.0 Ventura SCA policy. 
- `#15567 <https://github.com/cyb3rhq/cyb3rhq/pull/15567>`_ Added new ruleset for macOS 13 Ventura and older versions.
- `#16549 <https://github.com/cyb3rhq/cyb3rhq/pull/16549>`_ Added a new base ruleset for log sources collected from Amazon Security Lake.

Other
^^^^^
- `#16692 <https://github.com/cyb3rhq/cyb3rhq/pull/16692>`_ Added ``pyarrow`` and ``numpy`` Python dependencies.
- `#16692 <https://github.com/cyb3rhq/cyb3rhq/pull/16692>`_ Added ``importlib-metadata`` and ``zipp`` Python dependencies.
- `#17053 <https://github.com/cyb3rhq/cyb3rhq/pull/17053>`_ Updated ``Flask`` Python dependency to 2.2.5.

Resolved issues
---------------

This release resolves known issues as the following: 

Cyb3rhq manager
^^^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#16394 <https://github.com/cyb3rhq/cyb3rhq/pull/16394>`_             Fixed a bug causing agent groups tasks status in the cluster not to be stored. 
`#16478 <https://github.com/cyb3rhq/cyb3rhq/pull/16478>`_             Fixed memory leaks in Vulnerability Detector after disk failures. 
`#16530 <https://github.com/cyb3rhq/cyb3rhq/pull/16530>`_             Fixed a pre-decoder problem with the + symbol in the macOS ULS timestamp.
==============================================================    =============

Agent
^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#16517 <https://github.com/cyb3rhq/cyb3rhq/pull/16517>`_             Fixed an issue with MAC address reporting on Windows systems.
`#16857 <https://github.com/cyb3rhq/cyb3rhq/pull/16857>`_             Fixed Windows unit tests hanging during execution.
==============================================================    =============

RESTful API
^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#16381 <https://github.com/cyb3rhq/cyb3rhq/pull/16381>`_             Fixed agent insertion when no key is specified using ``POST /agents/insert`` endpoint.
==============================================================    =============

Cyb3rhq dashboard
^^^^^^^^^^^^^^^

==============================================================================================================================     =============
Reference                                                                                                                          Description
==============================================================================================================================     =============
`#5428 <https://github.com/cyb3rhq/cyb3rhq-kibana-app/pull/5428>`_ `#5432 <https://github.com/cyb3rhq/cyb3rhq-kibana-app/pull/5432>`_      Fixed a problem in the backend service to get the plugin configuration.
==============================================================================================================================     =============

Cyb3rhq Kibana plugin for Kibana 7.10.2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#5428 <https://github.com/cyb3rhq/cyb3rhq-kibana-app/pull/5428>`_    Fixed a problem in the backend service to get the plugin configuration.
==============================================================    =============

Cyb3rhq Kibana plugin for Kibana 7.16.x and 7.17.x
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#5428 <https://github.com/cyb3rhq/cyb3rhq-kibana-app/pull/5428>`_    Fixed a problem in the backend service to get the plugin configuration.
==============================================================    =============



Changelogs
----------

More details about these changes are provided in the changelog of each component:

- `cyb3rhq/cyb3rhq <https://github.com/cyb3rhq/cyb3rhq/blob/v4.4.2/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-dashboard <https://github.com/cyb3rhq/cyb3rhq-kibana-app/blob/v4.4.2-2.6.0/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-kibana-app 7.10.2 <https://github.com/cyb3rhq/cyb3rhq-kibana-app/blob/v4.4.2-7.10.2/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-kibana-app 7.17.x <https://github.com/cyb3rhq/cyb3rhq-kibana-app/blob/v4.4.2-7.17.9/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-splunk <https://github.com/cyb3rhq/cyb3rhq-splunk/blob/v4.4.2-8.2/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-packages <https://github.com/cyb3rhq/cyb3rhq-packages/releases/tag/v4.4.2>`_