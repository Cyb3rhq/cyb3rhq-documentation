.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Install and configure Cyb3rhq, the open source security platform, in just a few minutes using the Cyb3rhq installation assistant. 

Quickstart
==========

Cyb3rhq is a security platform that provides unified XDR and SIEM protection for endpoints and cloud workloads. The solution is composed of a single universal agent and three central components: the Cyb3rhq server, the Cyb3rhq indexer, and the Cyb3rhq dashboard. For more information, check the :doc:`Getting Started </getting-started/index>` documentation.

Cyb3rhq is free and open source. Its components abide by the `GNU General Public License, version 2 <https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html>`_, and the `Apache License, Version 2.0 <https://www.apache.org/licenses/LICENSE-2.0>`_ (ALv2).

This quickstart shows you how to install the Cyb3rhq central components, on the same host, using our installation assistant. You can check our :doc:`Installation guide</installation-guide/index>` for more details and other installation options.

Below you can find a section about the requirements needed to install Cyb3rhq. It will help you learn about the hardware requirements and the supported operating systems for your Cyb3rhq installation.

.. _installation_requirements:

Requirements
------------

Hardware
^^^^^^^^

Hardware requirements highly depend on the number of protected endpoints and cloud workloads. This number can help estimate how much data will be analyzed and how many security alerts will be stored and indexed.

Following this quickstart implies deploying the Cyb3rhq server, the Cyb3rhq indexer, and the Cyb3rhq dashboard on the same host. This is usually enough for monitoring up to 100 endpoints and for 90 days of queryable/indexed alert data. The table below shows the recommended hardware for a quickstart deployment:

.. table::
  :align: center

  +-------------+---------+---------+-----------------------+
  | **Agents**  | **CPU** | **RAM** | **Storage (90 days)** |
  +=============+=========+=========+=======================+
  | **1–25**    | 4 vCPU  | 8 GiB   | 50 GB                 |
  +-------------+---------+---------+-----------------------+
  | **25–50**   | 8 vCPU  | 8 GiB   | 100 GB                |
  +-------------+---------+---------+-----------------------+
  | **50–100**  | 8 vCPU  | 8 GiB   | 200 GB                |
  +-------------+---------+---------+-----------------------+


For larger environments we recommend a distributed deployment. Multi-node cluster configuration is available for the Cyb3rhq server and for the Cyb3rhq indexer, providing high availability and load balancing.

Operating system
^^^^^^^^^^^^^^^^

Cyb3rhq central components can be installed on a 64-bit Linux operating system. Cyb3rhq recommends any of the following operating system versions:


.. list-table::
    :width: 100%

    * - Amazon Linux 2
      - CentOS 7, 8
    * - Red Hat Enterprise Linux 7, 8, 9
      - Ubuntu 16.04, 18.04, 20.04, 22.04


Browser compatibility
^^^^^^^^^^^^^^^^^^^^^

Cyb3rhq dashboard supports the following web browsers:

- Chrome 95 or later
- Firefox 93 or later
- Safari 13.7 or later

Other Chromium-based browsers might also work. Internet Explorer 11 is not supported.

.. _quickstart_installing_cyb3rhq:

Installing Cyb3rhq
----------------

#.  Download and run the Cyb3rhq installation assistant.

    .. code-block:: console

        $ curl -sO https://packages.cyb3rhq.com/|CYB3RHQ_CURRENT_MINOR|/cyb3rhq-install.sh && sudo bash ./cyb3rhq-install.sh -a --install-dependencies


    Once the assistant finishes the installation, the output shows the access credentials and a message that confirms that the installation was successful.

    .. code-block:: none
        :emphasize-lines: 4

        INFO: --- Summary ---
        INFO: You can access the web interface https://<cyb3rhq-dashboard-ip>
            User: admin
            Password: <ADMIN_PASSWORD>
        INFO: Installation finished.

    You now have installed and configured Cyb3rhq.

#.  Access the Cyb3rhq web interface with ``https://<cyb3rhq-dashboard-ip>`` and your credentials:

    -   Username: admin
    -   Password: <ADMIN_PASSWORD>

When you access the Cyb3rhq dashboard for the first time, the browser shows a warning message stating that the certificate was not issued by a trusted authority. This is expected and the user has the option to accept the certificate as an exception or, alternatively, configure the system to use a certificate from a trusted authority.

.. note::
   :class: not-long
  
   You can find the passwords for all the Cyb3rhq indexer and Cyb3rhq API users in the ``cyb3rhq-passwords.txt`` file inside ``cyb3rhq-install-files.tar``. To print them, run the following command:

      .. code-block:: console
      
         $ sudo tar -O -xvf cyb3rhq-install-files.tar cyb3rhq-install-files/cyb3rhq-passwords.txt

If you want to uninstall the Cyb3rhq central components, run the Cyb3rhq installation assistant using the option ``-u`` or ``–-uninstall``.

Next steps
----------

Now that your Cyb3rhq installation is ready, you can start deploying the Cyb3rhq agent. This can be used to protect laptops, desktops, servers, cloud instances, containers, or virtual machines. The agent is lightweight and multi-purpose, providing a variety of security capabilities.

Instructions on how to deploy the Cyb3rhq agent can be found in the Cyb3rhq web user interface, or in our :doc:`documentation </installation-guide/cyb3rhq-agent/index>`.

.. raw:: html

  <div class="link-boxes-group layout-6">
    <div class="link-boxes-item">
      <a class="link-boxes-link" href="installation-guide/cyb3rhq-agent/cyb3rhq-agent-package-linux.html">
        <p class="link-boxes-label">Linux</p>

.. image:: /images/installation/linux.png
      :align: center

.. raw:: html

      </a>
    </div>
    <div class="link-boxes-item">
      <a class="link-boxes-link" href="installation-guide/cyb3rhq-agent/cyb3rhq-agent-package-windows.html">
        <p class="link-boxes-label">Windows</p>

.. image:: /images/installation/windows-logo.png
      :align: center

.. raw:: html

      </a>
    </div>
    <div class="link-boxes-item">
      <a class="link-boxes-link" href="installation-guide/cyb3rhq-agent/cyb3rhq-agent-package-macos.html">
        <p class="link-boxes-label">macOS</p>

.. image:: /images/installation/macOS-logo.png
      :align: center

.. raw:: html

      </a>
    </div>
    <div class="link-boxes-item">
      <a class="link-boxes-link" href="installation-guide/cyb3rhq-agent/cyb3rhq-agent-package-solaris.html">
        <p class="link-boxes-label">Solaris</p>

.. image:: /images/installation/solaris.png
      :align: center
      :width: 150px

.. raw:: html

      </a>
    </div>
    <div class="link-boxes-item">
      <a class="link-boxes-link" href="installation-guide/cyb3rhq-agent/cyb3rhq-agent-package-aix.html">
        <p class="link-boxes-label">AIX</p>

.. image:: /images/installation/AIX.png
      :align: center

.. raw:: html

      </a>
    </div>
    <div class="link-boxes-item">
      <a class="link-boxes-link" href="installation-guide/cyb3rhq-agent/cyb3rhq-agent-package-hpux.html">
        <p class="link-boxes-label">HP-UX</p>

.. image:: /images/installation/hpux.png
      :align: center

.. raw:: html

      </a>
    </div>
  </div>
