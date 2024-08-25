.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Cyb3rhq provides two types of storage for your data: indexed and archive. Learn more about the archive data in this section. 

.. _cloud_archive_data_access:

Access
======

To access your archive data, you need an AWS token that grants permission on the AWS S3 bucket of your environment. This token can be generated using the Cyb3rhq Cloud API.

   .. note::
      See the :doc:`Cyb3rhq Cloud CLI </cloud-service/cli/index>` section to learn how to list and download your archive data automatically.


Getting your API key and the AWS token
--------------------------------------

#. Obtain your Cyb3rhq Cloud API key by following the steps outlined in the API :doc:`Authentication </cloud-service/apis/authentication>` section.

#. Use the :cloud-api-ref:`POST /storage/token <tag/storage>` API endpoint with your key to get a temporary AWS token. For example, the following request generates an AWS token valid for ``3600`` seconds that grants access to the environment archive data with ID ``012345678ab``.

   .. code-block::

      curl -XPOST https://api.cloud.cyb3rhq.com/v2/storage/token -H "x-api-key: <YOUR_API_KEY>" -H "Content-Type: application/json" --data '
      {
         "environment_cloud_id": "012345678ab",
         "token_expiration": "3600"
      }'

   .. code-block:: console
      :class: output
      :emphasize-lines: 7-10

      {
         "environment_cloud_id": "012345678ab",
         "aws": {
            "s3_path": "cyb3rhq-cloud-cold-us-east-1/012345678ab",
            "region": "us-east-1",
            "credentials": {
               "access_key_id": "mUdT2dBjlHd...Gh7Ni1yZKR5If",
               "secret_access_key": "qEzCk63a224...5aB+e4fC1BR0G",
               "session_token": "MRg3t7HIuoA...4o4BXSAcPfUD8",
               "expires_in": 3600
            }
         }
      }



Generating the AWS `cyb3rhq_cloud_storage` profile
------------------------------------------------

Add the token to the AWS credentials file ``~/.aws/credentials``.

   .. code-block:: console
      :emphasize-lines: 4
      
      [cyb3rhq_cloud_storage]
      aws_access_key_id = mUdT2dBjlHd...Gh7Ni1yZKR5If
      aws_secret_access_key = qEzCk63a224...5aB+e4fC1BR0G
      aws_session_token = MRg3t7HIuoA...4o4BXSAcPfUD8

Listing archive data
---------------------

This command lists the archive data files of the environment `012345678ab`.

.. code-block:: console

   # aws --profile cyb3rhq_cloud_storage --region us-east-1 s3 ls --recursive s3://cyb3rhq-cloud-cold-us-east-1/012345678ab/

.. code-block:: none
   :class: output

   2024-04-19 17:50:06        493 012345678ab/output/alerts/2024/04/19/012345678ab_output_alerts_20240419T2050_VqaWCpX9oPfDkRpD.json.gz
   2024-04-19 18:00:05      77759 012345678ab/output/alerts/2024/04/19/012345678ab_output_alerts_20240419T2100_kdBY42OvE9QJuiia.json.gz

Examples
--------

Downloading archive data – Multiple files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command downloads the archive data files of the environment ``012345678ab`` into the ``/home/test/`` directory.

.. code-block:: console

   # aws --profile cyb3rhq_cloud_storage --region us-east-1 s3 cp --recursive s3://cyb3rhq-cloud-cold-us-east-1/012345678ab/ /home/test/

.. code-block:: none
   :class: output

   download: s3://cyb3rhq-cloud-cold-us-east-1/012345678ab/output/alerts/2024/04/19/012345678ab_output_alerts_20240419T2050_VqaWCpX9oPfDkRpD.json.gz to output/alerts/2024/04/19/012345678ab_output_alerts_20240419T2050_VqaWCpX9oPfDkRpD.json.gz
   download: s3://cyb3rhq-cloud-cold-us-east-1/012345678ab/output/alerts/2024/04/19/012345678ab_output_alerts_20240419T2100_kdBY42OvE9QJuiia.json.gz to output/alerts/2024/04/19/012345678ab_output_alerts_20240419T2100_kdBY42OvE9QJuiia.json.gz


Downloading archive data – Single file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command downloads the ``012345678ab_output_alerts_20240419T2050_VqaWCpX9oPfDkRpD.json.gz`` file of the environment ``012345678ab`` into the directory ``/home/test``.

.. code-block:: console

   # aws --profile cyb3rhq_cloud_storage --region us-east-1 s3 cp --recursive s3://cyb3rhq-cloud-cold-us-east-1/012345678ab/012345678ab_output_alerts_20240419T2050_VqaWCpX9oPfDkRpD.json.gz /home/test/

.. code-block:: none
   :class: output

   download: s3://cyb3rhq-cloud-cold-us-east-1/012345678ab/output/alerts/2024/04/19/012345678ab_output_alerts_20240419T2050_VqaWCpX9oPfDkRpD.json.gz to ./012345678ab_output_alerts_20240419T2050_VqaWCpX9oPfDkRpD.json.gz
