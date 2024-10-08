.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Cyb3rhq provides an automated way of building DEB and RPM packages. Learn how to build your own Cyb3rhq DEB and RPM packages in this section of our documentation.

Linux manager/agent
===================

Cyb3rhq provides an automated way of building DEB and RPM packages using Docker so there is no need for any other dependency.

To create a Debian or RPM package follow these steps:

Requirements
^^^^^^^^^^^^

-  Docker
-  Git

Download our cyb3rhq repository from GitHub and go to the packages directory.

.. code-block:: console

   $ git clone https://github.com/cyb3rhq/cyb3rhq && cd cyb3rhq/packages && git checkout v|CYB3RHQ_CURRENT|

Execute the ``generate_package.sh`` script with your desired options. This script builds a Docker image with all the necessary tools to create the DEB or RPM package and run a container that builds it:

.. code-block:: console

   # ./generate_package.sh -h

.. code-block:: none
   :class: output

   Usage: packages/generate_package.sh [OPTIONS]

     -b, --branch <branch>      [Optional] Select Git branch.
     -t, --target <target>      [Required] Target package to build: manager or agent.
     -a, --architecture <arch>  [Optional] Target architecture of the package [amd64/i386/ppc64le/arm64/armhf].
     -j, --jobs <number>        [Optional] Change number of parallel jobs when compiling the manager or agent. By default: 2.
     -r, --revision <rev>       [Optional] Package revision. By default: 0.
     -s, --store <path>         [Optional] Set the destination path of package. By default, an output folder will be created.
     -p, --path <path>          [Optional] Installation path for the package. By default: /var/ossec.
     -d, --debug                [Optional] Build the binaries with debug symbols. By default: no.
     -c, --checksum             [Optional] Generate checksum on the same directory than the package. By default: no.
     -l, --legacy               [Optional only for RPM] Build package for CentOS 5.
     --dont-build-docker        [Optional] Locally built docker image will be used instead of generating a new one.
     --tag                      [Optional] Tag to use with the docker image.
     --sources <path>           [Optional] Absolute path containing cyb3rhq source code. This option will use local source code instead of downloading it from GitHub. By default use the script path.
     --is_stage                 [Optional] Use release name in package.
     --system                   [Optional] Select Package OS [rpm, deb]. By default is 'deb'.
     --src                      [Optional] Generate the source package in the destination directory.
     --future                   [Optional] Build test future package x.30.0 Used for development purposes.
     -h, --help                 Show this help.

Below, you will find some examples of how to build a DEB and an RPM package.

.. tabs::

   .. group-tab:: DEB

      .. code-block:: console

         # ./generate_package.sh -s /tmp -t manager -a amd64 -r my_rev --system deb

      This command generates a |CYB3RHQ_CURRENT| Cyb3rhq manager DEB package with revision ``my_rev`` for ``amd64`` systems.

      .. code-block:: console

         # ./generate_package.sh -t agent -a amd64 -p /opt/ossec --system deb

      This command generates a |CYB3RHQ_CURRENT| Cyb3rhq agent DEB package with ``/opt/ossec/`` as installation directory for ``amd64`` systems.

   .. group-tab:: RPM

      .. note::

         Use the following architecture equivalences:
 
         -  ``amd64`` -> x86_64
         -  ``arm64`` -> aarch64
         -  ``armhf`` -> armv7hl

      .. code-block:: console

         # ./generate_package.sh -s /tmp -t manager -a amd64 -r my_rev --system rpm

      This command generates a |CYB3RHQ_CURRENT| Cyb3rhq manager RPM package with revision ``my_rev`` for x86_64 systems.

      .. code-block:: console

         # ./generate_package.sh -t agent -a amd64 -p /opt/ossec --system rpm

      This command generates a |CYB3RHQ_CURRENT| Cyb3rhq agent RPM package with ``/opt/ossec/`` as installation directory for x86_64 systems.
