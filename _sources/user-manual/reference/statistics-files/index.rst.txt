.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: The statistics files are documents that show real-time information about the Cyb3rhq environment. Learn more about it in this section of the documentation.

.. _reference_statistics_files:

Statistics files
================

The **statistics files** are documents that show real-time information about the Cyb3rhq environment as the processed events, received messages, and the state of the remote connections.

Agents statistical files:

  * :ref:`cyb3rhq-agentd.state <cyb3rhq_agentd_state_file>` - It shows the amount of events generated,
    last connection date and agent status, among other useful information related to the agent.

Manager statistical files:

  * :ref:`cyb3rhq-remoted.state <cyb3rhq_remoted_state_file>` - It shows information
    about the :ref:`remote daemon <cyb3rhq-remoted>`
  * :ref:`cyb3rhq-analysisd.state <cyb3rhq_analysisd_state_file>` - It shows information
    about the :ref:`analysis daemon <cyb3rhq-analysisd>`.

Manager and Agents statistical files:

  * :ref:`cyb3rhq-logcollector.state <cyb3rhq_logcollector_state_file>` - It shows information about :ref:`logcollector daemon <cyb3rhq-logcollector>`.

.. topic:: Contents

  .. toctree::
      :maxdepth: 1

      cyb3rhq-agentd-state
      cyb3rhq-remoted-state
      cyb3rhq-analysisd-state
      cyb3rhq-logcollector-state
