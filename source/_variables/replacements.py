###############################################################################
#
# Custom replacements
#
# This file contains the dictionary of custom replacements. Requires the 
# variables 'version', 'release' and 'is_latest_release' from 
# source/_variables/settings.py
#

import sys
import os
sys.path.append(os.path.abspath("_variables"))
from settings import version, is_latest_release, release


custom_replacements = {
    # === URLs and base URLs
    "|CHECKSUMS_URL|" : "https://packages.wazuh.com/4.x/checksums/cyb3rhq/",
    "|APK_CHECKSUMS_I386_URL|" : "alpine/x86",
    "|APK_CHECKSUMS_X86_64_URL|" : "alpine/x86_64",
    "|APK_CHECKSUMS_AARCH64_URL|" : "alpine/aarch64",
    "|APK_CHECKSUMS_ARMV7_URL|" : "alpine/armv7",
    "|APK_CHECKSUMS_ARMHF_URL|" : "alpine/armhf",
    "|APK_CHECKSUMS_PPC_URL|" : "alpine/ppc64le",
    "|APK_AGENT_I386_URL|" : "https://packages.wazuh.com/4.x/alpine/v3.12/main/x86/cyb3rhq-agent",
    "|APK_AGENT_X86_64_URL|" : "https://packages.wazuh.com/4.x/alpine/v3.12/main/x86_64/cyb3rhq-agent",
    "|APK_AGENT_AARCH64_URL|" : "https://packages.wazuh.com/4.x/alpine/v3.12/main/aarch64/cyb3rhq-agent",
    "|APK_AGENT_ARMV7_URL|" : "https://packages.wazuh.com/4.x/alpine/v3.12/main/armv7/cyb3rhq-agent",
    "|APK_AGENT_ARMHF_URL|" : "https://packages.wazuh.com/4.x/alpine/v3.12/main/armhf/cyb3rhq-agent",
    "|APK_AGENT_PPC_URL|" : "https://packages.wazuh.com/4.x/alpine/v3.12/main/ppc64le/cyb3rhq-agent",
    "|RPM_AGENT_URL|" : "https://packages.wazuh.com/4.x/yum/cyb3rhq-agent",
    "|RPM_MANAGER_URL|" : "https://packages.wazuh.com/4.x/yum/cyb3rhq-manager",
    "|DEB_AGENT_URL|" : "https://packages.wazuh.com/4.x/apt/pool/main/w/cyb3rhq-agent/cyb3rhq-agent",
    "|DEB_MANAGER_URL|" : "https://packages.wazuh.com/4.x/apt/pool/main/w/cyb3rhq-manager/cyb3rhq-manager",
    #
    "|CTI_URL|" : "https://cti.cyb3rhq.github.io/api/v1/catalog/contexts/vd_1.0.0/consumers/vd_4.8.0",
    #
    # === Global and Cyb3rhq version (cyb3rhq agent, manager, indexer, and dashboard)
    "|CYB3RHQ_CURRENT_MAJOR|" : "4.x",
    "|CYB3RHQ_CURRENT_MINOR|" : version,
    "|CYB3RHQ_CURRENT|" : release,
    "|PYTHON_CLOUD_CONTAINERS_MIN|": "3.8",
    "|PYTHON_CLOUD_CONTAINERS_MAX|": "3.11",

    # --- Revision numbers for Cyb3rhq agent and manager packages versions
    # Alpine APK packages revisions
    "|CYB3RHQ_REVISION_APK_AGENT_I386|" : "r1",
    "|CYB3RHQ_REVISION_APK_AGENT_X86_64|" : "r1",
    "|CYB3RHQ_REVISION_APK_AGENT_AARCH64|" : "r1",
    "|CYB3RHQ_REVISION_APK_AGENT_ARMV7|" : "r1",
    "|CYB3RHQ_REVISION_APK_AGENT_ARMHF|" : "r1",
    "|CYB3RHQ_REVISION_APK_AGENT_PPC|" : "r1",
    # Yum packages revisions
    "|CYB3RHQ_REVISION_YUM_AGENT_I386|" : "1",
    "|CYB3RHQ_REVISION_YUM_MANAGER_I386|" : "1",
    "|CYB3RHQ_REVISION_YUM_AGENT_I386_EL5|" : "1",
    #"|CYB3RHQ_REVISION_YUM_MANAGER_I386_EL5|" :
    "|CYB3RHQ_REVISION_YUM_AGENT_X86|" : "1",
    "|CYB3RHQ_REVISION_YUM_MANAGER_X86|" : "1",
    "|CYB3RHQ_REVISION_YUM_AGENT_X86_EL5|" : "1",
    #|CYB3RHQ_REVISION_YUM_MANAGER_X86_EL5|
    "|CYB3RHQ_REVISION_YUM_AGENT_AARCH64|" : "1",
    "|CYB3RHQ_REVISION_YUM_MANAGER_AARCH64|" : "1",
    "|CYB3RHQ_REVISION_YUM_AGENT_ARMHF|" : "1",
    #"|CYB3RHQ_REVISION_YUM_MANAGER_ARMHF|" : "1",
    "|CYB3RHQ_REVISION_YUM_AGENT_PPC|" : "1",
    #|CYB3RHQ_REVISION_YUM_MANAGER_PPC|" :
    # Deb packages revisions
    "|CYB3RHQ_REVISION_DEB_AGENT_I386|" : "1",
    "|CYB3RHQ_REVISION_DEB_MANAGER_I386|" : "1",
    "|CYB3RHQ_REVISION_DEB_AGENT_X86|" : "1",
    "|CYB3RHQ_REVISION_DEB_MANAGER_X86|" : "1",
    "|CYB3RHQ_REVISION_DEB_AGENT_AARCH64|" : "1",
    "|CYB3RHQ_REVISION_DEB_MANAGER_AARCH64|" : "1",
    "|CYB3RHQ_REVISION_DEB_AGENT_ARMHF|" : "1",
    "|CYB3RHQ_REVISION_DEB_MANAGER_ARMHF|" : "1",
    "|CYB3RHQ_REVISION_DEB_AGENT_PPC|" : "1",
    #"|CYB3RHQ_REVISION_DEB_MANAGER_PPC|" : 
    #
    # === Cyb3rhq indexer version revisions
    "|CYB3RHQ_INDEXER_CURRENT_REV|" : "1", # RPM and Deb
    #"|CYB3RHQ_INDEXER_CURRENT_REV_DEB|" :
    # --- Architectures for Cyb3rhq indexer packages
    "|CYB3RHQ_INDEXER_x64_RPM|" : "x86_64",
    "|CYB3RHQ_INDEXER_x64_DEB|" : "amd64",
    #
    # === Cyb3rhq dashboard version revisions
    "|CYB3RHQ_DASHBOARD_CURRENT_REV_RPM|" : "1",
    "|CYB3RHQ_DASHBOARD_CURRENT_REV_DEB|" : "1",
    # --- Architectures for Cyb3rhq dashboard packages
    "|CYB3RHQ_DASHBOARD_x64_RPM|" : "x86_64",
    "|CYB3RHQ_DASHBOARD_x64_DEB|" : "amd64",
    #
    # === Versions and revisions for other Cyb3rhq deployments
    #"|CYB3RHQ_CURRENT_MAJOR_AMI|" :
    #"|CYB3RHQ_CURRENT_MINOR_AMI|" :
    "|CYB3RHQ_CURRENT_AMI|" : release,
    "|CYB3RHQ_CURRENT_MAJOR_OVA|" : "4.x",
    #"|CYB3RHQ_CURRENT_MINOR_OVA|" :
    "|CYB3RHQ_CURRENT_OVA|" : release,
    #"|CYB3RHQ_CURRENT_MAJOR_DOCKER|" :
    "|CYB3RHQ_CURRENT_MINOR_DOCKER|" : version,
    "|CYB3RHQ_CURRENT_DOCKER|" : release,
    #"|CYB3RHQ_CURRENT_MAJOR_KUBERNETES|" :
    #"|CYB3RHQ_CURRENT_MINOR_KUBERNETES|" :
    "|CYB3RHQ_CURRENT_KUBERNETES|" : release,
    #"|CYB3RHQ_CURRENT_MAJOR_ANSIBLE|" :
    "|CYB3RHQ_CURRENT_MINOR_ANSIBLE|" : version,
    "|CYB3RHQ_CURRENT_ANSIBLE|" : release,
    #"|CYB3RHQ_CURRENT_MAJOR_PUPPET|" :
    #"|CYB3RHQ_CURRENT_MINOR_PUPPET|" :
    "|CYB3RHQ_CURRENT_PUPPET|" : release,
    #"|CYB3RHQ_CURRENT_MAJOR_FROM_SOURCES|" :
    "|CYB3RHQ_CURRENT_MINOR_FROM_SOURCES|" : version,
    "|CYB3RHQ_CURRENT_FROM_SOURCES|" : release,
    #"|CYB3RHQ_CURRENT_MAJOR_WIN_FROM_SOURCES|" :
    #"|CYB3RHQ_CURRENT_MINOR_WIN_FROM_SOURCES|" :
    "|CYB3RHQ_CURRENT_WIN_FROM_SOURCES|" : release,
    "|CYB3RHQ_CURRENT_WIN_FROM_SOURCES_REV|" : "1",
    #
    # === Versions and revisions for packages of specific operating systems
    "|CYB3RHQ_CURRENT_MAJOR_WINDOWS|" : "4.x",
    #"|CYB3RHQ_CURRENT_MINOR_WINDOWS|" :
    "|CYB3RHQ_CURRENT_WINDOWS|" : release,
    "|CYB3RHQ_REVISION_WINDOWS|" : "1",
    "|CYB3RHQ_CURRENT_MAJOR_OSX|" : "4.x",
    #"|CYB3RHQ_CURRENT_MINOR_OSX|" :
    "|CYB3RHQ_CURRENT_OSX|" : release,
    "|CYB3RHQ_REVISION_OSX|" : "1",
    "|CYB3RHQ_CURRENT_MAJOR_SOLARIS|" : "4.x",
    #"|CYB3RHQ_CURRENT_MINOR_SOLARIS|" :
    "|CYB3RHQ_CURRENT_SOLARIS|" : release, # Set here the lesser of CYB3RHQ_CURRENT_MAJOR_SOLARIS10 and 11 values
    #"|CYB3RHQ_REVISION_SOLARIS|" : "1",
    "|CYB3RHQ_CURRENT_MAJOR_SOLARIS10|" : "4.x",
    #"|CYB3RHQ_CURRENT_MINOR_SOLARIS10|" :
    "|CYB3RHQ_CURRENT_SOLARIS10|" : release,
    #"|CYB3RHQ_REVISION_SOLARIS10|" : "1",
    "|CYB3RHQ_CURRENT_MAJOR_SOLARIS11|" : "4.x",
    #"|CYB3RHQ_CURRENT_MINOR_SOLARIS11|" :
    "|CYB3RHQ_CURRENT_SOLARIS11|" : release,
    #"|CYB3RHQ_REVISION_SOLARIS11|" : "1",
    "|CYB3RHQ_CURRENT_MAJOR_SOLARIS10_i386|" : "4.x",
    #"|CYB3RHQ_CURRENT_MINOR_SOLARIS10_i386|" :
    "|CYB3RHQ_CURRENT_SOLARIS10_i386|" : release,
    #"|CYB3RHQ_REVISION_SOLARIS10_i386|" : "1",
    "|CYB3RHQ_CURRENT_MAJOR_SOLARIS10_SPARC|" : "4.x",
    #"|CYB3RHQ_CURRENT_MINOR_SOLARIS10_SPARC|" :
    "|CYB3RHQ_CURRENT_SOLARIS10_SPARC|" : release,
    #"|CYB3RHQ_REVISION_SOLARIS10_SPARC|" : "1",
    "|CYB3RHQ_CURRENT_MAJOR_SOLARIS11_i386|" : "4.x",
    #"|CYB3RHQ_CURRENT_MINOR_SOLARIS11_i386|" :
    "|CYB3RHQ_CURRENT_SOLARIS11_i386|" : release,
    #"|CYB3RHQ_REVISION_SOLARIS11_i386|" : "1",
    "|CYB3RHQ_CURRENT_MAJOR_SOLARIS11_SPARC|" : "4.x",
    #"|CYB3RHQ_CURRENT_MINOR_SOLARIS11_SPARC|" :
    "|CYB3RHQ_CURRENT_SOLARIS11_SPARC|" : release,
    #"|CYB3RHQ_REVISION_SOLARIS11_SPARC|" : "1",
    "|CYB3RHQ_CURRENT_MAJOR_AIX|" : "4.x",
    #"|CYB3RHQ_CURRENT_MINOR_AIX|" :
    "|CYB3RHQ_CURRENT_AIX|" : release,
    "|CYB3RHQ_REVISION_AIX|" : "1",
    "|CYB3RHQ_CURRENT_MAJOR_HPUX|" : "4.x",
    #"|CYB3RHQ_CURRENT_MINOR_HPUX|" :
    "|CYB3RHQ_CURRENT_HPUX|" : release,
    "|CYB3RHQ_REVISION_HPUX|" : "1",
    #
    # === Elastic
    # --- Filebeat
    "|FILEBEAT_LATEST|" : "7.10.2",
    "|FILEBEAT_LATEST_AMI|" : "7.10.2",
    "|FILEBEAT_LATEST_OVA|" : "7.10.2",
    # --- Open Distro for Elasticsearch
    "|OPEN_DISTRO_LATEST|" : "1.13.2",
    # --- Elasticsearch
    "|ELASTICSEARCH_ELK_LATEST|" : "7.17.13", # Basic license
    "|ELASTICSEARCH_LATEST|" : "7.10.2",
    # --- Other Elastic
    "|ELASTIC_6_LATEST|" : "6.8.8",
    #
    # === Splunk
    "|SPLUNK_LATEST|" : "8.2.8",
    "|CYB3RHQ_SPLUNK_CURRENT|" : release,
    #
    "|SPLUNK_LATEST_MINOR|" : "8.2",
    "|CYB3RHQ_SPLUNK_REV_CURRENT_LATEST|" : "1", # 8.2
    "|CYB3RHQ_SPLUNK_REV_CURRENT_8.1|" : "1",
}

if is_latest_release:
    custom_replacements["|CYB3RHQ_INDEXER_RPM_PKG_INSTALL|"] = ''
    custom_replacements["|CYB3RHQ_MANAGER_RPM_PKG_INSTALL|"] = ''
    custom_replacements["|CYB3RHQ_DASHBOARD_RPM_PKG_INSTALL|"] = ''
    custom_replacements["|CYB3RHQ_INDEXER_DEB_PKG_INSTALL|"] = ''
    custom_replacements["|CYB3RHQ_MANAGER_DEB_PKG_INSTALL|"] = ''
    custom_replacements["|CYB3RHQ_DASHBOARD_DEB_PKG_INSTALL|"] = ''
    custom_replacements["|CYB3RHQ_AGENT_RPM_PKG_INSTALL|"] = ''
    custom_replacements["|CYB3RHQ_AGENT_DEB_PKG_INSTALL|"] = ''
    custom_replacements["|CYB3RHQ_AGENT_ZYPP_PKG_INSTALL|"] = ''
    custom_replacements["|CYB3RHQ_AGENT_APK_PKG_INSTALL|"] = ''
else:
    custom_replacements["|CYB3RHQ_INDEXER_RPM_PKG_INSTALL|"] = '-' + custom_replacements["|CYB3RHQ_CURRENT|"] + '-' + custom_replacements["|CYB3RHQ_INDEXER_CURRENT_REV|"]
    custom_replacements["|CYB3RHQ_MANAGER_RPM_PKG_INSTALL|"] = '-' + custom_replacements["|CYB3RHQ_CURRENT|"] + '-' + custom_replacements["|CYB3RHQ_REVISION_YUM_MANAGER_X86|"]
    custom_replacements["|CYB3RHQ_DASHBOARD_RPM_PKG_INSTALL|"] = '-' + custom_replacements["|CYB3RHQ_CURRENT|"] + '-' + custom_replacements["|CYB3RHQ_DASHBOARD_CURRENT_REV_RPM|"]
    custom_replacements["|CYB3RHQ_INDEXER_DEB_PKG_INSTALL|"] = '=' + custom_replacements["|CYB3RHQ_CURRENT|"] + '-' + custom_replacements["|CYB3RHQ_INDEXER_CURRENT_REV|"]
    custom_replacements["|CYB3RHQ_MANAGER_DEB_PKG_INSTALL|"] = '=' + custom_replacements["|CYB3RHQ_CURRENT|"] + '-' + custom_replacements["|CYB3RHQ_REVISION_DEB_MANAGER_X86|"]
    custom_replacements["|CYB3RHQ_DASHBOARD_DEB_PKG_INSTALL|"] = '=' + custom_replacements["|CYB3RHQ_CURRENT|"] + '-' + custom_replacements["|CYB3RHQ_DASHBOARD_CURRENT_REV_DEB|"]
    custom_replacements["|CYB3RHQ_AGENT_RPM_PKG_INSTALL|"] = '-' + custom_replacements["|CYB3RHQ_CURRENT|"] + '-' + custom_replacements["|CYB3RHQ_REVISION_YUM_AGENT_X86|"]
    custom_replacements["|CYB3RHQ_AGENT_DEB_PKG_INSTALL|"] = '=' + custom_replacements["|CYB3RHQ_CURRENT|"] + '-' + custom_replacements["|CYB3RHQ_REVISION_DEB_AGENT_X86|"]
    custom_replacements["|CYB3RHQ_AGENT_ZYPP_PKG_INSTALL|"] = '-' + custom_replacements["|CYB3RHQ_CURRENT|"] + '-' + '1'
    custom_replacements["|CYB3RHQ_AGENT_APK_PKG_INSTALL|"] = '=' + custom_replacements["|CYB3RHQ_CURRENT|"] + '-' + custom_replacements["|CYB3RHQ_REVISION_APK_AGENT_X86_64|"]
