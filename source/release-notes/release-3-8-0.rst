.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Cyb3rhq 3.8.0 has been released. Check out our release notes to discover the changes and additions of this release.

.. _release_3_8_0:

3.8.0 Release notes - 18 January 2019
=====================================

This section shows the most relevant improvements and fixes in version 3.8.0. More details about these changes are provided in each component changelog:

- `cyb3rhq/cyb3rhq <https://github.com/cyb3rhq/cyb3rhq/blob/v3.8.0/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-api <https://github.com/cyb3rhq/cyb3rhq-api/blob/v3.8.0/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-ruleset <https://github.com/cyb3rhq/cyb3rhq-ruleset/blob/v3.8.0/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-kibana-app <https://github.com/cyb3rhq/cyb3rhq-kibana-app/blob/v3.8.0-6.5.4/CHANGELOG.md>`_
- `cyb3rhq/cyb3rhq-splunk <https://github.com/cyb3rhq/cyb3rhq-splunk/blob/v3.8.0-7.2.3/CHANGELOG.md>`_

Cyb3rhq core
----------

**Support for new AWS services**

- AWS Config
- AWS Trusted Advisor
- AWS KMS
- AWS Inspector
- Add support for IAM roles authentication in EC2 instances.

Adding new kind of buckets to your integration is as simple as adding an entry like this to your AWS configuration:

.. code-block:: xml

  <bucket type="config">
    <name>cyb3rhq-aws-wodle</name>
    <path>config</path>
  </bucket>


The alerts that Cyb3rhq sends to Elasticsearch are now including all these AWS additions, so you can track all your AWS services / buckets using Kibana.

**Windows events are collected in native JSON**

- The inventory features for Windows are now using native queries directly to the Windows API, this adds value for this feature, enriches the inventory for Windows and guarantees that you can check your Windows agent accurately.
- Windows events are now being fetched in JSON format, which provides a useful format for third-party software and makes Cyb3rhq be more optimized while analyzing Windows events. This improves Windows alerts result and analyzing performance. From this version, Windows agents apply a new rule set

.. thumbnail:: ../images/release-notes/3.8.0/event-channel-alert.png
  :title: New Windows alerts
  :align: center
  :width: 100%

- FIM for Windows agents now has the ability to detect changes in attributes and file permissions.

**Agents keys polling module**

When Remoted reads an invalid key, now it can retrieve it from an external database server and store it to the `client.keys` file.

Details:

- Integrated agent key request to external data sources.
- Look for missing or old agent keys when Remoted detects an authorization failure.
- Request agent keys by calling a defined executable or connecting to a local socket.

**FIM who-data changes**

- Added a health check for who-data monitoring features. It checks if the Audit events socket is working before starting the who-data engine in order to avoid start listening to it when it's blocked or disabled.
- Checks if a rule already exists before trying to insert it to avoid flooding in the `audit.log` file.
- Who-data module is now able to re-connect to an Audit socket even if the instance is using enforcing with SELinux. Before this enhancement, Cyb3rhq could not re-connect the socket after restart Cyb3rhq if enforcing was being used along Audit.

**CDB lists auto build**

Now the CDB lists are built at installation time, so there is no need to execute `ossec-makelists` as before for the default lists. Custom lists (added after installation) still need to be compiled manually.

**Other Cyb3rhq core fixes and improvements**

- When upgrading, databases used for FIM purposes are now auto-upgraded by Cyb3rhq (no need for scripts).
- Vulnerability detector has been improved for RedHat systems.
- This version also fixes some known issues when using Cyb3rhq on ARM, HP-UX or AIX systems.
- Logcollector component has been refactored, multiple known issues have been fixed, its performance has been also improved.
- Improved IP address validation in the option ``<white_list>`` (Credits to `@pillarsdotnet <https://github.com/pillarsdotnet>`_).
- Improved rule option ``<info>`` validation (Credits to `@pillarsdotnet <https://github.com/pillarsdotnet>`_).
- Fixed error description in the osquery configuration parser (Credits to `@pillarsdotnet <https://github.com/pillarsdotnet>`_).
- The FTS comment option ``<ftscomment>`` was not being read (Credits to `@pillarsdotnet <https://github.com/pillarsdotnet>`_).

Cyb3rhq API
---------

**New API calls for group management**

- Edit group configuration file (agent.conf) uploading XML file with new configuration. This addition brings the user the ability to **manage groups remotely**, from now and onward it's **no longer needed to SSH** into the manager instance to modify groups or to add/remove agents in groups.

.. code-block:: console

  # curl -u foo:bar -X POST -H 'Content-type: application/xml' -d @/tmp/agent.conf.xml \
      "http://localhost:55000/agents/groups/default/files/agent.conf?pretty"

.. code-block:: js
  :class: output

  {
    "error": 0,
    "data": "Agent configuration was updated successfully"
  }

- Add or remove agents of a group in bulk.
- Added a new parameter named format for fetching the agent.conf content in JSON/XML format depending on the parameter value.

**Cyb3rhq API also has these fixes for this version**

- Now the Cyb3rhq API service gets the group ID and user ID properly when using Docker containers.
- Added missing information when requesting certain files from a group.
- Rule variables from the Cyb3rhq ruleset are now replaced by its real value when fetching rules.

Cyb3rhq app
---------

**Group management from the app is now available**

Manage your groups from the app, this feature includes:

- Edit group configuration (agent.conf), just open the XML editor we've added, edit the group configuration and send it to the Cyb3rhq API.

.. thumbnail:: ../images/release-notes/3.8.0/xml-edit.png
  :title: XML editor
  :align: center
  :width: 100%

- Adding and removing agents in groups. An intuitive view has been added to drag-drop agents in your groups then a button is clicked and your groups are updated.

.. thumbnail:: ../images/release-notes/3.8.0/add-remove-agents.png
  :title: Add or remove agents
  :align: center
  :width: 100%

**New search bar for the agents' list**

- The search bar has been modified to provide an better user experience.
- It suggests filters, allows multiple filters at the same time, combines string searches with filters, same as before but now in one place.

.. thumbnail:: ../images/release-notes/3.8.0/search-bar.png
  :title: AWS sample alert
  :align: center
  :width: 100%

**New tables for an agent FIM monitored files**

- The app detects the agent OS in order to show the right FIM data. For instance, if it's a Windows agent, the app shows Windows registry entries.

.. thumbnail:: ../images/release-notes/3.8.0/fim-files-windows.png
  :title: FIM monitored files for Windows
  :align: center
  :width: 100%

- As most of the app tables, these tables include a search bar and sortable columns.

**Modify the Cyb3rhq monitoring index pattern name**

This was added before for Cyb3rhq alerts indices, now you can do the same for monitoring indices editing the app configuration file (config.yml).

.. code-block:: yaml

  # Default index pattern to use for Cyb3rhq monitoring
  cyb3rhq.monitoring.pattern: cyb3rhq-monitoring-3.x-*

**Edit the app configuration file (config.yml) from the app**

- Those settings are shown at Settings > Configuration as before but now they include a pencil icon which allows you to edit certain settings.
- Note: Some settings need that Kibana is restarted before being applied.

**Other app improvements**

- The Dev Tools utility has been improved, small bugs fixed, resizable columns by dragging.
- Template check from the app health check now accepts multipattern templates.
- All known fields for all the index patterns are now refreshed on the app health check too.
- Added "Registered date" and "Last keep alive" in agents table allowing you to sort by these fields.
- Now the app looks for the request target if the destination is unreachable. Now you'll know if it was Elasticsearch or the Cyb3rhq API.

Cyb3rhq ruleset
-------------

**New rules/decoders for Windows**

Our ruleset this time comes with some new rules/decoders for Windows:

- Added new rules to support the new Windows eventchannel decoder.
- Extend Auditd decoder to support more fields.

And we've added a new rule to alert when an agent is removed.
