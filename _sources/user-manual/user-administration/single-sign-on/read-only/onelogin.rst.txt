.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: OneLogin is a cloud-based identity and access management provider. Learn more about it and the read-only role in this section of the Cyb3rhq documentation.

OneLogin
========

`OneLogin <https://www.onelogin.com>`__ is a cloud-based identity and access management provider that provides a unified access management platform to enterprise-level businesses and organizations. In this guide, we integrate the OneLogin SSO to authenticate users into the Cyb3rhq platform. 

There are three stages in the single sign-on integration.

#. `OneLogin Configuration`_
#. `Cyb3rhq indexer configuration`_
#. `Cyb3rhq dashboard configuration`_
   
OneLogin Configuration
----------------------

#. Create an account in OneLogin. Request a free trial if you don't have a paid license.
#. Add the OneLogin extension to your browser.
#. Create a new user. 

   #. Log in to **OneLogin** web console, and select **Administration** > **Users** > **New User**.

      .. thumbnail:: /images/single-sign-on/onelogin/01-log-in-to-onelogin-web-console.png
         :title: Log in to OneLogin web console
         :align: center
         :width: 80%

   #. Complete the mandatory fields, assign a value in the **Department** field and click on **Save User**. In our case, the department is ``cyb3rhq-readonly``. This field will be used later in the Cyb3rhq indexer configuration as the backend role.

      .. thumbnail:: /images/single-sign-on/onelogin/read-only/02-complete-the-mandatory-fields-RO.png
         :title: Complete the mandatory fields
         :align: center
         :width: 80%

   #. Select the user, navigate to **More Actions** and click on **Change Password** to assign a password to the user.

      .. thumbnail:: /images/single-sign-on/onelogin/read-only/03-click-on-save-user-RO.png
         :title: Click on Save User
         :align: center
         :width: 80%

#. Create a new app using the **SAML Custom Connector (Advanced)** template and configure the SAML settings.

   #. Go to **Applications** tab > **Applications** and then click on **Add app**.

      .. thumbnail:: /images/single-sign-on/onelogin/04-create-a-new-app.png
         :title: Create a new app using the SAML Custom Connector (Advanced)
         :align: center
         :width: 80%

   #. Search for **SAML Custom Connector (Advanced)** application. In **Display Name**,  assign a name. In our case, we assigned the name ``Cyb3rhq``. Navigate to the **Configuration** tab and fill in the information:

      - **Audience (EntityID)**: ``cyb3rhq-saml``
      - **Recipient**: ``https://<CYB3RHQ_DASHBOARD_URL>/_opendistro/_security/saml/acs``
      - **ACS (Consumer) URL Validator**: ``https://<CYB3RHQ_DASHBOARD_URL>/_opendistro/_security/saml/acs``
      - **ACS (Consumer) URL**: ``https://<CYB3RHQ_DASHBOARD_URL>/_opendistro/_security/saml/acs``
      - **Login URL**: ``https://<CYB3RHQ_DASHBOARD_URL>``
      - **SAML initiator**: ``Service Provider``
      - **SAML nameID format**: ``Unspecified``
      - **SAML issuer type**: ``Specific``
      - **SAML signature element**: ``Response``
   
      Replace the ``<CYB3RHQ_DASHBOARD_URL>`` field with the corresponding URL of your Cyb3rhq dashboard instance.

      The configuration must be similar to the highlighted blue rectangles:

      .. thumbnail:: /images/single-sign-on/onelogin/05-search-for-saml-custom-connector.png
         :title: Search for SAML Custom Connector (Advanced) application
         :align: center
         :width: 80%   

      .. thumbnail:: /images/single-sign-on/onelogin/06-search-for-saml-custom-connector.png
         :title: Search for SAML Custom Connector (Advanced) application
         :align: center
         :width: 80%   

   #. Go to the **Parameters** tab and click on **+** to add a new parameter to the app:

      .. thumbnail:: /images/single-sign-on/onelogin/07-go-to-the-parameters-tab.png
         :title: Go to the Parameters tab
         :align: center
         :width: 80%   

   #. Edit the parameter details. In our case, we named the new parameter as **Roles**, then we selected the value **Department** and marked the  **Include in SAML assertion** checkbox. The rest of the app configuration is left as default.

      .. thumbnail:: /images/single-sign-on/onelogin/08-we-named-the-new-parameter-as-roles.png
         :title: We named the new parameter as Roles
         :align: center
         :width: 80%   

   #. Click on **Save** to apply the configuration.

#. Add the created user to the new app.

   #. Go to **Users** and select the created user. Go to **Applications** and click on **+**, select the **Allow the user to sign in** checkbox, and click on **Save**.

      .. thumbnail:: /images/single-sign-on/onelogin/09-add-the-created-user-to-the-new-app.png
         :title: Add the created user to the new app
         :align: center
         :width: 80%    

#. Get the ``metadata_onelogin.xml`` file from the application.

   #. Go to **Applications** >  **Applications** then select the **Cyb3rhq** app. Click on **More Actions** and then select **SAML Metadata**.

      .. thumbnail:: /images/single-sign-on/onelogin/10-click-on-more-actions.png
         :title: Click on More Actions and then select SAML Metadata
         :align: center
         :width: 80%
   
   #. Save the file as ``XML``. This will be the ``idp.metadata_file`` in the Cyb3rhq indexer security configuration.

   #. The **Issuer URL** will be the ``idp.entity_id`` in the Cyb3rhq indexer security configuration.

      .. thumbnail:: /images/single-sign-on/onelogin/11-save-the-file-as-xml.png
         :title: Save the file as XML
         :align: center
         :width: 80%
   
   #. The **Audience (EntityID)** will be the ``sp.entity_id`` in  the Cyb3rhq indexer security configuration.

      .. thumbnail:: /images/single-sign-on/onelogin/12-the-Audience-entityid.png
         :title: The Audience (EntityID) will be the sp.entity_id in  the Cyb3rhq indexer security configuration
         :align: center
         :width: 80%


   #. The ``roles_key`` is the name of the parameter added in the **Cyb3rhq** app. In our example, this is ``Roles``. 

Cyb3rhq indexer configuration
---------------------------

Edit the Cyb3rhq indexer security configuration files. We recommend that you back up these files before you carry out the configuration.

#. Generate a 64-character long random key using the following command.

   .. code-block:: console

      openssl rand -hex 32

   The output will be used as the ``exchange_key`` in the ``/etc/cyb3rhq-indexer/opensearch-security/config.yml`` file.

#. Place the ``metadata_onelogin.xml`` file within the ``/etc/cyb3rhq-indexer/opensearch-security/`` directory. Set the file ownership to ``cyb3rhq-indexer`` using the following command:

   .. code-block:: console
   
      # chown cyb3rhq-indexer:cyb3rhq-indexer /etc/cyb3rhq-indexer/opensearch-security/metadata_onelogin.xml

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
            saml_auth_domain2:
              http_enabled: true
              transport_enabled: true
              order: 1
              http_authenticator:
                type: saml
                challenge: true
                config:
                  idp:
                    metadata_file: '/etc/cyb3rhq-indexer/opensearch-security/metadata_onelogin.xml'
                    entity_id: 'https://app.onelogin.com/saml/metadata/xxxxxxx'
                  sp:
                    entity_id: cyb3rhq-saml
                  kibana_url: https://<CYB3RHQ_DASHBOARD_URL>
                  roles_key: Roles
                  exchange_key: 'b1d6dd32753374557dcf92e241......'
              authentication_backend:
                type: noop
      ...

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
   
Cyb3rhq dashboard configuration
-----------------------------

#. Create a new role mapping for the backend role. Follow these steps to create a new role mapping, and grant read-only permissions to the backend role.

   #. Log into the Cyb3rhq dashboard as administrator.
   #. Click the upper-left menu icon **☰** to open the options, go to **Indexer management** > **Security**, and then **Roles** to open the roles page.
   #. Click **Create role**, complete the empty fields with the following parameters, and then click **Create** to complete the task.

      - **Name**: Assign a name to the role.
      - **Cluster permissions**: ``cluster_composite_ops_ro``
      - **Index**: ``*``
      - **Index permissions**: ``read``
      - **Tenant permissions**: Select ``global_tenant`` and the ``Read only`` option.
   #. Select the newly created role.
   #. Select the **Mapped users** tab and click **Manage mapping**.
   #. Under **Backend roles**, add the value of the **Department** field in OneLogin configuration and click **Map** to confirm the action. In our case, the backend role is ``cyb3rhq-readonly``.
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
      - **Value**: Assign the value of the **Department** field in OneLogin configuration. In our case, this is ``cyb3rhq-readonly``.

      .. thumbnail:: /images/single-sign-on/onelogin/read-only/Cyb3rhq-role-mapping-RO.png
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

#. Restart the Cyb3rhq dashboard service.

   .. include:: /_templates/common/restart_dashboard.rst

#. Test the configuration. Go to your Cyb3rhq dashboard URL and log in with your OneLogin account.
