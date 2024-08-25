.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Deploying a Cyb3rhq cluster with Ansible.

Install a Cyb3rhq cluster
=======================

Cyb3rhq can be deployed as a distributed cluster with Ansible playbooks. The installation will follow the steps below:

.. contents::
   :local:
   :depth: 1
   :backlinks: none

1 - Accessing the cyb3rhq-ansible directory
-----------------------------------------

We access the contents of the directory on the Ansible server where we have cloned the repository to. We can see the roles we have by running the command below in the cloned directory:

.. code-block:: console

   # cd /etc/ansible/roles/cyb3rhq-ansible/
   # tree roles -d

.. code-block:: none
   :class: output

   roles
   ├── ansible-galaxy
   │   └── meta
   └── cyb3rhq
     ├── ansible-filebeat-oss
     │   ├── defaults
     │   ├── handlers
     │   ├── meta
     │   ├── tasks
     │   └── templates
     ├── ansible-cyb3rhq-agent
     │   ├── defaults
     │   ├── handlers
     │   ├── meta
     │   ├── tasks
     │   └── templates
     ├── ansible-cyb3rhq-manager
     │   ├── defaults
     │   ├── files
     │   │   └── custom_ruleset
     │   │       ├── decoders
     │   │       └── rules
     │   ├── handlers
     │   ├── meta
     │   ├── tasks
     │   ├── templates
     │   └── vars
     ├── cyb3rhq-dashboard
     │   ├── defaults
     │   ├── handlers
     │   ├── tasks
     │   ├── templates
     │   └── vars
     └── cyb3rhq-indexer
         ├── defaults
         ├── handlers
         ├── meta
         ├── tasks
         └── templates

And we can see the preconfigured playbooks we have by running the command below.:

.. code-block:: console

   # tree playbooks/

.. code-block:: none
   :class: output

   playbooks
   ├── ansible.cfg
   ├── cyb3rhq-agent.yml
   ├── cyb3rhq-dashboard.yml
   ├── cyb3rhq-indexer.yml
   ├── cyb3rhq-manager-oss.yml
   ├── cyb3rhq-production-ready.yml
   └── cyb3rhq-single.yml

Using the cyb3rhq-production-ready playbook, we will deploy a Cyb3rhq manager and indexer cluster using Ansible.

If you are running Ansible on macOS, ensure Docker is installed on your system. Modify the ``macos_localhost`` variable in ``cyb3rhq-production-ready.yml`` from ``false`` to ``true`` to ensure the certificates are created correctly.

Let’s see below, the content of the YAML file ``/etc/ansible/roles/cyb3rhq-ansible/playbooks/cyb3rhq-production-ready.yml`` that we are going to run for a complete installation of the server.

.. code-block:: console

   # cat cyb3rhq-production-ready.yml

.. code-block:: yaml
   :class: output

   # Certificates generation
     - hosts: wi1
       roles:
         - role: ../roles/cyb3rhq/cyb3rhq-indexer
           indexer_network_host: "{{ private_ip }}"
           indexer_cluster_nodes:
             - "{{ hostvars.wi1.private_ip }}"
             - "{{ hostvars.wi2.private_ip }}"
             - "{{ hostvars.wi3.private_ip }}"
           indexer_discovery_nodes:
             - "{{ hostvars.wi1.private_ip }}"
             - "{{ hostvars.wi2.private_ip }}"
             - "{{ hostvars.wi3.private_ip }}"
           perform_installation: false
       become: no
       vars:
         indexer_node_master: true
         instances:
           node1:
             name: node-1       # Important: must be equal to indexer_node_name.
             ip: "{{ hostvars.wi1.private_ip }}"   # When unzipping, the node will search for its node name folder to get the cert.
             role: indexer
           node2:
             name: node-2
             ip: "{{ hostvars.wi2.private_ip }}"
             role: indexer
           node3:
             name: node-3
             ip: "{{ hostvars.wi3.private_ip }}"
             role: indexer
           node4:
             name: node-4
             ip: "{{ hostvars.manager.private_ip }}"
             role: cyb3rhq
             node_type: master
           node5:
             name: node-5
             ip: "{{ hostvars.worker.private_ip }}"
             role: cyb3rhq
             node_type: worker
           node6:
             name: node-6
             ip: "{{ hostvars.dashboard.private_ip }}"
             role: dashboard
         macos_localhost: false
       tags:
         - generate-certs

   # Cyb3rhq indexer cluster
     - hosts: wi_cluster
       strategy: free
       roles:
         - role: ../roles/cyb3rhq/cyb3rhq-indexer
           indexer_network_host: "{{ private_ip }}"
       become: yes
       become_user: root
       vars:
         indexer_cluster_nodes:
           - "{{ hostvars.wi1.private_ip }}"
           - "{{ hostvars.wi2.private_ip }}"
           - "{{ hostvars.wi3.private_ip }}"
         indexer_discovery_nodes:
           - "{{ hostvars.wi1.private_ip }}"
           - "{{ hostvars.wi2.private_ip }}"
           - "{{ hostvars.wi3.private_ip }}"
         indexer_node_master: true
         instances:
           node1:
             name: node-1       # Important: must be equal to indexer_node_name.
             ip: "{{ hostvars.wi1.private_ip }}"   # When unzipping, the node will search for its node name folder to get the cert.
             role: indexer
           node2:
             name: node-2
             ip: "{{ hostvars.wi2.private_ip }}"
             role: indexer
           node3:
             name: node-3
             ip: "{{ hostvars.wi3.private_ip }}"
             role: indexer
           node4:
             name: node-4
             ip: "{{ hostvars.manager.private_ip }}"
             role: cyb3rhq
             node_type: master
           node5:
             name: node-5
             ip: "{{ hostvars.worker.private_ip }}"
             role: cyb3rhq
             node_type: worker
           node6:
             name: node-6
             ip: "{{ hostvars.dashboard.private_ip }}"
             role: dashboard

   # Cyb3rhq cluster
     - hosts: manager
       roles:
         - role: "../roles/cyb3rhq/ansible-cyb3rhq-manager"
         - role: "../roles/cyb3rhq/ansible-filebeat-oss"
           filebeat_node_name: node-4
       become: yes
       become_user: root
       vars:
         cyb3rhq_manager_config:
           connection:
               - type: 'secure'
                 port: '1514'
                 protocol: 'tcp'
                 queue_size: 131072
           api:
               https: 'yes'
           cluster:
               disable: 'no'
               node_name: 'master'
               node_type: 'master'
               key: 'c98b62a9b6169ac5f67dae55ae4a9088'
               nodes:
                   - "{{ hostvars.manager.private_ip }}"
               hidden: 'no'
         cyb3rhq_api_users:
           - username: custom-user
             password: SecretPassword1!
         filebeat_output_indexer_hosts:
                 - "{{ hostvars.wi1.private_ip }}"
                 - "{{ hostvars.wi2.private_ip }}"
                 - "{{ hostvars.wi3.private_ip }}"

     - hosts: worker
       roles:
         - role: "../roles/cyb3rhq/ansible-cyb3rhq-manager"
         - role: "../roles/cyb3rhq/ansible-filebeat-oss"
           filebeat_node_name: node-5
       become: yes
       become_user: root
       vars:
         cyb3rhq_manager_config:
           connection:
               - type: 'secure'
                 port: '1514'
                 protocol: 'tcp'
                 queue_size: 131072
           api:
               https: 'yes'
           cluster:
               disable: 'no'
               node_name: 'worker_01'
               node_type: 'worker'
               key: 'c98b62a9b6169ac5f67dae55ae4a9088'
               nodes:
                   - "{{ hostvars.manager.private_ip }}"
               hidden: 'no'
         filebeat_output_indexer_hosts:
                 - "{{ hostvars.wi1.private_ip }}"
                 - "{{ hostvars.wi2.private_ip }}"
                 - "{{ hostvars.wi3.private_ip }}"

   # Cyb3rhq dashboard node
     - hosts: dashboard
       roles:
         - role: "../roles/cyb3rhq/cyb3rhq-dashboard"
       become: yes
       become_user: root
       vars:
         indexer_network_host: "{{ hostvars.wi1.private_ip }}"
         dashboard_node_name: node-6
         cyb3rhq_api_credentials:
           - id: default
             url: https://{{ hostvars.manager.private_ip }}
             port: 55000
             username: custom-user
             password: SecretPassword1!
         ansible_shell_allow_world_readable_temp: true

Let’s take a closer look at the content.

-  The first line ``hosts``: indicates the machines where the commands below will be executed.

-  The ``roles``: section indicates the roles that will be executed on the hosts mentioned above. Specifically, we are going to install the role of cyb3rhq-manager (Cyb3rhq manager + API) and the role of filebeat.

-  The parameter ``filebeat_output_indexer_hosts``: indicates the host group of the Cyb3rhq indexer cluster.

More details on  default configuration variables can be found in the :doc:`variables references section <../reference>`.

2 - Preparing to run the playbook
---------------------------------

The YAML file cyb3rhq-production-ready.yml will provision a production-ready distributed Cyb3rhq environment. We will add the public and private IP addresses of the endpoints where the various components of the cluster will be installed to the Ansible hosts file. For this guide, the architecture includes 2 Cyb3rhq nodes, 3 Cyb3rhq indexer nodes, and a Cyb3rhq dashboard node.

The contents of the host file is:

.. code-block:: yaml

   wi1 ansible_host=<wi1_ec2_public_ip> private_ip=<wi1_ec2_private_ip> indexer_node_name=node-1
   wi2 ansible_host=<wi2_ec2_public_ip> private_ip=<wi2_ec2_private_ip> indexer_node_name=node-2
   wi3 ansible_host=<wi3_ec2_public_ip> private_ip=<wi3_ec2_private_ip> indexer_node_name=node-3
   dashboard  ansible_host=<dashboard_node_public_ip> private_ip=<dashboard_ec2_private_ip>
   manager ansible_host=<manager_node_public_ip> private_ip=<manager_ec2_private_ip>
   worker  ansible_host=<worker_node_public_ip> private_ip=<worker_ec2_private_ip>

   [wi_cluster]
   wi1
   wi2
   wi3

   [all:vars]
   ansible_ssh_user=centos
   ansible_ssh_private_key_file=/path/to/ssh/key.pem
   ansible_ssh_extra_args='-o StrictHostKeyChecking=no'

Let’s take a closer look at the content.

-  The ``ansible_host`` variable should contain the public IP address/FQDN for each node.
-  The ``private_ip`` variable should contain the private IP address/FQDN used for the internal cluster communications.
-  If the environment is located in a local subnet, ``ansible_host`` and ``private_ip`` variables should match.
-  The ansible_ssh variable specifies the ssh user for the nodes.

3 - Running the playbook
------------------------

Now, we are ready to run the playbook and start the installation. However, some of the operations to be performed on the remote systems will need sudo permissions. We can solve this in several ways, either by opting to enter the password when Ansible requests it or using  the `become <https://docs.ansible.com/ansible/latest/user_guide/become.html#id1>`_ option (to avoid entering passwords one by one).

#. Let's run the playbook.

   Switch to the playbooks folder on the Ansible server and proceed to run the command below:

   .. code-block:: console

      # ansible-playbook cyb3rhq-production-ready.yml -b -K

#. We can check the status of the new services on our respective nodes.

   -  Cyb3rhq indexer.

      .. code-block:: console

         # systemctl status cyb3rhq-indexer

   -  Cyb3rhq dashboard

      .. code-block:: console

         # systemctl status cyb3rhq-dashboard

   -  Cyb3rhq manager.

      .. code-block:: console

         # systemctl status cyb3rhq-manager

   -  Filebeat.

      .. code-block:: console

         # systemctl status filebeat

.. note::

	- 	The Cyb3rhq dashboard can be accessed by visiting ``https://<CYB3RHQ_DASHBOARD_IP_ADDRESS>``

	- 	The default credentials for Cyb3rhq deployed using ansible is:

		| Username: admin
		|	Password: changeme
		| These credentials should be changed using the password changing tool.
