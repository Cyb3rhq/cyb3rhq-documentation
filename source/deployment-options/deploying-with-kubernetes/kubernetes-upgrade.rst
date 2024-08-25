.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Check out how to upgrade Cyb3rhq installed in Kubernetes, creating a new pod linked to the same volume but with the new updated version.

.. _kubernetes_upgrade:

Upgrade Cyb3rhq installed in Kubernetes
=====================================

Checking which files are exported to the volume
-----------------------------------------------

Our Kubernetes deployment uses our Cyb3rhq images from Docker. If we look at the following code extracted from the Cyb3rhq configuration using Docker, we can see which directories and files are used in the upgrade.

.. code-block:: none
    
    /var/ossec/api/configuration
    /var/ossec/etc
    /var/ossec/logs
    /var/ossec/queue
    /var/ossec/var/multigroups
    /var/ossec/integrations
    /var/ossec/active-response/bin
    /var/ossec/agentless
    /var/ossec/wodles
    /etc/filebeat
    /var/lib/filebeat
    /usr/share/cyb3rhq-dashboard/config/
    /usr/share/cyb3rhq-dashboard/certs/
    /var/lib/cyb3rhq-indexer
    /usr/share/cyb3rhq-indexer/certs/
    /usr/share/cyb3rhq-indexer/opensearch.yml
    /usr/share/cyb3rhq-indexer/opensearch-security/internal_users.yml


Any modification related to these files will also be made in the associated volume. When the replica pod is created, it will get those files from the volume, keeping the previous changes.


Recreating certificates
-----------------------

Upgrading from a version earlier than v4.8.0 requires that you recreate the SSL certificates. Follow instructions in :ref:`kubernetes_ssl_certificates` for this.

Configuring the upgrade
-----------------------

To upgrade to version |CYB3RHQ_CURRENT_MINOR|, you can follow one of two strategies.

-  `Using default manifests`_ : This strategy uses the default manifests for Cyb3rhq |CYB3RHQ_CURRENT_MINOR|. It replaces the cyb3rhq-kubernetes manifests of your outdated Cyb3rhq version.
-  `Keeping custom manifests`_ : This strategy preserves the cyb3rhq-kubernetes manifests of your outdated Cyb3rhq deployment. It ignores the manifests of the latest Cyb3rhq version.

Using default manifests
^^^^^^^^^^^^^^^^^^^^^^^

#. Checkout the tag for the current version of cyb3rhq-kubernetes:

   .. code-block::

      # git checkout v|CYB3RHQ_CURRENT_DOCKER|

#. `Apply the new configuration`_

Keeping custom manifests
^^^^^^^^^^^^^^^^^^^^^^^^

In Cyb3rhq 4.4, some paths are different to those in earlier versions. You have to update the old paths with the new ones if you are keeping your custom manifests.

``old-path`` -> ``new-path``

-  ``/usr/share/cyb3rhq-dashboard/config/certs/`` -> ``/usr/share/cyb3rhq-dashboard/certs/``
-  ``/usr/share/cyb3rhq-indexer/config/certs/`` -> ``/usr/share/cyb3rhq-indexer/certs/``
-  ``/usr/share/cyb3rhq-indexer/plugins/opensearch-security/securityconfig/`` -> ``/usr/share/cyb3rhq-indexer/opensearch-security/``

To upgrade your deployment keeping your custom manifests, do the following.

#. If you are updating from 4.3, edit the following files and update them with the new paths in 4.4. You can see the new paths next to each file in the samples below.

   -  ``cyb3rhq/indexer_stack/cyb3rhq-dashboard/dashboard-deploy.yaml``

      .. code-block:: yaml

         image: 'cyb3rhq/cyb3rhq-dashboard:|CYB3RHQ_CURRENT_KUBERNETES|'
         mountPath: /usr/share/cyb3rhq-dashboard/certs/cert.pem
         mountPath: /usr/share/cyb3rhq-dashboard/certs/key.pem
         mountPath: /usr/share/cyb3rhq-dashboard/certs/root-ca.pem
         value: /usr/share/cyb3rhq-dashboard/certs/cert.pem
         value: /usr/share/cyb3rhq-dashboard/certs/key.pem

   -  ``cyb3rhq/indexer_stack/cyb3rhq-dashboard/dashboard_conf/opensearch_dashboards.yml``

      .. code-block:: yaml

         server.ssl.key: "/usr/share/cyb3rhq-dashboard/certs/key.pem"
         server.ssl.certificate: "/usr/share/cyb3rhq-dashboard/certs/cert.pem"
         opensearch.ssl.certificateAuthorities: ["/usr/share/cyb3rhq-dashboard/certs/root-ca.pem"]

   -  ``cyb3rhq/indexer_stack/cyb3rhq-indexer/cluster/indexer-sts.yaml``

      .. code-block:: yaml

         image: 'cyb3rhq/cyb3rhq-indexer:|CYB3RHQ_CURRENT_KUBERNETES|'
         mountPath: /usr/share/cyb3rhq-indexer/certs/node-key.pem
         mountPath: /usr/share/cyb3rhq-indexer/certs/node.pem
         mountPath: /usr/share/cyb3rhq-indexer/certs/root-ca.pem
         mountPath: /usr/share/cyb3rhq-indexer/certs/admin.pem
         mountPath: /usr/share/cyb3rhq-indexer/certs/admin-key.pem
         mountPath: /usr/share/cyb3rhq-indexer/opensearch.yml
         mountPath: /usr/share/cyb3rhq-indexer/opensearch-security/internal_users.yml

   -  ``cyb3rhq/indexer_stack/cyb3rhq-indexer/indexer_conf/opensearch.yml``

      .. code-block:: yaml

         plugins.security.ssl.http.pemcert_filepath: /usr/share/cyb3rhq-indexer/certs/node.pem
         plugins.security.ssl.http.pemkey_filepath: /usr/share/cyb3rhq-indexer/certs/node-key.pem
         plugins.security.ssl.http.pemtrustedcas_filepath: /usr/share/cyb3rhq-indexer/certs/root-ca.pem
         plugins.security.ssl.transport.pemcert_filepath: /usr/share/cyb3rhq-indexer/certs/node.pem
         plugins.security.ssl.transport.pemkey_filepath: /usr/share/cyb3rhq-indexer/certs/node-key.pem
         plugins.security.ssl.transport.pemtrustedcas_filepath: /usr/share/cyb3rhq-indexer/certs/root-ca.pem

   -  ``cyb3rhq/cyb3rhq_managers/cyb3rhq-master-sts.yaml``

      .. code-block:: yaml

         image: 'cyb3rhq/cyb3rhq-manager:|CYB3RHQ_CURRENT_KUBERNETES|'

   -  ``cyb3rhq/cyb3rhq_managers/cyb3rhq-worker-sts.yaml``

      .. code-block:: yaml

         image: 'cyb3rhq/cyb3rhq-manager:|CYB3RHQ_CURRENT_KUBERNETES|'

#. `Apply the new configuration`_

Apply the new configuration
---------------------------

The last step is to apply the new configuration:

- EKS cluster

    .. code-block:: console

         $ kubectl apply -k envs/eks/

- Other cluster types

    .. code-block:: console

         $ kubectl apply -k envs/local-env/


.. code-block:: none
    :class: output

     statefulset.apps "cyb3rhq-manager-master" configured

This process will end the old pod while creating a new one with the new version, linked to the same volume. Once the Pods are booted, the update will be ready, and we can check the new version of Cyb3rhq installed, the cluster, and the changes that have been maintained through the use of the volumes.
