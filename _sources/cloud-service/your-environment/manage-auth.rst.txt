.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Learn how to manage access to your Cyb3rhq WUI: authentication and authorization, how to create and set a Cyb3rhq admin user, and more. 

.. _cloud_your_environment_manage_wui_access:

Authentication and authorization
================================

You can use the native support for managing and authenticating users or integrate with external user management systems.

   .. note::
      
      You cannot log in to the Cyb3rhq WUI of your environment with your Cyb3rhq Cloud account credentials. To log in to Cyb3rhq WUI, use the default credentials from the Cyb3rhq Cloud Console page or the credentials of any user you already created in Cyb3rhq WUI.
  

Native support for users and roles
----------------------------------

The Cyb3rhq WUI allows you to add users, create roles, and map roles to users. The following sections highlight more on this.

- `Creating an internal user and mapping it to Cyb3rhq`_
- `Creating and setting a Cyb3rhq admin user`_
- `Creating and setting a Cyb3rhq read-only user`_


Creating an internal user and mapping it to Cyb3rhq
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Follow these steps to create an internal user and map it to its appropriate role.

#. Log into your :ref:`Cyb3rhq dashboard <cloud_wui_access>` as administrator.

#. Click the upper-left menu icon **☰** to open the options, go to **Indexer management** > **Security**, and then **Internal users** to open the internal users' page.

#. Click **Create internal user**, complete the empty fields with the requested information, and click **Create** to complete the action.

#. Follow these steps to map the user to the appropriate role:
   
   #. Click the upper-left menu icon **☰** to open the options, go to **Indexer management** > **Security**, select **Roles** to open the page, and click the role name selected to open the window.
   #. Select the **Mapped users** tab and click **Manage mapping**.
   #. Add the user you created in the previous steps and click **Map** to confirm the action.

#. Follow these steps to map the user with Cyb3rhq:
   
   #. Click the upper-left menu icon **☰** to open the options, go to **Server management** > **Security**, and then **Roles mapping** to open the page.
   #. Click **Create Role mapping** and complete the empty fields with the following parameters:
   
      - **Role mapping name**: Assign a name to the role mapping.
      - **Roles**: Select the Cyb3rhq roles that you want to map the user with.
      - **Internal users**: Select the internal user created previously.
  
   #. Click **Save role mapping** to save and map the user with Cyb3rhq.


Creating and setting a Cyb3rhq admin user
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Follow these steps to create an internal user, create a new role mapping, and give administrator permissions to the user.

#. Log into your :ref:`Cyb3rhq dashboard <cloud_wui_access>` as administrator.

#. Click the upper-left menu icon **☰** to open the options, go to **Indexer management** > **Security**, and then **Internal users** to open the internal users' page.

#. Click **Create internal user**, complete the empty fields with the requested information, and click **Create** to complete the action.

#. Follow these steps to map the user to the appropriate role:

   #. Click the upper-left menu icon **☰** to open the options, go to **Indexer management** > **Security**, and then **Roles** to open the roles page.

   #. Search for the **all_access** role in the roles list and select it.

   #. Click **Actions** and select **Duplicate**.

   #. Assign a name to the new role, then click **Create** to confirm the action.

   #. On the newly created role page, select the **Mapped users** tab and click **Manage mapping**.
   
   #. Add the user you created in the previous steps and click **Map** to confirm the action.

   .. note:: Reserved roles are restricted for any permission customizations. You can create a custom role with the same permissions or duplicate a reserved role for further customization.   

#. Follow these steps to map the user with Cyb3rhq:
   
   #. Click the upper-left menu icon **☰** to open the options, go to **Server management** > **Security**, and then **Roles mapping** to open the page.
   #. Click **Create Role mapping** and complete the empty fields with the following parameters:
   
      - **Role mapping name**: Assign a name to the role mapping.
      - **Roles**: Select ``administrator``.
      - **Internal users**: Select the internal user created previously.
  
   #. Click **Save role mapping** to save and map the user with Cyb3rhq as *administrator*. 



Creating and setting a Cyb3rhq read-only user
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Follow these steps to create an internal user, create a new role mapping, and give read-only permissions to the user.

#. Log into your :ref:`WUI <cloud_wui_access>` as administrator.

#. Click the upper-left menu icon **☰** to open the options, go to **Indexer management** > **Security**, and then **Internal users** to open the internal users' page.

#. Click **Create internal user**, complete the empty fields with the requested information, and click **Create** to complete the action.

#. Follow these steps to map the user to the appropriate role:

   #. Click the upper-left menu icon **☰** to open the options, go to **Indexer management** > **Security**, and then **Roles** to open the roles page.

   #. Click **Create role**, complete the empty fields with the following parameters, and then click **Create** to complete the task. 
     
      - **Name**: Assign a name to the role.
       
      - **Cluster permissions**: ``cluster_composite_ops_ro``

      - **Index**: ``*``

      - **Index permissions**: ``read``

      - **Tenant permissions**: ``global_tenant`` and select the **Read only** option.

   #. Select the **Mapped users** tab and click **Manage mapping**.
   
   #. Add the user you created in the previous steps and click **Map** to confirm the action.   

#. Follow these steps to map the user with Cyb3rhq:

   #. Click the upper-left menu icon **☰** to open the options, go to **Server management** > **Security**, and then **Roles mapping** to open the page.

   #. Click **Create Role mapping** and complete the empty fields with the following parameters:

      - **Role mapping name**: Assign a name to the role mapping.
      - **Roles**: Select ``readonly``.
      - **Internal users**: Select the internal user created previously.

   #. Click **Save role mapping** to save and map the user with Cyb3rhq as *read-only*. 

To add more read-only users, you can skip the role creation task and map the users to the already existing read-only role.


Integrating with external user management systems
-------------------------------------------------

You can configure Cyb3rhq to communicate with an external user management system such as LDAP to authenticate users. Open a support ticket through the **Help** section on your Cyb3rhq Cloud Console to perform this integration.
