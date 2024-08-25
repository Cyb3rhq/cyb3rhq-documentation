.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Check out this guide to learn how to install the Cyb3rhq agent if you are deploying Cyb3rhq with Ansible, an open source platform designed for automating tasks.

Install Cyb3rhq Agent
===================

We can install the Cyb3rhq agent on endpoints using the roles and playbooks available in the Cyb3rhq Ansible repository. The Ansible server must have access to the endpoints where the agents are to be installed.

.. contents::
   :local:
   :depth: 1
   :backlinks: none

.. note::

	- 	SSH key-pairing should already be configured between the ansible deployment server and the endpoints.
	- 	Add the endpoints where the agent will be deployed in the Ansible hosts file under the ``[cyb3rhq-agents]`` hosts group.

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

And we can see the preconfigured playbooks we have by running the command below:

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

For the agent deployment, we are going to use the role of cyb3rhq-agent, which contains the necessary commands to install an agent and register it in our Cyb3rhq environment. Below is the content of the YAML file ``/etc/ansible/roles/cyb3rhq-ansible/playbooks/cyb3rhq-agent.yml`` we are going to run for a complete installation of the Cyb3rhq agent.

.. code-block:: yaml

	---
	- hosts: <CYB3RHQ_AGENT_IP_ADDRESS>
	  become: yes
	  become_user: root
	  roles:
	    - ../roles/cyb3rhq/ansible-cyb3rhq-agent
	  vars:
	    cyb3rhq_managers:
	      - address: <CYB3RHQ_MANAGER_IP_ADDRESS>
	        port: 1514
	        protocol: tcp
	        api_port: 55000
	        api_proto: 'https'
	        api_user: cyb3rhq
	        max_retries: 5
	        retry_interval: 5

Let’s take a closer look at the content.

- 	The first line ``hosts``: indicates the machines where the commands in the playbook will be executed.
- 	The ``roles``: section indicates the roles that will be executed on the hosts specified. In this case, we are going to install the role of cyb3rhq-agent.
- 	The variables list ``cyb3rhq_managers``: indicates details for the connection with the Cyb3rhq manager. This list overwrites the default configuration.

There are several variables we can use to customize the installation or configuration. If we want to change the default configuration:

- 	We can change the ``/etc/ansible/roles/cyb3rhq-ansible/roles/cyb3rhq/ansible-cyb3rhq-agent/defaults/main.yml`` file directly.
- 	Alternatively, we can create another YAML file with the content we want to change in the configuration. If we want to do this, we can find more information about the :doc:`Cyb3rhq agent role <../roles/cyb3rhq-agent>`.

More details on default configuration variables can be found in the :doc:`variables references section <../reference>`.

2 - Preparing to run the playbook
---------------------------------

We can create a similar YAML file or modify the one we already have to adapt it to our configuration. We will use the host group of the endpoints where we are going to install the Cyb3rhq agent in the hosts section. In this case, it is ``cyb3rhq-agents``. Make sure to replace these values with your agents actual data. Add and remove lines accordingly. The hosts file will look like this:

.. tabs::
   
   .. group-tab:: Generic

      .. code-block:: yaml

         [cyb3rhq-agents]
         agent_1 ansible_host=<CYB3RHQ_MANAGER_IP_ADDRESS> ansible_ssh_user=<USERNAME>

   .. group-tab:: Windows

      .. code-block:: yaml

         [cyb3rhq-agents]
         agent_1 ansible_host=<CYB3RHQ_MANAGER_IP_ADDRESS>

         [cyb3rhq-agents:vars]
         ansible_user=<USERNAME>
         ansible_password=<PASSWORD>
         ansible_connection=winrm
         ansible_winrm_server_cert_validation=ignore
         ansible_ssh_port=5986

We will also add the IP address of the Cyb3rhq server to the ``cyb3rhq_managers:`` section.

Our resulting file is:

.. code-block:: yaml

	---
	- hosts: cyb3rhq-agents
	  become: yes
	  become_user: root
	  roles:
	    - ../roles/cyb3rhq/ansible-cyb3rhq-agent
	  vars:
	    cyb3rhq_managers:
	      - address: <CYB3RHQ_MANAGER_IP_ADDRESS>
	        port: 1514
	        protocol: tcp
	        api_port: 55000
	        api_proto: 'https'
	        api_user: cyb3rhq
	        max_retries: 5
	        retry_interval: 5

3 - Running the playbook
------------------------

Now, we are ready to run the playbook and start the installation. However, some of the operations to be  performed on the remote systems will need sudo permissions. We can solve this in several ways, either by opting to enter the password when Ansible requests it or using the `become <https://docs.ansible.com/ansible/latest/user_guide/become.html#id1>`_ option (to avoid entering passwords one by one).

#.	Let’s run the playbook.

	Switch to the playbooks folder on the Ansible server and proceed to run the command below:

	.. code-block:: console

		# ansible-playbook cyb3rhq-agent.yml -b -K

#. Once the deployment completes, we can check the status of the Cyb3rhq agent on the endpoints.

	.. code-block:: console

		# systemctl status cyb3rhq-agent

	We can also view agent information from the Cyb3rhq server.

	.. code-block:: console

		# /var/ossec/bin/agent_control -l

..
		We can see the agent connection in the Cyb3rhq dashboard.

		.. thumbnail:: ../../../images/ansible/ansible-agent2.png
		   :title: Ansible agent 1
		   :align: center
		   :width: 80%

		.. thumbnail:: ../../../images/ansible/ansible-agent.png
		   :title: Ansible agent 2
		   :align: center
		   :width: 80%
