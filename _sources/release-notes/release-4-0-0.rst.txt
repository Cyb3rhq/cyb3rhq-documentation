.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Cyb3rhq 4.0.0 has been released. Check out our release notes to discover the changes and additions of this release.

.. _release_4_0_0:

4.0.0 Release notes - 23 October 2020
=====================================

This section lists the changes in version 4.0.0. More details about these changes are provided in the changelog of each component:

- `cyb3rhq/cyb3rhq <https://github.com/cyb3rhq/cyb3rhq/blob/v4.0.0/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-kibana-app <https://github.com/cyb3rhq/cyb3rhq-kibana-app/blob/4.0-7.9/CHANGELOG.md>`_
- `cyb3rhq/ruleset <https://github.com/cyb3rhq/cyb3rhq-ruleset/blob/4.0/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-packages <https://github.com/cyb3rhq/cyb3rhq-packages/blob/master/CHANGELOG.md>`_

Highlights
----------

- The agent enrollment is now performed on the main daemon initialization. There is no need to request a key using an external CLI anymore. Agents are now able to request a key to the manager on their own if no key was defined on startup or if the manager has rejected the connection (Agents in ``3.x`` version are still 100% compatible with ``4.x`` version). 

- Cyb3rhq API RBAC: Configure users, roles, and policies to manage access permissions. Cyb3rhq WUI now permits granular control over access to resources depending on user roles, this will allow enterprises to manage user accounts that fulfill different functions in the security of the environment.

- Cyb3rhq API is now embedded in the Cyb3rhq manager.

- Cyb3rhq manager and agents will use TCP as the default communication protocol.

- The Windows agent MSI installer is now signed using DigiCert instead of GlobalSign. DigiCert is known for being present on more Windows versions including the oldest ones.

- FIM implements now a set of settings to control the module temporal files disk usage. This means that now we can choose the amount of disk space used by the report change utility. The diff option reports changes in the monitored files, to do so, it creates a compressed copy of the file and checks if it changes. This method may use a lot of disk space. Cyb3rhq 4.0 introduces new capabilities to limit the space used.


Breaking changes
----------------

- The agent-auth tool starts the deprecation cycle (to be deprecated in v5.0.0). The agent registration on demand will still be available using CLI.

- The API is now embedded in the Cyb3rhq manager, no cyb3rhq-api package will be installed anymore.

- Cyb3rhq manager and agents are no longer using UDP as the default communication protocol. TCP is enabled by default.

- OpenSCAP policies removed from RPM and DEB packages. Folder present policies in the agent installation will be removed.


Cyb3rhq core
----------

Added
^^^^^

**Cyb3rhq API**

- Embedded Cyb3rhq API with Cyb3rhq Manager, there is no need to install Cyb3rhq API.

- Migrated Cyb3rhq API server from NodeJS to Python.

- Added asynchronous ``aiohttp`` server for the Cyb3rhq API.

- The new Cyb3rhq API is approximately 5 times faster on average.

- Added OpenAPI based Cyb3rhq API specification.

- Improved Cyb3rhq API reference documentation based on OpenAPI spec using redoc.

- Added a new yaml Cyb3rhq API configuration file.

- Added new endpoints to manage API configuration and deprecated ``configure_api.sh``.

- Added RBAC support to Cyb3rhq API.

- Added new endpoints for Cyb3rhq API security management.

- Added SQLAlchemy ORM based database for RBAC.

- Added a new JWT authentication method.

- Cyb3rhq API up and running by default in all nodes for a clustered environment.

- Added new and improved error handling.

- Added tavern and docker based Cyb3rhq API integration tests.

- Added new and unified Cyb3rhq API response structure.

- Added new endpoints for Cyb3rhq API users management.

- Added a new endpoint to restart agents that belong to a node.

- Added and improved ``q`` filter in several endpoints.

- Tested and improved Cyb3rhq API security.

- Added DDOS blocking system.

- Added brute force attack blocking system.

- Added content-type validation.

- Added and updated framework unit tests to increase coverage.

- Added improved support for monitoring paths from environment variables.

- Added auto-enrollment capability. Agents are now able to request a key from the manager if the current key is missing or wrong.

**Vulnerability Detector**

- Redhat vulnerabilities are now fetched from OVAL benchmarks.

- Debian vulnerable packages are now fetched from the Security Tracker.

- The Debian Security Tracker feed can be loaded from a custom location.

- Allow compressed feeds for offline updates.

- The manager now updates the MSU feed automatically.

- CVEs with no affected version defined in all the feeds are now reported.

- CVEs vulnerable for the vendor and missing in the NVD are now reported.

Changed
^^^^^^^
- Changed multiple Cyb3rhq API endpoints.

- Refactored framework module in SDK and core.

- FIM Windows events handling refactored.

- Changed framework to access ``global.db`` using ``cyb3rhq-db``.

- Changed ``agent-info`` synchronization task in Cyb3rhq cluster.

Fixed
^^^^^

- Fixed an error with the last scan time in syscheck endpoints.

- Added support for monitoring directories that contain commas.

- Fixed a bug where configuring a directory to be monitored as realtime and whodata resulted in realtime prevailing.

- Fixed using an incorrect mutex while deleting inotify watches.

- Fixed a bug that could cause multiple FIM threads to request the same temporary file.

- Fixed a bug where deleting a file permanently in Windows would not trigger an alert.

- Fixed a typo in the file monitoring options log entry.

- Fixed an error where monitoring a drive in Windows under scheduled or realtime mode would generate alerts from the recycle bin.

- When monitoring a drive in Windows in the format ``U:``, it will monitor ``U:\`` instead of the agent's working directory.

- Fixed a bug where monitoring a drive in Windows with recursion_level set to 0 would trigger alerts from files inside its subdirectories.

- Fixed an Azure wodle dependency error. The package azure-storage-blob>12.0.0 does not include a component used.

**Vulnerability Detector**

- Vulnerabilities of Windows Server 2019 which do not affect to Windows 10 were not being reported.

- Vulnerabilities patched by a Microsoft update with no supersedence were not being reported.

- Vulnerabilities patched by more than one Microsoft update were not being evaluated against all the patches.

- Duplicated alerts in Windows 10.

- Syscollector now discards hotfixes that are not fully installed.

- Syscollector now collects hotfixes that were not being parsed.

Removed
^^^^^^^

- Removed Cyb3rhq API cache endpoints.

- Removed Cyb3rhq API rootcheck endpoints.

- Deprecated Debian Jessie and Wheezy for Vulnerability Detector (EOL).


Cyb3rhq Kibana plugin
-------------------

Added
^^^^^

- Support for Cyb3rhq v4.0.0.

- Support for Kibana v7.9.1 and v7.9.2.

- Support for Open Distro 1.10.1.

- Added a RBAC security layer integrated with Open Distro and X-Pack.

- Added remoted and analysisd statistics.

- Expand supported deployment variables.

- Added new configuration view settings for GCP integration.

- Added logic to change the ``metafields`` configuration of Kibana.

Changed
^^^^^^^

- Migrated the default index-pattern to ``cyb3rhq-alerts-*``.

- Removed the ``known-fields`` functionality.

- Security Events dashboard redesigned.

- Redesigned the app settings configuration with categories.

- Moved the cyb3rhq-registry file to Kibana optimize folder.


Fixed
^^^^^

- Format options in ``cyb3rhq-alerts`` index-pattern are not overwritten now.

- Prevent blank page in detail agent view.

- Navigable agents name in Events.

- Index pattern is not being refreshed.

- Reporting fails when agent is pinned and compliance controls are visited.

- Reload rule detail does not work properly with the related rules.

- Fix search bar filter in Manage agent of group.


Cyb3rhq ruleset
-------------

- Changed compliance rules groups and removed ``alert_by_email`` option by default.

- Let the Ruleset update tool pick up the current version branch by default.


Cyb3rhq packages
--------------

Added
^^^^^

- Added Open Distro for Elasticsearch packages to Cyb3rhq's software repository.

Changed
^^^^^^^

- Cyb3rhq services are no longer enabled nor started in a fresh install.

- Cyb3rhq services will be restarted on upgrade if they were running before upgrading them.

- Cyb3rhq API and Cyb3rhq Manager services are unified in a single cyb3rhq-manager service.

- Cyb3rhq plugin for Kibana package has been renamed.

- Cyb3rhq VM now uses Cyb3rhq and Open Distro for Elasticsearch.

Fixed
^^^^^

- Unit files for systemd are now installed on ``/usr/lib/systemd/system``.

- Improved the upgrade of unit files.

- ``ossec-init.conf`` file now shows the build date for any system.

- Fixed an error setting SCA file permissions on ``.deb`` packages.

Removed
^^^^^^^

- The Cyb3rhq API package has been removed. Now, the Cyb3rhq API is embedded into the Cyb3rhq Manager installation.

- Removed OpenSCAP files and integration.


Cyb3rhq documentation
-------------------

Added
^^^^^
- Added instructions to install Cyb3rhq along with Open Distro for Elasticsearch.

- Added scripts, created by the Cyb3rhq team, that allow the user to install Cyb3rhq and Elastic Stack automatically. 

- Added tabs in the installation guide to ease the navigation through the different options available.

- Added a 'More installation alternatives' section that provides instructions on how to install Cyb3rhq along with commercial options like Elastic Stack basic license or Splunk. This section also includes instructions on how to install Cyb3rhq from sources.

Changed
^^^^^^^

- Reorganized the installation guide to help the user through the installation process of Cyb3rhq and Elastic Stack in a single section.

- Split the installation guide in all-in-one installation and distributed deployment.

- Reorganized the upgrade guide.
