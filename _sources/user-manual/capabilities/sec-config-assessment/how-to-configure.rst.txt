
.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Check out this section of our documentation to learn more about how to configure Security Configuration Assessment in Cyb3rhq.

How to configure SCA
====================

Cyb3rhq agents include the appropriate policies for their particular operating system during installation. For the full list of officially supported policy files, see the table :ref:`available_sca_policies`. These policies are included with the Cyb3rhq server installation so that they can be easily enabled.

For a detailed description of the various configuration parameters of SCA, please check the :ref:`SCA reference <reference_sec_config_assessment>`.


Enabling and disabling policies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, the Cyb3rhq agent runs scans for every policy (``.yaml`` or ``.yml`` files) present in their ruleset folder:

- Linux and Unix-based agents: ``/var/ossec/ruleset/sca``.
- Windows agents: ``C:\Program Files (x86)\ossec-agent\ruleset\sca``.
- macOS agents: ``/Library/Ossec/ruleset/sca``.

.. warning::
    The contents of the aforementioned default ruleset folders are neither kept across installations nor updates. Place them under an alternative folder if you wish to modify or add new policies.

To enable a policy file outside the Cyb3rhq agent installation folder, add the policy file path to the ``<sca>`` block in the Cyb3rhq agent configuration file. An example is shown below:

.. code-block:: xml

    <sca>
      <policies>
        <policy><FULLPATH_TO_CUSTOM_SCA_POLICY_FILE></policy>
      </policies>
    </sca>

You can also specify a relative path to the Cyb3rhq installation directory:

.. code-block:: xml

    <sca>
      <policies>
        <policy>etc/shared/<CUSTOM_SCA_POLICY_FILE></policy>
      </policies>
    </sca>

There are two ways to disable policies on the Cyb3rhq agent. The simplest one is renaming the policy file by adding ``.disabled`` (or anything different from ``.yaml`` or ``.yml``) after their YAML extension. 

The second is to disable them from the Cyb3rhq agent ``ossec.conf`` file by adding a line such as the following to the ``<policy>`` section of the SCA module:

.. code-block:: xml

    <sca>
      <policies>
        <policy enabled="no">etc/shared/<POLICY_FILE_TO_DISABLE></policy>
      </policies>
    </sca>

.. _share_policy_files_and_configuration_with_the_Cyb3rhq_agents:

How to share policy files and configuration with the Cyb3rhq agents
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As described in the :doc:`centralized configuration </user-manual/reference/centralized-configuration>` section, the Cyb3rhq manager can push files and configurations to connected Cyb3rhq agents.

You can enable this feature to push policy files to the Cyb3rhq agents in defined groups. By default, every Cyb3rhq agent belongs to the ``default`` group, which is used here as an example:

#. On the Cyb3rhq agent, edit the ``local_internal_options.conf`` file to allow the execution of commands in SCA policies sent from the Cyb3rhq server:

     .. code-block:: console

        # echo "sca.remote_commands=1" >> /var/ossec/etc/local_internal_options.conf


    .. note::
        By enabling remote command execution, the Cyb3rhq server gains the ability to execute commands on the monitored endpoint. Remote commands are disabled by default as a security measure, which helps reduce the attack surface in case the Cyb3rhq server is compromised.

        You do not need to enable remote commands if you add the policy files to each agent without using the Cyb3rhq server to push them. For example, you can manually create the policy file directly on the monitored endpoint, or use ``scp`` to copy the policy file to the monitored endpoint.    

#. On the Cyb3rhq server, place a new policy file in the ``/var/ossec/etc/shared/default`` folder and change its ownership. Replace ``<NEW_POLICY_FILE>`` with your policy name. 

     .. code-block:: console
        
        # chown cyb3rhq:cyb3rhq /var/ossec/etc/shared/default/<NEW_POLICY_FILE>


#. Add the following configuration block to the Cyb3rhq server ``/var/ossec/etc/shared/default/agent.conf`` file to configure the new policy file in the Cyb3rhq agent:


     .. code-block:: xml
        :emphasize-lines: 5

        <agent_config>
          <!-- Shared agent configuration here -->
          <sca>
            <policies>
                <policy>etc/shared/<NEW_POLICY_FILE></policy>
            </policies>
          </sca>
        </agent_config>

   All files remotely pushed from the Cyb3rhq server are saved in the ``/<CYB3RHQ_HOME_DIRECTORY>/etc/shared/`` directory on the agent endpoints regardless of the group they belong to. We specify the relative file path of the policy in the configuration because the full file path could differ depending on the operating system of the monitored endpoint.

The new ``<sca>`` block in the Cyb3rhq server ``/var/ossec/etc/shared/default/agent.conf`` file is merged with the ``<sca>`` block on the Cyb3rhq agent side, and the new configuration is added.
