.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Learn how to uninstall the Cyb3rhq agent.
  
Uninstalling the Cyb3rhq agent
============================

This section describes how to uninstall Cyb3rhq agents installed across the different operating systems below:

-  :ref:`Linux <uninstalling_linux_agent>`
-  :ref:`Windows <uninstalling_windows_agent>`
-  :ref:`macOS <uninstalling_macos_agent>`
-  :ref:`Solaris <uninstalling_solaris_agent>`
-  :ref:`AIX <uninstalling_aix_agent>`
-  :ref:`HPUX <uninstalling_hpux_agent>`

.. _uninstalling_linux_agent:

Uninstalling a Linux Cyb3rhq agent
--------------------------------

Run the following commands to uninstall a Linux agent.


#. Remove the Cyb3rhq agent installation. 

   .. tabs::
 
      .. group-tab:: Yum
  
         .. include:: ../../_templates/installations/cyb3rhq/yum/uninstall_cyb3rhq_agent.rst
 
      .. group-tab:: APT
 
         .. include:: ../../_templates/installations/cyb3rhq/deb/uninstall_cyb3rhq_agent.rst

      .. group-tab:: ZYpp
  
         .. include:: ../../_templates/installations/cyb3rhq/zypp/uninstall_cyb3rhq_agent.rst

      .. group-tab:: APK
  
         .. include:: ../../_templates/installations/cyb3rhq/apk/uninstall_cyb3rhq_agent.rst

#. Disable the Cyb3rhq agent service. 

   .. include:: ../../_templates/installations/cyb3rhq/common/disable_cyb3rhq_agent_service.rst

The Cyb3rhq agent is now completely removed from your Linux endpoint.

.. _uninstalling_windows_agent:

Uninstalling a Windows Cyb3rhq agent
----------------------------------

To uninstall the agent, the original Windows installer file is required to perform the unattended process:

  .. code-block:: none
  
      msiexec.exe /x cyb3rhq-agent-|CYB3RHQ_CURRENT_WINDOWS|-|CYB3RHQ_REVISION_WINDOWS|.msi /qn  

The Cyb3rhq agent is now completely removed from your Windows endpoint.

.. _uninstalling_macos_agent:

Uninstalling a macOS Cyb3rhq agent
--------------------------------

Follow these steps to uninstall the Cyb3rhq agent from your macOS endpoint.

#. Stop the Cyb3rhq agent service.

    .. code-block:: console

      # launchctl unload /Library/LaunchDaemons/com.cyb3rhq.agent.plist

#. Remove the ``/Library/Ossec/`` folder.

    .. code-block:: console

      # /bin/rm -r /Library/Ossec

#. Remove ``launchdaemons`` and ``StartupItems``.

    .. code-block:: console

      # /bin/rm -f /Library/LaunchDaemons/com.cyb3rhq.agent.plist
      # /bin/rm -rf /Library/StartupItems/CYB3RHQ

#. Remove the Cyb3rhq user and group.

    .. code-block:: console

      # /usr/bin/dscl . -delete "/Users/cyb3rhq"
      # /usr/bin/dscl . -delete "/Groups/cyb3rhq"

#. Remove from ``pkgutil``.

    .. code-block:: console

      # /usr/sbin/pkgutil --forget com.cyb3rhq.pkg.cyb3rhq-agent

The Cyb3rhq agent is now completely removed from your macOS endpoint.

.. _uninstalling_solaris_agent:

Uninstalling a Solaris Cyb3rhq agent
----------------------------------

Select the Solaris version you want to uninstall.

.. tabs::

  .. group-tab:: Solaris 10

    .. include:: ../../_templates/installations/cyb3rhq/solaris/uninstall_cyb3rhq_agent_s10.rst

  .. group-tab:: Solaris 11

    .. include:: ../../_templates/installations/cyb3rhq/solaris/uninstall_cyb3rhq_agent_s11.rst

The Cyb3rhq agent is now completely removed from your Solaris endpoint.

.. _uninstalling_aix_agent:

Uninstalling an AIX Cyb3rhq agent
-------------------------------

Follow the steps below to uninstall the Cyb3rhq agent from the AIX endpoint.

.. code-block:: console

   # rpm -e cyb3rhq-agent

Some files are not removed from the filesystem by the package manager. Delete the ``/var/ossec/`` folder if you want to remove all files completely. 

The Cyb3rhq agent is now completely removed from your AIX system

.. _uninstalling_hpux_agent:

Uninstalling an HP-UX Cyb3rhq agent
---------------------------------

Follow the steps below to uninstall the Cyb3rhq agent from the HP-UX endpoint.

#. Stop the Cyb3rhq agent service.


   .. code-block:: console

      # /var/ossec/bin/cyb3rhq-control stop

#. Delete ``cyb3rhq`` user and group:

   .. code-block:: console

      # groupdel cyb3rhq
      # userdel cyb3rhq

#. Remove Cyb3rhq files.

   .. code-block:: console

      # rm -rf /var/ossec

The Cyb3rhq agent is now completely removed from your HP-UX endpoint.
