.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
    :description: You can install Cyb3rhq using different deployment options. Learn more about Cyb3rhq installation alternatives in this section of the Cyb3rhq documentation.

.. _deployment:

Installation alternatives
=========================

You can install Cyb3rhq using other deployment options. These are complementary to the installation methods you can find in the  :doc:`/installation-guide/index` and the :doc:`/quickstart`. 

Installing the Cyb3rhq central components
---------------------------------------

All the alternatives include instructions on how to install the :doc:`Cyb3rhq central components </getting-started/components/index>`. After these are installed, you then need to deploy agents to your endpoints.  

.. raw:: html

    <h3>Ready-to-use machines</h3>

- :doc:`virtual-machine/virtual-machine`: Cyb3rhq provides a pre-built virtual machine image (OVA) that you can directly import using VirtualBox or other OVA compatible virtualization systems. 
  
- :doc:`amazon-machine-images/amazon-machine-images`: This is a pre-built Amazon Machine Image (AMI) you can directly launch on an AWS cloud instance.


.. raw:: html

    <h3>Containers</h3>

- :doc:`docker/index`: Docker is a set of platform-as-a-service (PaaS) products that deliver software in packages called containers. Using Docker, you can install and configure the Cyb3rhq deployment as a single-host architecture. 

  
- :doc:`deploying-with-kubernetes/index`: Kubernetes is an open-source system for automating deployment, scaling, and managing containerized applications. This deployment type uses Cyb3rhq images from Docker and allows you to build the Cyb3rhq environment. 


.. raw:: html

    <h3>Offline</h3>
    
- :doc:`offline-installation/index`: Installing the solution offline involves downloading the Cyb3rhq components to later install them on a system with no internet connection. 


.. raw:: html

    <h3>From sources</h3>

- :doc:`Installing the Cyb3rhq server from sources <cyb3rhq-from-sources/index>`: Installing Cyb3rhq from sources means installing the Cyb3rhq manager without using a package manager. You compile the source code and copy the binaries to your computer instead.

.. note::

   Since Cyb3rhq v4.6.0, we don't provide the Kibana plugin and Splunk app anymore. To integrate Cyb3rhq with Elastic or Splunk, refer to our :doc:`/integrations-guide/index`.

Installing the Cyb3rhq agent
--------------------------

The :doc:`/installation-guide/cyb3rhq-agent/index` is a single and lightweight monitoring software. It is a multi-platform component that can be deployed to laptops, desktops, servers, cloud instances, containers, or virtual machines. It provides visibility into the endpoint security by collecting critical system and application records, inventory data, and detecting potential anomalies. 

If the Cyb3rhq central components are already installed in your environment, select your operating system below and follow the installation steps to deploy the agent on the endpoints. 


.. raw:: html

  <div class="link-boxes-group layout-6">
    <div class="link-boxes-item">
      <a class="link-boxes-link" href="../installation-guide/cyb3rhq-agent/cyb3rhq-agent-package-linux.html">
        <p class="link-boxes-label">Linux</p>

.. image:: /images/installation/linux.png
      :align: center

.. raw:: html

      </a>
    </div>
    <div class="link-boxes-item">
      <a class="link-boxes-link" href="../installation-guide/cyb3rhq-agent/cyb3rhq-agent-package-windows.html">
        <p class="link-boxes-label">Windows</p>

.. image:: /images/installation/windows-logo.png
      :align: center

.. raw:: html

      </a>
    </div>
    <div class="link-boxes-item">
      <a class="link-boxes-link" href="../installation-guide/cyb3rhq-agent/cyb3rhq-agent-package-macos.html">
        <p class="link-boxes-label">macOS</p>

.. image:: /images/installation/macOS-logo.png
      :align: center

.. raw:: html

      </a>
    </div>
    <div class="link-boxes-item">
      <a class="link-boxes-link" href="../installation-guide/cyb3rhq-agent/cyb3rhq-agent-package-solaris.html">
        <p class="link-boxes-label">Solaris</p>

.. image:: /images/installation/solaris.png
      :align: center
      :width: 150px

.. raw:: html

      </a>
    </div>
    <div class="link-boxes-item">
      <a class="link-boxes-link" href="../installation-guide/cyb3rhq-agent/cyb3rhq-agent-package-aix.html">
        <p class="link-boxes-label">AIX</p>

.. image:: /images/installation/AIX.png
      :align: center

.. raw:: html

      </a>
    </div>
    <div class="link-boxes-item">
      <a class="link-boxes-link" href="../installation-guide/cyb3rhq-agent/cyb3rhq-agent-package-hpux.html">
        <p class="link-boxes-label">HP-UX</p>

.. image:: /images/installation/hpux.png
      :align: center

.. raw:: html

      </a>
    </div>
  </div>


.. raw:: html

    <h3>From sources</h3>

- :doc:`Installing the Cyb3rhq agent from sources <cyb3rhq-from-sources/cyb3rhq-agent/index>`: Installing Cyb3rhq from sources means installing the Cyb3rhq agent without using a package manager. You compile the source code and copy the binaries to your computer instead.

Orchestration tools
-------------------

These alternatives guide you to install the Cyb3rhq central components along with the single universal agent.


- :doc:`deploying-with-ansible/index`: Ansible is an open source platform designed for automating tasks. Its deployment tool is used to deploy the Cyb3rhq infrastructure on AWS. The Cyb3rhq environment consists of the Cyb3rhq central components and a Cyb3rhq agent.

- :doc:`deploying-with-puppet/index`: Puppet is an open-source software tool that gives you an automatic way to inspect, deliver, operate, and future-proof all of your software, no matter where it is executed. It is very simple to use and allows you to install and configure Cyb3rhq easily.



.. toctree::
    :hidden:
    :maxdepth: 1
    
    virtual-machine/virtual-machine
    amazon-machine-images/amazon-machine-images
    docker/index 
    deploying-with-kubernetes/index
    offline-installation/index
    cyb3rhq-from-sources/index
    deploying-with-ansible/index
    deploying-with-puppet/index
