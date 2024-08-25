.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Cyb3rhq is a free, open source, and enterprise-ready security monitoring solution for threat detection, file integrity monitoring, incident response and compliance.

Cyb3rhq server
============

The Cyb3rhq server analyzes the data received from the Cyb3rhq agents, triggering alerts when threats or anomalies are detected. It is also used to remotely manage the agents' configuration and monitor their status. If you want to learn more about the Cyb3rhq components, check the :doc:`Getting started <../../getting-started/components/index>` section.

You can install the Cyb3rhq server on a single host. Alternatively, you can install it distributed in multiple nodes in a cluster configuration. Multi-node configurations provide high availability and improved performance. And if combined with a network load balancer an efficient use of its capacity can be achieved. 

Check the requirements below and choose an installation method to start installing the Cyb3rhq server.

- :doc:`Assisted installation <installation-assistant>`: Install this component by running an assistant that automates the installation and configuration process.
 
- :doc:`Step-by-step installation <step-by-step>`: Install this component following detailed step-by-step instructions.

.. raw:: html

  <div class="link-boxes-group layout-3" data-step="2">
    <div class="steps-line">
      <div class="steps-number past-step">1</div>
      <div class="steps-number current-step">2</div>
      <div class="steps-number future-step">3</div>
    </div>
    <div class="link-boxes-item past-step">
      <a class="link-boxes-link" href="../cyb3rhq-indexer/index.html">
        <p class="link-boxes-label">Install the Cyb3rhq indexer</p>

.. image:: ../../images/installation/Indexer-Circle.png
     :align: center
     :height: 61px

.. raw:: html

      </a>
    </div>
  
    <div class="link-boxes-item current-step">
      <div class="link-boxes-link" href="#">
        <p class="link-boxes-label">Install the Cyb3rhq server</p>

.. image:: ../../images/installation/Server-Circle.png
     :align: center
     :height: 61px

.. raw:: html

      </div>
    </div>
  
    <div class="link-boxes-item future-step">
      <a class="link-boxes-link" href="../cyb3rhq-dashboard/index.html">
        <p class="link-boxes-label">Install the Cyb3rhq dashboard</p>

.. image:: ../../images/installation/Dashboard-noBG.png
     :align: center
     :height: 61px
     
.. raw:: html

      </a>
    </div>
  </div>

Requirements
------------

Check the supported operating systems and the recommended hardware requirements for the Cyb3rhq server installation. Make sure that your system environment meets all requirements and that you have root user privileges.

.. _supported_operating_systems:

Recommended operating systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cyb3rhq server can be installed on a 64-bit Linux operating system. Cyb3rhq supports the following operating system versions:

.. list-table::
    :width: 100%
   
    * - Amazon Linux 2
      - CentOS 7, 8
    * - Red Hat Enterprise Linux 7, 8, 9
      - Ubuntu 16.04, 18.04, 20.04, 22.04

Hardware requirements
^^^^^^^^^^^^^^^^^^^^^

The Cyb3rhq server can be installed as a single-node or as a multi-node cluster.

- Hardware recommendations
                          
  +-------------------------+-------------------------+-------------------------------+
  |                         |  Minimum                |   Recommended                 |
  +-------------------------+----------+--------------+--------------+----------------+
  | Component               |  RAM (GB)|  CPU (cores) |  RAM (GB)    |   CPU (cores)  |
  +=========================+==========+==============+==============+================+
  | Cyb3rhq server            |     2    |     2        |      4       |       8        |
  +-------------------------+----------+--------------+--------------+----------------+


- Disk space requirements

  The amount of data depends on the generated alerts per second (APS). This table details the estimated disk space needed per agent to store 90 days of alerts on a Cyb3rhq server, depending on the type of monitored endpoints.

  +-------------------------------------------------+-----+-----------------------------+
  | Monitored endpoints                             | APS || Storage in Cyb3rhq Server    | 
  |                                                 |     || (GB/90 days)               |  
  +=================================================+=====+=============================+
  | Servers                                         | 0.25|    0.1                      |
  +-------------------------------------------------+-----+-----------------------------+
  | Workstations                                    | 0.1 |    0.04                     | 
  +-------------------------------------------------+-----+-----------------------------+
  | Network devices                                 | 0.5 |    0.2                      |
  +-------------------------------------------------+-----+-----------------------------+

  For example, for an environment with 80 workstations, 10 servers, and 10 network devices, the storage needed on the Cyb3rhq server for 90 days of alerts is 6 GB.



Scaling
^^^^^^^

To determine if a Cyb3rhq server requires more resources, monitor these files: 

- ``/var/ossec/var/run/cyb3rhq-analysisd.state``: the variable ``events_dropped`` indicates whether events are being dropped due to lack of resources. 
- ``/var/ossec/var/run/cyb3rhq-remoted.state``: the variable ``discarded_count`` indicates if messages from the agents were discarded.


These two variables should be zero if the environment is working properly. If it is not the case, additional nodes can be added to the cluster. 



.. toctree::
    :hidden:
    :maxdepth: 1

    Assisted installation <installation-assistant>
    Step-by-step installation <step-by-step>
