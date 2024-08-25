.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Learn more about the process of installing and configuring the Cyb3rhq deployment on Docker in this section of our documentation. 

Deployment on Docker
====================

This section details the process of installing Cyb3rhq on Docker.

`Docker <https://www.docker.com/>`_ is an open platform for building, delivering, and running applications inside software containers. Docker containers package up software, including everything needed to run: code, runtime, system tools, system libraries, and settings. Docker enables separating applications from infrastructure. This guarantees that the application always runs the same, regardless of the environment the container is running on. Containers run in the cloud or on-premises.

You can install Cyb3rhq using the Docker images we have created, such as ``cyb3rhq/cyb3rhq-manager``, ``cyb3rhq/cyb3rhq-indexer`` and ``cyb3rhq/cyb3rhq-dashboard``. You can find all the Cyb3rhq Docker images in the `Docker hub <https://hub.docker.com/u/cyb3rhq>`_.

In the :doc:`/deployment-options/docker/docker-installation` section, you can see how to install Docker. You can find how to install Cyb3rhq on Docker in the :doc:`/deployment-options/docker/cyb3rhq-container`. Read the :doc:`/deployment-options/docker/container-usage` section to learn how to access the services and containers, manage data volumes, and execute a shell. Finally, you can find answers to some frequent questions in the :doc:`/deployment-options/docker/faq-cyb3rhq-container`.


.. toctree::
   :maxdepth: 1
   :hidden:

   docker-installation
   cyb3rhq-container
   container-usage
   upgrading-cyb3rhq-docker
   data-migration
   faq-cyb3rhq-container
