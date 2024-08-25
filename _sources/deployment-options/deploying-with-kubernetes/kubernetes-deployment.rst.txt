.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Learn more about Kubernetes deployment with Cyb3rhq in this section of the Cyb3rhq documentation. 

Deployment
==========

Clone this repository to deploy the necessary services and pods.

    .. code-block:: console

        $ git clone https://github.com/cyb3rhq/cyb3rhq-kubernetes.git -b v|CYB3RHQ_CURRENT_KUBERNETES| --depth=1
        $ cd cyb3rhq-kubernetes

.. _kubernetes_ssl_certificates:

Setup SSL certificates
^^^^^^^^^^^^^^^^^^^^^^

You can generate self-signed certificates for the Cyb3rhq indexer cluster using the script at ``cyb3rhq/certs/indexer_cluster/generate_certs.sh`` or provide your own.

You can generate self-signed certificates for the Cyb3rhq dashboard cluster using the script at ``cyb3rhq/certs/dashboard_http/generate_certs.sh`` or provide your own.

The required certificates are imported via secretGenerator on the ``kustomization.yml`` file:


    .. code-block:: yaml

        secretGenerator:
            - name: indexer-certs
              files:
                - certs/indexer_cluster/root-ca.pem
                - certs/indexer_cluster/node.pem
                - certs/indexer_cluster/node-key.pem
                - certs/indexer_cluster/dashboard.pem
                - certs/indexer_cluster/dashboard-key.pem
                - certs/indexer_cluster/admin.pem
                - certs/indexer_cluster/admin-key.pem
                - certs/indexer_cluster/filebeat.pem
                - certs/indexer_cluster/filebeat-key.pem
            - name: dashboard-certs
              files:
                - certs/dashboard_http/cert.pem
                - certs/dashboard_http/key.pem
                - certs/indexer_cluster/root-ca.pem


Setup storage class (optional for non-EKS cluster)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Depending on the type of cluster you’re running, the Storage Class may have a different provisioner.

You can check yours by running ``kubectl get sc``. You will see something like this:

   .. code-block:: console

        $ kubectl get sc
        NAME                          PROVISIONER            RECLAIMPOLICY   VOLUMEBINDINGMODE   ALLOWVOLUMEEXPANSION   AGE
        elk-gp2                       microk8s.io/hostpath   Delete          Immediate           false                  67d
        microk8s-hostpath (default)   microk8s.io/hostpath   Delete          Immediate           false                  54d

 
The provisioner column displays microk8s.io/hostpath, you must edit the file ``envs/local-env/storage-class.yaml`` and set up this provisioner.


Apply all manifests using kustomize
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are two variants of the manifest: ``eks`` and ``local-env``. The eks manifest should be used if you are using the EKS cluster, while the local-env manifest should be used for other cluster types.

It is possible to adjust resources for the cluster by editing patches on ``envs/eks/`` or ``envs/local-env/``, depending on which manifest you want to deploy. You can tune CPU, memory as well as storage for persistent volumes of each of the cluster objects. This could be undone by removing these patches from the ``kustomization.yaml`` or altering the patches themselves with different values.

We can deploy the cluster with a single command by using the customization file:

- EKS cluster

  .. code-block:: console

      $ kubectl apply -k envs/eks/

 
- Other cluster types

  .. code-block:: console

      $ kubectl apply -k envs/local-env/


Verifying the deployment
^^^^^^^^^^^^^^^^^^^^^^^^

**Namespace**

    .. code-block:: console

        $ kubectl get namespaces | grep cyb3rhq

    .. code-block:: none
        :class: output

        cyb3rhq         Active    12m

**Services**

    .. code-block:: console

        $ kubectl get services -n cyb3rhq

    .. code-block:: none
        :class: output

        NAME                  TYPE           CLUSTER-IP       EXTERNAL-IP        PORT(S)                          AGE
        indexer               ClusterIP      xxx.yy.zzz.24    <none>             9200/TCP                         12m
        dashboard             ClusterIP      xxx.yy.zzz.76    <none>             5601/TCP                         11m
        cyb3rhq                 LoadBalancer   xxx.yy.zzz.209   internal-a7a8...   1515:32623/TCP,55000:30283/TCP   9m
        cyb3rhq-cluster         ClusterIP      None             <none>             1516/TCP                         9m
        Cyb3rhq-indexer         ClusterIP      None             <none>             9300/TCP                         12m
        cyb3rhq-workers         LoadBalancer   xxx.yy.zzz.26    internal-a7f9...   1514:31593/TCP                   9m


**Deployments**

    .. code-block:: console

        $ kubectl get deployments -n cyb3rhq

    .. code-block:: none
        :class: output

        NAME             DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
        cyb3rhq-dashboard  1         1         1            1           11m

**Statefulset**

    .. code-block:: console

        $ kubectl get statefulsets -n cyb3rhq

    .. code-block:: none
        :class: output

        NAME                   READY   AGE
        cyb3rhq-indexer          3/3     15m
        cyb3rhq-manager-master   1/1     15m
        cyb3rhq-manager-worker   2/2     15m

**Pods**

    .. code-block:: console

        $ kubectl get pods -n cyb3rhq

    .. code-block:: none
        :class: output

        NAME                              READY     STATUS    RESTARTS   AGE
        cyb3rhq-indexer-0                   1/1       Running   0          15m
        cyb3rhq-dashboard-f4d9c7944-httsd   1/1       Running   0          14m
        cyb3rhq-manager-master-0            1/1       Running   0          12m
        cyb3rhq-manager-worker-0-0          1/1       Running   0          11m
        cyb3rhq-manager-worker-1-0          1/1       Running   0          11m


**Accessing Cyb3rhq dashboard**

In case you created domain names for the services, you should be able to access the dashboard using the proposed domain name: ``https://cyb3rhq.your-domain.com``. Cloud providers usually provide an external IP address or hostname for direct access to the dashboard. This can be viewed by checking the services:

    .. code-block:: console
 
         $ kubectl get services -o wide -n cyb3rhq



    .. code-block:: none
        :class: output

         NAME                  TYPE           CLUSTER-IP       EXTERNAL-IP                      PORT(S)                          AGE       SELECTOR
         dashboard             LoadBalancer   xxx.xx.xxx.xxx   xxx.xx.xxx.xxx                   80:31831/TCP,443:30974/TCP       15m       app=cyb3rhq-dashboard


**Optional**: On a local cluster deployment where the external IP address is not accessible, you can use ``port-forward``:
 
.. code-block:: console

   $ kubectl -n cyb3rhq port-forward --address <INTERFACE_IP_ADDRESS> service/dashboard 8443:443
  
Where ``<INTERFACE_IP_ADDRESS>`` is the IP address of the Kubernetes host.

The Cyb3rhq dashboard is accessible on ``https://<INTERFACE_IP_ADDRESS>:8443``.

The default credentials are ``admin:SecretPassword``.

Change the password of Cyb3rhq users
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To improve security, you can change the default password of the Cyb3rhq users. There are two types of Cyb3rhq users:

-  Cyb3rhq indexer users
-  Cyb3rhq API users

Cyb3rhq indexer users
~~~~~~~~~~~~~~~~~~~

 To change the password of the default ``admin`` and ``kibanaserver`` users, do the following.

.. warning::

   If you have custom users, add them to the ``internal_users.yml`` file. Otherwise, executing this procedure deletes them.

Closing your Cyb3rhq dashboard session
....................................

Before starting the password change process, we recommend to log out of your Cyb3rhq dashboard session.

If you don't log out, persistent session cookies might cause errors when accessing Cyb3rhq after changing user passwords.

Setting a new hash
..................

#. Start a Bash shell in ``cyb3rhq-indexer-0``.

   .. code-block:: console

      # kubectl exec -it cyb3rhq-indexer-0 -n cyb3rhq -- /bin/bash

#. Run these commands to generate the hash of your new password. When prompted, input the new password and press **Enter**.

   .. code-block:: console

	  cyb3rhq-indexer@cyb3rhq-indexer-0:~$ export JAVA_HOME=/usr/share/cyb3rhq-indexer/jdk
	  cyb3rhq-indexer@cyb3rhq-indexer-0:~$ bash /usr/share/cyb3rhq-indexer/plugins/opensearch-security/tools/hash.sh

#. Copy the generated hash and exit the Bash shell.

#. Open the ``cyb3rhq/indexer_stack/cyb3rhq-indexer/indexer_conf/internal_users.yml`` file. Locate the block for the user you are changing password for.

#. Replace the hash.

   -  ``admin`` user

      .. code-block:: YAML
         :emphasize-lines: 3

         ...
         admin:
             hash: "$2y$12$K/SpwjtB.wOHJ/Nc6GVRDuc1h0rM1DfvziFRNPtk27P.c4yDr9njO"
             reserved: true
             backend_roles:
             - "admin"
             description: "Demo admin user"
 
         ...

   -  ``kibanaserver`` user

      .. code-block:: YAML
         :emphasize-lines: 3

         ...
         kibanaserver:
             hash: "$2a$12$4AcgAt3xwOWadA5s5blL6ev39OXDNhmOesEoo33eZtrq2N0YrU3H."
             reserved: true
             description: "Demo kibanaserver user"
 
         ...

Setting the new password
........................

.. warning::

   Don't use the ``$`` or ``&`` characters in your new password. These characters can cause errors during deployment.

#. Encode your new password in base64 format. Avoid inserting a trailing newline character to maintain the hash value. For example, use the ``-n`` option with the ``echo`` command as follows.

   .. code-block::
      
      # echo -n "NewPassword" | base64

#. Edit the indexer or dashbboard secrets configuration file as follows. Replace the value of the ``password`` field with your new encoded password.

   -  To change the ``admin`` user password, edit the ``cyb3rhq/secrets/indexer-cred-secret.yaml`` file.

      .. code-block:: YAML
         :emphasize-lines: 8

         ...
         apiVersion: v1
         kind: Secret
         metadata:
             name: indexer-cred
         data:
             username: YWRtaW4=              # string "admin" base64 encoded
             password: U2VjcmV0UGFzc3dvcmQ=  # string "SecretPassword" base64 encoded
         ...

   -  To change the ``kibanaserver`` user password, edit the ``cyb3rhq/secrets/dashboard-cred-secret.yaml`` file.

      .. code-block:: YAML
         :emphasize-lines: 8

         ...
         apiVersion: v1
         kind: Secret
         metadata:
             name: dashboard-cred
         data:
             username: a2liYW5hc2VydmVy  # string "kibanaserver" base64 encoded
             password: a2liYW5hc2VydmVy  # string "kibanaserver" base64 encoded
         ...

Applying the changes
....................

#. Apply the manifest changes

   -  EKS cluster

      .. code-block:: console

         # kubectl apply -k envs/eks/

   -  Other cluster types

      .. code-block:: console

         # kubectl apply -k envs/local-env/

#. Start a bash shell in ``cyb3rhq-indexer-0`` once more.

   .. code-block:: console

      # kubectl exec -it cyb3rhq-indexer-0 -n cyb3rhq -- /bin/bash

#. Set the following variables:

   .. code-block:: console

      export INSTALLATION_DIR=/usr/share/cyb3rhq-indexer
      CACERT=$INSTALLATION_DIR/certs/root-ca.pem
      KEY=$INSTALLATION_DIR/certs/admin-key.pem
      CERT=$INSTALLATION_DIR/certs/admin.pem
      export JAVA_HOME=/usr/share/cyb3rhq-indexer/jdk

#. Wait for the Cyb3rhq indexer to initialize properly. The waiting time can vary from two to five minutes. It depends on the size of the cluster, the assigned resources, and the speed of the network. Then, run the ``securityadmin.sh`` script to apply all changes.

   .. code-block:: console

      $ bash /usr/share/cyb3rhq-indexer/plugins/opensearch-security/tools/securityadmin.sh -cd /usr/share/cyb3rhq-indexer/opensearch-security/ -nhnv -cacert  $CACERT -cert $CERT -key $KEY -p 9200 -icl -h $NODE_NAME

#. Delete all Cyb3rhq manager pods to update the component credentials.

   .. code-block:: console

      $ kubectl delete -n cyb3rhq pod/cyb3rhq-manager-master-0 pod/cyb3rhq-manager-worker-0 pod/cyb3rhq-manager-worker-1

#. Login with the new credentials on the Cyb3rhq dashboard.

Cyb3rhq API users
~~~~~~~~~~~~~~~

The ``cyb3rhq-wui`` user is the user to connect with the Cyb3rhq API by default. Follow these steps to change the password.

.. note::

   The password for Cyb3rhq API users must be between 8 and 64 characters long. It must contain at least one uppercase and one lowercase letter, a number, and a symbol.

#. Encode your new password in base64 format. Avoid inserting a trailing newline character to maintain the hash value. For example, use the ``-n`` option with the ``echo`` command as follows.

   .. code-block::
      
      # echo -n "NewPassword" | base64

#. Edit the ``cyb3rhq/secrets/cyb3rhq-api-cred-secret.yaml`` file and replace the value of the ``password`` field.

   .. code-block:: YAML
      :emphasize-lines: 8

      apiVersion: v1
      kind: Secret
      metadata:
          name: cyb3rhq-api-cred
          namespace: cyb3rhq
      data:
          username: d2F6dWgtd3Vp          # string "cyb3rhq-wui" base64 encoded
          password: UGFzc3dvcmQxMjM0LmE=  # string "MyS3cr37P450r.*-" base64 encoded

#. Apply the manifest changes.

    .. code-block:: console

        # kubectl apply -k envs/eks/

#. Restart pods for Cyb3rhq dashboard and Cyb3rhq manager master.

Agents
^^^^^^

Cyb3rhq agents are designed to monitor hosts. To start using them:

#. :doc:`Install the agent </installation-guide/cyb3rhq-agent/index>`.
#. Enroll the agent by modifying the file ``/var/ossec/etc/ossec.conf``. Change the “transport protocol” to TCP and replace the ``MANAGER_IP`` with the external IP address of the service pointing to port 1514 or with the hostname provided by the cloud provider

To learn more about registering agents, see the :doc:`Cyb3rhq agent enrollment </user-manual/agent/agent-enrollment/index>` section of the documentation.
