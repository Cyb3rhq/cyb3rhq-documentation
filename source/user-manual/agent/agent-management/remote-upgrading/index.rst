.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Cyb3rhq agents can be upgraded remotely from the Cyb3rhq server. Learn more in this section of the documentation.

Remote upgrading
==================

Cyb3rhq agents can be upgraded remotely from the Cyb3rhq server. The Cyb3rhq manager performs this upgrade and sends each enrolled agent a WPK (Cyb3rhq signed package) file containing the files needed to upgrade to the new version. This streamlines the upgrade process across your installation and eliminates the need to access each agent individually.

Cyb3rhq provides access to an updated WPK repository for each new release. All available WPK files can be found :doc:`here <wpk-files/wpk-list>`. Users can also generate custom WPK files and host them in a custom repository. Custom WPK files can be created by following the steps described in :doc:`Custom WPK creation <wpk-files/index>`.

.. note::

   The upgrade procedure is performed by the :doc:`agent upgrade module <agent-upgrade-module>`.

Learn more about remote upgrading of the Cyb3rhq agents in the following sections:

.. toctree::
   :maxdepth: 2

   upgrading-agent
   wpk-files/index
   agent-upgrade-module

