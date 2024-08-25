.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Cyb3rhq 4.0.4 has been released. Check out our release notes to discover the changes and additions of this release.

.. _release_4_0_4:

4.0.4 Release notes - 14 January 2021
=====================================

This section lists the changes in version 4.0.4. More details about these changes are provided in the changelog of each component:

- `cyb3rhq/cyb3rhq <https://github.com/cyb3rhq/cyb3rhq/blob/v4.0.4/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-kibana-app <https://github.com/cyb3rhq/cyb3rhq-kibana-app/blob/v4.0.4-7.9.3/CHANGELOG.md>`_


Cyb3rhq core
----------

Added
^^^^^

**API**

- Missing secure headers for API responses to fulfill the OWASP recommendations.
- New option to disable uploading configurations containing remote commands. 
- New option to choose the SSL ciphers. Default value TLSv1.2.

Changed 
^^^^^^^

**API**

- Restore and update API configuration endpoints have been deprecated. 
- JWT token expiration time set to 15 minutes.


Fixed
^^^^^

**API**

- Fixed a path traversal flaw (`CVE-2021-26814 <https://nvd.nist.gov/vuln/detail/CVE-2021-26814>`_) affecting 4.0.0 to 4.0.3 at ``/manager/files`` and ``/cluster/{node_id}/files`` endpoints. This vulnerability allowed authenticated users to execute arbitrary code with administrative privileges via ``/manager/files`` URI. An authenticated user to the service could exploit incomplete input validation on the ``/manager/files`` API to inject arbitrary code within the API service script. Thanks to Davide Meacci for reporting this vulnerability. 

**Framework**

- Bug with client.keys file handling when adding agents without authd.

**Core**

- The purge of the Redhat vulnerabilities database before updating it. 


Cyb3rhq Kibana plugin
-------------------

Added
^^^^^

- Support for Cyb3rhq v4.0.4.
