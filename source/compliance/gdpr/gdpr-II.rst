.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Check out this section to learn more about how to use Cyb3rhq for GDPR II (The General Data Protection Regulation of the European Union). 
  
GDPR II, Principles <gdpr_II>
=============================

This chapter describes requirements concerning the basic principles of GDPR for processing personal data.

Chapter II, Article 5 Head 1(f)
-------------------------------

**Principles relating to processing of personal data, Head 1 (f)**: *“Personal data shall be processed in a manner that ensures appropriate security of the personal data, including protection against unauthorized or unlawful processing and against accidental loss, destruction or damage, using appropriate technical or organizational measures (integrity and confidentiality).”*

The article requires confidentiality and integrity when processing user data. The :doc:`File Integrity Monitoring (FIM) </user-manual/capabilities/file-integrity/index>` module of Cyb3rhq helps with this requirement by monitoring files and folders. The Cyb3rhq FIM module generates alerts when it detects file creation, modification, or deletion events. The FIM module keeps a record of the cryptographic checksum and other attributes from a file or a registry key in the case of a Windows endpoint, and regularly compares them to the current attributes of the file.

Below are some examples of Cyb3rhq rules tagged as ``gdpr_II_5.1.f``:

.. code-block:: xml
	:emphasize-lines: 5, 12

	<rule id="550" level="7">
	    <category>ossec</category>
	    <decoded_as>syscheck_integrity_changed</decoded_as>
	    <description>Integrity checksum changed.</description>
	    <group>syscheck,pci_dss_11.5,gpg13_4.11,gdpr_II_5.1.f,</group>
	</rule>

	<rule id="554" level="5">
	    <category>ossec</category>
	    <decoded_as>syscheck_new_entry</decoded_as>
	    <description>File added to the system.</description>
	    <group>syscheck,pci_dss_11.5,gpg13_4.11,gdpr_II_5.1.f,</group>
  	</rule>

Use case: Detect file changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this use case, you have to configure the Cyb3rhq agent on an Ubuntu 22.04 endpoint to detect changes in the ``/root/personal_data`` directory. Then, you need to modify a file to trigger an alert.

Ubuntu endpoint
~~~~~~~~~~~~~~~

#. Switch to the ``root`` user:

	.. code-block:: console

		$ sudo su

#. Create the directory ``personal_data`` in the ``/root`` directory:

	.. code-block:: console

		# mkdir /root/personal_data

#. Create the file ``subject_data.txt`` in the ``/root/personal_data`` directory  and include some content:

	.. code-block:: console

		# touch /root/personal_data/subject_data.txt
		# echo "User01= user03_ID" >> /root/personal_data/subject_data.txt

#. Add the configuration highlighted to the ``<syscheck>`` block of the Cyb3rhq agent configuration file ``/var/ossec/etc/ossec.conf``:

	.. code-block:: xml
		:emphasize-lines: 2

		<syscheck>
		  <directories realtime="yes" check_all="yes" report_changes="yes">/root/personal_data</directories>
		</syscheck>

#. Restart the Cyb3rhq agent to apply the changes:

	.. code-block:: console

		# systemctl restart cyb3rhq-agent

#. Modify the file by changing the content of ``subject_data.txt`` from ``User01= user03_ID`` to ``User01= user02_ID``:

	.. code-block:: console

		# echo "User01= user02_ID" > /root/personal_data/subject_data.txt
		# cat /root/personal_data/subject_data.txt

	.. code-block:: none
		:class: output

		User01= user02_ID

On the Cyb3rhq dashboard, an alert detects the modification of the ``subject_data.txt`` file. The alert is also tagged with ``gdpr_II_5.1.f``.

.. thumbnail:: /images/compliance/gdpr/fim-file-mod.png
    :title: File modification alert visualization
    :align: center
    :width: 80%

