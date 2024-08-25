.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: LDAP can handle both authentication and authorization of users accessing the Cyb3rhq dashboard. Find out how to integrate LDAP with the Cyb3rhq platform in this section of the documentation.
  
LDAP integration
================

Lightweight Directory Access Protocol (LDAP) is often used for centralizing user authentication and authorization data. It is also used to store structured data such as employee records, contact information, and more. LDAP can handle both authentication and authorization of users accessing the Cyb3rhq dashboard.

Authentication is the process of verifying the identity of users or systems to ensure that they provide valid credentials, such as username and password. Authorization, on the other hand, is granting access to a user or system based on their identity. It retrieves the backend roles for the user and determines what actions they are allowed to perform on the Cyb3rhq dashboard. 

In this section, we outline the required configuration to integrate LDAP with the Cyb3rhq platform. The guide assumes you already have an LDAP server or Microsoft Active Directory. 

.. topic:: Required parameters

   The following parameters are required to make the configurations on the Cyb3rhq indexer instance:

   -  ``hosts``: This is your LDAP server and its port (by default it is 389 for LDAP and 636 for LDAP over SSL).
   -  ``bind_dn``: The credential to authenticate to your LDAP server.
   -  ``password``: The password to authenticate to your LDAP server.
   -  ``enable_ssl``: Specifies whether to use LDAP over SSL (LDAPS). This can be set to true or false. 
   -  ``pemtrustedcas_filepath``: The absolute path to the Privacy Enhanced Mail (PEM) file containing the root Certificate Authority (CA) of your Active Directory/LDAP server. This is required when ``enable_ssl`` is set to true.
   - ``userbase``: Specifies the subtree in the directory where user information is stored.
   -  ``usersearch``: The actual LDAP query that the Security plugin executes when trying to authenticate a user. 
   -  ``username_attribute``: The Security plugin uses this attribute of the directory entry to look for the user name. If set to null, the Distinguished Name (DN) is used (default).
   -  ``rolebase``: Specifies the subtree in the directory where role/group information is stored.
   -  ``rolesearch``: The actual LDAP query that the Security plugin executes when trying to determine the roles of a user.
   -  ``userrolename``: If the roles/groups of a user are not stored in the groups subtree, but as an attribute of the user’s directory entry, define this attribute name here.
   - ``rolename``: The attribute of the role entry that should be used as the role name.
   -  ``skip_users``: Array of users that should be skipped when retrieving roles. Wildcards and regular expressions are supported.

   .. note::

      -  The LDAP attribute types such as Common Name (CN), Organizational Unit (OU), Distinguished Name (DN), and Domain Component (DC) used in this integration are from a test LDAP server. Replace them with the corresponding values from your LDAP server.
      -  It is recommended to clear the browser cache and cookies before the integration is carried out.
      -  The ``securityadmin`` script has to be executed with root user privileges.
      -  You need an account with administrator privileges on the Cyb3rhq dashboard.

LDAP server configuration
-------------------------

Depending on your LDAP server configuration, you need to create users and groups or use existing ones. You also have to obtain some information from your AD/LDAP server:

-  Create an OU for the Users (or use an already created OU). Get the DN of the OU, in our example: ``ou=people,dc=example,dc=org``.
-  Create an OU for the Group(s) (or use an already created OU). Get the DN of the OU, in our example: ``ou=Groups,dc=example,dc=org``.
-  Create a user with sufficient privileges to bind to the service. Get the DN of the user, in our example, this is ``cn=admin,dc=example,dc=org``.
-  Create a group where the users with access to Cyb3rhq will be placed, in our example this is the ``Administrator`` and ``readonly`` groups. 
-  Get the FQDN of the LDAP server or Domain Controller.

Authentication and authorization configuration
----------------------------------------------

The ``auhtc`` section of the Cyb3rhq indexer security configuration file handles authentication, while the ``authz`` section handles authorization. We recommend that you back up the ``/etc/cyb3rhq-indexer/opensearch-security/config.yml`` file before you carry out this configuration.

#. Save the LDAP server certificate. If you don’t have access to the root CA file of the LDAP server, run the following command on the Cyb3rhq indexer node to retrieve the certificate. Replace ``<FQDN_LDAP_SERVER>`` with the Fully Qualified Domain Name of your LDAP server:

   .. code-block:: console

      $ echo -n | openssl s_client -connect <FQDN_LDAP_SERVER>:636 | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > ldapcacert.pem

   The command copies everything between ``-----BEGIN CERTIFICATE-----`` and ``-----END CERTIFICATE-----`` (including these delimiters) and saves it in a new text file.

#. Place the certificate file within the ``/etc/cyb3rhq-indexer/opensearch-security/`` directory. Set the file ownership to ``cyb3rhq-indexer`` using the following command:


   .. code-block:: console

      chown cyb3rhq-indexer:cyb3rhq-indexer /etc/cyb3rhq-indexer/opensearch-security/ldapcacert.pem

#. Edit the ``/etc/cyb3rhq-indexer/opensearch-security/config.yml`` file and change the appropriate values.

   -  Under the ``authc`` section, modify the ``LDAP`` configuration. Your configuration should be similar to this:

      .. code-block:: yaml
         :emphasize-lines: 13, 14, 18-24

         authc:
           ldap:
             description: "Authenticate via LDAP or Active Directory"
             http_enabled: true
             transport_enabled: false
             order: 5
             http_authenticator:
               type: basic
               challenge: false
             authentication_backend:
               type: ldap
               config:
                 enable_ssl: true #Set to true if LDAPS is enabled, otherwise set to false.
                 pemtrustedcas_filepath: /etc/cyb3rhq-indexer/opensearch-security/ldapcacert.pem #Required when enable_ssl is set to true
                 enable_start_tls: false
                 enable_ssl_client_auth: false
                 verify_hostnames: true
                 hosts:
                 - <FQDN_LDAP_SERVER>:636 #Port 389 for LDAP, 636 for LDAPS
                 bind_dn: cn=admin,dc=example,dc=org
                 password: <PASSWORD>
                 userbase: 'ou=people,dc=example,dc=org'
                 usersearch: (cn={0})  #Depending on your LDAP schema this can be CN, sAMAccountName, etc
                 username_attribute: cn

   -  Under the ``authz`` section, modify the ``LDAP`` configuration. Your configuration should be similar to this:

      .. code-block:: yaml
         :emphasize-lines: 9, 10, 14-27

         authz:
           roles_from_myldap:
             description: "Authorize via LDAP or Active Directory"
             http_enabled: true
             transport_enabled: true
             authorization_backend:
               type: ldap
               config:
                 enable_ssl: true #Set to true if LDAPS is enabled, otherwise set to false.
                 pemtrustedcas_filepath: /etc/cyb3rhq-indexer/opensearch-security/ldapcacert.pem #Required when enable_ssl is set to true
                 enable_start_tls: false
                 enable_ssl_client_auth: false
                 verify_hostnames: true
                 hosts:
                 - <FQDN_LDAP_SERVER>:636 #Port 389 for LDAP, 636 for LDAPS
                 bind_dn: cn=admin,dc=example,dc=org
                 password: <PASSWORD>
                 userbase: 'ou=people,dc=example,dc=org'
                 usersearch: (cn={0}) #Depending on your LDAP schema this can be cn, sAMAccountName, etc
                 username_attribute: cn
                 rolebase: ou=Groups,dc=example,dc=org #This is the subtree in the directory that contains the role/group
                 rolesearch: '(member={0})' #Depending on your LDAP schema this can be member, memberOf, etc
                 userrolename: memberof
                 rolename: cn
                 skip_users:
                   - admin
                   - kibanaserver

   Change the following parameters to their corresponding value:

   -  ``pemtrustedcas_filepath``
   -  ``hosts``
   -  ``bind_dn``
   -  ``password``
   -  ``userbase``
   -  ``usersearch``
   -  ``username_attribute``
   -  ``rolebase``
   -  ``rolesearch``
   -  ``userrolename``
   -  ``rolename``

#. Run the ``securityadmin`` script to load the configuration changes made in the ``config.yml`` file.

   .. code-block:: console

      # export JAVA_HOME=/usr/share/cyb3rhq-indexer/jdk/ && bash /usr/share/cyb3rhq-indexer/plugins/opensearch-security/tools/securityadmin.sh -f /etc/cyb3rhq-indexer/opensearch-security/config.yml -icl -key /etc/cyb3rhq-indexer/certs/admin-key.pem -cert /etc/cyb3rhq-indexer/certs/admin.pem -cacert /etc/cyb3rhq-indexer/certs/root-ca.pem -h 127.0.0.1 -nhnv

   The ``-h`` flag specifies the hostname or the IP address of the Cyb3rhq indexer node. Note that this command uses 127.0.0.1, set your Cyb3rhq indexer address if necessary.

   The command output must be similar to the following:

   .. code-block:: output

      Security Admin v7
      Will connect to 127.0.0.1:9200 ... done
      Connected as "CN=admin,OU=Cyb3rhq,O=Cyb3rhq,L=California,C=US"
      OpenSearch Version: 2.6.0
      Contacting opensearch cluster 'opensearch' and wait for YELLOW clusterstate ...
      Clustername: cyb3rhq-cluster
      Clusterstate: YELLOW
      Number of nodes: 1
      Number of data nodes: 1
      .opendistro_security index already exists, so we do not need to create one.
      Populate config from /home/cyb3rhq
      Will update '/config' with /etc/cyb3rhq-indexer/opensearch-security/config.yml 
         SUCC: Configuration for 'config' created or updated
      SUCC: Expected 1 config types for node {"updated_config_types":["config"],"updated_config_size":1,"message":null} is 1 (["config"]) due to: null
      Done with success

Map LDAP role to Cyb3rhq dashboard
--------------------------------

LDAP can be used for authorization by retrieving the backend roles associated with a user. This backend role can be used to determine the access privileges of a user on the Cyb3rhq dashboard. In this section, we map the LDAP roles to the administrator and read-only roles on the Cyb3rhq dashboard.

.. contents::
   :local:
   :depth: 1
   :backlinks: none

Setup administrator role
^^^^^^^^^^^^^^^^^^^^^^^^

Follow these steps to create a new role mapping and grant administrator permissions to the backend role.

#. Configure the ``roles_mapping.yml`` file to map the role (CN) we have in our LDAP server to the appropriate Cyb3rhq indexer role. In our case, we map users in the ``Administrator`` group in LDAP to the ``all_access`` role on Cyb3rhq indexer.

   Edit the ``/etc/cyb3rhq-indexer/opensearch-security/roles_mapping.yml`` file and change the following values:

   .. code-block:: yaml
      :emphasize-lines: 6

      all_access:
        reserved: false
        hidden: false
        backend_roles:
        - "admin"
        - "Administrator"
        description: "Maps admin to all_access"

#. Run the ``securityadmin`` script to load the configuration changes made in the ``roles_mapping.yml`` file:

   .. code-block:: console

      # export JAVA_HOME=/usr/share/cyb3rhq-indexer/jdk/ && bash /usr/share/cyb3rhq-indexer/plugins/opensearch-security/tools/securityadmin.sh -f /etc/cyb3rhq-indexer/opensearch-security/roles_mapping.yml -icl -key /etc/cyb3rhq-indexer/certs/admin-key.pem -cert /etc/cyb3rhq-indexer/certs/admin.pem -cacert /etc/cyb3rhq-indexer/certs/root-ca.pem -h 127.0.0.1 -nhnv

   The ``-h`` flag specifies the hostname or the IP address of the Cyb3rhq indexer node. Note that this command uses 127.0.0.1, set your Cyb3rhq indexer address if necessary.

   The command output must be similar to the following:

   .. code-block:: output

      Security Admin v7
      Will connect to 127.0.0.1:9200 ... done
      Connected as "CN=admin,OU=Cyb3rhq,O=Cyb3rhq,L=California,C=US"
      OpenSearch Version: 2.6.0
      Contacting opensearch cluster 'opensearch' and wait for YELLOW clusterstate ...
      Clustername: cyb3rhq-cluster
      Clusterstate: GREEN
      Number of nodes: 1
      Number of data nodes: 1
      .opendistro_security index already exists, so we do not need to create one.
      Populate config from /etc/cyb3rhq-indexer/opensearch-security
      Will update '/rolesmapping' with /etc/cyb3rhq-indexer/opensearch-security/roles_mapping.yml 
         SUCC: Configuration for 'rolesmapping' created or updated
      Done with success
      SUCC: Expected 1 config types for node {"updated_config_types":["rolesmapping"],"updated_config_size":1,"message":null} is 1 (["rolesmapping"]) due to: null

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

      .. thumbnail:: /images/manual/user-administration/ldap/select-roles-mapping.gif
         :title: Roles mapping selection
         :alt: Roles mapping selection
         :align: center
         :width: 80%

   #. Click **Create Role mapping** and complete the empty fields with the following parameters:

      -  **Role mapping name**: Assign a name to the role mapping.
      -  **Roles**: Select ``administrator``.
      -  **Custom rules**: Click **Add new rule** to expand this field.
      -  **User field**: ``backend_roles``.
      -  **Search operation**: ``FIND``.
      -  **Value**: Assign the name of your backend role in your LDAP server. In our case, this is a group named ``Administrator`` which contains users with  administrator roles

      .. thumbnail:: /images/manual/user-administration/ldap/create-administrator-new-role-mapping.png
         :title: Create administrator new role mapping
         :alt: Create administrator new role mapping
         :align: center
         :width: 80%

   #. Click **Save role mapping** to save and map the backend role with Cyb3rhq as administrator.

#. Restart the Cyb3rhq dashboard service using this command:

   .. code-block:: console

      # systemctl restart cyb3rhq-dashboard

#. Test the configuration. To test the configuration, go to your Cyb3rhq dashboard URL and log in with your LDAP details.

Setup read-only role
^^^^^^^^^^^^^^^^^^^^

#. Follow these steps to create a new role mapping and grant read-only permissions to the backend role.

   #. Log into the Cyb3rhq dashboard as administrator.
   #. Click the upper-left menu icon **☰** to open the options, go to **Indexer management** > **Security**, and then **Roles** to open the roles page.
   #. Click **Create role**, complete the empty fields with the following parameters, and then click **Create** to complete the task.

      -  **Name**: Assign a name to the role.
      -  **Cluster permissions**: **cluster_composite_ops_ro**
      -  **Index**: **\***
      -  **Index permissions**: **read**
      -  **Tenant permissions**: **global_tenant** and select the **Read only** option.
   #. Select the newly created role.
   #. Select the **Mapped users** tab and click **Manage mapping**.
   #. Under **Backend roles**, assign the name of the read-only role you have in your LDAP server and click on  **Map** to confirm the action. In our case, the backend role (CN) is ``readonly``.

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

   #. Click the upper-left menu icon **☰** to open the menu on the Cyb3rhq dashboard, go to **Server management** > **Security**, and then **Roles mapping** to open the page.

      .. thumbnail:: /images/manual/user-administration/ldap/select-roles-mapping.gif
         :title: Roles mapping selection
         :alt: Roles mapping selection
         :align: center
         :width: 80%

   #. Click **Create Role mapping** and complete the empty fields with the following parameters:

      -  **Role mapping name**: Assign a name to the role mapping.
      -  **Roles**: Select ``readonly``.
      -  **Custom rules**: Click **Add new rule** to expand this field.
      -  **User field**: ``backend_roles``.
      -  **Search operation**: ``FIND``.
      -  **Value**: Assign the name of your backend role in your LDAP server. In our case, this is a group named ``readonly`` which contains users with read only roles.


      .. thumbnail:: /images/manual/user-administration/ldap/create-readonly-new-role-mapping.png
         :title: Create readonly new role mapping
         :alt: Create readonly new role mapping
         :align: center
         :width: 80%
   
   #. Click **Save role mapping** to save and map the backend role with Cyb3rhq as *read-only*.

#. Restart the Cyb3rhq dashboard service using this command:

   .. code-block:: console

      # systemctl restart cyb3rhq-dashboard

#. Test the configuration. To test the configuration, go to your Cyb3rhq dashboard URL and log in with your LDAP details.
