.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Okta Inc. provides technologies that enable secure user authentication into applications. Learn more about it and the administrator role in this section of the Cyb3rhq documentation.

Okta
====

`Okta Inc. <https://www.okta.com/>`_ is an identity and access management company that provides technologies that enable secure user authentication into applications. In this guide, we integrate the Okta IdP to authenticate users into the Cyb3rhq platform.

There are three stages in the single sign-on integration.

#. `Okta Configuration`_
#. `Cyb3rhq indexer configuration`_
#. `Cyb3rhq dashboard configuration`_

Okta Configuration
------------------

#. Create an account on Okta. Request a free trial if you don't have a paid license.

#. Create a new user. 

   #. From your okta admin console page, navigate to **Directory** > **People**.   

      .. thumbnail:: /images/single-sign-on/okta/01-navigate-to-directory-people.png
          :title: Navigate to Directory - People
          :align: center
          :width: 80%
     
   #. From the **People** section, select **Add Person**, fill in the details of the new user, and click **Save** as seen in the following screenshots.

      .. thumbnail:: /images/single-sign-on/okta/02-select-add-person.png
          :title: Select add person
          :align: center
          :width: 80%
     
      .. thumbnail:: /images/single-sign-on/okta/03-click-save.png
          :title: Click save
          :align: center
          :width: 80%
         
#. Create a new group. Navigate to **Directory** > **Groups** and add a group.
   
     .. thumbnail:: /images/single-sign-on/okta/04-navigate-to-directory-groups.png
        :title: Navigate to directory groups
        :align: center
        :width: 80%    
 
    Create a new group using any name. In our case, we name it ``cyb3rhq-admins``. This name will be used as our ``backend_roles`` in ``roles_mapping.yml``.

#. Add the new user to the new group. Navigate to **Directory** > **Groups**  and select your group. Click on **Assign People** and add the user to the group created.


     .. thumbnail:: /images/single-sign-on/okta/05-navigate-to-directory-groups.png
        :title: Navigate to Directory - Groups - <YOUR_GROUP>
        :align: center
        :width: 80%   

#. Create a new app. Configure the SAML settings while you create the app.
   
   #. Navigate to the **Applications** section in Okta. Select **Create App Integration**.

      .. thumbnail:: /images/single-sign-on/okta/06-navigate-to-applications-section.png
         :title: Navigate to the Applications section in Okta
         :align: center
         :width: 80%   

   #. In the **Create a new application integration** window, select **SAML 2.0** and click **Next**.

      .. thumbnail:: /images/single-sign-on/okta/07-create-new-application.png
         :title: Create a new application integration
         :align: center
         :width: 80%   

   #. Assign a name to the application and click on **Next**. In our case, we assign the name ``cyb3rhq-sso-app``.

      .. thumbnail:: /images/single-sign-on/okta/08-assign-name.png
         :title: Assign a name to the application
         :align: center
         :width: 80%   
     
   #. In the **Configure SAML** menu, you’ll find the **SAML Settings** section, modify the following parameters:
   
      - **Single sign on URL**: input ``https://<CYB3RHQ_DASHBOARD_URL>/_opendistro/_security/saml/acs`` and replace the ``<CYB3RHQ_DASHBOARD_URL>`` field with the corresponding URL.
      - **Audience URI (SP Entity ID)**: input ``cyb3rhq-saml``. This is the ``SP Entity ID`` value which will be used later in the ``config.yml`` on the Cyb3rhq indexer instance.
      - **Other Requestable SSO URLs**: click on **Show Advanced Settings** to access this option. Input ``https://<CYB3RHQ_DASHBOARD_URL>/_opendistro/_security/saml/acs/idpinitiated`` and replace the ``<CYB3RHQ_DASHBOARD_URL>`` field with the corresponding URL.

      You can leave the rest of the values as default.

      .. thumbnail:: /images/single-sign-on/okta/09-saml-settings-section.png
         :title: SAML settings section
         :align: center
         :width: 80%

      .. thumbnail:: /images/single-sign-on/okta/09b-other-requestable-sso-urls.png
         :title: Other Requestable SSO URLs
         :align: center
         :width: 80%

   #. In the **Group Attribute Statements** section put ``Roles`` as the name. The value for ``Roles`` will be used as the ``roles_key`` parameter in the Cyb3rhq indexer configuration. For the filter field, select **Matches regex** and type ``.*``. 

      .. thumbnail:: /images/single-sign-on/okta/10-group-attribute-statements-section.png
         :title: Group Attribute Statements section
         :align: center
         :width: 80%   

   #. Proceed by clicking next and on the feedback page, select the options seen in the screenshot below. Click on **Finish** and proceed to the next step.

      .. thumbnail:: /images/single-sign-on/okta/11-click-on-finish.png
         :title: Click on Finish and proceed to the next step
         :align: center
         :width: 80%   

#. Add the new app to the new group. Navigate to **Directory** > **Groups**  and select your group. Click on **Applications** and select **Assign Applications**. From here, assign the app created in step 5 and click on **Done** to save the changes.
   
   .. thumbnail:: /images/single-sign-on/okta/12-navigate-to-directory-groups.png
      :title: Navigate to Directory - Groups - <YOUR_GROUP>
      :align: center
      :width: 80%   

   .. thumbnail:: /images/single-sign-on/okta/13-select-assign-applications.png
      :title: Select Assign Applications
      :align: center
      :width: 80%

#. Note the necessary parameters from the SAML settings of the new app. The parameters already obtained during the integration are:

   - ``sp.entity_id``: ``cyb3rhq-saml``
   - ``roles_key``: ``Roles``
   - ``kibana_url``: ``https://<CYB3RHQ_DASHBOARD_URL>``

   To obtain the remaining parameters, navigate to **Applications** > **Applications**, select your app and click **Sign On**. 

   Under **SAML Signing Certificates**, select **View IdP metadata** of the active certificate. This will open in a new tab. Copy the URL as this will be the ``idp.metadata_url``.

   Now, on the same page, click on  **View SAML setup instructions**. Copy the **Identity Provider Issuer URL**, it will be the ``idp.entity_id``.

   Copy the blob of the **X.509 Certificate** excluding the ``-----BEGIN CERTIFICATE-----`` and ``-----END CERTIFICATE-----`` lines. This will be used as the ``exchange_key``:

     .. thumbnail:: /images/single-sign-on/okta/14-navigate-to-applications.png
        :title: Navigate to Applications - Applications - <YOUR_APP> - Sign On
        :align: center
        :width: 80%

   This information can also be found in the metadata XML file.

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
                    metadata_url: 'https://....okta.com/app/..../sso/saml/metadata'
                    entity_id: 'http://www.okta.com/....'
                  sp:
                    entity_id: cyb3rhq-saml
                  kibana_url: https://<CYB3RHQ_DASHBOARD_URL>
                  roles_key: Roles
                  exchange_key: 'b1d6dd32753374557dcf92e241.........'
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

   Configure the ``roles_mapping.yml`` file to map the Okta group to the appropriate Cyb3rhq indexer role. In our case, we map it to the  ``all_access`` role:

      .. code-block:: console
         :emphasize-lines: 6

         all_access:
           reserved: false
           hidden: false
           backend_roles:
           - "admin"
           - "<GROUP_NAME>"

   Replace ``<GROUP_NAME>`` with the name you gave to your group in Step 3. In our case, this is ``cyb3rhq-admins``.

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
      - **Value**: Assign the name you gave to your group in Step 3 of Okta configuration, in our case, this is ``cyb3rhq-admins``. 

      .. thumbnail:: /images/single-sign-on/okta/Cyb3rhq-role-mapping.png
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

#. Test the configuration. Go to your Cyb3rhq dashboard URL and log in with your Okta account. 


