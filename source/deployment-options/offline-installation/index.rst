.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Discover the offline step-by-step process to install the Cyb3rhq central components without connection to the Internet.

Offline installation
====================

You can install Cyb3rhq even when there is no connection to the Internet. Installing the solution offline involves downloading the Cyb3rhq central components to later install them on a system with no Internet connection. The Cyb3rhq server, the Cyb3rhq indexer, and the Cyb3rhq dashboard can be installed and configured on the same host in an all-in-one deployment, or each component can be installed on a separate host as a distributed deployment, depending on your environment needs. 

For more information about the hardware requirements and the recommended operating systems, check the :ref:`Requirements <installation_requirements>` section.

.. note:: You need root user privileges to run all the commands described below.

Prerequisites
-------------

- ``curl``, ``tar``, and ``setcap`` need to be installed in the target system where the offline installation will be carried out. ``gnupg`` might need to be installed as well for some Debian-based systems.

- In some systems, the command ``cp`` is an alias for ``cp -i`` — you can check this by running ``alias cp``. If this is your case, use ``unalias cp`` to avoid being asked for confirmation to overwrite files.

Download the packages and configuration files
---------------------------------------------

#. Run the following commands from any Linux system with Internet connection. This action executes a script that downloads all required files for the offline installation on x86_64 architectures. Select the package format to download.
    
   .. tabs::

        .. group-tab:: RPM

            .. code-block:: console
        
               # curl -sO https://packages.cyb3rhq.com/|CYB3RHQ_CURRENT_MINOR|/cyb3rhq-install.sh
               # chmod 744 cyb3rhq-install.sh
               # ./cyb3rhq-install.sh -dw rpm

        .. group-tab:: DEB

            .. code-block:: console
        
               # curl -sO https://packages.cyb3rhq.com/|CYB3RHQ_CURRENT_MINOR|/cyb3rhq-install.sh
               # chmod 744 cyb3rhq-install.sh
               # ./cyb3rhq-install.sh -dw deb
          
#. Download the certificates configuration file.

      .. code-block:: console
        
         # curl -sO https://packages.cyb3rhq.com/|CYB3RHQ_CURRENT_MINOR|/config.yml

#. Edit ``config.yml`` to prepare the certificates creation.

   -  If you are performing an all-in-one deployment, replace ``"<indexer-node-ip>"``, ``"<cyb3rhq-manager-ip>"``, and ``"<dashboard-node-ip>"`` with ``127.0.0.1``.
        
   -  If you are performing a distributed deployment, replace the node names and IP values with the corresponding names and IP addresses. You need to do this for all the Cyb3rhq server, the Cyb3rhq indexer, and the Cyb3rhq dashboard nodes. Add as many node fields as needed.


#.  Run the ``./cyb3rhq-install.sh -g`` to create the certificates. For a multi-node cluster, these certificates need to be later deployed to all Cyb3rhq instances in your cluster.

    .. code-block:: console
    
        # ./cyb3rhq-install.sh -g            

#. Copy or move the following files to a directory on the host(s) from where the offline installation will be carried out. You can use ``scp`` for this.

   -  ``cyb3rhq-install.sh``
   -  ``cyb3rhq-offline.tar.gz``
   -  ``cyb3rhq-install-files.tar``

Next steps
----------

Once the Cyb3rhq files are ready and copied to the specified hosts, it is necessary to install the Cyb3rhq components.


.. toctree::
  :maxdepth: 1

  installation-assistant
  step-by-step