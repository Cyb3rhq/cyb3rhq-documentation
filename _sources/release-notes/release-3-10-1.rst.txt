.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Cyb3rhq 3.10.1 has been released. Check out our release notes to discover the changes and additions of this release.

.. _release_3_10_1:

3.10.1 Release notes - 19 September 2019
========================================

This section lists the changes in version 3.10.1. More details about these changes are provided in each component changelog:

- `cyb3rhq/cyb3rhq <https://github.com/cyb3rhq/cyb3rhq/blob/v3.10.1/CHANGELOG.md>`_

Cyb3rhq core
----------

- Fix error in Remoted when reloading agent keys (locked mutex disposal).
- Fix invalid read error in Remoted counters.

Cyb3rhq API
---------

- Fixed error after removing a high volume of agents from a group using the Cyb3rhq API.
