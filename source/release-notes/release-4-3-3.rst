.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
      :description: Cyb3rhq 4.3.3 has been released. Check out our release notes to discover the changes and additions of this release.

.. _release_4_3_3:

4.3.3 Release notes - 1 June 2022
=================================

This section lists the changes in version 4.3.3. Every update of the Cyb3rhq solution is cumulative and includes all enhancements and fixes from previous releases.

What's new
----------

This release includes new features or enhancements.

Cyb3rhq Kibana plugin
^^^^^^^^^^^^^^^^^^^

- Cyb3rhq Kibana plugin is now compatible with Cyb3rhq 4.3.3.

Cyb3rhq Splunk app
^^^^^^^^^^^^^^^^

- Cyb3rhq Splunk app is now compatible with Cyb3rhq 4.3.3. 


Resolved issues
---------------

This release resolves known issues. 

Manager
^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#13651 <https://github.com/cyb3rhq/cyb3rhq/pull/13651>`_             Avoid creating duplicated ``<client>`` configuration blocks during deployment. 
==============================================================    =============


Agent
^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#13642 <https://github.com/cyb3rhq/cyb3rhq/pull/13642>`_             Prevent `Agentd` from resetting its configuration on ``<client>`` block re-definition.
==============================================================    =============


Cyb3rhq dashboard
^^^^^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#4151 <https://github.com/cyb3rhq/cyb3rhq-kibana-app/pull/4151>`_    The Cyb3rhq dashboard troubleshooting URL is now fixed. 
==============================================================    =============

Cyb3rhq Kibana plugin for Kibana 7.10.2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#4150 <https://github.com/cyb3rhq/cyb3rhq-kibana-app/pull/4150>`_    The Cyb3rhq Kibana plugin troubleshooting URL is now fixed.
==============================================================    =============

Cyb3rhq Kibana plugin for Kibana 7.16.x and 7.17.x
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

==============================================================    =============
Reference                                                         Description
==============================================================    =============
`#4146 <https://github.com/cyb3rhq/cyb3rhq-kibana-app/pull/4146>`_    A bug that prevented removing implicit filters in modules is now fixed.  
`#4150 <https://github.com/cyb3rhq/cyb3rhq-kibana-app/pull/4150>`_    The Cyb3rhq Kibana plugin troubleshooting URL is now fixed. 
==============================================================    =============



Changelogs
----------

More details about these changes are provided in the changelog of each component:

- `cyb3rhq/cyb3rhq <https://github.com/cyb3rhq/cyb3rhq/blob/v4.3.3/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-dashboard <https://github.com/cyb3rhq/cyb3rhq-kibana-app/blob/v4.3.3-1.2.0-wzd/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-kibana-app <https://github.com/cyb3rhq/cyb3rhq-kibana-app/blob/v4.3.3-7.17.3/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-splunk <https://github.com/cyb3rhq/cyb3rhq-splunk/blob/v4.3.3-8.2.6/CHANGELOG.md>`_