.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
	:description: Check out this guide to learn how to install the Cyb3rhq manager if you are deploying Cyb3rhq with Ansible, an open source platform designed for automating tasks.
	
Install Cyb3rhq manager
=====================

Once the Ansible repository has been cloned, we proceed to install the Cyb3rhq manager. The installation will follow the steps below:

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

Using the ansible-cyb3rhq-manager and ansible-filebeat-oss roles, we will install and configure the Cyb3rhq manager, and Filebeat components.

Let’s see below, the content of the YAML file ``/etc/ansible/roles/cyb3rhq-ansible/playbooks/cyb3rhq-manager-oss.yml`` that we are going to run for a complete installation of the server.

.. code-block:: console

	# cat cyb3rhq-manager-oss.yml

.. code-block:: yaml
	:class: output

	---
	- hosts: managers
	  roles:
	    - role: ../roles/cyb3rhq/ansible-cyb3rhq-manager
	    - role: ../roles/cyb3rhq/ansible-filebeat-oss
	      filebeat_output_indexer_hosts:
	      - "<indexer-node-1>:9200"
	      - "<indexer-node-2>:9200"
	      - "<indexer-node-2>:9200"

Let's take a closer look at the content.

-  The first line ``hosts``: indicates the machines where the commands below will be executed.

-  The ``roles``: section indicates the roles that will be executed on the hosts mentioned above. Specifically, we are going to install the role of cyb3rhq-manager (Cyb3rhq manager + API) and the role of filebeat.

-  The parameter ``filebeat_output_indexer_hosts``: indicates the host group of the Cyb3rhq indexer cluster.

There are several variables we can use to customize the installation or configuration. If we want to change the default configuration:

-  We can change the following files:

	-  ``/etc/ansible/roles/cyb3rhq-ansible/roles/cyb3rhq/ansible-cyb3rhq-manager/defaults/main.yml``
	- 	``/etc/ansible/roles/cyb3rhq-ansible/roles/cyb3rhq/ansible-filebeat-oss/defaults/main.yml``
		
-  Alternatively, we also can create another YAML file with the content we want to change for Filebeat and the Cyb3rhq manager. We can find more information about the roles in this :doc:`section <../roles/index>`

More details on  default configuration variables can be found in the :doc:`variables references section <../reference>`.

2 - Preparing to run the playbook
---------------------------------

We can create a similar YAML file or modify the one we already have to adapt it to our configuration. In this case, we are going to modify the cyb3rhq-manager-oss.yml file and include the IP address of the machine where we are going to install the Cyb3rhq manager in the hosts section and the IP address of the machine where we installed the Cyb3rhq indexer service to the ``filebeat_output_indexer_hosts`` field.

Our resulting file is:

.. code-block:: yaml

	---
	- hosts: all_in_one
	  roles:
	    - role: ../roles/cyb3rhq/ansible-cyb3rhq-manager
	    - role: ../roles/cyb3rhq/ansible-filebeat-oss
	      filebeat_node_name: node-1
	      filebeat_output_indexer_hosts:
	      - "127.0.0.1:9200"

3 - Running the playbook
------------------------

Now, we are ready to run the playbook and start the installation. However, some of the operations to be performed on the remote systems will need sudo permissions. We can solve this in several ways, either by opting to enter the password when Ansible requests it or using  the `become <https://docs.ansible.com/ansible/latest/user_guide/become.html#id1>`_ option (to avoid entering passwords one by one).

#. Let’s run the playbook.

	Switch to the playbooks folder on the Ansible server and proceed to run the command below:
	
	.. code-block:: console

		# ansible-playbook cyb3rhq-manager-oss.yml -b -K

#. We can check the status of the new services on our Cyb3rhq server.

	-  **Cyb3rhq manager**

		.. code-block:: console

			# systemctl status cyb3rhq-manager

	-  **Filebeat**

		.. code-block:: console

			# systemctl status filebeat

.. note::
	
	- 	The Cyb3rhq dashboard can be accessed by visiting ``https://<CYB3RHQ_DASHBOARD_IP_ADDRESS>``

	- 	The default credentials for Cyb3rhq deployed using ansible is:
		
		|	Username: admin
		| Password: changeme
		| These credentials should be changed using the password changing tool.
