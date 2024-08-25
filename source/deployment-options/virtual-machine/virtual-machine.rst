.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: The pre-built Cyb3rhq Virtual Machine includes all Cyb3rhq components ready-to-use. Test all Cyb3rhq capabilities with our OVA.  

.. _virtual_machine:

Virtual Machine (OVA)
=====================

Cyb3rhq provides a pre-built virtual machine image in Open Virtual Appliance (OVA) format. This can be directly imported to VirtualBox or other OVA compatible virtualization systems. Take into account that this VM only runs on 64-bit systems. It does not provide high availability and scalability out of the box. However, these can be implemented by using :doc:`distributed deployment </installation-guide/index>`.


Download the `virtual appliance (OVA) <https://packages.cyb3rhq.com/|CYB3RHQ_CURRENT_MAJOR_OVA|/vm/cyb3rhq-|CYB3RHQ_CURRENT_OVA|.ova>`_, which contains the following components:

    - Amazon Linux 2
    - Cyb3rhq manager |CYB3RHQ_CURRENT_OVA|
    - Cyb3rhq indexer |CYB3RHQ_CURRENT_OVA|
    - Filebeat-OSS |FILEBEAT_LATEST_OVA|
    - Cyb3rhq dashboard |CYB3RHQ_CURRENT_OVA|

Packages list
-------------

.. |VM_AL2_64_OVA| replace:: `cyb3rhq-|CYB3RHQ_CURRENT_OVA|.ova <https://packages.cyb3rhq.com/|CYB3RHQ_CURRENT_MAJOR_OVA|/vm/cyb3rhq-|CYB3RHQ_CURRENT_OVA|.ova>`__ (`sha512 <https://packages.cyb3rhq.com/|CYB3RHQ_CURRENT_MAJOR_OVA|/checksums/cyb3rhq/|CYB3RHQ_CURRENT_OVA|/cyb3rhq-|CYB3RHQ_CURRENT_OVA|.ova.sha512>`__)
.. |CYB3RHQ_OVA_VERSION| replace:: |CYB3RHQ_CURRENT_OVA|

+----------------+--------------+--------------+----------------------+------------------+
|  Distribution  | Architecture | VM Format    | Version              | Package          |
+================+==============+==============+======================+==================+
| Amazon Linux 2 |    64-bit    |      OVA     | |CYB3RHQ_OVA_VERSION|  | |VM_AL2_64_OVA|  |
+----------------+--------------+--------------+----------------------+------------------+

Hardware requirements
---------------------

The following requirements have to be in place before the Cyb3rhq VM can be imported into a host operating system:

- The host operating system has to be a 64-bit system. 
- Hardware virtualization has to be enabled on the firmware of the host.
- A virtualization platform, such as VirtualBox, should be installed on the host system.

Out of the box, the Cyb3rhq VM is configured with the following specifications:

.. |OVA_COMPONENT| replace:: Cyb3rhq v|CYB3RHQ_CURRENT_OVA| OVA

+------------------+----------------+--------------+--------------+
|    Component     |   CPU (cores)  |   RAM (GB)   | Storage (GB) |
+==================+================+==============+==============+
| |OVA_COMPONENT|  |       4        |      8       |     50       |
+------------------+----------------+--------------+--------------+

However, this hardware configuration can be modified depending on the number of protected endpoints and indexed alert data. More information about requirements can be found :doc:`here </quickstart>`. 

Import and access the virtual machine
-------------------------------------

#. Import the OVA to the virtualization platform.

#. If you're using VirtualBox, set the ``VMSVGA`` graphic controller. Setting another graphic controller freezes the VM window.

   #. Select the imported VM.
   #. Click **Settings** > **Display**
   #. In **Graphic controller**, select the ``VMSVGA`` option.

#. Start the machine.
#. Access the virtual machine using the following user and password. You can use the virtualization platform or access it via SSH.
 
   .. code-block:: none

      user: cyb3rhq-user
      password: cyb3rhq

   SSH ``root`` user login has been deactivated; nevertheless, the ``cyb3rhq-user`` retains sudo privileges. Root privilege escalation can be achieved by executing the following command:

   .. code-block:: console

      sudo -i

Access the Cyb3rhq dashboard
--------------------------

Shortly after starting the VM, the Cyb3rhq dashboard can be accessed from the web interface by using the following credentials:

  .. code-block:: none

     URL: https://<cyb3rhq_server_ip>
     user: admin
     password: admin


You can find ``<cyb3rhq_server_ip>``  by typing the following command in the VM:

  .. code-block:: none

     ip a


Configuration files
-------------------

All components included in this virtual image are configured to work out-of-the-box, without the need to modify any settings. However, all components can be fully customized. These are the configuration files locations:

  - Cyb3rhq manager: ``/var/ossec/etc/ossec.conf``

  - Cyb3rhq indexer: ``/etc/cyb3rhq-indexer/opensearch.yml``
  
  - Filebeat-OSS: ``/etc/filebeat/filebeat.yml``
  
  - Cyb3rhq dashboard: 

     - ``/etc/cyb3rhq-dashboard/opensearch_dashboards.yml``

     - ``/usr/share/cyb3rhq-dashboard/data/cyb3rhq/config/cyb3rhq.yml``

VirtualBox time configuration
-----------------------------

In case of using VirtualBox, once the virtual machine is imported it may run into issues caused by time skew when VirtualBox synchronizes the time of the guest machine. To avoid this situation, enable the ``Hardware Clock in UTC Time`` option in the ``System`` tab of the virtual machine configuration.

.. note::
  By default, the network interface type is set to Bridged Adapter. The VM will attempt to obtain an IP address from the network DHCP server. Alternatively, a static IP address can be set by configuring the appropriate network files in the Amazon Linux operating system on which the VM is based.


Once the virtual machine is imported and running, the next step is to :doc:`deploy the Cyb3rhq agents </installation-guide/cyb3rhq-agent/index>` on the systems to be monitored.


Upgrading the VM
----------------

The virtual machine can be upgraded as a traditional installation:

  - :doc:`Upgrading the Cyb3rhq central components </upgrade-guide/upgrading-central-components>`
