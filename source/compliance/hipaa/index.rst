.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Cyb3rhq helps organizations meet technical compliance requirements, including HIPAA. Learn how our capabilities assist with each of HIPAA standard requirements.

.. _hipaa:

Using Cyb3rhq for HIPAA compliance
================================

The Health Insurance Portability and Accountability Act (HIPAA) has specifications and procedures for handling health information. This act aims to improve the effectiveness of healthcare services. It includes standards for electronic health care transactions and code sets. It also includes standards for security and unique health identifiers. Because changes in technology can impact the privacy and security of healthcare data, HIPAA provisions have sections that require the use of federal privacy protections for individually identifiable health information.

Part 164, subpart C (Security Standards For The Protection Of Electronic Protected Health Information), provides guidelines for the transmission, handling, storage, and protection of electronic healthcare information.

Cyb3rhq has various capabilities that assist with HIPAA compliance such as log data analysis, file integrity monitoring, configuration assessment, threat detection and response.

Cyb3rhq includes default rules and decoders for detecting security incidents, system errors, security misconfigurations, and policy violations. By default, these rules are mapped to the associated HIPAA standard. In addition to the default rule mapping provided by Cyb3rhq, it’s possible to map your custom rules to one or more HIPAA standards by adding the compliance identifier in the ``<group>`` tag of the rule. The syntax used to map a rule to a HIPAA standard is ``hipaa_`` followed by the number of the requirement, for example, ``hipaa_164.312.b``. Refer to the :doc:`ruleset section </user-manual/ruleset/index>` for more information. 

The `Cyb3rhq for HIPAA guide (PDF) <https://cyb3rhq.com/resources/Cyb3rhq-for-IPAA-guide-V2.0.pdf>`_ focuses on part 164, subpart C (Security Standards For The Protection Of Electronic Protected Health Information) of the HIPAA standard. This guide explains how the various Cyb3rhq modules assist in complying with HIPAA standards.

We have use cases in the following sections that show how to use Cyb3rhq capabilities and modules to comply with HIPAA standards:

.. toctree::
    :maxdepth: 1

    visualization-and-dashboard
    log-data-analysis
    configuration-assessment
    malware-detection
    file-integrity-monitoring
    vulnerability-detection
    active-response
