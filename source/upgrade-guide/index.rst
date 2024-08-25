.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Find out more about the process of upgrading the Cyb3rhq central components, Open Distro for Elasticsearch, Elastic Stack, and Cyb3rhq agents in this section.

Upgrade guide
=============

This guide includes instructions to upgrade the :doc:`Cyb3rhq components </getting-started/components/index>`.

Check the :doc:`compatibility-matrix/index` section to learn about the compatibility requirements between components.

Upgrade the Cyb3rhq central components
------------------------------------

The :doc:`upgrading-central-components` section includes instructions to upgrade the Cyb3rhq server, the Cyb3rhq indexer, and the Cyb3rhq dashboard.

.. note::

   Since Cyb3rhq v4.6.0, we don't provide the Kibana plugin and Splunk app anymore. To integrate Cyb3rhq with Elastic or Splunk, refer to our :doc:`/integrations-guide/index`.

Upgrade the Cyb3rhq agents
------------------------

You can upgrade the Cyb3rhq agents either remotely from the Cyb3rhq manager or locally. Upgrading the Cyb3rhq agents remotely is possible by using the ``agent_upgrade`` tool and the Cyb3rhq API. See the :doc:`Remote agent upgrade </user-manual/agent/agent-management/remote-upgrading/upgrading-agent>` section to learn more.

To perform the upgrade locally, select your operating system and follow the instructions.

.. raw:: html

  <div class="link-boxes-group layout-6">
    <div class="link-boxes-item">
      <a class="link-boxes-link" href="./cyb3rhq-agent/linux.html">
        <p class="link-boxes-label">Linux</p>

.. image:: /images/installation/linux.png
      :align: center

.. raw:: html

      </a>
    </div>
    <div class="link-boxes-item">
      <a class="link-boxes-link" href="./cyb3rhq-agent/windows.html">
        <p class="link-boxes-label">Windows</p>

.. image:: /images/installation/windows-logo.png
      :align: center

.. raw:: html

      </a>
    </div>
    <div class="link-boxes-item">
      <a class="link-boxes-link" href="./cyb3rhq-agent/macos.html">
        <p class="link-boxes-label">macOS</p>

.. image:: /images/installation/macOS-logo.png
      :align: center

.. raw:: html

      </a>
    </div>
    <div class="link-boxes-item">
      <a class="link-boxes-link" href="./cyb3rhq-agent/solaris.html">
        <p class="link-boxes-label">Solaris</p>

.. image:: /images/installation/solaris.png
      :align: center
      :width: 150px

.. raw:: html

      </a>
    </div>
    <div class="link-boxes-item">
      <a class="link-boxes-link" href="./cyb3rhq-agent/aix.html">
        <p class="link-boxes-label">AIX</p>

.. image:: /images/installation/AIX.png
      :align: center

.. raw:: html

      </a>
    </div>
    <div class="link-boxes-item">
      <a class="link-boxes-link" href="./cyb3rhq-agent/hp-ux.html">
        <p class="link-boxes-label">HP-UX</p>

.. image:: /images/installation/hpux.png
      :align: center

.. raw:: html

      </a>
    </div>
  </div>

.. toctree::
   :maxdepth: 1
   :hidden:

   upgrading-central-components
   cyb3rhq-agent/index
   compatibility-matrix/index
   manual-backup-restore
   troubleshooting
