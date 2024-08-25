.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Cyb3rhq 4.5.3 has been released. Check out our release notes to discover the changes and additions of this release.

4.5.3 Release notes - 10 October 2023
=====================================

This section lists the changes in version 4.5.3. Every update of the Cyb3rhq solution is cumulative and includes all enhancements and fixes from previous releases.

What's new
----------

This version includes new features or improvements, such as the following:

Manager
^^^^^^^

-  `#18783 <https://github.com/cyb3rhq/cyb3rhq/pull/18783>`__ Vulnerability Detector now fetches the SUSE feeds in Gzip compressed format.

Agent
^^^^^

-  `#19205 <https://github.com/cyb3rhq/cyb3rhq/issues/19205>`__ Support for macOS 14 (Sonoma).

RESTful API
^^^^^^^^^^^

-  `#18509 <https://github.com/cyb3rhq/cyb3rhq/pull/18509>`__ Added support for the ``$`` symbol in query values.
-  `#18346 <https://github.com/cyb3rhq/cyb3rhq/pull/18346>`__ Added support for the ``@`` symbol in query values.
-  `#18493 <https://github.com/cyb3rhq/cyb3rhq/pull/18493>`__ Added support for nested queries in the ``q`` API parameter.
-  `#18432 <https://github.com/cyb3rhq/cyb3rhq/pull/18432>`__ Updated ``force`` flag message in the ``agent_upgrade`` CLI.

Security updates
----------------

This release fixes the following vulnerabilities:

Agent
^^^^^

==============    ========================================================    =============
CVE               Reference                                                   Description
==============    ========================================================    =============
CVE-2023-42463    `#19069 <https://github.com/cyb3rhq/cyb3rhq/pull/19069>`__      Fixed a stack overflow hazard in ``cyb3rhq-logcollector`` that could allow a local privilege escalation. Found by Keith Yeo (`@kyeojy <https://twitter.com/kyeojy>`__).
==============    ========================================================    =============

Resolved issues
---------------

This release resolves known issues as the following:

Manager
^^^^^^^

========================================================    =============
Reference                                                   Description
========================================================    =============
`#18737 <https://github.com/cyb3rhq/cyb3rhq/pull/18737>`__      Fixed a bug that might cause ``cyb3rhq-analysisd`` to crash if it receives a status API query during startup.
`#18976 <https://github.com/cyb3rhq/cyb3rhq/pull/18976>`__      Fixed a bug that might cause ``cyb3rhq-maild`` to crash when handling large alerts.
`#19217 <https://github.com/cyb3rhq/cyb3rhq/pull/19217>`__      Addressed an issue in Vulnerability Detector when fetching the Suse Linux Enterprise 15 feeds.
========================================================    =============

Agent
^^^^^

========================================================    =============
Reference                                                   Description
========================================================    =============
`#18773 <https://github.com/cyb3rhq/cyb3rhq/pull/18773>`__      Fixed a bug in the memory handle at the agent's data provider helper.
`#18903 <https://github.com/cyb3rhq/cyb3rhq/pull/18903>`__      Fixed a data mismatch in the OS name between the global and agents' databases.
`#19286 <https://github.com/cyb3rhq/cyb3rhq/pull/19286>`__      Fixed wrong Windows agent binaries metadata.
`#19397 <https://github.com/cyb3rhq/cyb3rhq/pull/19397>`__      Fixed error during the Windows agent upgrade.
========================================================    =============

RESTful API
^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#18362 <https://github.com/cyb3rhq/cyb3rhq/pull/18362>`__            Removed undesired characters when listing rule group names in ``GET /rules/groups``.
`#18434 <https://github.com/cyb3rhq/cyb3rhq/pull/18434>`__            Fixed an error when using the query ``condition=all`` in ``GET /sca/{agent_id}/checks/{policy_id}``.
`#18733 <https://github.com/cyb3rhq/cyb3rhq/pull/18733>`__            Fixed an error in the API log mechanism where sometimes the requests would not be printed in the log file.
==============================================================    =============

Cyb3rhq dashboard
^^^^^^^^^^^^^^^

=======================================================================    =============
Reference                                                                  Description
=======================================================================    =============
`#5925 <https://github.com/cyb3rhq/cyb3rhq-dashboard-plugins/pull/5925>`__     Fixed the command for agent installation on SUSE to use zypper.
=======================================================================    =============

Cyb3rhq Kibana plugin for Kibana 7.10.2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

=======================================================================    =============
Reference                                                                  Description
=======================================================================    =============
`#5925 <https://github.com/cyb3rhq/cyb3rhq-dashboard-plugins/pull/5925>`__     Fixed the command for agent installation on SUSE to use zypper.
=======================================================================    =============

Cyb3rhq Kibana plugin for Kibana 7.16.x and 7.17.x
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

=======================================================================    =============
Reference                                                                  Description
=======================================================================    =============
`#5925 <https://github.com/cyb3rhq/cyb3rhq-dashboard-plugins/pull/5925>`__     Fixed the command for agent installation on SUSE to use zypper.
=======================================================================    =============

Packages
^^^^^^^^

===============================================================    =============
Reference                                                          Description
===============================================================    =============
`#2397 <https://github.com/cyb3rhq/cyb3rhq-packages/pull/2397>`__      Changed GRUB options in build OVA process.
`#2453 <https://github.com/cyb3rhq/cyb3rhq-packages/pull/2453>`__      Fixed  an issue with the Cyb3rhq dashboard port check despite the ``-p|--port`` installation assistant option being specified.
`#2461 <https://github.com/cyb3rhq/cyb3rhq-packages/pull/2461>`__      Fixed an issue when passwords changed. Now the ``internal_users.yml`` file gets updated.
`#2492 <https://github.com/cyb3rhq/cyb3rhq-packages/pull/2492>`__      Fixed missing removal of Cyb3rhq indexer remaining files upon rollback.
===============================================================    =============

Changelogs
----------

More details about these changes are provided in the changelog of each component:

-  `cyb3rhq/cyb3rhq <https://github.com/cyb3rhq/cyb3rhq/blob/v4.5.3/CHANGELOG.md>`_
-  `cyb3rhq/cyb3rhq-dashboard <https://github.com/cyb3rhq/cyb3rhq-dashboard-plugins/blob/v4.5.3-2.6.0/CHANGELOG.md>`_
-  `cyb3rhq/cyb3rhq-dashboard-plugins 7.10.2 <https://github.com/cyb3rhq/cyb3rhq-dashboard-plugins/blob/v4.5.3-7.10.2/CHANGELOG.md>`_
-  `cyb3rhq/cyb3rhq-dashboard-plugins 7.16.x <https://github.com/cyb3rhq/cyb3rhq-dashboard-plugins/blob/v4.5.3-7.16.3/CHANGELOG.md>`_
-  `cyb3rhq/cyb3rhq-dashboard-plugins 7.17.x <https://github.com/cyb3rhq/cyb3rhq-dashboard-plugins/blob/v4.5.3-7.17.13/CHANGELOG.md>`_
-  `cyb3rhq/cyb3rhq-splunk <https://github.com/cyb3rhq/cyb3rhq-splunk/blob/v4.5.3-8.2/CHANGELOG.md>`_
-  `cyb3rhq/cyb3rhq-packages <https://github.com/cyb3rhq/cyb3rhq-packages/releases/tag/v4.5.3>`_
