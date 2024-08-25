.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Jumpcloud is a Unified Device and Identity Access Management platform. Learn more about it and the administrator role in this section of the Cyb3rhq documentation.

Jumpcloud
=========

`Jumpcloud <https://jumpcloud.com/>`__, is a Unified Device and Identity Access Management platform that provides services such as Multi-Factor Authentication (MFA), Single Sign-On, password management, and cloud directory. In this guide, we integrate the Jumpcloud SSO to authenticate users into the Cyb3rhq platform.

There are three stages in the single sign-on integration.

#. `Jumpcloud Configuration`_
#. `Cyb3rhq indexer configuration`_
#. `Cyb3rhq dashboard configuration`_

Jumpcloud Configuration
-----------------------

#. Create an account in Jumpcloud. Request a free trial if you don't have a paid license.
#. Create a new user. This step can be skipped if you are just testing, you can use your Jumpcloud ``admin`` user for example.

   #. Go to **User Management**, click on **Users** > **(+)** >  **Manual user entry**. Fill in the user information, activate the user and click on **save user**. 

      .. thumbnail:: /images/single-sign-on/jumpcloud/01-go-to-user-management-and-click-on-users.png
          :title: Go to User Management and click on Users
          :align: center
          :width: 80%

#. Create a new group and assign the user.

   #. Go to **User Management** > **User Groups** > **(+)** and give a name to the group. In our case, this is ``Cyb3rhq admins``.

      .. thumbnail:: /images/single-sign-on/jumpcloud/02-go-to-user-management-user-groups.png
          :title: Go to User Management - User Groups
          :align: center
          :width: 80%

      The name you give to your group will be used in the configuration. It will be our ``backend_roles`` in ``roles_mapping.yml``.

   #. In the selected **User Groups**,  go to the **Users** tab, select the newly created user and Save the changes.

      .. thumbnail:: /images/single-sign-on/jumpcloud/03-go-to-users-tab.png
          :title: Go to the Users tab and select the newly created user 
          :align: center
          :width: 80%

#. Create a new app. Configure the SAML settings while you create the app.

   #. Under the User Authentication section, go to **SSO Applications**, select **+ Add New Application**, and select **Custom Application**.

      .. thumbnail:: /images/single-sign-on/jumpcloud/04-go-to-SSO.png
          :title: Add new SSO application
          :align: center
          :width: 80%    

      .. thumbnail:: /images/single-sign-on/jumpcloud/05-select-custom-app.png
          :title: Select custom application
          :align: center
          :width: 80%    

   #. Complete the **Create New Application Integration** page with the appropriate information.

      -  Click **Next** on the **Select Application** page.
      -  Check the **Manage Single Sign-On (SSO)** and **Configure SSO with SAML** options on the **Select Options** page. Click **Next** to proceed to the next step.
      -  Assign a **Display Label** to the application, and click the **Show this application in User Portal** checkbox on the **Enter General Info** page. Click **Save Application** to apply the settings. 
      -  Click **Configure Application** on the Review page.

      .. thumbnail:: /images/single-sign-on/jumpcloud/06-select-application.png
          :title: Custom application selected
          :alt: Custom application selected
          :align: center
          :width: 80%    

      .. thumbnail:: /images/single-sign-on/jumpcloud/07-select-manage-sso.png
          :title: Configure SSO options
          :alt: Configure SSO options
          :align: center
          :width: 80%    

      .. thumbnail:: /images/single-sign-on/jumpcloud/08-enter-general-info.png
          :title: Enter general info
          :alt: Enter general info
          :align: center
          :width: 80%    

      .. thumbnail:: /images/single-sign-on/jumpcloud/09-go-to-review.png
          :title: Confirm new application integration
          :alt: Confirm new application integration
          :align: center
          :width: 80%    

   #. Complete the SSO tab with the appropriate information.

      - **IdP Entity ID**: ``cyb3rhq`` (this will be the ``idp.entity_id`` in our Cyb3rhq indexer configuration).
      - **SP Entity ID**: ``cyb3rhq-saml`` (this will be the ``sp.entity_id`` in our Cyb3rhq indexer configuration).
      - **ACS URL**: ``https://<CYB3RHQ_DASHBOARD_URL>/_opendistro/_security/saml/acs``
      - Check **Sign Assertion**.
      - Check **Declare Redirect Endpoint**.
      - Check **include group attribute** and add **Roles** as the attribute. This will be used later in the ``config.yml`` configuration file.

      The rest of the options can be left as their default values.

      .. thumbnail:: /images/single-sign-on/jumpcloud/10-complete-the-sso-tab.png
          :title: Complete the SSO tab
          :align: center
          :width: 80%   

      .. thumbnail:: /images/single-sign-on/jumpcloud/11-complete-the-sso-tab.png      
          :title: Complete the SSO tab
          :align: center
          :width: 80%    

      .. thumbnail:: /images/single-sign-on/jumpcloud/12-complete-the-sso-tab.png
          :title: Complete the SSO tab
          :align: center
          :width: 80%    

      .. thumbnail:: /images/single-sign-on/jumpcloud/13-complete-the-sso-tab.png
          :title: Complete the SSO tab
          :align: center
          :width: 80%    

   #. On the **User Groups** tab, select the **Group** created previously and click **save**.

      .. thumbnail:: /images/single-sign-on/jumpcloud/14-on-the-user-groups-tab.png
          :title: On the User Groups tab, select the Group created previously
          :align: center
          :width: 80% 

#. Note the necessary parameters from the SAML settings of the new app.

   Open the recently created application and go to the **SSO** tab, select **Export Metadata**. This will be our ``metadata_file``. Place the metadata file in the configuration directory of the Cyb3rhq indexer. The path to the directory is ``/etc/cyb3rhq-indexer/opensearch-security/``.

   .. thumbnail:: /images/single-sign-on/jumpcloud/15-go-to-the-sso-tab.png
       :title: Go to the SSO tab and select Export Metadata
       :align: center
       :width: 80%

Cyb3rhq indexer configuration
---------------------------

Edit the Cyb3rhq indexer security configuration files. We recommend that you back up these files before you carry out the configuration.

#. Generate a 64-character long random key using the following command.

   .. code-block:: console

      openssl rand -hex 32

   The output will be used as the ``exchange_key`` in the ``/etc/cyb3rhq-indexer/opensearch-security/config.yml`` file.

#. Place the ``metadata_jumpcloud.xml`` file within the ``/etc/cyb3rhq-indexer/opensearch-security/`` directory. Set the file ownership to ``cyb3rhq-indexer`` using the following command:

   .. code-block:: console

      # chown cyb3rhq-indexer:cyb3rhq-indexer /etc/cyb3rhq-indexer/opensearch-security/metadata_jumpcloud.xml

#. Edit the ``/etc/cyb3rhq-indexer/opensearch-security/config.yml`` file and change the following values:

   - Set the ``order`` in ``basic_internal_auth_domain`` to ``0`` and the ``challenge`` flag to ``false``.

   - Include a ``saml_auth_domain`` configuration under the ``authc`` section similar to the following:

   .. code-block:: yaml
      :emphasize-lines: 7,10,22,23,25,26,27,28,29

          authc:
      ...
            basic_internal_auth_domain:
              description: "Authenticate via HTTP Basic against internal users database"
              http_enabled: true
              transport_enabled: true
              order: 0
              http_authenticator:
                type: "basic"
                challenge: false
              authentication_backend:
                type: "intern"
            saml_auth_domain:
              http_enabled: true
              transport_enabled: true
              order: 1
              http_authenticator:
                type: saml
                challenge: true
                config:
                  idp:
                    metadata_file: '/etc/cyb3rhq-indexer/opensearch-security/metadata_jumpcloud.xml'
                    entity_id: cyb3rhq
                  sp:
                    entity_id: cyb3rhq-saml
                    forceAuthn: true
                  kibana_url: https://<CYB3RHQ_DASHBOARD_URL>
                  roles_key: Roles
                  exchange_key: 'b1d6dd32753374557dcf92e241.......'
              authentication_backend:
                type: noop

   Ensure to change the following parameters to their corresponding value:

      - ``idp.metadata_file``
      - ``idp.entity_id``
      - ``sp.entity_id``
      - ``kibana_url``
      - ``roles_key``
      - ``exchange_key``

#. Run the ``securityadmin`` script to load the configuration changes made in the ``config.yml`` file. 

   .. code-block:: console

      # export JAVA_HOME=/usr/share/cyb3rhq-indexer/jdk/ && bash /usr/share/cyb3rhq-indexer/plugins/opensearch-security/tools/securityadmin.sh -f /etc/cyb3rhq-indexer/opensearch-security/config.yml -icl -key /etc/cyb3rhq-indexer/certs/admin-key.pem -cert /etc/cyb3rhq-indexer/certs/admin.pem -cacert /etc/cyb3rhq-indexer/certs/root-ca.pem -h 127.0.0.1 -nhnv
      
   The ``-h`` flag specifies the hostname or the IP address of the Cyb3rhq indexer node. Note that this command uses 127.0.0.1, set your Cyb3rhq indexer address if necessary.

   The command output must be similar to the following:

   .. code-block:: console
      :class: output

      Security Admin v7
      Will connect to 127.0.0.1:9200 ... done
      Connected as "CN=admin,OU=Cyb3rhq,O=Cyb3rhq,L=California,C=US"
      OpenSearch Version: 2.10.0
      Contacting opensearch cluster 'opensearch' and wait for YELLOW clusterstate ...
      Clustername: cyb3rhq-cluster
      Clusterstate: GREEN
      Number of nodes: 1
      Number of data nodes: 1
      .opendistro_security index already exists, so we do not need to create one.
      Populate config from /etc/cyb3rhq-indexer/opensearch-security
      Will update '/config' with /etc/cyb3rhq-indexer/opensearch-security/config.yml 
         SUCC: Configuration for 'config' created or updated
      SUCC: Expected 1 config types for node {"updated_config_types":["config"],"updated_config_size":1,"message":null} is 1 (["config"]) due to: null
      Done with success
   
#. Edit the ``/etc/cyb3rhq-indexer/opensearch-security/roles_mapping.yml`` file and change the following values:

   Configure the ``roles_mapping.yml`` file to map the Jumpcloud user group to the appropriate Cyb3rhq indexer role. In our case, we map the ``Cyb3rhq admins`` group to the ``all_access`` role:

   .. code-block:: console
      :emphasize-lines: 6

      all_access:
        reserved: false
        hidden: false
        backend_roles:
        - "admin"
        - "Cyb3rhq admins"
        description: "Maps admin to all_access"

#. Run the ``securityadmin`` script to load the configuration changes made in the ``roles_mapping.yml`` file. 

   .. code-block:: console

      # export JAVA_HOME=/usr/share/cyb3rhq-indexer/jdk/ && bash /usr/share/cyb3rhq-indexer/plugins/opensearch-security/tools/securityadmin.sh -f /etc/cyb3rhq-indexer/opensearch-security/roles_mapping.yml -icl -key /etc/cyb3rhq-indexer/certs/admin-key.pem -cert /etc/cyb3rhq-indexer/certs/admin.pem -cacert /etc/cyb3rhq-indexer/certs/root-ca.pem -h 127.0.0.1 -nhnv      

   The ``-h`` flag specifies the hostname or the IP address of the Cyb3rhq indexer node. Note that this command uses 127.0.0.1, set your Cyb3rhq indexer address if necessary.
      
   The command output must be similar to the following:
       
   .. code-block:: console
      :class: output

      Security Admin v7
      Will connect to 127.0.0.1:9200 ... done
      Connected as "CN=admin,OU=Cyb3rhq,O=Cyb3rhq,L=California,C=US"
      OpenSearch Version: 2.10.0
      Contacting opensearch cluster 'opensearch' and wait for YELLOW clusterstate ...
      Clustername: cyb3rhq-cluster
      Clusterstate: GREEN
      Number of nodes: 1
      Number of data nodes: 1
      .opendistro_security index already exists, so we do not need to create one.
      Populate config from /etc/cyb3rhq-indexer/opensearch-security
      Will update '/rolesmapping' with /etc/cyb3rhq-indexer/opensearch-security/roles_mapping.yml 
         SUCC: Configuration for 'rolesmapping' created or updated
      SUCC: Expected 1 config types for node {"updated_config_types":["rolesmapping"],"updated_config_size":1,"message":null} is 1 (["rolesmapping"]) due to: null
      Done with success

Cyb3rhq dashboard configuration
-----------------------------

#. Check the value of ``run_as`` in the ``/usr/share/cyb3rhq-dashboard/data/cyb3rhq/config/cyb3rhq.yml`` configuration file. If ``run_as`` is set to ``false``, proceed to the next step.

   .. code-block:: yaml
      :emphasize-lines: 7

      hosts:
        - default:
            url: https://127.0.0.1
            port: 55000
            username: cyb3rhq-wui
            password: "<cyb3rhq-wui-password>"
            run_as: false

   If ``run_as`` is set to ``true``, you need to add a role mapping on the Cyb3rhq dashboard. To map the backend role to Cyb3rhq, follow these steps:

   #. Click **☰** to open the menu on the Cyb3rhq dashboard, go to **Server management** > **Security**, and then **Roles mapping** to open the page.

      .. thumbnail:: /images/single-sign-on/Cyb3rhq-role-mapping.gif
         :title: Cyb3rhq role mapping
         :alt: Cyb3rhq role mapping 
         :align: center
         :width: 80%

   #. Click **Create Role mapping** and complete the empty fields with the following parameters:

      - **Role mapping name**: Assign a name to the role mapping.
      - **Roles**: Select ``administrator``.
      - **Custom rules**: Click **Add new rule** to expand this field.
      - **User field**: ``backend_roles``
      - **Search operation**: ``FIND``
      - **Value**: Assign the name of the Jumpcloud user group. In our case, this is  ``Cyb3rhq admins``.

      .. thumbnail:: /images/single-sign-on/jumpcloud/Cyb3rhq-role-mapping.png
         :title: Create Cyb3rhq role mapping
         :alt: Create Cyb3rhq role mapping 
         :align: center
         :width: 80%      

   #. Click **Save role mapping** to save and map the backend role with Cyb3rhq as administrator.

#. Edit the Cyb3rhq dashboard configuration file. Add these configurations to ``/etc/cyb3rhq-dashboard/opensearch_dashboards.yml``. We recommend that you back up these files before you carry out the configuration.

   .. code-block:: console  

      opensearch_security.auth.type: "saml"
      server.xsrf.allowlist: ["/_opendistro/_security/saml/acs", "/_opendistro/_security/saml/logout", "/_opendistro/_security/saml/acs/idpinitiated"]
      opensearch_security.session.keepalive: false

#. Restart the Cyb3rhq dashboard service.

   .. include:: /_templates/common/restart_dashboard.rst

#. Test the configuration. Go to your Cyb3rhq dashboard URL and log in with your Jumpcloud account. 



