.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Cyb3rhq 4.8.1 has been released. Check out our release notes to discover the changes and additions of this release.

4.8.1 Release notes - 18 July 2024
==================================

This section lists the changes in version 4.8.1. Every update of the Cyb3rhq solution is cumulative and includes all enhancements and fixes from previous releases.

What's new
----------

This release includes new features or enhancements as the following:

Manager
^^^^^^^

-  `#24357 <https://github.com/cyb3rhq/cyb3rhq/pull/24357>`__ Added dedicated RSA keys for keystore encryption.

RESTful API
^^^^^^^^^^^

-  `#24173 <https://github.com/cyb3rhq/cyb3rhq/pull/24173>`__ Updated the ``GET /manager/version/check`` endpoint response to always include the ``uuid`` field.

Other
^^^^^

-  `#24108 <https://github.com/cyb3rhq/cyb3rhq/pull/24108>`__ Upgraded external ``Jinja2`` library dependency version to ``3.1.4``.
-  `#23925 <https://github.com/cyb3rhq/cyb3rhq/pull/23925>`__ Upgraded external ``requests`` library dependency version to ``2.32.2``.

Packages
^^^^^^^^

-  `#3005 <https://github.com/cyb3rhq/cyb3rhq-packages/pull/3005>`__ Added ``-A|--api`` option validation to the ``cyb3rhq-passwords-tool.sh`` script for changing API user credentials.

Resolved issues
---------------

This release resolves known issues as the following:

Manager
^^^^^^^

-  `#24308 <https://github.com/cyb3rhq/cyb3rhq/pull/24308>`__ Fixed a bug in ``upgrade_agent`` CLI where it occasionally hung without showing a response.
-  `#24341 <https://github.com/cyb3rhq/cyb3rhq/pull/24341>`__ Fixed a bug in ``upgrade_agent`` CLI where it occasionally raised an unhandled exception.
-  `#24509 <https://github.com/cyb3rhq/cyb3rhq/pull/24509>`__ Changed keystore cipher algorithm to remove the reuse of ``sslmanager.cert`` and ``sslmanager.key``.

Agent
^^^^^

-  `#23989 <https://github.com/cyb3rhq/cyb3rhq/pull/23989>`__ Fixed the macOS agent to retrieve correct CPU name.

Dashboard plugin
^^^^^^^^^^^^^^^^

-  `#6778 <https://github.com/cyb3rhq/cyb3rhq-dashboard-plugins/pull/6778>`__ Removed the unnecessary ``delay`` body parameter on server API requests.
-  `#6777 <https://github.com/cyb3rhq/cyb3rhq-dashboard-plugins/pull/6777>`__ Fixed home KPI links with custom or index pattern where the title is different from the ID.
-  `#6793 <https://github.com/cyb3rhq/cyb3rhq-dashboard-plugins/pull/6793>`__ Fixed the colors related to vulnerability severity levels on the Vulnerability Detection dashboard.
-  `#6827 <https://github.com/cyb3rhq/cyb3rhq-dashboard-plugins/pull/6827>`__ Fixed pinned agent error in vulnerabilities events tab.

Changelogs
----------

The repository changelogs provide more details about the changes.

Product repositories
^^^^^^^^^^^^^^^^^^^^

-  `cyb3rhq/cyb3rhq <https://github.com/cyb3rhq/cyb3rhq/blob/v4.8.1/CHANGELOG.md>`__
-  `cyb3rhq/cyb3rhq-dashboard-plugins <https://github.com/cyb3rhq/cyb3rhq-dashboard-plugins/blob/v4.8.1-2.10.0/CHANGELOG.md>`__
-  `cyb3rhq/cyb3rhq-packages <https://github.com/cyb3rhq/cyb3rhq-packages/blob/v4.8.1/CHANGELOG.md>`__

Auxiliary repositories
^^^^^^^^^^^^^^^^^^^^^^^

-  `cyb3rhq/cyb3rhq-ansible <https://github.com/cyb3rhq/cyb3rhq-ansible/blob/v4.8.1/CHANGELOG.md>`__
-  `cyb3rhq/cyb3rhq-kubernetes <https://github.com/cyb3rhq/cyb3rhq-kubernetes/blob/v4.8.1/CHANGELOG.md>`__
-  `cyb3rhq/cyb3rhq-puppet <https://github.com/cyb3rhq/cyb3rhq-puppet/blob/v4.8.1/CHANGELOG.md>`__
-  `cyb3rhq/cyb3rhq-docker <https://github.com/cyb3rhq/cyb3rhq-docker/blob/v4.8.1/CHANGELOG.md>`__

-  `cyb3rhq/cyb3rhq-qa <https://github.com/cyb3rhq/cyb3rhq-qa/blob/v4.8.1/CHANGELOG.md>`__
-  `cyb3rhq/qa-integration-framework <https://github.com/cyb3rhq/qa-integration-framework/blob/v4.8.1/CHANGELOG.md>`__

-  `cyb3rhq/cyb3rhq-documentation <https://github.com/cyb3rhq/cyb3rhq-documentation/blob/v4.8.1/CHANGELOG.md>`__
