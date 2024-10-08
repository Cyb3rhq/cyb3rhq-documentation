.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: The Cyb3rhq security platform protects cloud workloads by monitoring the infrastructure at two levels: Endpoint level and Cloud infrastructure level. Find more information in this getting started use case.

Cloud workload protection
=========================

The Cyb3rhq security platform provides threat detection, configuration compliance, and continuous monitoring for on-premises, cloud, and hybrid environments. It protects cloud workloads by monitoring the infrastructure at two levels:

-  **Endpoint level**: monitoring cloud instances or virtual machines using the lightweight :doc:`Cyb3rhq agent </getting-started/components/cyb3rhq-agent>`.
-  **Cloud infrastructure level**: monitoring cloud service activity by collecting and analyzing data from the provider API. Cyb3rhq supports Amazon AWS, Microsoft Azure, and Google Cloud.

We describe some benefits of using Cyb3rhq to enhance security operations, protect cloud-native applications, and facilitate compliance efforts for a secure cloud environment.

Cloud log data analysis and retention
-------------------------------------

Cloud environments generate large amounts of log data, vital for identifying security incidents. The Cyb3rhq rules and decoders are responsible for parsing and analyzing log data to detect anomalous events. Cyb3rhq collects and analyzes log data from various cloud platforms and services, such as AWS, Azure, Google Cloud, Office 365, and GitHub.

The image below is an example of an AWS dashboard on Cyb3rhq showing the trend of events collected from the cloud infrastructure.

.. thumbnail:: /images/getting-started/use-cases/cloud-workload-protection/aws-dashboard.png
   :title: AWS dashboard on Cyb3rhq
   :alt: AWS dashboard on Cyb3rhq
   :align: center
   :width: 80%

Cyb3rhq monitors and logs activities in the cloud, providing a centralized view of user actions across the entire cloud infrastructure. Cyb3rhq has out-of-the-box rules to detect suspicious or unauthorized activities. In addition to the in-built rules, users can :doc:`create custom rules </user-manual/ruleset/rules/custom>` to consolidate threat detection.

Amazon web services
^^^^^^^^^^^^^^^^^^^

Cyb3rhq has dedicated modules for :doc:`monitoring and securing AWS cloud infrastructure </cloud-security/amazon/index>`. Some of the AWS services that Cyb3rhq monitors include:

-  **Amazon Guardduty** is a threat detection service that continuously monitors for malicious activity and unauthorized behavior, ensuring the protection of AWS accounts, workloads, and data stored in Amazon S3.
-  **Amazon Inspector** is an automated security assessment service that helps improve the security and compliance of applications deployed on AWS.
-  **Amazon Key Management Service (KMS)** is used for cryptographic key management across AWS services. 
-  **Amazon Macie** is a fully managed data security and privacy service. It automatically detects unencrypted S3 buckets, publicly accessible buckets, and buckets shared with external AWS accounts.
-  **Amazon Virtual Private Cloud (VPC)** provisions a logically isolated section of the AWS Cloud where AWS resources can be launched on a virtual network defined by the user.
-  **AWS Config** assesses, audits, and evaluates the configurations of your AWS resources. It helps the users review changes in configurations and relationships between AWS resources.
-  **AWS Cloudtrail** enables governance, compliance, operational auditing, and risk auditing of your AWS account. With CloudTrail, you can log, continuously monitor, and retain account activity related to actions across your AWS infrastructure.
-  **AWS Trusted Advisor** helps users reduce costs, increase performance, and improve security by optimizing their AWS environment. It provides real-time guidance to help users provision their resources following AWS best practices.
-  **AWS Web Application Firewall (WAF)** helps protect your web applications or APIs against common web exploits that may affect availability, compromise security, or consume excessive resources.

Microsoft Azure
^^^^^^^^^^^^^^^

Cyb3rhq has a dedicated module that pulls logs from and :doc:`monitors Azure platform </cloud-security/azure/index>`. This module obtains data from critical Azure services, including:

-  **Log Analytics API**: The Log Analytics API is a core component of the Azure Monitor service and is used to aggregate and analyze log data. The sources of such data are cloud applications, operating systems, and Azure resources. The Cyb3rhq module for Azure is capable of querying the Log Analytics API, pulling the logs collected by the Azure Monitor service.
-  **Blob Storage API**: Logs from Azure services are optionally pushed to Azure Blob Storage. Specifically, it is possible to configure an Azure service to export logs to a container in a storage account created for that purpose. Afterward, the Cyb3rhq agent will download those logs via its integration with the Blob Storage API.
-  **Active Directory Graph API**: The Azure Active Directory (AD) Graph API provides access to AZURE AD through REST API endpoints. It is used by Cyb3rhq to monitor Active Directory events (for example, creation of a new user, update of user properties, disablement of user accounts, etc.)

Google Cloud Platform
^^^^^^^^^^^^^^^^^^^^^

Cyb3rhq monitors Google Cloud services by pulling events from the Google Pub/Sub messaging service, a middleware for event ingestion and delivery. This integration helps detect threats targeting your Google Cloud assets. For more information, please refer to :doc:`Using Cyb3rhq to monitor GCP services </cloud-security/gcp/index>`.

Office 365
^^^^^^^^^^

Cyb3rhq includes a dedicated module designed to interact with the Office 365 Management Activity API. This module is responsible for fetching logs from Office 365 and making them available for analysis within the Cyb3rhq platform. The Management Activity API serves as the source of audit logs for Office 365, containing information about various actions and events within the Office 365 environment. These logs are organized into tenant-specific content blobs and classified based on their content type and source. Cyb3rhq performs analysis, alerting, and reporting on these logs, enhancing the security and compliance monitoring capabilities within the Office 365 environment. For more detailed information, please refer to :doc:`Using Cyb3rhq to monitor Office 365 </cloud-security/office365/index>`.

GitHub
^^^^^^

Cyb3rhq has a GitHub module that utilizes the GitHub API to pull GitHub audit logs, which contain information about actions performed by organization members. This log includes essential details such as the user who initiated the action, the nature of the action (e.g., repository creation, access changes, etc.),  the timestamp indicating when the action took place and others. Cyb3rhq collects, processes, and stores these logs, enabling analysis, alerting, and reporting. Refer to :doc:`Using Cyb3rhq to monitor GitHub </cloud-security/github/index>` for more information.

Protect cloud-native applications
---------------------------------

Cyb3rhq provides protection for cloud-native applications, safeguarding them against security threats and vulnerabilities. It integrates with container orchestration platforms like Kubernetes and Docker, allowing it to monitor and analyze container activity in real time. Cyb3rhq detects suspicious container behavior, unauthorized image changes, and potential security misconfigurations, ensuring the overall integrity of containerized applications.

The image below shows alerts generated from a monitored Docker infrastructure.

.. thumbnail:: /images/getting-started/use-cases/cloud-workload-protection/docker-infrastructure-alerts.png
   :title: Docker infrastructure alerts
   :alt: Docker infrastructure alerts
   :align: center
   :width: 80%

Some additional use cases for using Cyb3rhq to monitor cloud-native applications are:

-  `Auditing Kubernetes with Cyb3rhq <https://cyb3rhq.github.io/blog/auditing-kubernetes-with-cyb3rhq/>`__
-  `Monitoring GKE audit logs <https://cyb3rhq.github.io/blog/monitoring-gke-audit-logs/>`__
-  :ref:`Monitoring user interaction with Docker resources <monitoring_user_interaction_with_docker_resources>`
-  :ref:`Monitoring container runtime <monitoring_container_runtime>`

Furthermore, the Cyb3rhq integration with cloud service providers enables monitoring and analysis of cloud-native application logs, ensuring comprehensive visibility into the environment and facilitating effective security operations.

Promote security operations in the cloud
----------------------------------------

Cyb3rhq promotes security operations within cloud environments by allowing security teams to detect and respond to threats, mitigating damages, and reducing the overall impact on the cloud infrastructure. Furthermore, Cyb3rhq facilitates red and blue team activities. The platform's customizable rules enable organizations to simulate attacks and test their security defenses. Blue teams can use the insights gained on Cyb3rhq from red team activities to fine-tune their security measures and strengthen their defenses. The following resources demonstrate how to use the Stratus Red Team tool to simulate attacks on some cloud platforms and how to detect them with Cyb3rhq:

-  `Adversary emulation on AWS with Stratus Red Team and Cyb3rhq <https://cyb3rhq.github.io/blog/adversary-emulation-on-aws-with-stratus-red-team-and-cyb3rhq/>`__
-  `Adversary emulation on GCP with Stratus Red Team and Cyb3rhq <https://cyb3rhq.github.io/blog/adversary-emulation-on-gcp-with-stratus-red-team-and-cyb3rhq/>`__

.. thumbnail:: /images/getting-started/use-cases/cloud-workload-protection/detection-results.png
   :title: Detection results
   :alt: Detection results
   :align: center
   :width: 80%

The centralized logging and reporting capabilities of Cyb3rhq simplify compliance management within cloud environments. It helps organizations meet regulatory requirements by capturing and storing audit trails, ensuring accountability, and facilitating the investigation of security incidents. Refer to the :doc:`Cyb3rhq dashboard  </getting-started/components/cyb3rhq-dashboard>` documentation for more information about how Cyb3rhq aids analysis, reporting, and compliance efforts.