.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Learn about Cyb3rhq Puppet module in this section of the Cyb3rhq documentation.

.. _cyb3rhq_puppet_module:

Cyb3rhq Puppet module
===================

This `module <https://github.com/cyb3rhq/cyb3rhq-puppet>`_ has been authored by Nicolas Zin and updated by Jonathan Gazeley and Michael Porter. Cyb3rhq has forked it with the purpose of maintaining it. Thank you to the authors for their contribution.


Install Cyb3rhq module
--------------------

Download and install the Cyb3rhq module from Puppet Forge:

  .. code-block:: console

    # puppet module install cyb3rhq-cyb3rhq --version |CYB3RHQ_CURRENT_PUPPET|

  .. code-block:: none
    :class: output

    Notice: Preparing to install into /etc/puppetlabs/code/environments/production/modules ...
    Notice: Downloading from https://forgeapi.puppet.com ...
    Notice: Installing -- do not interrupt ...
    /etc/puppetlabs/code/environments/production/modules
    └─┬ cyb3rhq-cyb3rhq (v|CYB3RHQ_CURRENT|)
      ├── puppet-nodejs (v7.0.1)
      ├── puppet-selinux (v3.4.1)
      ├── puppetlabs-apt (v7.7.1)
      ├─┬ puppetlabs-concat (v6.4.0)
      │ └── puppetlabs-translate (v2.2.0)
      ├── puppetlabs-firewall (v2.8.1)
      ├─┬ puppetlabs-powershell (v4.1.0)
      │ └── puppetlabs-pwshlib (v0.10.1)
      └── puppetlabs-stdlib (v6.6.0)


This module installs and configures Cyb3rhq agent and manager.


Install a stack via Puppet
--------------------------

Single Node
^^^^^^^^^^^

You can use  the manifest shown below to deploy a single-node stack. This stack consists of:

-  Cyb3rhq dashboard
-  Cyb3rhq indexer
-  Cyb3rhq manager
-  Filebeat

To configure the manager before deployment, check the configuration variables for the Cyb3rhq manager class section in :ref:`ref_cyb3rhq_puppet`.

Create the ``stack.pp`` file at ``/etc/puppetlabs/code/environments/production/manifests/`` with the contents below. Here, ``puppet-aio-node`` refers to the hostname or IP address of the puppet agent.

.. code-block:: puppet

   $discovery_type = 'single-node'
   stage { 'certificates': }
   stage { 'repo': }
   stage { 'indexerdeploy': }
   stage { 'securityadmin': }
   stage { 'dashboard': }
   stage { 'manager': }
   Stage[certificates] -> Stage[repo] -> Stage[indexerdeploy] -> Stage[securityadmin] -> Stage[manager] -> Stage[dashboard]
   Exec {
   timeout => 0,
   }
   node "puppet-server" {
   class { 'cyb3rhq::certificates':
     indexer_certs => [['node-1','127.0.0.1']],
     manager_certs => [['master','127.0.0.1']],
     dashboard_certs => ['127.0.0.1'],
     stage => certificates,
   }
   }
   node "puppet-aio-node" {
   class { 'cyb3rhq::repo':
   stage => repo,
   }
   class { 'cyb3rhq::indexer':
     stage => indexerdeploy,
   }
   class { 'cyb3rhq::securityadmin':
   stage => securityadmin
   }
   class { 'cyb3rhq::manager':
     stage => manager,
   }
   class { 'cyb3rhq::filebeat_oss':
     stage => manager,
   }
   class { 'cyb3rhq::dashboard':
     stage => dashboard,
   }
   }

Multi Node
^^^^^^^^^^

Using the multi-node manifest below, you can deploy a distributed stack consisting of the following nodes on three different servers or Virtual Machines (VM).

-  3 indexer nodes
-  Manager master node
-  Manager worker node
-  Dashboard node

You must include the IP addresses of the servers where you are installing each application.

.. code-block:: puppet
   :emphasize-lines: 1-6

   $node1host   = 'x.x.x.x'
   $node2host   = 'x.x.x.x'
   $node3host   = 'x.x.x.x'
   $masterhost    = 'x.x.x.x'
   $workerhost    = 'x.x.x.x'
   $dashboardhost = 'x.x.x.x'
   $indexer_node1_name = 'node1'
   $indexer_node2_name = 'node2'
   $indexer_node3_name = 'node3'
   $master_name = 'master'
   $worker_name = 'worker'
   $cluster_size = '3'
   $indexer_discovery_hosts = [$node1host, $node2host, $node3host]
   $indexer_cluster_initial_master_nodes = [$node1host, $node2host, $node3host]
   $indexer_cluster_CN = [$indexer_node1_name, $indexer_node2_name, $indexer_node3_name]
   # Define stage for order execution
   stage { 'certificates': }
   stage { 'repo': }
   stage { 'indexerdeploy': }
   stage { 'securityadmin': }
   stage { 'dashboard': }
   stage { 'manager': }
   Stage[certificates] -> Stage[repo] -> Stage[indexerdeploy] -> Stage[securityadmin] -> Stage[manager] -> Stage[dashboard]
   Exec {
   timeout => 0,
   }
   node "puppet-server" {
   class { 'cyb3rhq::certificates':
     indexer_certs => [["$indexer_node1_name","$node1host" ],["$indexer_node2_name","$node2host" ],["$indexer_node3_name","$node3host" ]],
     manager_master_certs => [["$master_name","$masterhost"]],
     manager_worker_certs => [["$worker_name","$workerhost"]],
     dashboard_certs => ["$dashboardhost"],
     stage => certificates
   }
   class { 'cyb3rhq::repo':
   stage => repo
   }
   }
   node "puppet-cyb3rhq-indexer-node1" {
   class { 'cyb3rhq::repo':
   stage => repo
   }
   class { 'cyb3rhq::indexer':
     indexer_node_name => "$indexer_node1_name",
     indexer_network_host => "$node1host",
     indexer_node_max_local_storage_nodes => "$cluster_size",
     indexer_discovery_hosts => $indexer_discovery_hosts,
     indexer_cluster_initial_master_nodes => $indexer_cluster_initial_master_nodes,
     indexer_cluster_CN => $indexer_cluster_CN,
     stage => indexerdeploy
   }
   class { 'cyb3rhq::securityadmin':
   indexer_network_host => "$node1host",
   stage => securityadmin
   }
   }
   node "puppet-cyb3rhq-indexer-node2" {
   class { 'cyb3rhq::repo':
   stage => repo
   }
   class { 'cyb3rhq::indexer':
     indexer_node_name => "$indexer_node2_name",
     indexer_network_host => "$node2host",
     indexer_node_max_local_storage_nodes => "$cluster_size",
     indexer_discovery_hosts => $indexer_discovery_hosts,
     indexer_cluster_initial_master_nodes => $indexer_cluster_initial_master_nodes,
     indexer_cluster_CN => $indexer_cluster_CN,
     stage => indexerdeploy
   }
   }
   node "puppet-cyb3rhq-indexer-node3" {
   class { 'cyb3rhq::repo':
   stage => repo
   }
   class { 'cyb3rhq::indexer':
     indexer_node_name => "$indexer_node3_name",
     indexer_network_host => "$node3host",
     indexer_node_max_local_storage_nodes => "$cluster_size",
     indexer_discovery_hosts => $indexer_discovery_hosts,
     indexer_cluster_initial_master_nodes => $indexer_cluster_initial_master_nodes,
     indexer_cluster_CN => $indexer_cluster_CN,
     stage => indexerdeploy
   }
   }
   node "puppet-cyb3rhq-manager-master" {
   class { 'cyb3rhq::repo':
   stage => repo
   }
   class { 'cyb3rhq::manager':
     ossec_cluster_name => 'cyb3rhq-cluster',
     ossec_cluster_node_name => 'cyb3rhq-master',
     ossec_cluster_node_type => 'master',
     ossec_cluster_key => '01234567890123456789012345678912',
     ossec_cluster_bind_addr => "$masterhost",
     ossec_cluster_nodes => ["$masterhost"],
     ossec_cluster_disabled => 'no',
     stage => manager
   }
   class { 'cyb3rhq::filebeat_oss':
     filebeat_oss_indexer_ip => "$node1host",
     cyb3rhq_node_name => "$master_name",
     stage => manager
   }
   }
   node "puppet-cyb3rhq-manager-worker" {
   class { 'cyb3rhq::repo':
   stage => repo
   }
   class { 'cyb3rhq::manager':
     ossec_cluster_name => 'cyb3rhq-cluster',
     ossec_cluster_node_name => 'cyb3rhq-worker',
     ossec_cluster_node_type => 'worker',
     ossec_cluster_key => '01234567890123456789012345678912',
     ossec_cluster_bind_addr => "$masterhost",
     ossec_cluster_nodes => ["$masterhost"],
     ossec_cluster_disabled => 'no',
     stage => manager
   }
   class { 'cyb3rhq::filebeat_oss':
     filebeat_oss_indexer_ip => "$node1host",
     cyb3rhq_node_name => "$worker_name",
     stage => manager
   }
   }
   node "puppet-cyb3rhq-dashboard" {
   class { 'cyb3rhq::repo':
   stage => repo,
   }
   class { 'cyb3rhq::dashboard':
     indexer_server_ip  => "$node1host",
     manager_api_host   => "$masterhost",
     stage => dashboard
   }
   }

The correspondence of the IP addresses with the puppet nodes described in the manifest is as follows:

-  ``puppet-cyb3rhq-indexer-node1`` = ``node1host``. Cyb3rhq indexer node1.
-  ``puppet-cyb3rhq-indexer-node2`` = ``node2host``. Cyb3rhq indexer node2.
-  ``puppet-cyb3rhq-indexer-node3`` = ``node3host``. Cyb3rhq indexer node3.
-  ``puppet-cyb3rhq-manager-master`` = ``masterhost``. Cyb3rhq manager master.
-  ``puppet-cyb3rhq-manager-worker`` = ``workerhost``. Cyb3rhq manager worker.
-  ``puppet-cyb3rhq-dashboard`` = ``dashboardhost``. Cyb3rhq dashboard node.

The ``cyb3rhq::certificates`` class needs to be applied on the Puppet server (``puppet-server``) where the Cyb3rhq module is installed. This is necessary because the archives module is used to distribute files to all servers in the Cyb3rhq stack deployment.

If you need more Cyb3rhq indexer nodes, add new variables. For example ``indexer_node4_name`` and ``node4host``. Add them to the following arrays:

-  ``indexer_discovery_hosts``
-  ``indexer_cluster_initial_master_nodes``
-  ``indexer_cluster_CN``
-  ``indexer_certs``

In addition, you need to add a new node instance similar to ``puppet-cyb3rhq-indexer-node2`` or ``puppet-cyb3rhq-indexer-node3``. Unlike the instance for Cyb3rhq indexer node1, these instances don't run ``securityadmin``.

In case you need to add a Cyb3rhq manager worker server, add a new variable such as ``worker2host``. Add the variable to the ``manager_worker_certs`` array. For example, ``['worker',"$worker2host"]``. Then, replicate the node instance ``puppet-cyb3rhq-manager-worker`` with the new server.

Place the file at ``/etc/puppetlabs/code/environments/production/manifests/`` in your Puppet master. It executes on the specified node once the ``runinterval`` time, as set in ``puppet.conf``, elapses. However, if you want to run the manifest immediately on a specific node, run the following command on the node:

.. code-block:: console

   # puppet agent -t

Change Password for Cyb3rhq users
-------------------------------

Follow the instructions in the :doc:`Password Management </user-manual/user-administration/password-management>` section to change your Cyb3rhq user passwords. Once you change them, set the new passwords within the classes used for deploying the Cyb3rhq Stack.

Indexer users
^^^^^^^^^^^^^

-  ``admin`` user:

   .. code-block:: puppet

      node "puppet-agent.com" {
        class { 'cyb3rhq::dashboard':
          dashboard_password => '<NEW_PASSWORD>'
        }
      }

-  ``kibanaserver`` user:

   .. code-block:: puppet

      node "puppet-agent.com" {
        class { 'cyb3rhq::filebeat_oss':
          filebeat_oss_elastic_password  => '<NEW_PASSWORD>'
        }
      }

Cyb3rhq API users
^^^^^^^^^^^^^^^

-  ``cyb3rhq-wui`` user:

   .. code-block:: puppet

      node "puppet-agent.com" {
        class { 'cyb3rhq::dashboard':
          dashboard_cyb3rhq_api_credentials => '<NEW_PASSWORD>'
        }
      }

Install Cyb3rhq agent via Puppet
------------------------------

The agent is configured by installing the ``cyb3rhq::agent`` class.

Here is an example of a manifest ``cyb3rhq-agent.pp`` (please replace  ``<MANAGER_IP_ADDRESS>`` with your manager IP address).

  .. code-block:: puppet

   node "puppet-agent.com" {
     class { 'cyb3rhq::repo':
     }
     class { "cyb3rhq::agent":
       cyb3rhq_register_endpoint => "<MANAGER_IP_ADDRESS>",
       cyb3rhq_reporting_endpoint => "<MANAGER_IP_ADDRESS>"
     }
   }


Place the file at ``/etc/puppetlabs/code/environments/production/manifests/`` in your Puppet master and it will be executed in the specified node after the ``runinterval`` time set in ``puppet.conf``. However, if you want to run it first, try the following command in the Puppet agent.

  .. code-block:: console

    # puppet agent -t

.. _ref_cyb3rhq_puppet:

Reference Cyb3rhq puppet
----------------------

+-----------------------------------------------------------------+-----------------------------------------------------------------+---------------------------------------------+
| Sections                                                        | Variables                                                       | Functions                                   |
+=================================================================+=================================================================+=============================================+
| :ref:`Cyb3rhq manager class <reference_cyb3rhq_manager_class>`      | :ref:`Alerts <ref_server_vars_alerts>`                          | :ref:`email_alert <ref_server_email_alert>` |
|                                                                 |                                                                 |                                             |
|                                                                 | :ref:`Authd <ref_server_vars_authd>`                            | :ref:`command <ref_server_command>`         |
|                                                                 |                                                                 |                                             |
|                                                                 | :ref:`Cluster <ref_server_vars_cluster>`                        | :ref:`activeresponse <ref_server_ar>`       |
|                                                                 |                                                                 |                                             |
|                                                                 | :ref:`Global <ref_server_vars_global>`                          |                                             |
|                                                                 |                                                                 |                                             |
|                                                                 | :ref:`Localfile <ref_server_vars_localfile>`                    |                                             |
|                                                                 |                                                                 |                                             |
|                                                                 | :ref:`Rootcheck <ref_server_vars_rootcheck>`                    |                                             |
|                                                                 |                                                                 |                                             |
|                                                                 | :ref:`Syscheck <ref_server_vars_syscheck>`                      |                                             |
|                                                                 |                                                                 |                                             |
|                                                                 | :ref:`Syslog output <ref_server_vars_syslog_output>`            |                                             |
|                                                                 |                                                                 |                                             |
|                                                                 | :ref:`Vulnerability Detection <ref_server_vars_vuln_detection>` |                                             |
|                                                                 |                                                                 |                                             |
|                                                                 | :ref:`Cyb3rhq API <ref_server_vars_cyb3rhq_api>`                    |                                             |
|                                                                 |                                                                 |                                             |
|                                                                 | :ref:`Wodle OpenSCAP <ref_server_vars_wodle_openscap>`          |                                             |
|                                                                 |                                                                 |                                             |
|                                                                 | :ref:`Wodle CIS-CAT <ref_server_vars_ciscat>`                   |                                             |
|                                                                 |                                                                 |                                             |
|                                                                 | :ref:`Wodle osquery <ref_server_vars_wodle_osquery>`            |                                             |
|                                                                 |                                                                 |                                             |
|                                                                 | :ref:`Wodle Syscollector <ref_server_vars_wodle_syscollector>`  |                                             |
|                                                                 |                                                                 |                                             |
|                                                                 | :ref:`Misc <ref_server_vars_misc>`                              |                                             |
+-----------------------------------------------------------------+-----------------------------------------------------------------+---------------------------------------------+
| :ref:`Cyb3rhq agent class <reference_cyb3rhq_agent_class>`          | :ref:`Active response <ref_agent_vars_ar>`                      |                                             |
|                                                                 |                                                                 |                                             |
|                                                                 | :ref:`Agent enrollment <ref_agent_vars_enroll>`                 |                                             |
|                                                                 |                                                                 |                                             |
|                                                                 | :ref:`Client settings <ref_agent_vars_client>`                  |                                             |
|                                                                 |                                                                 |                                             |
|                                                                 | :ref:`Localfile <ref_agent_vars_localfile>`                     |                                             |
|                                                                 |                                                                 |                                             |
|                                                                 | :ref:`Rootcheck <ref_agent_vars_rootcheck>`                     |                                             |
|                                                                 |                                                                 |                                             |
|                                                                 | :ref:`SCA <ref_agent_vars_sca>`                                 |                                             |
|                                                                 |                                                                 |                                             |
|                                                                 | :ref:`Syscheck <ref_agent_vars_syscheck>`                       |                                             |
|                                                                 |                                                                 |                                             |
|                                                                 | :ref:`Wodle OpenSCAP <ref_agent_vars_wodle_openscap>`           |                                             |
|                                                                 |                                                                 |                                             |
|                                                                 | :ref:`Wodle CIS-CAT <ref_agent_vars_wodle_ciscat>`              |                                             |
|                                                                 |                                                                 |                                             |
|                                                                 | :ref:`Wodle osquery <ref_agent_vars_wodle_osquery>`             |                                             |
|                                                                 |                                                                 |                                             |
|                                                                 | :ref:`Wodle Syscollector <ref_agent_vars_wodle_syscollector>`   |                                             |
|                                                                 |                                                                 |                                             |
|                                                                 | :ref:`Misc <ref_agent_vars_misc>`                               |                                             |
|                                                                 |                                                                 |                                             |
+-----------------------------------------------------------------+-----------------------------------------------------------------+---------------------------------------------+

.. topic:: Contents

 .. toctree::
    :maxdepth: 1

    reference-cyb3rhq-puppet/cyb3rhq-manager-class
    reference-cyb3rhq-puppet/cyb3rhq-agent-class

