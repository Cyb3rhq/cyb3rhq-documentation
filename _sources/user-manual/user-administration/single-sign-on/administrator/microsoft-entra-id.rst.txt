.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Microsoft Entra ID is a cloud-based identity and access management service by Microsoft. Learn more about it and the administrator role in this section of the Cyb3rhq documentation.

Microsoft Entra ID
==================

`Microsoft Entra ID <https://portal.azure.com/>`_ (ME-ID) is a cloud-based identity and access management service by Microsoft. It provides single sign-on, multifactor authentication, and access to internal and cloud developed applications. In this guide, we integrate the Microsoft Entra ID IdP to authenticate users into the Cyb3rhq platform.

There are three stages in the single sign-on integration.

#. Microsoft Entra ID Configuration
#. Cyb3rhq indexer configuration
#. Cyb3rhq dashboard configuration
   
 .. note::
    You may have to request a free trial at least to complete the configuration. 

Microsoft Entra ID Configuration
--------------------------------

#. Create a Microsoft account or use your own if you already have one.
#. Go to `Microsoft Azure Portal <https://portal.azure.com/>`_ and sign in with your Microsoft account.
#. Create an app in **Microsoft Entra ID**.

   #. Go to **Microsoft Entra ID** > **Enterprise applications** > **New application** and **Create your own application**. 

   #. Select **Integrate any other application you don't find in the gallery**. Give a name to your application and click **Add**. In our case, we name this application ``cyb3rhq-sso``.

   .. thumbnail:: /images/single-sign-on/azure-active-directory/01-go-to-azure-active-directory.png
      :title: Create an app in Microsoft Entra ID
      :align: center
      :width: 80%

#. Create a role for your application.

   #. Go back to **Microsoft Entra ID** and click on **App registrations**.

      .. thumbnail:: /images/single-sign-on/azure-active-directory/02-click-on-app-registrations.png
         :title: Click on App registrations
         :align: center
         :width: 80%

   #. Select your new app under **All applications** and **click Manifest**.

      .. thumbnail:: /images/single-sign-on/azure-active-directory/03-select-your-new-apps.png
         :title: Select your new app
         :align: center
         :width: 80%

   #. Add a new role to your application's **Manifest**:

      .. code-block:: console

         {
            "allowedMemberTypes": [
               "User"
            ],
            "description": "Cyb3rhq role",
            "displayName": "Cyb3rhq_role",
            "id": "<application_id>",
            "isEnabled": true,
            "lang": null,
            "origin": "Application",
            "value": "Cyb3rhq_role"
         },
   
      - ``description``: can be any value that you want.
      - ``id``: should be the ID of your application. You can find it in the application's overview menu or at the top of the Manifest in the field ``appId``.
      - ``value``: defines the name of the role. In this case, ``Cyb3rhq_role``, which will be the value for the role to be mapped on the ``roles_mapping.yml`` file.
      - ``displayName``: can be the same as ``value``.

      .. thumbnail:: /images/single-sign-on/azure-active-directory/04-add-a-new-role.png
         :title: Add a new role to your application's Manifest
         :align: center
         :width: 80%

   #. Save the changes and proceed to the next step.

#. Assign a user to the app.

   #. In **Microsoft Entra ID**, go to **Enterprise applications**, select your application and then click on **Assign users and groups** (or **Users and Groups** in the panel to the left).

      .. thumbnail:: /images/single-sign-on/azure-active-directory/05-assign-a-user-to-the-app.png
         :title: Assign a user to the app
         :align: center
         :width: 80%

   #. Click on **Add user/group**, assign a **user** and select the role we created in **Manifest**.

      .. thumbnail:: /images/single-sign-on/azure-active-directory/06-click-on-add-user-group.png
         :title: Click on Add user/group
         :align: center
         :width: 80%

#. Configure Single sign-on.

   #. Go to **Enterprise applications**, select your application and then click on **Set up single sign-on > SAML**.

      .. thumbnail:: /images/single-sign-on/azure-active-directory/07-configure-single-sign-on.png
         :title: Configure Single sign-on
         :align: center
         :width: 80%

      .. thumbnail:: /images/single-sign-on/azure-active-directory/08-set-up-single-sign-on-SAML.png
         :title: Set up single sign-on > SAML
         :align: center
         :width: 80%
    
      .. thumbnail:: /images/single-sign-on/azure-active-directory/09-set-up-single-sign-on-SAML.png
         :title: Set up single sign-on > SAML 
         :align: center
         :width: 80%
    
      .. thumbnail:: /images/single-sign-on/azure-active-directory/10-set-up-single-sign-on-SAML.png
         :title: Set up single sign-on > SAML
         :align: center
         :width: 80%

   #. In option 1, under  **Basic SAML Configuration**, click **edit** and set ``cyb3rhq-saml`` as **Identifier (Entity ID)** and ``https://<CYB3RHQ_DASHBOARD_URL>/_opendistro/_security/saml/acs`` as **Reply URL (Assertion Consumer Service URL)**, and ``https://<CYB3RHQ_DASHBOARD_URL>`` as **Sign on URL (Optional)**. Replace ``<CYB3RHQ_DASHBOARD_URL>`` with the corresponding value. Save and proceed to the next step.

      .. thumbnail:: /images/single-sign-on/azure-active-directory/11-click-edit-and-set-cyb3rhq-saml.png
         :title: Click edit and set cyb3rhq-saml
         :align: center
         :width: 80%

   #. In option 2 under **Attributes & Claims**, click **edit** and select **Add new claim**. Select **Roles** as the name and **user.assignedroles** as **Source attribute**. This claim will be mapped with ``roles_key`` on the Cyb3rhq indexer configuration.

      .. thumbnail:: /images/single-sign-on/azure-active-directory/12-click-edit-and-select-add-new-claim.png
         :title: Click edit and select Add new claim
         :align: center
         :width: 80%

#. Note the necessary parameters. In the **Enterprise applications** menu, select your application and then click on **Single sign-on**. Note some parameters that will be used in the Cyb3rhq indexer configuration.

   -  In option 3 **SAML Certificate**, the **App Federation Metadata Url** will be the ``idp.metadata_url`` in the Cyb3rhq indexer configuration file.
   -  In option 4 **Set up <YOUR APPLICATION>**, the **Microsoft Entra ID Identifier** will be our ``idp.entity_id``.

Cyb3rhq indexer configuration
---------------------------

Edit the Cyb3rhq indexer security configuration files. We recommend that you back up these files before you carry out the configuration.

#. Generate a 64-character long random key using the following command.

   .. code-block:: console

      openssl rand -hex 32

   The output will be used as the ``exchange_key`` in the ``/etc/cyb3rhq-indexer/opensearch-security/config.yml`` file.

#. Edit the ``/etc/cyb3rhq-indexer/opensearch-security/config.yml`` file and change the following values:

   - Set the ``order`` in ``basic_internal_auth_domain`` to ``0`` and the ``challenge`` flag to ``false``.

   - Include a ``saml_auth_domain`` configuration under the ``authc`` section similar to the following:

   .. code-block:: yaml
      :emphasize-lines: 7,10,22,23,25,26,27,28

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
              transport_enabled: false
              order: 1
              http_authenticator:
                type: saml
                challenge: true
                config:
                  idp:
                    metadata_url: https://login.microsoftonline.com/...
                    entity_id: https://sts.windows.net/...
                  sp:
                    entity_id: cyb3rhq-saml
                  kibana_url: https://<CYB3RHQ_DASHBOARD_URL>
                  roles_key: Roles
                  exchange_key: 'b1d6dd32753374557dcf92e241.......'
              authentication_backend:
                type: noop


   Ensure to change the following parameters to their corresponding value:

   - ``idp.metadata_url``
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

   Configure the ``roles_mapping.yml`` file to map the role we have in Microsoft Entra ID to the appropriate Cyb3rhq indexer role. In this case, we map the ``Cyb3rhq_role`` in Microsoft Entra ID to the ``all_access`` role in Cyb3rhq indexer:

   .. code-block:: console
      :emphasize-lines: 6

      all_access:
        reserved: false
        hidden: false
        backend_roles:
        - "admin"
        - "Cyb3rhq_role"
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
      - **Value**: Assign the backend role from the Microsoft Entra ID configuration, in our case, this is ``Cyb3rhq_role``. 

      .. thumbnail:: /images/single-sign-on/azure-active-directory/Cyb3rhq-role-mapping.png
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

#. Test the configuration. Go to your Cyb3rhq dashboard URL and log in with your Microsoft account. 
