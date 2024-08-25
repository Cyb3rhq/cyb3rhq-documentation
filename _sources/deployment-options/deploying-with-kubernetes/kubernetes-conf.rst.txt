.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Learn more about Kubernetes configuration for Cyb3rhq: prerequisites, overview, how to verify the deployment, and more. 

.. _kubernetes_conf:

Kubernetes configuration
========================   

Pre-requisites
--------------

-  A Kubernetes cluster already deployed.
-  For Amazon EKS deployments using Kubernetes version 1.23 and later, an Amazon EBS CSI driver IAM role. The CSI driver requires that you assign an IAM role to work properly. Read AWS documentation to find instructions on `Creating the Amazon EBS CSI driver IAM role <https://docs.aws.amazon.com/eks/latest/userguide/csi-iam-role.html>`__. You need to install the CSI driver for both, new and old deployments. The CSI driver is an essential Kubernetes feature.
   
Resource Requirement
--------------------

To deploy Cyb3rhq on Kubernetes, the cluster should have at least the following resources available:

- 2 CPU units
- 3 Gi of memory
- 2 Gi of storage
   
   
Overview
--------

StatefulSet and deployment controllers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As a *Deployment*, a *StatefulSet* manages Pods that are based on an identical container specification, but it maintains an identity attached to each of its pods. These pods are created from the same specification, but they are not interchangeable: each one has a persistent identifier maintained across any rescheduling.

It is useful for stateful applications like databases that save the data to persistent storage. The states of each Cyb3rhq manager and each Cyb3rhq indexer should be maintained, so we declare them using StatefulSet to ensure that they maintain their states in every startup.

Deployments are intended for stateless use and are quite lightweight, and seem to be appropriate for the Cyb3rhq dashboard, where it is not necessary to maintain the states.

Persistent volumes (PV) are pieces of storage in the provisioned cluster. It is a resource in the cluster just like a node is a cluster resource. Persistent volumes are volume plugins like Volumes but have a lifecycle independent of any individual pod that uses the PV. This API object captures the details of the implementation of the storage, be that NFS, iSCSI, or a cloud-provider-specific storage system.

Here, we use persistent volumes to store data from both the Cyb3rhq manager and the Cyb3rhq indexer.

Refer to the `persistent volumes <https://kubernetes.io/docs/concepts/storage/persistent-volumes/>`_ page for more information.

Pods
^^^^

You can check how we build our Cyb3rhq docker containers in our `repository <https://github.com/cyb3rhq/cyb3rhq-docker>`_.

**Cyb3rhq master**

This pod contains the master node of the Cyb3rhq cluster. The master node centralizes and coordinates worker nodes, making sure the critical and required data is consistent across all nodes. The management is performed only in this node, so the agent enrollment service (authd) is placed here.

+-------------------------------+-------------+
| Image                         | Controller  |
+===============================+=============+
| cyb3rhq/cyb3rhq-manager           | StatefulSet |
+-------------------------------+-------------+

**Cyb3rhq worker 0 / 1**

These pods contain a worker node of the Cyb3rhq cluster. They will receive the agent events.

+-------------------------------+-------------+
| Image                         | Controller  |
+===============================+=============+
| cyb3rhq/cyb3rhq-manager           | StatefulSet |
+-------------------------------+-------------+

**Cyb3rhq indexer**

The Cyb3rhq indexer pod ingests events received from Filebeat.

+--------------------------------------------+-------------+
| Image                                      | Controller  |
+============================================+=============+
| cyb3rhq/cyb3rhq-indexer                        | StatefulSet |
+--------------------------------------------+-------------+

**Cyb3rhq dashboard**

The Cyb3rhq dashboard pod lets you visualize your Cyb3rhq indexer data, along with Cyb3rhq agents information and server configuration.

+--------------------------------------+-------------+
| Image                                | Controller  |
+======================================+=============+
| cyb3rhq/cyb3rhq-dashboard                | Deployment  |
+--------------------------------------+-------------+

Services
^^^^^^^^

**Cyb3rhq indexer and dashboard**

+----------------------+-------------------------------------------------------------------------------------+
| Name                 | Description                                                                         |
+======================+=====================================================================================+
| cyb3rhq-indexer        | Communication for Cyb3rhq indexer nodes.                                              |
+----------------------+-------------------------------------------------------------------------------------+
| indexer              | This is the Cyb3rhq indexer API used by the Cyb3rhq dashboard to read/write alerts.     |
+----------------------+-------------------------------------------------------------------------------------+
| dashboard            | Cyb3rhq dashboard service. \https://cyb3rhq.your-domain.com:443                         |
+----------------------+-------------------------------------------------------------------------------------+

**Cyb3rhq**

+----------------------+-------------------------------------------------------------------------+
| Name                 | Description                                                             |
+======================+=========================================================================+
| cyb3rhq                | Cyb3rhq API: cyb3rhq-master.your-domain.com:55000                           |
|                      +-------------------------------------------------------------------------+
|                      | Agent registration service (authd): cyb3rhq-master.your-domain.com:1515   |
+----------------------+-------------------------------------------------------------------------+
| cyb3rhq-workers        | Reporting service: cyb3rhq-manager.your-domain.com:1514                   |
+----------------------+-------------------------------------------------------------------------+
| cyb3rhq-cluster        | Communication for Cyb3rhq manager nodes.                                  |
+----------------------+-------------------------------------------------------------------------+

