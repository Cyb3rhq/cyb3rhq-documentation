.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Cyb3rhq provides an automated way of generating a Virtual machine in OVA format. Learn how to build a Virtual machine with Cyb3rhq central components installed in this section.  

Virtual machine
===============

We provide an automated way of generating a virtual machine (VM). The ``generate_ova.sh`` script orchestrates the creation of an OVA-formatted VM, ready to run the Cyb3rhq central components.

Requirements
------------

-  `Virtual Box <https://www.virtualbox.org/manual/UserManual.html#installation>`__
-  `Vagrant <https://www.vagrantup.com/docs/installation/>`__
-  `Git <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>`__
-  `Python <https://www.python.org/download/releases/2.7/>`__

We recommend using a system with at least the following hardware specifications:

+----------------+--------------+
|   CPU (cores)  |   RAM (GB)   |
+================+==============+
|       4        |      8       |
+----------------+--------------+

Creating the Cyb3rhq VM
---------------------

To create the virtual machine follow these steps:

#. Download our *cyb3rhq-packages* repository from GitHub and navigate to the ``ova/`` directory. Select the version, for example, ``v|CYB3RHQ_CURRENT_OVA|``.

   .. code-block:: console

      $ git clone https://github.com/cyb3rhq/cyb3rhq-packages && cd cyb3rhq-packages/ova && git checkout v|CYB3RHQ_CURRENT_OVA|

#. Execute the ``generate_ova.sh`` script.

   .. code-block:: console

      $ ./generate_ova.sh

The last command above builds a VM with Cyb3rhq central components. It uses production packages by default. If you're building a pre-release version, you must select the development packages instead.

   .. code-block:: console

      $ ./generate_ova.sh -r dev

The ``-r`` or ``--repository`` option selects the stage to use for the packages. For example:

-  ``prod``: Packages released for production environments.
-  ``dev``: Pre-release packages for testing and development purposes.

Check all available options by running the following command.

.. code-block:: console

   $ ./generate_ova.sh -h
