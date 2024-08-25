.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: The Cyb3rhq server API is an open source RESTful API that allows interaction with the Cyb3rhq manager. Learn more in this section of the documentation.

Cyb3rhq server API
================

The Cyb3rhq server API is an open source RESTful API that allows interaction with the Cyb3rhq manager from a web browser, a command-line tool such as cURL, or any script or program capable of making web requests. The Cyb3rhq dashboard relies on the Cyb3rhq server API to remotely manage the Cyb3rhq server infrastructure. You can utilize the Cyb3rhq server API to perform common tasks such as adding agents, restarting the manager(s) or agent(s), or looking up details about File Integrity Monitoring (FIM).

Here is a list of the Cyb3rhq server API capabilities:

-  Cyb3rhq agent management
-  Cyb3rhq manager control and overview
-  Cluster control and overview
-  File integrity monitoring control and search
-  MITRE ATT&CK and CIS-CAT overview
-  Ruleset information
-  Testing and verification of rules and decoders
-  Syscollector information
-  Role-Based Access Control (RBAC)
-  API management (HTTPS, configuration)
-  Users management
-  Statistical information
-  Error handling
-  Query remote configuration

Refer to the :doc:`Cyb3rhq server API reference </user-manual/api/reference>` for details about all the Cyb3rhq server API endpoints. Also consider :doc:`use cases <use-cases>` for example usage of the Cyb3rhq server API.

.. topic:: Contents

   .. toctree::
      :maxdepth: 2

      getting-started
      configuration
      securing-api
      rbac/index
      queries
      use-cases
      reference
