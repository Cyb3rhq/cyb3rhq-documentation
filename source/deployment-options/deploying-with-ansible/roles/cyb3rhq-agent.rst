.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Learn how to use a preconfigured role to install and configure the Cyb3rhq Agent on different hosts in this section of the Cyb3rhq documentation.
  
Cyb3rhq Agent
-----------

This role is designed to install and configure the Cyb3rhq Agent on different hosts. There are agent installer packages for Linux, macOS, and Windows machines. This role can also enroll the agent in the Cyb3rhq Manager. Below are some variables you can use to customize the installation:

-  ``cyb3rhq_managers``: This specifies a list of Cyb3rhq manager node(s) for Cyb3rhq agents to report to.
-  ``cyb3rhq_agent_authd``: This specifies a set of options to register the Cyb3rhq agent on the Cyb3rhq server. This requires the ``cyb3rhq-authd`` service to be running on the Cyb3rhq server.

To use the role in a playbook, a YAML file ``cyb3rhq-agent.yml`` can be created with the contents below:

.. code-block:: yaml

   - hosts: all:!cyb3rhq-manager
     roles:
      - ansible-cyb3rhq-agent

You can maintain different environments using a variable definition YAML file for each one:

-  For a production environment, the variables can be saved in ``vars-production.yml``:

.. code-block:: yaml

   cyb3rhq_managers:
     - address: <CYB3RHQ_MANAGER_IP_ADDRESS>
       port: 1514
       protocol: udp
   cyb3rhq_agent_authd:
     registration_address: <CYB3RHQ_MANAGER_IP_ADDRESS>
     enable: true
     port: 1515
     ssl_agent_ca: null
     ssl_auto_negotiate: 'no'

-  For a development environment, the variables can be saved in ``vars-development.yml``:

.. code-block:: yaml

   cyb3rhq_managers:
     - address: <CYB3RHQ_MANAGER_IP_ADDRESS>
       port: 1514
       protocol: udp
   cyb3rhq_agent_authd:
     registration_address: <CYB3RHQ_MANAGER_IP_ADDRESS>
     enable: true
     port: 1515
     ssl_agent_ca: null
     ssl_auto_negotiate: 'no'

To run the playbook for a specific environment, the command below is run:

.. code-block:: console

   $ ansible-playbook cyb3rhq-agent.yml -e@vars-production.yml

The example above for a production environment will install a Cyb3rhq agent in all host groups except the ``cyb3rhq-manager`` group. Then, it will register them against the ``cyb3rhq-manager`` with IP address ``10.1.1.12``.

Please review the :ref:`variables references <cyb3rhq_ansible_reference_agent>` section to see all variables available for this role.
