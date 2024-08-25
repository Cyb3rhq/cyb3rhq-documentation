.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Cyb3rhq 3.13.1 has been released. Check out our release notes to discover the changes and additions of this release.

.. _release_3_13_1:

3.13.1 Release notes - 15 July 2020
===================================

This section lists the changes in version 3.13.1. More details about these changes are provided in each component changelog:

- `cyb3rhq/cyb3rhq <https://github.com/cyb3rhq/cyb3rhq/blob/v3.13.1/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-kibana-app <https://github.com/cyb3rhq/cyb3rhq-kibana-app/blob/3.13.1-7.8.0/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-api <https://github.com/cyb3rhq/cyb3rhq-api/blob/3.13/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-splunk <https://github.com/cyb3rhq/cyb3rhq-splunk/blob/3.13-8.0/CHANGELOG.md>`_

Cyb3rhq core
----------

- Added the settings ``<max_retries>`` and ``<retry_interval>`` to adjust the amount of connection retries and the agent failover interval.
- Fixed ``Modulesd`` crash caused by Vulnerability Detector when OS inventory is disabled for the agent.

Cyb3rhq Kibana app
----------------

- Support for Cyb3rhq v3.13.1.

Cyb3rhq API
---------

- New validator added to the endpoint ``/sca/:agent_id/checks/:policy_id`` that allows using filter the SCA checks by ``reason``, ``status``, and ``command``.

Cyb3rhq Splunk
------------

- Support for Cyb3rhq v3.13.1.
- Support for Splunk v8.0.4.
- Updated references of the field ``vulnerability.reference`` to ``vulnerability.references``.
- Fixed ``cyb3rhq-monitoring`` indices on Splunk 8.0+ version.
