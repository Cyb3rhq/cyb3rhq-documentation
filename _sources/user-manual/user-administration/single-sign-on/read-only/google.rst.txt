.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Google Workspace is a collection of cloud computing, productivity and collaboration tools. Learn more about it and the read-only role in this section of the Cyb3rhq documentation.

Google
======

`Google Workspace <https://workspace.google.com/>`_, developed and marketed by Google, is a collection of cloud computing, productivity, and collaboration tools.  In this guide, we integrate Google IdP to authenticate users into the Cyb3rhq platform. 

There are three stages in the single sign-on integration.

#. `Google Configuration`_
#. `Cyb3rhq indexer configuration`_
#. `Cyb3rhq dashboard configuration`_

Google Configuration
--------------------

#. Create an account in Google Workspace. A Google Workspace account is required for this configuration. Request a free trial if you don't have a paid license.

#. Go to https://admin.google.com/ac/apps/unified and sign in with your Google Admin account.
#. Create an app with **Add custom SAML app**.

   #. Go to **Apps** > **Web and mobile apps** > **Add App**, then **Add custom SAML app**. Enter an **App name** and click **CONTINUE**.

      .. thumbnail:: /images/single-sign-on/google/01-go-to-apps.png
         :title: Go to Apps > Website and mobile apps
         :align: center
         :width: 80%

   #. Take note of the following parameters, as they will be used during the Cyb3rhq indexer configuration:

      -  **Entity ID**: This will be used later as the ``idp.entity_id``.
      -  Select **DOWNLOAD METADATA** and place the metadata file in the ``configuration`` directory of the Cyb3rhq indexer. The path to the directory is ``/etc/cyb3rhq-indexer/opensearch-security/``.

      .. thumbnail:: /images/single-sign-on/google/02-take-note-of-the-parameters.png
         :title: Take note of the parameters
         :align: center
         :width: 80%

   #. Select **CONTINUE** and configure the following:

      -  **ACS URL**: ``https://<CYB3RHQ_DASHBOARD_URL>/_opendistro/_security/saml/acs``. Replace the Cyb3rhq dashboard URL field with the appropriate URL or IP address.
      -  **Entity ID**: Use any name here. This will be the ``sp.entity_id`` in the Cyb3rhq indexer configuration file. In our case, the value is ``cyb3rhq-saml``.

      .. thumbnail:: /images/single-sign-on/google/03-select-continue-and-configure.png
         :title: Select CONTINUE and configure
         :align: center
         :width: 80%

   #. Leave the remaining parameters with their default values, then select **CONTINUE**.

   #. Click on **ADD MAPPING**. Under Employee details, choose **Department** and under App attributes, type **Roles**. Click **FINISH**. 

      Google doesn't support sending the Group membership attribute as part of the SAML Assertion (as the other Identity Providers do). So in this example, we are going to use **Department** as the attribute whose value will be used as our ``roles_key`` in the Cyb3rhq indexer configuration. In this case, the value for the **Department** attribute will be stored as ``Roles``.

      .. thumbnail:: /images/single-sign-on/google/04-click-on-add-mapping.png
         :title: Click on ADD MAPPING under Employee details
         :align: center
         :width: 80%

#. Turn ON access for everyone.

   #. Select the recently created app and click on **User access**.

      .. thumbnail:: /images/single-sign-on/google/05-turn-on-access-for-everyone.png
         :title: Turn ON access for everyone
         :align: center
         :width: 80%

   #. Select **ON for everyone** and click **SAVE**.

      .. thumbnail:: /images/single-sign-on/google/06-select-on-for-everyone.png
         :title: Select ON for everyone and click SAVE
         :align: center
         :width: 80%

#. Define the attribute for users.

   #. Go to **Directory** then **Users**.

      .. thumbnail:: /images/single-sign-on/google/07-define-the-attribute-for-users.png
         :title: Define the attribute for users
         :align: center
         :width: 80%

   #. Select a user,  go to **User information**, then edit **Employee information**.

      .. thumbnail:: /images/single-sign-on/google/08-select-a-user.png
         :title: Select a user
         :align: center
         :width: 80%

      .. thumbnail:: /images/single-sign-on/google/09-edit-employee-information.png
         :title: Edit Employee information
         :align: center
         :width: 80%

   #. Add a value to the **Department** field, in this example, we add ``cyb3rhq-readonly``, click on **SAVE**. This value will be used as the backend role in the Cyb3rhq dashboard configuration.

      .. thumbnail:: /images/single-sign-on/google/read-only/10-add-a-value-to-the-department-field-RO.png
        :title:  Add a value to the Department field
        :align: center
        :width: 80%


Cyb3rhq indexer configuration
---------------------------

Edit the Cyb3rhq indexer security configuration files. We recommend that you back up these files before you carry out the configuration.

#. Generate a 64-character long random key using the following command.

   .. code-block:: console

      openssl rand -hex 32

   The output will be used as the ``exchange_key`` in the ``/etc/cyb3rhq-indexer/opensearch-security/config.yml`` file. 

#. Place the ``Google_Metadata.xml`` file within the ``/etc/cyb3rhq-indexer/opensearch-security/`` directory. Set the file ownership to ``cyb3rhq-indexer`` using the following command:

   .. code-block:: console

      # chown cyb3rhq-indexer:cyb3rhq-indexer /etc/cyb3rhq-indexer/opensearch-security/Google_Metadata.xml

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
                    metadata_file: '/etc/cyb3rhq-indexer/opensearch-security/Google_Metadata.xml'
                    entity_id: 'https://accounts.google.com/o/saml2?idpid=C02…'
                  sp:
                    entity_id: cyb3rhq-saml
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
   #. Under **Backend roles**, add the value of the **Department** field you created in Google Workspace and click **Map** to confirm the action. In our case, the backend role is ``cyb3rhq-readonly``.
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
      - **Value**: Assign the value of the **Department** field you created in Google Workspace. In our case, the backend role is ``cyb3rhq-readonly``.

      .. thumbnail:: /images/single-sign-on/google/read-only/Cyb3rhq-role-mapping-RO.png
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

#. Test the configuration. Go to your Cyb3rhq dashboard URL and log in with your Google Workspace account. 
