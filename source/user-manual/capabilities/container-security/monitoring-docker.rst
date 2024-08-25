.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Learn how to monitor Docker servers and container events with Cyb3rhq in this section of our documentation.

Using Cyb3rhq to monitor Docker
=============================

To maintain the security and compliance of your Docker environment, it is crucial to proactively monitor both your Docker server and containers. The Docker server is the backbone of your container infrastructure and manages the deployment of containers and resource allocation. By monitoring the Docker server, you can keep track of resource usage, unauthorized access attempts, performance issues, and other security concerns.

However, it is not enough to monitor only the Docker server, you also need to monitor the containers themselves. Container monitoring provides insight into the activities of your containers, such as network connections, file system changes, and process executions. Monitoring these activities helps to detect suspicious behavior, identify malware or malicious processes, and respond to security incidents in real-time.

By monitoring both the Docker server and the containers, you can proactively detect and respond to security threats, ensuring the security and compliance of your Docker environment to regulatory standards.

Take the following steps to monitor your Docker environment with Cyb3rhq:

#. :doc:`Install the Cyb3rhq agent </installation-guide/cyb3rhq-agent/index>` on your Docker server. The Cyb3rhq agent secures the underlying Docker infrastructure by monitoring the server where the Docker daemon is running.
#. :ref:`Enable the Cyb3rhq Docker listener <enable-cyb3rhq-docker-listener>` to monitor container activity. The Docker listener runs on the agent deployed on the Docker server to collect and forward Docker-related logs to the Cyb3rhq server.

.. _enable-cyb3rhq-docker-listener:

Enable the Cyb3rhq Docker listener
--------------------------------

The Docker listener allows the Cyb3rhq agent to capture Docker events and forward them to the Cyb3rhq server. The following sections describe how to install the Python Docker module and enable the Cyb3rhq Docker listener.

Python
^^^^^^

The Docker container module requires `Python 3 <https://www.python.org/>`__. Specifically, it's compatible with
`Python |PYTHON_CLOUD_CONTAINERS_MIN|–|PYTHON_CLOUD_CONTAINERS_MAX| <https://www.python.org/downloads/>`_. While later Python versions should work as well, we can't assure they are compatible.

Docker library for Python
^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::

   The Cyb3rhq manager includes all dependencies installed. These steps are only necessary when configuring the integration in a Cyb3rhq agent.

`Python Docker library <https://pypi.org/project/docker/>`_ is the official Python library for the Docker Engine API. The Cyb3rhq docker integration requires ``docker 6.0.0``.

.. tabs::

   .. group-tab:: Python 3.7–3.10

      .. code-block:: console

         $ pip3 install docker==7.1.0 urllib3==2.2.2 requests==2.32.2

   .. group-tab:: Python 3.11

      .. code-block:: console

         $ pip3 install docker==7.1.0 urllib3==2.2.2 requests==2.32.2 --break-system-packages
      
      .. note::

         This command modifies the default externally managed Python environment. See the `PEP 668 <https://peps.python.org/pep-0668/>`__ description for more information.
         
         To prevent the modification, you can run ``pip3 install --upgrade pip`` within a virtual environment. You must update the docker ``/var/ossec/wodles/docker/DockerListener`` script shebang with your virtual environment interpreter. For example: ``#!</path/to/your/virtual/environment>/bin/python3``.

Configure the Cyb3rhq agent
^^^^^^^^^^^^^^^^^^^^^^^^^

Perform the following steps on the Docker server to configure the Cyb3rhq agent to forward Docker events to the Cyb3rhq server.

#. Add the following configuration to the Cyb3rhq agent configuration file ``/var/ossec/etc/ossec.conf`` to enable the Docker listener:

   .. code-block:: XML

      <wodle name="docker-listener">
        <disabled>no</disabled>
      </wodle>

#. Restart the Cyb3rhq agent to apply the changes:

   .. code-block:: console

      # systemctl restart cyb3rhq-agent

Cyb3rhq Docker dashboard
----------------------

The Cyb3rhq Docker dashboard offers a centralized and user-friendly interface that allows you to monitor the security of your Dockerized infrastructure. With real-time insights and actionable information, the Cyb3rhq Docker listener dashboard empowers system administrators and security teams to detect and respond to potential threats, ensuring the integrity and reliability of containerized applications. From monitoring container events to analyzing logs and implementing custom rules, this dashboard streamlines the security management process, enhancing the overall protection of your Docker environment.


Cyb3rhq Docker listener configuration options
-------------------------------------------

In this section, we provide more information about the Cyb3rhq Docker listener and all possible configuration options. The Docker listener has the main options and the scheduling options.

Main options
^^^^^^^^^^^^

The main options allow you to enable or disable the Docker listener, and to configure the number of attempts to rerun the listener in case it fails. The two main options are ``disabled`` and ``attempts``.

disabled
~~~~~~~~

The ``disabled`` option allows you to enable or disable the Docker listener.

+----------------+----------+
| Default value  | no       |
+----------------+----------+
| Allowed values | yes, no  |
+----------------+----------+

attempts
~~~~~~~~

The ``attempts`` option specifies the number of attempts to execute the listener in case it fails.

+----------------+--------------------+
| Default value  | 5                  |
+----------------+--------------------+
| Allowed values | A positive number  |
+----------------+--------------------+

Scheduling options
^^^^^^^^^^^^^^^^^^

The scheduling options allow you to configure when the Docker listener should execute. The available scheduling options are ``run_on_start``, ``interval``, ``day``, ``wday``, and ``time``. The Docker listener runs on start by default when enabled without any scheduling options.

run_on_start
~~~~~~~~~~~~

Run the Docker listener immediately when the Cyb3rhq agent starts.

+----------------+----------+
| Default value  | yes      |
+----------------+----------+
| Allowed values | yes, no  |
+----------------+----------+

interval
~~~~~~~~

Waiting time to rerun the Docker listener in case it fails.

.. |interval_allowed_values| replace:: A positive number that should contain a suffix character indicating a time unit, such as s (seconds), m (minutes), h (hours), d (days), M (months).

+----------------+----------------------------+
| Default value  | 1m                         |
+----------------+----------------------------+
| Allowed values | |interval_allowed_values|  |
+----------------+----------------------------+

day
~~~

Day of the month to run the scan.

+----------------+---------------------------+
| Default value  | n/a                       |
+----------------+---------------------------+
| Allowed values | Day of the month [1..31]  |
+----------------+---------------------------+

.. note::

   When the ``day`` option is set, the interval value must be a multiple of months. By default, the interval is set to a month.

wday
~~~~

Day of the week to run the scan. This option is *not compatible* with the ``day`` option.

+----------------+------------------------+
| Default value  | n/a                    |
+----------------+------------------------+
| Allowed values | Day of the week:       |
|                |                        |
|                | -  sunday/sun          |
|                | -  monday/mon          |
|                | -  tuesday/tue         |
|                | -  wednesday/wed       |
|                | -  thursday/thu        |
|                | -  friday/fri          |
|                | -  saturday/sat        |
+----------------+------------------------+

.. note::

   When the ``wday`` option is set, the interval value must be a multiple of weeks. By default, the interval is set to a week.

time
~~~~

Time of the day to run the scan. It has to be represented in the format hh:mm.

+----------------+---------------------------+
| Default value  | n/a                       |
+----------------+---------------------------+
| Allowed values | Time of day *[hh:mm]*     |
+----------------+---------------------------+

.. note::

   When only the ``time`` option is set, the interval value must be a multiple of days or weeks. By default, the interval is set to a day.

Example configuration
---------------------

The example configuration below shows an enabled Docker listener. The listener attempts to execute five times at ten-minute intervals if it fails.

.. code-block:: XML

   <wodle name="docker-listener">
     <interval>10m</interval>
     <attempts>5</attempts>
     <run_on_start>no</run_on_start>
     <disabled>no</disabled>
   </wodle>
