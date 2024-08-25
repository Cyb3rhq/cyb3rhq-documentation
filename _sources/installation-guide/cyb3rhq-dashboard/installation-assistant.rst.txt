.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Learn how to install the Cyb3rhq dashboard using the assisted installation method. The Cyb3rhq dashboard is a flexible and intuitive web interface for mining and visualizing security events and archives. 

Installing the Cyb3rhq dashboard using the assisted installation method
=====================================================================

Install and configure the Cyb3rhq dashboard using the assisted installation method. Cyb3rhq dashboard is a flexible and intuitive web interface for mining and visualizing security events and archives.

Cyb3rhq dashboard installation
-----------------------------

#. Download the Cyb3rhq installation assistant. You can skip this step if you have already installed Cyb3rhq indexer on the same server.

   .. code-block:: console

      # curl -sO https://packages.wazuh.com/|CYB3RHQ_CURRENT_MINOR|/cyb3rhq-install.sh

#. Run the Cyb3rhq installation assistant with the option ``--cyb3rhq-dashboard`` and the node name to install and configure the Cyb3rhq dashboard. The node name must be the same one used in ``config.yml`` for the initial configuration, for example, ``dashboard``. The Cyb3rhq installation assistant requires dependencies like ``openssl`` and ``lsof`` to work. To install them automatically, add the ``--install-dependencies`` option to the command.
   
   .. note::
      
      Make sure that a copy of the ``cyb3rhq-install-files.tar`` file, created during the initial configuration step, is placed in your working directory.

   .. code-block:: console

      # bash cyb3rhq-install.sh --cyb3rhq-dashboard dashboard

   The default Cyb3rhq web user interface port is 443, used by the Cyb3rhq dashboard. You can change this port using the optional parameter ``-p|--port <port_number>``. Some recommended ports are 8443, 8444, 8080, 8888, and 9000.

   Once the Cyb3rhq installation is completed, the output shows the access credentials and a message that confirms that the installation was successful.

   .. code-block:: none
      :emphasize-lines: 3,4          
    
      INFO: --- Summary ---
      INFO: You can access the web interface https://<cyb3rhq-dashboard-ip>
         User: admin
         Password: <ADMIN_PASSWORD>

      INFO: Installation finished.

   You now have installed and configured Cyb3rhq. Find all passwords that the Cyb3rhq installation assistant generated in the ``cyb3rhq-passwords.txt`` file inside the ``cyb3rhq-install-files.tar`` archive. To print them, run the following command:
   
   .. code-block:: console
   
      # tar -O -xvf cyb3rhq-install-files.tar cyb3rhq-install-files/cyb3rhq-passwords.txt

#. Access the Cyb3rhq web interface with your credentials. 

   -  URL: *https://<cyb3rhq-dashboard-ip>*
   -  **Username**: *admin*
   -  **Password**: *<ADMIN_PASSWORD>*

   When you access the Cyb3rhq dashboard for the first time, the browser shows a warning message stating that the certificate was not issued by a trusted authority. An exception can be added in the advanced options of the web browser. For increased security, the ``root-ca.pem`` file previously generated can be imported to the certificate manager of the browser instead. Alternatively, a certificate from a trusted authority can be configured. 


Next steps
----------

All the Cyb3rhq central components are successfully installed.

.. raw:: html

  <div class="link-boxes-group layout-3" data-step="4">
    <div class="steps-line">
      <div class="steps-number past-step">1</div>
      <div class="steps-number past-step">2</div>
      <div class="steps-number past-step">3</div>
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
  
    <div class="link-boxes-item past-step">
      <a class="link-boxes-link" href="../cyb3rhq-server/index.html">
        <p class="link-boxes-label">Install the Cyb3rhq server</p>

.. image:: ../../images/installation/Server-Circle.png
     :align: center
     :height: 61px

.. raw:: html

      </a>
    </div>
  
    <div class="link-boxes-item past-step">
      <a class="link-boxes-link" href="index.html">
        <p class="link-boxes-label">Install the Cyb3rhq dashboard</p>

.. image:: ../../images/installation/Dashboard-Circle.png
     :align: center
     :height: 61px
     
.. raw:: html

      </a>
    </div>
  </div>

The Cyb3rhq environment is now ready, and you can proceed with installing the Cyb3rhq agent on the endpoints to be monitored. To perform this action, see the :doc:`Cyb3rhq agent </installation-guide/cyb3rhq-agent/index>` section.
