.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Learn how to restore a backup of key files of your Cyb3rhq agent installation.
  
Cyb3rhq agent
===========

Restore your Cyb3rhq agent installation by following these steps.

.. note::
   
   You need root user privileges to execute the commands below.

Linux
-----

You need to have a new installation of the Cyb3rhq agent on a Linux endpoint. Follow the :doc:`/installation-guide/cyb3rhq-agent/cyb3rhq-agent-package-linux` guide to perform a fresh Cyb3rhq agent installation.

Preparing the data restoration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Compress the files generated after performing the :doc:`Cyb3rhq files backup </migration-guide/files-backup/creating/cyb3rhq-agent>` and transfer them to the respective monitored endpoints.

   .. code-block:: console

      # tar -cvzf cyb3rhq_agent.tar.gz ~/cyb3rhq_files_backup/ 

#. Move the compressed file to the root ``/`` directory of your node:

   .. code-block:: console

      # mv cyb3rhq_agent.tar.gz /
      # cd /

#. Decompress the backup files and change the current working directory to the directory based on the date and time of the backup files.

   .. code-block:: console

      # tar -xzvf cyb3rhq_agent.tar.gz
      # cd ~/cyb3rhq_files_backup/<DATE_TIME>

Restoring Cyb3rhq agent files
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Perform the steps below to restore the Cyb3rhq agent files on a Linux endpoint.

#. Stop the Cyb3rhq agent to prevent any modification to the Cyb3rhq agent files during the restore process:

   .. code-block:: console

      # systemctl stop cyb3rhq-agent

#. Restore Cyb3rhq agent data, certificates, and configuration files, and change the file permissions and ownerships accordingly:

   .. code-block:: console

      # sudo cp var/ossec/etc/client.keys /var/ossec/etc/ 
      # chown cyb3rhq:cyb3rhq /var/ossec/etc/client.keys
      # sudo cp var/ossec/etc/ossec.conf /var/ossec/etc/
      # chown root:cyb3rhq /var/ossec/etc/ossec.conf
      # sudo cp var/ossec/etc/internal_options.conf /var/ossec/etc/
      # chown root:cyb3rhq /var/ossec/etc/internal_options.conf
      # sudo cp var/ossec/etc/local_internal_options.conf /var/ossec/etc/
      # chown root:cyb3rhq /var/ossec/etc/local_internal_options.conf
      # sudo cp -r var/ossec/etc/*.pem /var/ossec/etc/
      # chown -R root:cyb3rhq /var/ossec/etc/*.pem
      # sudo cp -r var/ossec/logs/* /var/ossec/logs/
      # chown -R cyb3rhq:cyb3rhq /var/ossec/logs/
      # sudo cp -r var/ossec/queue/rids/* /var/ossec/queue/rids/
      # chown -R cyb3rhq:cyb3rhq /var/ossec/queue/rids/

#. Restore your custom files such as local SCA policies, active response scripts, and wodle commands if there are any and change the file permissions. Adapt the following command accordingly. 

   .. code-block:: console

      # sudo cp var/ossec/etc/<SCA_DIRECTORY>/<CUSTOM_SCA_FILE> /var/ossec/etc/<SCA_DIRECTORY>/
      # chown cyb3rhq:cyb3rhq /var/ossec/etc/custom-sca-files/<CUSTOM_SCA_FILE>
      # sudo cp var/ossec/active-response/bin/<CUSTOM_ACTIVE_RESPONSE_SCRIPT> /var/ossec/active-response/bin/
      # chown root:cyb3rhq /var/ossec/active-response/bin/<CUSTOM_ACTIVE_RESPONSE_SCRIPT> 
      # sudo cp var/ossec/wodles/<CUSTOM_WODLE_SCRIPT> /var/ossec/wodles/
      # chown root:cyb3rhq /var/ossec/wodles/<CUSTOM_WODLE_SCRIPT>

#. Start the Cyb3rhq agent service: 

   .. code-block:: console

      # systemctl start cyb3rhq-agent

Windows
-------

You need to have a new installation of the Cyb3rhq agent on a Windows endpoint. Follow the :doc:`/installation-guide/cyb3rhq-agent/cyb3rhq-agent-package-windows` guide to perform a fresh Cyb3rhq agent installation.

Preparing the data restoration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Compress the files generated after performing the :doc:`Cyb3rhq files backup <../creating/cyb3rhq-agent>` and transfer them to the ``Downloads`` directory of the respective agent endpoints.

#. Decompress the file using `7-Zip <https://www.7-zip.org/>`__ or any of your preferred tools.

Restoring Cyb3rhq agent files
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Perform the steps below to restore the Cyb3rhq agent files on a Windows endpoint.

#. Stop the Cyb3rhq agent to prevent any modification to the Cyb3rhq agent files during the restore process by running the following command on the Command Prompt as an administrator:

   .. code-block:: doscon

      NET STOP Cyb3rhqSvc

#. Launch PowerShell or the CMD utility as an administrator and navigate to the ``cyb3rhq_files_backup/<DATE_TIME>`` folder that contains the backup files.

#. Run the following commands to copy the Cyb3rhq agent data, certificates, and configurations:

   .. code-block:: doscon

      > xcopy client.keys "C:\Program Files (x86)\ossec-agent\" /H /I /K /S /X /Y
      > xcopy ossec.conf "C:\Program Files (x86)\ossec-agent\" /H /I /K /S /X /Y
      > xcopy internal_options.conf "C:\Program Files (x86)\ossec-agent\" /H /I /K /S /X /Y
      > xcopy local_internal_options.conf "C:\Program Files (x86)\ossec-agent\" /H /I /K /S /X /Y
      > xcopy *.pem "C:\Program Files (x86)\ossec-agent\" /H /I /K /S /X /Y
      > xcopy ossec.log "C:\Program Files (x86)\ossec-agent\" /H /I /K /S /X /Y
      > xcopy logs\* "C:\Program Files (x86)\ossec-agent\"  /H /I /K /S /X /Y
      > xcopy rids\* "C:\Program Files (x86)\ossec-agent\"  /H /I /K /S /X /Y

   You can also copy these files using the *drag and drop* method.

#. Restore your custom files, such as local SCA policies, active response scripts, and wodle commands, if there are any. Adapt the following command accordingly.

   .. code-block:: doscon

      > xcopy <SCA_DIRECTORY>\<CUSTOM_SCA_FILE> “C:\Program Files (x86)\ossec-agent\<SCA_DIRECTORY>” /H /I /K /S /X /Y
      > xcopy active-response\bin\<CUSTOM_ACTIVE_RESPONSE_SCRIPT> "C:\Program Files (x86)\ossec-agent\active-response\bin\" /H /I /K /S /X /Y
      > xcopy wodles\<CUSTOM_WODLE_SCRIPT> "C:\Program Files (x86)\ossec-agent\wodles\" /H /I /K /S /X /Y

#. Start the Cyb3rhq agent service by running the following command on the Command Prompt as an administrator:

   .. code-block:: doscon

      NET START Cyb3rhqSvc

macOS
-----

You need to have a new installation of the Cyb3rhq agent on a macOS endpoint. Follow the :doc:`/installation-guide/cyb3rhq-agent/cyb3rhq-agent-package-macos` guide to perform a fresh Cyb3rhq agent installation.

Preparing the data restoration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Compress the files generated after performing the :doc:`Cyb3rhq files backup <../creating/cyb3rhq-agent>` and transfer them to the endpoint with the Cyb3rhq agent installed.

   .. code-block:: console

      # tar -cvzf cyb3rhq_agent.tar.gz ~/cyb3rhq_files_backup/ 

#. Move the compressed file to the ``Downloads`` directory of your node:

   .. code-block:: console

      # mv cyb3rhq_agent.tar.gz ~/Downloads
      # cd ~/Downloads

#. Decompress the backup files and change the current working directory to the directory based on the date and time of the backup files.

   .. code-block:: console

      # tar -xzvf cyb3rhq_agent.tar.gz
      # cd cyb3rhq_files_backup/<DATE_TIME>

Restoring Cyb3rhq agent files
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Perform the steps below to restore Cyb3rhq agent files on a macOS endpoint.

#. Stop the Cyb3rhq agent to prevent any modification to the Cyb3rhq agent files during the restore process:

   .. code-block:: console

      # launchctl unload /Library/LaunchDaemons/com.cyb3rhq.agent.plist

#. Restore Cyb3rhq agent data, certificates, and configuration files:

   .. code-block:: console

      # cp Library/Ossec/etc/client.keys /Library/Ossec/etc/
      # cp Library/Ossec/etc/ossec.conf /Library/Ossec/etc/
      # cp Library/Ossec/etc/internal_options.conf /Library/Ossec/etc/
      # cp Library/Ossec/etc/local_internal_options.conf /Library/Ossec/etc/
      # cp -R Library/Ossec/etc/*.pem /Library/Ossec/etc/
      # cp -R Library/Ossec/logs/* /Library/Ossec/logs/
      # cp -R Library/Ossec/queue/rids/* /Library/Ossec/queue/rids/ 

#. Restore custom files, such as local SCA policies, active response, and wodle scripts, if there are any.

   .. code-block:: console

      # sudo cp Library/Ossec/<SCA_DIRECTORY>/<CUSTOM_SCA_FILE> /Library/Ossec/<SCA_DIRECTORY>/
      # sudo cp Library/Ossec/active-response/bin/<CUSTOM_ACTIVE_RESPONSE_SCRIPT> /Library/Ossec/active-response/bin/
      # sudo cp Library/Ossec/wodles/<CUSTOM_WODLE_SCRIPT> /Library/Ossec/wodles/

#. Start the Cyb3rhq agent service:

   .. code-block:: console

      # launchctl load /Library/LaunchDaemons/com.cyb3rhq.agent.plist

Verifying data restoration
^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Run the command below on your Cyb3rhq server to check if the Cyb3rhq agent is connected and active:

   .. code-block:: console

      # /var/ossec/bin/agent_control -l

2. Using the Cyb3rhq dashboard, navigate to **Active agents**. Select your Cyb3rhq agent to see the data from the backup, such as **Threat Hunting**, **Vulnerability Detection**, **Configuration Assessment**, and others.
