.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Keycloak is an open source identity and access management tool. Learn more about it and the read-only role in this section of the Cyb3rhq documentation.

Keycloak
========

`Keycloak <https://www.keycloak.org/>`_ is an open source identity and access management tool. It provides user federation, strong authentication, user management, and fine-grained authorization for modern applications and services. In this guide, we integrate the KeyCloak IdP to authenticate users into the Cyb3rhq platform.

There are three stages in the single sign-on integration:

#. `KeyCloak configuration`_
#. `Cyb3rhq indexer configuration`_
#. `Cyb3rhq dashboard configuration`_

KeyCloak configuration
----------------------

#. Create a new realm. Log in to the Keycloak admin console, expand the **master** drop-down menu and click **Add Realm**. Input a name in the **Realm name** field; in our case, this is named ``Cyb3rhq``. Click on **Create** to apply this configuration.

   .. thumbnail:: /images/single-sign-on/keycloak/01-create-a-new-realm.png
      :title: Create a new realm
      :align: center
      :width: 80%    
 
#. Create a new client. In the newly created realm, navigate to **Clients > Create Client** and  modify the following parameters:

      - **Client type**: select ``SAML`` from the drop-down menu. 
      - **Client ID**: input ``cyb3rhq-saml``. This is the ``SP Entity ID`` value which will be used later in the ``config.yml`` on the Cyb3rhq indexer instance.
     
   You can leave the rest of the values as default. Click **Save** to apply the configuration.

   .. thumbnail:: /images/single-sign-on/keycloak/02-create-a-new-client.png
      :title: Create a new client
      :align: center
      :width: 80%    

#. Configure client settings.

   #. Navigate to **Clients > Settings** and ensure the **Enabled** button is turned on. Complete the section with these parameters:

      - **Client ID**: ``cyb3rhq-saml``
      - **Name**: ``Cyb3rhq SSO``
      - **Valid redirect URIs**: ``https://<CYB3RHQ_DASHBOARD_URL>/*``
      - **IDP-Initiated SSO URL name**: ``cyb3rhq-dashboard``
      - **Name ID format**: ``username``
      - **Force POST binding**: ``ON``
      - **Include AuthnStatement**: ``ON``
      - **Sign documents**: ``ON``
      - **Sign assertions**: ``ON``
      - **Signature algorithm**: ``RSA_SHA256``
      - **SAML signature key name**: ``KEY_ID``
      - **Canonicalization method**: ``EXCLUSIVE``
      - **Front channel logout**: ``ON``

      Replace the ``<CYB3RHQ_DASHBOARD_URL>`` field with the corresponding URL of your Cyb3rhq dashboard instance.

      The configuration must be similar to the highlighted blue rectangles:   

      .. thumbnail:: /images/single-sign-on/keycloak/03-configure-client-settings.png
         :title: Configure client settings
         :align: center
         :width: 80%    
      
      .. thumbnail:: /images/single-sign-on/keycloak/04-configure-client-settings.png
         :title: Configure client settings
         :align: center
         :width: 80%    

      .. thumbnail:: /images/single-sign-on/keycloak/05-configure-client-settings.png
         :title: Configure client settings
         :align: center
         :width: 80%    

      .. thumbnail:: /images/single-sign-on/keycloak/06-configure-client-settings.png
         :title: Configure client settings
         :align: center
         :width: 80%    
            
      You can leave the rest of the values as default. Click **Save** to apply the configuration.

   #. Navigate to **Clients > Keys** and complete the section with these parameters:
   
      - **Client signature required**: ``Off``

      .. thumbnail:: /images/single-sign-on/keycloak/07-client-signature-required.png
         :title: Client signature required
         :align: center
         :width: 80%  

   #. Navigate to **Clients > Advanced > Fine Grain SAML Endpoint Configuration** and complete the section with these parameters:

      - **Assertion Consumer Service POST Binding URL**: ``https://<CYB3RHQ_DASHBOARD_URL>/_opendistro/_security/saml/acs/idpinitiated``
      - **Logout Service Redirect Binding URL**: ``https://<CYB3RHQ_DASHBOARD_URL>``

      .. thumbnail:: /images/single-sign-on/keycloak/08-fine-grain-saml-endpoint-configuration.png
         :title: Fine Grain SAML Endpoint Configuration
         :align: center
         :width: 80%  

      You can leave the rest of the values as default. Click **Save** to apply the configuration.

#. Create a new role. Navigate to **Realm roles > Create role** and complete the section with these parameters:

   - **Role name**: Input ``cyb3rhq-readonly``. This will be our backend role in the Cyb3rhq indexer configuration.

      .. thumbnail:: /images/single-sign-on/keycloak/read-only/09-create-a-new-role-RO.png
         :title: Create a new role
         :align: center
         :width: 80%  

   Click on **Save** to apply the configuration.

#. Create a new user. 

   #. Navigate to **Users > Add user** and fill in the required information.

      .. thumbnail:: /images/single-sign-on/keycloak/10-create-a-new-user.png
         :title: Create a new user
         :align: center
         :width: 80% 

      Click on **Create** to apply the configuration.

   #. Navigate to **Users > Credentials > Set password** and input a password for the newly created user. You will use these credentials to log in to the Cyb3rhq dashboard.

      .. thumbnail:: /images/single-sign-on/keycloak/11-set-password.png
         :title: Set password
         :align: center
         :width: 80% 

      Click on **Save** to apply the configuration.

#. Create a new group and assign the user.

   #. Go to **Groups > Create group** and assign a name to the group. In our case, this is **Cyb3rhq read only**.
   
      .. thumbnail:: /images/single-sign-on/keycloak/read-only/12-create-a-new-group-RO.png
         :title: Create a new group
         :align: center
         :width: 80% 

   #. Click on the newly created group, navigate to **Members > Add member** and select the user created in the previous step. Click on **Add** to add it to the group.
   
      .. thumbnail:: /images/single-sign-on/keycloak/read-only/13-add-member-RO.png
         :title: Add member
         :align: center
         :width: 80% 

   #. In the newly created group details, go to **Role Mapping > Assign role** and select the ``cyb3rhq-readonly`` role created in step 3. Click on **Assign** to apply the configuration. 

      .. thumbnail:: /images/single-sign-on/keycloak/read-only/14-assign-role-RO.png
         :title: Assign role
         :align: center
         :width: 80% 

#. Configure protocol mapper.

   #. Navigate to **Client scopes > role_list > Mappers > Configure a new mapper**. 

      .. thumbnail:: /images/single-sign-on/keycloak/15-configure-a-new-mapper.png
         :title: Configure a new mapper
         :align: center
         :width: 80% 

   #. Select **Role list** from the list as seen below:

      .. thumbnail:: /images/single-sign-on/keycloak/16-select-role-list.png
         :title: Select Role list
         :align: center
         :width: 80% 

   #. Complete the **Add mapper** section with these parameters:

      - **Mapper type**: ``Role list``
      - **Name**: ``cyb3rhqRoleKey``. You can use any name here.
      - **Role attribute name**: ``Roles``. This will be the ``roles_key`` on the Cyb3rhq indexer configuration.
      - **SAML Attribute NameFormat**: ``Basic``  
      - **Single Role Attribute**: ``On``

      .. thumbnail:: /images/single-sign-on/keycloak/17-complete-the-add-mapper-section.png
         :title: Complete the Add mapper section
         :align: center
         :width: 80% 

   Click on **Save** to apply the configuration.

#. Note the necessary parameters from the SAML settings of Keycloak.

   #. The parameters already obtained during the integration are:

      - ``sp.entity_id``: ``cyb3rhq-saml``
      - ``roles_key``: ``Roles``
      - ``kibana_url``: ``https://<CYB3RHQ_DASHBOARD_URL>``

   #. To obtain the remaining parameters.
   
      #. Navigate to **Clients** and select the name of your client. In our case, this is **cyb3rhq-saml**. 
      #. Navigate to **Action > Download adapter config**, and ensure the Format option is **Mod Auth Mellon files**. 
      #. Click on **Download** to download the remaining files.

      .. thumbnail:: /images/single-sign-on/keycloak/18-download-adapter-config.png
         :title: Download adapter config
         :align: center
         :width: 80% 

   #. The downloaded files contain the ``idp.metadata.xml`` file and the ``sp.metadata.xml`` file.

      -  The ``idp.entityID`` parameter is in the ``idp.metadata.xml`` file.

      .. thumbnail:: /images/single-sign-on/keycloak/19-the-exchange_key-parameter.png
         :title: The exchange_key parameter
         :align: center
         :width: 80%

Cyb3rhq indexer configuration
---------------------------

Edit the Cyb3rhq indexer security configuration files. We recommend that you back up these files before you carry out the configuration.

#. Generate a 64-character long random key using the following command.

   .. code-block:: console

      openssl rand -hex 32

   The output will be used as the ``exchange_key`` in the ``/etc/cyb3rhq-indexer/opensearch-security/config.yml`` file.

#. Place the ``idp.metadata.xml`` and ``sp.metadata.xml`` files within the ``/etc/cyb3rhq-indexer/opensearch-security/`` directory. Set the file ownership to cyb3rhq-indexer using the following command:

   .. code-block:: console

      chown cyb3rhq-indexer:cyb3rhq-indexer /etc/cyb3rhq-indexer/opensearch-security/idp.metadata.xml
      chown cyb3rhq-indexer:cyb3rhq-indexer /etc/cyb3rhq-indexer/opensearch-security/sp.metadata.xml

#. Edit the ``/etc/cyb3rhq-indexer/opensearch-security/config.yml`` file and change the following values:
 
   - Set the ``order`` in ``basic_internal_auth_domain`` to ``0``, and set the ``challenge`` flag to ``false``.  
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
              transport_enabled: false
              order: 1
              http_authenticator:
                type: saml
                challenge: true
                config:
                  idp:
                    metadata_file: '/etc/cyb3rhq-indexer/opensearch-security/idp.metadata.xml'
                    entity_id: 'http://192.168.XX.XX:8080/realms/Cyb3rhq'
                  sp:
                    entity_id: cyb3rhq-saml
                    metadata_file: '/etc/cyb3rhq-indexer/opensearch-security/sp.metadata.xml'
                  kibana_url: https://<CYB3RHQ_DASHBOARD_ADDRESS>
                  roles_key: Roles
                  exchange_key: 'b1d6dd32753374557dcf92e241.......'
              authentication_backend:
                type: noop

   Ensure to change the following parameters to their corresponding value:

   - ``idp.metadata_file``  
   - ``idp.entity_id``
   - ``sp.entity_id``
   - ``sp.metadata_file``
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

Cyb3rhq dashboard configuration
-----------------------------

#. Create a new role mapping for the backend role. Follow these steps to create a new role mapping, and grant read-only permissions to the backend role.

   #. Log into the Cyb3rhq dashboard as administrator.
   #. Click the upper-left menu icon **☰** to open the options, go to **Indexer management** > **Security**, and then **Roles** to open the roles page.
   #. Click **Create role**, complete the empty fields with the following parameters, and then click **Create** to complete the task.

      -  **Name**: Assign a name to the role.
      -  **Cluster permissions**: ``cluster_composite_ops_ro``
      -  **Index**: ``*``
      -  **Index permissions**: ``read``
      -  **Tenant permissions**: Select ``global_tenant`` and the ``Read only`` option.
   #. Select the newly created role.
   #. Select the **Mapped users** tab and click **Manage mapping**.
   #. Under **Backend roles**, add the value of the **Role name** attribute in Keycloak configuration and click **Map** to confirm the action. In our case, the backend role is ``cyb3rhq-readonly``.
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
      - **Roles**: Select ``readonly``.
      - **Custom rules**: Click **Add new rule** to expand this field.
      - **User field**: ``backend_roles``
      - **Search operation**: ``FIND``
      - **Value**: Assign the value of the realm role in Keycloak configuration. In our case, this is ``cyb3rhq-readonly``.  

      .. thumbnail:: /images/single-sign-on/keycloak/read-only/Cyb3rhq-role-mapping-RO.png
         :title: Create Cyb3rhq role mapping
         :alt: Create Cyb3rhq role mapping 
         :align: center
         :width: 80%

   #. Click **Save role mapping** to save and map the backend role with Cyb3rhq as *read-only*.


#. Edit the Cyb3rhq dashboard configuration file. Add these configurations to ``/etc/cyb3rhq-dashboard/opensearch_dashboards.yml``. We recommend that you back up these files before you carry out the configuration.

   .. code-block:: console  

      opensearch_security.auth.type: "saml"
      server.xsrf.allowlist: ["/_opendistro/_security/saml/acs", "/_opendistro/_security/saml/logout", "/_opendistro/_security/saml/acs/idpinitiated"]
      opensearch_security.session.keepalive: false

#. Restart the Cyb3rhq dashboard service using this command:

   .. include:: /_templates/common/restart_dashboard.rst

#. Test the configuration. Go to your Cyb3rhq dashboard URL and log in with your Keycloak account. 
