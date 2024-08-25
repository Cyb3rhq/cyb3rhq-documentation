.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Cyb3rhq 3.8.1 has been released. Check out our release notes to discover the changes and additions of this release.

.. _release_3_8_1:

3.8.1 Release notes - 24 January 2019
=====================================

This section shows the most relevant improvements and fixes in version 3.8.1. More details about these changes are provided in each component changelog:

- `cyb3rhq/cyb3rhq <https://github.com/cyb3rhq/cyb3rhq/blob/v3.8.1/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-api <https://github.com/cyb3rhq/cyb3rhq-api/blob/v3.8.1/CHANGELOG.md>`_

Cyb3rhq core
----------

- Fixed memory leak in Logcollector when reading Windows eventchannel.
- Fixed version comparisons on Red Hat systems in vulnerability detector module.

Cyb3rhq API
---------

- Fixed an issue with the log rotation module which may makes the Cyb3rhq API unavailable on Debian systems.
- Fixed improper error handling. Prevented internal paths to be printed in error output.
