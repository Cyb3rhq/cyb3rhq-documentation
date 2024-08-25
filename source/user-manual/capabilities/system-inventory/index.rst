.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: A system inventory is a resource that contains information about the hardware and software assets within an IT infrastructure. Learn more about it here.

.. _system_inventory:

System inventory
================

A system inventory is a resource that contains information about the hardware and software assets within an IT infrastructure. Keeping an inventory of all assets helps organizations maximize the visibility of hardware and software in their environment. An up-to-date system inventory is essential for maintaining good IT hygiene within an enterprise network.

To maintain a centralized system inventory, Cyb3rhq agents collect system information from monitored endpoints and send it to the Cyb3rhq server. The Cyb3rhq Syscollector module is responsible for collecting such data from each agent. The data the Cyb3rhq agent collects includes hardware and operating system information, installed software details, network interfaces, ports, and running processes. The Cyb3rhq agent can also collect data about Windows updates from Windows endpoints. You can configure what kind of information you want the Syscollector module to collect or ignore. 

Users can generate system inventory reports from the Cyb3rhq dashboard, which can be valuable resources during threat hunting and IT hygiene exercises. The information contained in the report can be used to identify unwanted applications, processes, services, and malicious artifacts.


.. topic:: Contents

    .. toctree::
        :maxdepth: 2

        how-it-works
        configuration
        viewing-system-inventory-data
        generating-system-inventory-reports
        available-inventory-fields
        compatibility-matrix
        using-syscollector-information-to-trigger-alerts