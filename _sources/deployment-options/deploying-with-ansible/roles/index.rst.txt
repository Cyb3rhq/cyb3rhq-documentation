.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Learn how to use our preconfigured roles to deploy Cyb3rhq indexer and dashboard components, Cyb3rhq Manager and Cyb3rhq Agents.

Roles
=====

You can use our preconfigured roles to deploy the Cyb3rhq indexer and dashboard components, Cyb3rhq Manager, and Cyb3rhq Agents. First, clone our `GitHub repository <https://github.com/cyb3rhq/cyb3rhq-ansible>`_ directly to your Ansible roles folder:

.. code-block:: console

   # cd /etc/ansible/roles
   # git clone --branch v|CYB3RHQ_CURRENT_ANSIBLE| https://github.com/cyb3rhq/cyb3rhq-ansible.git

Below we briefly explain how to use these roles. Please check out the `Ansible Playbook Documentation <http://docs.ansible.com/ansible/playbooks.html>`_ for more information on Ansible roles.

.. topic:: Contents

   .. toctree::
      :maxdepth: 2

      cyb3rhq-indexer
      cyb3rhq-dashboard
      cyb3rhq-filebeat
      cyb3rhq-manager
      cyb3rhq-agent
