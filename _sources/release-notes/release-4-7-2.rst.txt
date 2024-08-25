.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Cyb3rhq 4.7.2 has been released. Check out our release notes to discover the changes and additions of this release.

4.7.2 Release notes - 10 January 2024
=====================================

This section lists the changes in version 4.7.2. Every update of the Cyb3rhq solution is cumulative and includes all enhancements and fixes from previous releases.

What's new
----------

This release includes new features or enhancements as the following:

Cyb3rhq manager
^^^^^^^^^^^^^

- `#21142 <https://github.com/cyb3rhq/cyb3rhq/pull/21142>`__ Added minimum time constraint of 1 hour for downloading the Vulnerability Detector feed.

Cyb3rhq agent
^^^^^^^^^^^

- `#20638 <https://github.com/cyb3rhq/cyb3rhq/pull/20638>`__ Added request timeouts for the external and cloud integrations. This prevents indefinite waiting for a response.

Ruleset
^^^^^^^

- `#17565 <https://github.com/cyb3rhq/cyb3rhq/pull/17565>`__ Added new SCA policy for Debian 12 systems.

Other
^^^^^

- `#20798 <https://github.com/cyb3rhq/cyb3rhq/pull/20798>`__ Upgraded external ``aiohttp`` library dependency to version ``3.9.1`` to address a security vulnerability.

Cyb3rhq dashboard
^^^^^^^^^^^^^^^

- `#6191 <https://github.com/cyb3rhq/cyb3rhq-dashboard-plugins/pull/6191>`__ Added **Hostname** and **Board Serial** information to **Agents** > **Inventory data**.
- `#6208 <https://github.com/cyb3rhq/cyb3rhq-dashboard-plugins/pull/6208>`__ Added contextual information to the deploy agent steps.

Packages 
^^^^^^^^

- `#2670 <https://github.com/cyb3rhq/cyb3rhq-packages/pull/2670>`__ Removed installed dependencies that were part of the Cyb3rhq installation assistant. This ensures a clean post-installation state.
- `#2677 <https://github.com/cyb3rhq/cyb3rhq-packages/pull/2677>`__ Removed ``gnupg`` package as RPM dependency in the Cyb3rhq installation assistant.
- `#2693 <https://github.com/cyb3rhq/cyb3rhq-packages/pull/2693>`__ Added Debian12 SCA files.

Resolved issues
---------------

This release resolves known issues as the following: 

Cyb3rhq manager
^^^^^^^^^^^^^

===========================================================  =============
 Reference                                                   Description
===========================================================  =============
`#21011 <https://github.com/cyb3rhq/cyb3rhq/pull/21011>`__       ``cyb3rhq-remoted`` now logs the warning regarding invalid message size from agents in hex format.
`#20658 <https://github.com/cyb3rhq/cyb3rhq/pull/20658>`__       Fixed a bug within the Windows Eventchannel decoder to ensure proper handling of Unicode characters.
`#20735 <https://github.com/cyb3rhq/cyb3rhq/pull/20735>`__       Fixed data validation for decoding Windows Eventchannel XML input strings.
===========================================================  =============

Cyb3rhq agent
^^^^^^^^^^^

===========================================================  =============
 Reference                                                   Description
===========================================================  =============
`#20656 <https://github.com/cyb3rhq/cyb3rhq/pull/20656>`__       Implemented validation for the format of the IP address parameter in the ``host_deny`` active response.
`#20594 <https://github.com/cyb3rhq/cyb3rhq/pull/20594>`__       Fixed a bug in the Windows agent that might lead it to crash when gathering forwarded Windows events.
`#20447 <https://github.com/cyb3rhq/cyb3rhq/pull/20447>`__       Fixed issue with the ``profile`` prefix in parsing AWS configuration profiles.
`#20660 <https://github.com/cyb3rhq/cyb3rhq/pull/20660>`__       Fixed parsing and validation for the AWS regions argument, expanding the AWS regions list accordingly.
===========================================================  =============

Ruleset
^^^^^^^

===========================================================  =============
 Reference                                                   Description
===========================================================  =============
`#20663 <https://github.com/cyb3rhq/cyb3rhq/pull/20663>`__       Updated AWS Macie rules to show relevant fields in alert details.
===========================================================  =============

Cyb3rhq dashboard
^^^^^^^^^^^^^^^

=================================================================================================================================================    =============
 Reference                                                                                                                                           Description
=================================================================================================================================================    =============
`#6185 <https://github.com/cyb3rhq/cyb3rhq-dashboard-plugins/pull/6185>`__                                                                               Fixed Agents preview page load when there are no registered agents.
`#6206 <https://github.com/cyb3rhq/cyb3rhq-dashboard-plugins/pull/6206>`__, `#6213 <https://github.com/cyb3rhq/cyb3rhq-dashboard-plugins/pull/6213>`__       Changed the endpoint to get Cyb3rhq server auth configuration to ``manager/configuration/auth/auth``.
`#6224 <https://github.com/cyb3rhq/cyb3rhq-dashboard-plugins/pull/6224>`__                                                                               Fixed error navigating back to agent in some scenarios.
=================================================================================================================================================    =============

Packages
^^^^^^^^

=====================================================================     =============
Reference                                                                 Description
=====================================================================     =============
`#2667 <https://github.com/cyb3rhq/cyb3rhq-packages/pull/2667>`_              Fixed warning message when generating certificates.
=====================================================================     =============

Changelogs
----------

More details about these changes are provided in the changelog of each component:

- `cyb3rhq/cyb3rhq <https://github.com/cyb3rhq/cyb3rhq/blob/v4.7.2/CHANGELOG.md>`__
- `cyb3rhq/cyb3rhq-dashboard <https://github.com/cyb3rhq/cyb3rhq-dashboard-plugins/blob/v4.7.2-2.8.0/CHANGELOG.md>`__
- `cyb3rhq/cyb3rhq-packages <https://github.com/cyb3rhq/cyb3rhq-packages/releases/tag/v4.7.2>`__
