.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: The Cyb3rhq agent uses the Syscollector module to gather relevant information from the monitored endpoint. Learn how Syscollector works in this section.

How it works
============

As mentioned above, the Cyb3rhq agent uses the Syscollector module to gather relevant information from the monitored endpoint. Once the agent service starts on a monitored endpoint, the Syscollector module runs periodical scans and collects data on the system properties defined in your configuration. The data is first stored in a temporal local database on the endpoint. 

The agent forwards the newly collected data from its local database to the Cyb3rhq server. Each agent uses a separate database on the Cyb3rhq server. The Cyb3rhq server updates the appropriate tables of the inventory database on the Cyb3rhq server using the information the agent sends. For example, the Cyb3rhq server stores hardware-related information in a table called ``sys_hwinfo``.

The Cyb3rhq dashboard automatically displays the data stored in the inventory database. However, you can query the database using the Cyb3rhq API or the ``SQLite`` tool. In addition, the :doc:`vulnerability detection </user-manual/capabilities/vulnerability-detection/index>` module uses :ref:`packages <syscollector_packages>` and :ref:`Windows updates <syscollector_hotfixes>` information in the inventory to detect vulnerable and patched software on monitored endpoints.



        