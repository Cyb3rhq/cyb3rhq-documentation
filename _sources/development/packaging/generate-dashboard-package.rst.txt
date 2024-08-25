.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Cyb3rhq provides an automated way of building packages for the Cyb3rhq components. Learn how to build your own Cyb3rhq dashboard package in this section of our documentation.

Cyb3rhq dashboard
===============

The packages generation process is orchestrated by the ``build-packages.sh`` script, which is found within the ``dev-tools/build-packages/`` folder of the repository. This script is responsible for bundling plugins into one single application in tar, rpm and/or deb distributions. It takes the following parameters:

-  version
-  revision
-  distribution
-  cyb3rhq-dashboard, cyb3rhq-dashboard-plugins, and cyb3rhq-security-dashboards-plugin package paths

Official packages are built through a GitHub Actions pipeline, however, the process is designed to be independent enough for maximum portability. The building process is self-contained in the application code.

Build manually
^^^^^^^^^^^^^^

Requirements:

-  Docker

Generating zip packages
~~~~~~~~~~~~~~~~~~~~~~~

To use the script you first need to generate the packages from these repositories:

-  ``cyb3rhq-dashboard``
-  ``cyb3rhq-security-dashboards-plugin`` 
-  ``cyb3rhq-dashboard-plugins``

To build the packages, follow these steps:

#. Clone the Cyb3rhq dashboard repository and build the application.

   .. code:: console

      # git clone -b <BRANCH_OR_TAG> https://github.com/cyb3rhq/cyb3rhq-dashboard.git
      # cd cyb3rhq-dashboard/
      # yarn osd bootstrap
      # yarn build --linux --skip-os-packages --release

   Example:

   .. code:: console

      # git clone -b 4.9.0 https://github.com/cyb3rhq/cyb3rhq-dashboard.git
      # cd cyb3rhq-dashboard/
      # yarn osd bootstrap
      # yarn build --linux --skip-os-packages --release

#. Clone the Cyb3rhq Security Dashboards Plugin repository in the plugins folder and build the plugin.

   .. code:: console

      # cd plugins/
      # git clone -b <BRANCH_OR_TAG> https://github.com/cyb3rhq/cyb3rhq-security-dashboards-plugin.git
      # cd cyb3rhq-security-dashboards-plugin/
      # yarn
      # yarn build

   Example:

   .. code:: console

      # cd plugins/
      # git clone -b 4.9.0 https://github.com/cyb3rhq/cyb3rhq-security-dashboards-plugin.git
      # cd cyb3rhq-security-dashboards-plugin/
      # yarn
      # yarn build

#. Clone the Cyb3rhq dashboard plugins repository in the plugins folder, move the contents of the plugins folder to the folder where the repository was cloned and build the plugins.

   .. note::

      The yarn build command requires an entry specifying the OpenSearch Dashboard version. This version can be obtained from the ``package.json`` file.

   .. code:: console

      # cd ../
      # git clone -b <BRANCH_OR_TAG> https://github.com/cyb3rhq/cyb3rhq-dashboard-plugins.git
      # cd cyb3rhq-dashboard-plugins/
      # cp -r plugins/* ../
      # cd ../main
      # yarn
      # yarn build
      # cd ../cyb3rhq-core/
      # yarn
      # yarn build
      # cd ../cyb3rhq-check-updates/
      # yarn
      # yarn build

   Example:

   .. code:: console

      # cd ../
      # git clone -b 4.9.0 https://github.com/cyb3rhq/cyb3rhq-dashboard-plugins.git
      # cd cyb3rhq-dashboard-plugins/
      # cp -r plugins/* ../
      # cd ../main
      # yarn
      # yarn build
      # cd ../cyb3rhq-core/
      # yarn
      # yarn build
      # cd ../cyb3rhq-check-updates/
      # yarn
      # yarn build

#. Zip the packages and move them to the packages folder

   .. code:: console

      # cd ../../../
      # mkdir packages
      # cd packages
      # zip -r -j ./dashboard-package.zip ../cyb3rhq-dashboard/target/opensearch-dashboards-2.13.0-linux-x64.tar.gz
      # zip -r -j ./security-package.zip ../cyb3rhq-dashboard/plugins/cyb3rhq-security-dashboards-plugin/build/security-dashboards-<OPENSEARCH_VERSION>.0.zip
      # zip -r -j ./cyb3rhq-package.zip ../cyb3rhq-dashboard/plugins/cyb3rhq-check-updates/build/cyb3rhqCheckUpdates-<OPENSEARCH_VERSION>.zip ../cyb3rhq-dashboard/plugins/main/build/cyb3rhq-<OPENSEARCH_VERSION>.zip ../cyb3rhq-dashboard/plugins/cyb3rhq-core/build/cyb3rhqCore-<OPENSEARCH_VERSION>.zip

   Example:

   .. code:: console

      # cd ../../../
      # mkdir packages
      # cd packages
      # zip -r -j ./dashboard-package.zip ../cyb3rhq-dashboard/target/opensearch-dashboards-2.13.0-linux-x64.tar.gz
      # zip -r -j ./security-package.zip ../cyb3rhq-dashboard/plugins/cyb3rhq-security-dashboards-plugin/build/security-dashboards-2.13.0.0.zip
      # zip -r -j ./cyb3rhq-package.zip ../cyb3rhq-dashboard/plugins/cyb3rhq-check-updates/build/cyb3rhqCheckUpdates-2.13.0.zip ../cyb3rhq-dashboard/plugins/main/build/cyb3rhq-2.13.0.zip ../cyb3rhq-dashboard/plugins/cyb3rhq-core/build/cyb3rhqCore-2.13.0.zip

At this point you must have three packages in the ``packages`` folder:

-  ``dashboard-package.zip``
-  ``security-package.zip``
-  ``cyb3rhq-package.zip``

Using the script
~~~~~~~~~~~~~~~~

Run the ``build-packages.sh`` script in the ``dev-tools/build-packages/`` folder of the repository. The script requires the following parameters:

-  ``-v``: Version of the package.
-  ``-r``: Revision of the package.
-  ``--deb`` or ``--rpm``: Distribution of the package.
-  ``-a``: Path to the ``cyb3rhq-package.zip``.
-  ``-s``: Path to the ``security-package.zip``.
-  ``-b``: Path to the ``dashboard-package.zip``.

.. code:: console

   # cd ../cyb3rhq-dashboard/dev-tools/build-packages/
   # ./build-packages.sh -v <VERSION> -r <REVISION> --<DISTRIBUTION_(--deb_OR_--rpm)> -a file:///<PATH_TO_cyb3rhq-package.zip> -s file:///<PATH_TO_security-package.zip> -b file:///<PATH_TO_dashboard-package.zip>

Example:

.. code:: console

   # cd ../cyb3rhq-dashboard/dev-tools/build-packages/
   # ./build-packages.sh -v 4.9.0 -r 1 --deb -a file:///packages/cyb3rhq-package.zip -s file:///packages/security-package.zip -b file:///packages/dashboard-package.zip

The package will be generated in the ``output`` folder of the same directory where the script is located.

Build with Docker image
^^^^^^^^^^^^^^^^^^^^^^^

With this option you can create an image that has the package in tar.gz format and then if desired you can use the created package to generate the .deb or .rpm file.

#. Clone the Cyb3rhq dashboard repository.

   .. code:: console
   
      # git clone -b <BRANCH_OR_TAG> https://github.com/cyb3rhq/cyb3rhq-dashboard.git
      # cd cyb3rhq-dashboard/dev-tools/build-packages/
   
   Example:
   
   .. code:: console
   
      # git clone -b 4.9.0 https://github.com/cyb3rhq/cyb3rhq-dashboard.git
      # cd cyb3rhq-dashboard/dev-tools/build-packages/

#. Build the Docker image with the following parameters:

   -  ``NODE_VERSION``: Node version to use in the ``.nvmrc`` file.
   -  ``CYB3RHQ_DASHBOARDS_BRANCH``: Branch of the Cyb3rhq dashboards repository.
   -  ``CYB3RHQ_DASHBOARDS_PLUGINS``: Branch of the Cyb3rhq dashboards Plugins repository.
   -  ``CYB3RHQ_SECURITY_DASHBOARDS_PLUGIN_BRANCH``: Branch of the Cyb3rhq Security Dashboards Plugin repository.
   -  ``OPENSEARCH_DASHBOARDS_VERSION``: Version of the OpenSearch Dashboards. You can find the version in the ``package.json`` file of the Cyb3rhq dashboards repository.
   -  ``-t``: Tag of the image.

   .. code:: console
   
      # docker build \
      --build-arg NODE_VERSION=<NODE_VERSION> \
      --build-arg CYB3RHQ_DASHBOARDS_BRANCH=<BRANCH_OF_cyb3rhq-dashboard> \
      --build-arg CYB3RHQ_DASHBOARDS_PLUGINS=<BRANCH_OF_cyb3rhq-dashboard-plugins> \
      --build-arg CYB3RHQ_SECURITY_DASHBOARDS_PLUGIN_BRANCH=<BRANCH_OF_cyb3rhq-security-dashboards-plugin> \
      --build-arg OPENSEARCH_DASHBOARDS_VERSION=<OPENSEARCH_DASHBOARDS_VERSION> \
      -t <TAG_OF_IMAGE> \ 
      -f cyb3rhq-dashboard.Dockerfile .

   Example:
   
   .. code:: console
   
      # docker build \
      --build-arg NODE_VERSION=18.19.0 \
      --build-arg CYB3RHQ_DASHBOARDS_BRANCH=4.9.0 \
      --build-arg CYB3RHQ_DASHBOARDS_PLUGINS=4.9.0 \
      --build-arg CYB3RHQ_SECURITY_DASHBOARDS_PLUGIN_BRANCH=4.9.0 \
      --build-arg OPENSEARCH_DASHBOARDS_VERSION=2.13.0 \
      -t wzd:4.9.0 \
      -f cyb3rhq-dashboard.Dockerfile .

#. Run the Docker image:

   .. code:: console
   
      # docker run -d --rm --name cyb3rhq-dashboard-package <TAG_OF_IMAGE> tail -f /dev/null
   
   Example:
   
   .. code:: console
   
      # docker run -d --rm --name cyb3rhq-dashboard-package wzd:4.9.0 tail -f /dev/null

#. Copy the package to the host:

   .. code:: console
   
      # docker cp cyb3rhq-dashboard-package:/home/node/packages/. <PATH_TO_SAVE_THE_PACKAGE>

   Example:
   
   .. code:: console
   
      # docker cp cyb3rhq-dashboard-package:/home/node/packages/. /

   This copies the final package and the packages that were used to generate the final package.

#. Optional. If you want to generate the .deb or .rpm file, you can use the script ``launcher.sh`` in the ``dev-tools/build-packages/rpm/`` or ``dev-tools/build-packages/deb/`` folder of the repository with the following parameters:

   -  ``-v``: Version of the package.
   -  ``-r``: Revision of the package.
   -  ``-p``: Path to the package in tar.gz format generated in the previous step
   
   .. code:: console
   
      # ./launcher.sh -v <VERSION> -r <REVISION> -p <PATH_TO_PACKAGE>
   
   Example:
   
   .. code:: console
   
      # ./launcher.sh -v 4.9.0 -r 1 -p file:///cyb3rhq-dashboard-4.9.0-1-linux-x64.tar.gz

The package will be generated in the ``output`` folder of the ``rpm`` or ``deb`` folder.